from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from backend.api import models
from backend.api import serializers


@csrf_exempt
def top(request):
    if request.method == 'GET':
        model = models.Movie.objects.all()
        serializer = serializers.Movie(model, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def movies(request):
    if request.method == 'GET':
        model = models.Movie.objects.all()
        serializer = serializers.Movie(model, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.Movie(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def comments(request):
    if request.method == 'GET':
        model = models.Comment.objects.all()
        serializer = serializers.Comment(model, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = serializers.Movie(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
