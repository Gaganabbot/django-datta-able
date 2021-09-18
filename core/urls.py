# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from django.urls import path, include  # add this
from apps.app import views, urls
from apps.Finance import views, urls
from apps.Health import views, urls
from apps.Skill import views,urls
from apps.Analytics import views,urls

urlpatterns = [
    path('admin', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login / register
    path("", include("apps.app.urls")),
    path("apps", include("apps.Finance.urls")),
    path("apps", include("apps.Health.urls")),
    path("apps", include("apps.Skill.urls")),
    path("apps", include("apps.Analytics.urls"))          # UI Kits Html files
]
