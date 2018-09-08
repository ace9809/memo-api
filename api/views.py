from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from rest_framework.response import Response
from api.serializers import MemoSerializer
from api.models import Memo

@api_view(('GET', ))
def api_root(request, format=None):
    return Response({
        'memo': reverse('memo-list', request=request, format=format),
    })


class MemoList(generics.ListAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class MemoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class MemoCreate(generics.CreateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class MemoDestroy(generics.DestroyAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer

class MemoUpdate(generics.UpdateAPIView):
    queryset = Memo.objects.all()
    serializer_class = MemoSerializer
