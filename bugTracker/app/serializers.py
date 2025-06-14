from rest_framework import serializers
from django.contrib.auth.models import User
from app.models import Project


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):

        user = User(email=validated_data["email"])

        user.set_password(validated_data["password"])
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)  # Hash the password on update

        instance.save()
        return instance


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["created_by"]  # ✅ fix


from rest_framework import serializers
from .models import Ticket, Project
from django.contrib.auth.models import User


class TicketSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Ticket
        fields = [
            "id",
            "project",
            "title",
            "description",
            "status",
            "priority",
            "created_by",
            "created_at",
        ]
        read_only_fields = ["created_at", "created_by"]
