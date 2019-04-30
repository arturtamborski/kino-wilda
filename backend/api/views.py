from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.db.models import F, Count

from rest_framework import parsers
from rest_framework import generics

from backend.api import models
from backend.api import serializers


@csrf_exempt
@require_http_methods(['GET'])
def top(request):
    objs = models.Movie.objects \
        .values(movie_id=F('id')) \
        .annotate(total_comments=Count('comment')) \
        .order_by('-total_comments')
    serializer = serializers.Movie(objs, many=True)

    # todo: should be done in SQL/ORM
    for idx, data in enumerate(serializer.data):
        data['rank'] = idx + 1

    return JsonResponse(serializer.data, safe=False)


class Movie(generics.ListCreateAPIView):
    serializer_class = serializers.Movie
    queryset = serializer_class.Meta.model.objects.all()
    parser_classes = (parsers.JSONParser,)

    def get(self, request, *args, **kwargs):
        sort = request.GET.get('sort')

        objects = self.serializer_class.Meta.model.objects.all()

        # todo: move sorting and filtering to serializer
        if sort:
            objects = objects.order_by(sort)

        serializer = self.serializer_class(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)


class Comment(generics.ListCreateAPIView):
    serializer_class = serializers.Comment
    queryset = serializer_class.Meta.model.objects.all()
    parser_classes = (parsers.JSONParser,)

    def get(self, request, *args, **kwargs):
        objects = self.serializer_class.Meta.model.objects.all()
        serializer = self.serializer_class(objects, many=True)
        return JsonResponse(serializer.data, safe=False)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(data=serializer.data, status=201)
        return JsonResponse(data=serializer.errors, status=400)
