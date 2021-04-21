# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import *

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('tables/', views.buyer, name='buyer'),
    path('sku/', views.load_sku, name='load_sku'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
