# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    project_name = models.CharField(max_length=200)
    project_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, related_name='%(class)s_requests_created_by', on_delete=models.CASCADE)
    assigned_to = models.ForeignKey(User, related_name='%(class)s_requests_assigned_to', on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)



