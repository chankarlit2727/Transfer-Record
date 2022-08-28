from django.db.models import Q
from model_utils import Choices
from rest_framework import status, permissions, serializers, viewsets
from rest_framework.decorators import api_view, permission_classes

from serializers import RecordSerializer, DeleteRecordSerializer
from .models import Record
from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response


def index(request):
    return render(request, 'transfer/main.html')


class RecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = RecordSerializer

    def list(self, request, **kwargs):
        try:
            record = query_record_by_args(**request.query_params)
            record_serializer = RecordSerializer(record['items'], many=True)
            response = {
                'draw': record['draw'],
                'recordsTotal': record['total'],
                'recordsFiltered': record['total'],
                'data': record_serializer.data,
            }
            return Response(response, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        record = Record.objects.all()
        record_id = get_object_or_404(record, pk=pk)
        serializer = RecordSerializer(record)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteRecordViewSet(viewsets.ModelViewSet):
    queryset = Record.objects.all()
    serializer_class = DeleteRecordSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        instance = self.get_object()
        return super(DeleteRecordViewSet, self).destroy(request, pk, *args, **kwargs)


def query_record_by_args(**kwargs):
    print(kwargs)
    draw = int(kwargs.get('draw', None)[0])
    length = int(kwargs.get('length', None)[0])
    start = int(kwargs.get('start', None)[0])
    search_value = kwargs.get('search[value]', None)[0]
    order_column = kwargs.get('order[0][column]', None)[0]
    order = kwargs.get('order[0][dir]', None)[0]

    order_column = SCAN_ORDER_COLUMN_CHOICES[order_column]
    if order == 'asc':
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


SCAN_ORDER_COLUMN_CHOICES = Choices(
    ('0', 'record_progress'),
    ('1', 'record_type'),
    ('2', 'record_annotation'),
    ('3', 'record_theatre'),
    ('4', 'record_datetime'),
    ('5', 'record_status'),
    ('6', 'record_exception_messages'),
)


# def get_record(self, pk):
#     try:
#         self.model = Record.objects.get(record_id=pk)
#         return self.model
#     except Record.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#
# def delete(self, pk):
#     model = self.get_record(self, pk)
#     model.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)
