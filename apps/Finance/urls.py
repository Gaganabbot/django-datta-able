from django.urls import path, re_path
from apps.Finance import views
import apps

urlpatterns = [

    # The home page
    path('/work', views.WorkEfficiency, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
