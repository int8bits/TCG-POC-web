
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .models import Card
from .serializers import CardListSerializer, CardDetailSerializer


class CardViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = get_list_or_404(Card)
        serializer = CardListSerializer(queryset, many=True)

        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Card, pk=pk)
        serializer = CardDetailSerializer(queryset)

        return Response(serializer.data)
