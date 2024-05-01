import json
from typing import Any, Dict, List, Union
from pprint import pprint
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Max


from .models import Champion
from .serializers import ChampionSerializer

from .ChampionConfigurationGenerator import ChampionConfigurationGenerator


def index(request):
    return HttpResponse("Hello, world. You're at the lor_backend index.")


@api_view(["GET"])
def get_champion(request: Any, id: int) -> Response:
    if request.method == "GET":
        try:
            champion: Champion = Champion.objects.get(pk=id)
            serializer: ChampionSerializer = ChampionSerializer(champion)

            championConfigurationGenerator = ChampionConfigurationGenerator()
            championConfiguration: Dict[str, Dict[str, str]] = championConfigurationGenerator.generate_random_champion_configuration_with_url(
                champion_configuration=serializer.data,
            )
        
            return Response(championConfiguration, status=status.HTTP_200_OK)

        except Champion.DoesNotExist:
            championConfigurationGenerator = ChampionConfigurationGenerator()

            random_champion: Dict[str, str] = championConfigurationGenerator.generate_random_champion_configuration()
            championConfiguration: Dict[str, Dict[str, str]] = championConfigurationGenerator.generate_random_champion_configuration_with_url(
                champion_configuration=random_champion,
            )

            random_champion["unique_id"] = 1
            while Champion.objects.filter(unique_id=random_champion["unique_id"]).exists():
                random_champion["unique_id"] += 1

            serializer: ChampionSerializer = ChampionSerializer(data=random_champion)
            if serializer.is_valid():
                serializer.save()
                champion_with_url: Dict[str, Union[int, str]] = championConfigurationGenerator.generate_random_champion_configuration_with_url(
                    champion_configuration=random_champion,
                )
                return Response(champion_with_url, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def get_data(request: Any, file: str) -> HttpResponse:
    if request.method == "GET":
        try:
            with open(f"lor_backend/assets/{file}.json", "r") as json_file:
                data = json.load(json_file)
                return HttpResponse(json.dumps(data), content_type="application/json")
        except FileNotFoundError:
            return HttpResponse(json.dumps({}), content_type="application/json")


@api_view(["POST"])
def get_random_champion(request: Any) -> Response:
    if request.method == "POST":
        print("Getting random champion")
        allowedChampionList: List[str] = request.data.get("allowedChampionList", [])

        championConfigurationGenerator = ChampionConfigurationGenerator()
        random_champion: Dict[str, str] = championConfigurationGenerator.generate_random_champion_configuration()
        random_champion["unique_id"] = 1
        while Champion.objects.filter(unique_id=random_champion["unique_id"]).exists():
            random_champion["unique_id"] += 1

        serializer: ChampionSerializer = ChampionSerializer(data=random_champion)
        if serializer.is_valid():
            serializer.save()
            random_champion_with_url: Dict[str, Union[int, str]] = championConfigurationGenerator.generate_random_champion_configuration_with_url(
                champion_configuration=random_champion,
            )
            return Response(random_champion_with_url, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
