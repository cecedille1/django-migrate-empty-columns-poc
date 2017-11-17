# -*- coding: utf-8 -*-

from django.db import models

class Poc(models.Model):
    f2 = models.IntegerField(
        primary_key=True,
    )
