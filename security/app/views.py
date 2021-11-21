from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def sg_register(request):
    if request.method == 'POST':
        request_data = JSONParser().parse(request)
        print(request_data)
        if "mob" in request_data and "email" in request_data and "pass" in request_data:
            print(request_data)
            rsp = {"msg" : "recieved at security!"}
            return JsonResponse(rsp, status=status.HTTP_201_CREATED)
        else:
            rsp = {"msg": "keys are not valid"}
            return JsonResponse(rsp, status=status.HTTP_400_BAD_REQUEST)
    rsp = {"msg":"not recieved"}
    return JsonResponse(rsp, status=status.HTTP_400_BAD_REQUEST)
