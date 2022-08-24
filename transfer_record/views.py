from django.shortcuts import render, redirect
import requests
from rest_framework import status
from rest_framework.decorators import api_view

from .models import Record
from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from requests.auth import HTTPBasicAuth
import urllib3
import json


def index(request):
    all_data = Record.objects.all()
    return render(request, 'transfer/main.html', {'all_data': all_data})


def get_record(request, pk):
    try:
        model = Record.objects.get(record_id=pk)
        return model
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


def delete(request, pk):
    model = get_record(request, pk)
    model.delete()
    return redirect('/transfer/')

