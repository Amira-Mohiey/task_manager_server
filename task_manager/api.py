from tastypie.resources import ModelResource
from tastypie.authorization import  Authorization
from tastypie.authentication import BasicAuthentication
from .models import Task
from django.contrib.auth.models import User
from tastypie import fields
from .customAuth import CustomAuthorization

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        authorization =  Authorization()
        authentication = BasicAuthentication()
        resource_name = 'user'

class TaskResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'created_by')
    class Meta:
        queryset = Task.objects.all()
        resource_name = 'task'
        authorization = CustomAuthorization()
        authentication=BasicAuthentication()
        allowed_methods = ['get','post','put','delete']