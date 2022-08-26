from django.db.models import Q
from django.shortcuts import render, redirect
import requests
from model_utils import Choices
from rest_framework import status, permissions, serializers
from rest_framework.decorators import api_view, permission_classes
from .models import Record
from django.shortcuts import render
from rest_framework.response import Response


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def record_data(request):
    record = query_record_by_args(**request.query_params)
    record_serializer = TaskSerializerScan(record['items'], many=True)
    response = {
        'draw': record['draw'],
        'recordsTotal': record['total'],
        'recordsFiltered': record['total'],
        'data': record_serializer.data,
    }
    return Response(response)


def query_record_by_args(**kwargs):
    print(kwargs)
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = SCAN_ORDER_COLUMN_CHOICES[order_column]
    if order == 'desc':
        order_column = '-' + order_column

    queryset = Record.objects.all()

    if search_value:
        queryset = queryset.filter(Q(record_progress__icontains=search_value) |
                                   Q(record_type__icontains=search_value) |
                                   Q(record_annotation__icontains=search_value) |
                                   Q(record_theatre__icontains=search_value) |
                                   Q(record_datetime__icontains=search_value) |
                                   Q(record_status__icontains=search_value))

    total = queryset.count()
    count = queryset.count()
    queryset = queryset.order_by(order_column)[start:start + length]
    return {
        'items': queryset,
        'count': count,
        'total': total,
        'draw': draw
    }


class TaskSerializerScan(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = '__all__'


SCAN_ORDER_COLUMN_CHOICES = Choices(
    ('0', 'record_progress'),
    ('1', 'record_type'),
    ('2', 'record_annotation'),
    ('3', 'record_theatre'),
    ('4', 'record_datetime'),
    ('5', 'record_status'),
    ('6', 'record_exception_messages'),
)


def index(request):
    return render(request, 'transfer/main.html')


@api_view(['DELETE'])
@permission_classes((permissions.AllowAny,))
def delete(request, pk):
    model = get_record(request, pk)
    model.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


def get_record(request, pk):
    try:
        model = Record.objects.get(record_id=pk)
        return model
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)



