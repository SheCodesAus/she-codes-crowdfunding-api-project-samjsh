from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer
from django.http import Http404
from rest_framework import status

#Create your views here
class ProjectDetail(APIView):

    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk) 
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk) 
        serializer = ProjectSerializer(project) 
        return Response(serializer.data) 

class ProjectList(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("hello")
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            serializer.save()
            print("saved!")
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        print("invalid")
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        