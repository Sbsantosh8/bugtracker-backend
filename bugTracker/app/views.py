from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.serializers import UserSerializer, ProjectSerializer


class UserView(APIView):

    def get(self, request):
        try:

            users = User.objects.all()
            if users.exists():
                serializer = UserSerializer(users, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)

            else:

                return Response(
                    {"message": "No Users Exists !"}, status=status.HTTP_404_NOT_FOUND
                )

        except Exception as e:
            return Response(
                {"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectView(APIView):

    def post(self, request):

        serializer = ProjectSerializer(data=request.data)
        print("before entering serilizer is valid()")
        if serializer.is_valid():
            print("after valid before save")
            serializer.save(serializer.save(created_by=request.user))
            print("after save of view")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
