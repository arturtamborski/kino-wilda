from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import F, Count

from django.forms.models import model_to_dict

from rest_framework import parsers
from rest_framework import generics

from backend.api import models
from backend.api import serializers

from backend.api import helpers


@csrf_exempt
@require_http_methods(['GET'])
def top(request):
    json = []

    objects = models.Movie.objects \
        .values(movie_id=F('id')) \
        .annotate(total_comments=Count('comment')) \
        .order_by('-total_comments')

    # todo: should be done in SQL/ORM?
    for idx, obj in enumerate(objects):
        json.append({
            'rank': idx + 1,
            'movie_id': obj['movie_id'],
            'total_comments': obj['total_comments'],
        })

    return JsonResponse(json, safe=False)


class Movie(generics.ListCreateAPIView):
    serializer_class = serializers.Movie
    model_class = serializer_class.Meta.model
    queryset = serializer_class.Meta.model.objects.all()
    parser_classes = (parsers.JSONParser,)

    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort')

        objects = self.model_class.objects.all()

        # todo: move sorting and filtering to serializer
        if sort:
            objects = objects.order_by(sort)

        serializer = self.serializer_class(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        title = request.data.get('title', '')

        if not len(title):
            return JsonResponse(data={'title': 'this field is required'}, status=400)

        try:
            obj = self.model_class.objects.get(title__exact=title)
            json = model_to_dict(obj)
        except self.model_class.DoesNotExist:
            json = helpers.fetch_movie_from_omdb(title)

            if 'Error' in json:
                return JsonResponse(data=json, status=400)

            json = {
                'title': json['Title'],
                'year': int(json['Year']),
                'plot': json['Plot'],
            }

            self.model_class(**json).save()
        return JsonResponse(data=json, status=200)


class Comment(generics.ListCreateAPIView):
    serializer_class = serializers.Comment
    model_class = serializer_class.Meta.model
    queryset = serializer_class.Meta.model.objects.all()
    parser_classes = (parsers.JSONParser,)

    def get(self, request, *args, **kwargs):
        movie_id = request.GET.get('movie_id', None)

        if movie_id:
            objects = self.model_class.objects.filter(movie_id=movie_id)
        else:
            objects = self.model_class.objects.all()

        serializer = self.serializer_class(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if not serializer.is_valid():
            return JsonResponse(data=serializer.errors, status=400)

        serializer.save()
        return JsonResponse(data=serializer.data, status=201)
