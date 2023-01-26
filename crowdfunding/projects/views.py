from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project
from .serializers import ProjectSerializer

class ProjectDetail(APIView): 

    def get_object(self, pk): 
        return Project.objects.get(pk=pk) 

    def get(self, request, pk): 
        project = self.get_object(pk) 
        serializer = ProjectSerializer(project) 
        return Response(serializer.data) 

class ProjectList(APIView):
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    #below block has been added
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

#request body (this block has also been added)
{
	"title": "Project one",
	"description": "The first project.",
	"goal": 150,
	"image": "https://via.placeholder.com/300.jpg",
	"is_open": True,
	"date_created": "2020-03-20T14:28:23.382748Z",
	"owner": "Real Creator"
}
