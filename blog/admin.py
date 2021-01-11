from django.contrib import admin

# Register your models here.
from .models import Article

# 将Article注册到admin
admin.site.register(Article)
