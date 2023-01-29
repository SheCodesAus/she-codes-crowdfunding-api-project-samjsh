from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Project, Pledge, Comment #, Pledge added from DRF doc 2
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer, CommentSerializer #last two words added from DRF doc 2
from django.http import Http404
from rest_framework import status, generics #, generics added from DRF doc 2
from .models import Pledge #added
from rest_framework import status, permissions #added from permissions doc
from .permissions import IsOwnerOrReadOnly #added from permissions doc

#Create your views here
class ProjectDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    # def get_object(self, pk):
    #     try:
    #         return Project.objects.get(pk=pk) 
    #     except Project.DoesNotExist:
    #         raise Http404
    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk) 
        serializer = ProjectDetailSerializer(project) #amended ProjectSerializer to ProjectDetailSerializer from DRF doc 2
        return Response(serializer.data) 
    
    # block added from permissions doc
    def put(self, request, pk):
        project = self.get_object(pk)
        data = request.data
        serializer = ProjectDetailSerializer(
            instance=project,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #added from permissions page
    
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("hello")
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            print("valid")
            serializer.save(owner=request.user) #owner=request.user added from user doc
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

#New class added from DRF doc 2
class PledgeList(generics.ListCreateAPIView):
    queryset = Pledge.objects.all()
    serializer_class = PledgeSerializer
    
    def perform_create(self, serializer): #from this line, added from user doc
        serializer.save(supporter=self.request.user)
        
#Added from comment section
class CommentDetail(APIView):
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly    ]
    def get_object(self, pk):
        print("get comment object")
        try:
            comment = Comment.objects.get(pk=pk)
            self.check_object_permissions(self.request, comment)
            return comment
        except Comment.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        print("get comment ")
        comment = self.get_object(pk) 
        serializer = CommentSerializer(comment)
        return Response(serializer.data) 
    
    def put(self, request, pk):
        print("put comment object")
        comment = self.get_object(pk)
        data = request.data
        serializer = CommentSerializer(
            instance=comment,
            data=data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
        

class CommentList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly] #added from permissions page
    
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("post comment")
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            print("comment valid")
            serializer.save(author=request.user) #owner=request.user added from user doc
            print("saved comment!")
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
                )
        print("invalid comment")
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )