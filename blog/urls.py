# -*- coding: utf-8 -*-#

# ------------------------------------------------------------------------------
# Name:         urls.py
# Description:
# Author:       Allen
# Time:         2021/1/11 14:33
# ------------------------------------------------------------------------------
from django.urls import path, include
import blog.views

urlpatterns = [
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),
]
