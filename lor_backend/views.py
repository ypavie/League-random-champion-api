from django.http import HttpResponse
from .models import Champion
from .serializers import ChampionSerializer
from .utils import generate_random_champion
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response as JSONResponse
import json


def index(request):
    return HttpResponse("Hello, world. You're at the lor_backend index.")


@api_view(['GET'])
def get_champion(request, id):
    if request.method == 'GET':
        try:
            champion = Champion.objects.get(pk=id)
            serializer = ChampionSerializer(champion)
            return JSONResponse(serializer.data)

        except Champion.DoesNotExist:
            ban_list = request.GET.getlist('ids')
            print(ban_list)
            random_champion = generate_random_champion(ban_list)
            random_champion['unique_id'] = id
            serializer = ChampionSerializer(data=random_champion)
            if serializer.is_valid():
                serializer.save()
                return JSONResponse(serializer.data, status=status.HTTP_201_CREATED)
            return JSONResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_data(request, file):
    if request.method == 'GET':
        try:
            with open(f"lor_backend/assets/{file}.json", "r") as json_file:
                data = json.load(json_file)
                return HttpResponse(json.dumps(data), content_type="application/json")
        except FileNotFoundError:
            return HttpResponse(json.dumps({}), content_type="application/json")
