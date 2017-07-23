# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    task_title = models.CharField(max_length=200)
    task_description = models.CharField(max_length=200)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)



