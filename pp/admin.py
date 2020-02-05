from django.contrib import admin
from django.shortcuts import reverse

from pp.models import Pizza


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
