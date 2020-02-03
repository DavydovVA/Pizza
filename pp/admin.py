from django.contrib import admin
from django.shortcuts import reverse

from pp.models import Pizza


@admin.register(Pizza)
class MemAdmin(admin.ModelAdmin):
    exclude = ('slug',)


admin.site.site_url = reverse('pp:index')
