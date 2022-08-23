from django.shortcuts import render
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


@api_view(['DELETE'])
def delete(request, pk):
    try:
        record = Record.objects.get(pk=pk)
    except Record.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        record.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

def getLink(request):
    queryset = Record.objects.all()[:10]
    return JsonResponse({"link": list(queryset.values())})

# class CreateLink(CreateView):
#     model = Link
#     fields = ['link_name', 'link_text', 'link_status_code']
#
#     def form_valid(self, form):
#         try:
#             link_text = form.instance.link_text
#             clean_link_text = ipaddress.IPv4Address(link_text)
#             print('valid')
#             full_link = "https://" + link_text + ":9005/"
#             print(full_link)
#             link_ip_address = requests.get(full_link, auth=('admin', 'Puw5uTru'), verify=False)
#             status = link_ip_address.status_code
#             print(status)
#             if status == 200:
#                 form.instance.link_text = full_link
#                 form.instance.link_status_code = True
#                 form.save()
#                 return super().form_valid(form)
#         except:
#             print('Invalid')
#             form.instance.link_text = full_link
#             form.instance.link_status_code = False
#             form.save()
#             return super().form_valid(form)
#
#
# class UpdateLink(UpdateView):
#     model = Link
#     fields = ['link_name', 'link_text', 'link_status_code']
#
#     def form_valid(self, form):
#         try:
#             link_text = form.instance.link_text
#             link_ip_address = requests.get(link_text, auth=('admin', 'Puw5uTru'), verify=False)
#             status = link_ip_address.status_code
#             if status == 200:
#                 form.instance.link_status_code = True
#                 form.save()
#
#             return super().form_valid(form)
#         except:
#             form.instance.link_status_code = False
#             form.save()
#             return super().form_valid(form)
#
#
# class DeleteLink(DeleteView):
#     model = Link
#     success_url = reverse_lazy('index')
