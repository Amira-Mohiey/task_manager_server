from tastypie.constants import ALL_WITH_RELATIONS,ALL
from tastypie.resources import ModelResource
from tastypie.authorization import  Authorization
from tastypie.authentication import BasicAuthentication
from .models import Task
from django.contrib.auth.models import User
from tastypie import fields
from .customAuth import CustomAuthorization

class UserResource(ModelResource):
    # tasks = fields.ToManyField('task_manager.api.resources.TaskResource','tasks', null=True, blank=True)
    class Meta:
        queryset = User.objects.all()
        authorization = Authorization()
        filtering = {
            'username': ALL
        }
        authentication = BasicAuthentication()
        resource_name = 'user'


class TaskResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'created_by')

    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        filtering = {
            'user': ALL_WITH_RELATIONS
        }
        fields = ['user', 'task_title', 'task_description']
        authorization = CustomAuthorization()
        authentication = BasicAuthentication()
        allowed_methods = ['get', 'post', 'put', 'delete']
