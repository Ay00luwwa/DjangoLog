# from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class TestView(APIView):
    def get(self, request, *args, **kwargs ):
        response = dict(status='Success', result='Get')
        return Response(response, 200)
    
    
    def post(self, request, *args, **kwargs ):
        response = dict(status='Success', result='Post')
        return Response(response, 200)