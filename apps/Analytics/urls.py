from django.urls import path, re_path
from apps.Analytics import views
import apps
urlpatterns = [

    # The home page
    path('/analytics', views.Analytics, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', apps.app.views.pages, name='pages'),

]