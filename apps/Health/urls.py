from django.urls import path, re_path
from apps.Health import views
import apps
urlpatterns = [

    # The home page
    path('/health', views.HealthWellbeing, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', apps.app.views.pages, name='pages'),

]