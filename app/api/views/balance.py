from django.shortcuts import render
from rest_framework import generics, serializers
from rest_framework.response import Response
from service_tastemeasure.models import BalanceGame

class BalanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BalanceGame
        fields = (
            'date', 'nickname', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20'
            )


class BalanceResult(generics.ListAPIView):
    queryset = BalanceGame.objects.all()
    serializer_class = BalanceSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        serializer = serializer_class(queryset, many=True)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        return Response(serializer.data)