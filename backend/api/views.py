from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from rest_framework.parsers import JSONParser
from annoying.functions import get_object_or_None

from backend.api import models
from backend.api import serializers


@csrf_exempt
@require_http_methods(['GET'])
def top(request):
    model = models.Movie.objects.all()
    serializer = serializers.Movie(model, many=True)
    print('check what is serializer and how to add new items')
    breakpoint()
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
@require_http_methods(['GET', 'POST'])
def movies(request):
    if request.method == 'GET':
        sort = request.GET.get('sort')
        only = request.GET.get('only')

        if only and only.split(',') in serializers.Movie.Meta.fields:
            objs = models.Movie.objects.values_list(only)
        else:
            objs = models.Movie.objects.all()

        if sort and sort in serializers.Movie.Meta.fields:
            objs = objs.order_by(sort)

        serializer = serializers.Movie(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

    data = JSONParser().parse(request)
    serializer = serializers.Movie(data=data)

    if serializer.is_valid(raise_exception=True):
        title = serializer['title']
        obj = get_object_or_None(models.Movie, title__icontains=title)

        if obj:
            return JsonResponse(serializers.Movie(data=obj, status=201))

        # not present in db, need to fetch it
        print('fetching from external db...')



@csrf_exempt
@require_http_methods(['GET', 'POST'])
def comments(request):
    if request.method == 'GET':
        sort = request.GET.get('sort')
        only = request.GET.get('only')

        if only and only.split(',') in serializers.Comment.Meta.fields:
            objs = models.Comment.objects.values_list(only)
        else:
            objs = models.Comment.objects.all()

        if sort and sort in serializers.Comment.Meta.fields:
            objs = objs.order_by(sort)

        serializer = serializers.Comment(objs, many=True)
        return JsonResponse(serializer.data, safe=False)

    data = JSONParser().parse(request)
    serializer = serializers.Comment(data=data)

    if serializer.is_valid(raise_exception=True):
        movie_id = serializer['id']
        text = serializer['text']
        serializer.save()
        return JsonResponse(serializer.data, status=201)
