from django.contrib import admin

from app.models import Work, Category, MainImage

admin.site.register(Category)
admin.site.register(Work)
admin.site.register(MainImage)
