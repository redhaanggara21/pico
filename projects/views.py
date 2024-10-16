from rest_framework import serializers, viewsets
from django.contrib.auth import get_user_model
from rest_framework.decorators import action
from rest_framework.response import Response

from task.views import TaskSerializer
from task.models import Task
from .models import Project


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.PrimaryKeyRelatedField(
            queryset=get_user_model().objects.all())

    class Meta:
        model = Project
        fields = ['id', 'title', 'description', 'user',
                  'created_at', 'updated_at']


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    @action(detail=False)
    def get_project_tasks(self, request, pk=None):
        project_tasks = Task.objects.filter(project=pk)
        serializer = self.get_serializer(project_tasks)
        return Response(serializer.data)


class ProjectTaskViewSet(viewsets.ViewSet):
    def list(self, request, *args, **kwargs):
        queryset = Task.objects.filter(project=kwargs['list_pk'])
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)