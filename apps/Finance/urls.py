from django.urls import path, re_path
from apps.Finance import views
import apps

urlpatterns = [

    # The home page
    path('/work', views.WorkEfficiency, name='home'),
    path('/work/add', views.AddWork, name='home'),
    path('/work/update/<str:pk>', views.UpdateWork, name='home'),
    path('/work/delete/<str:pk>', views.DeleteWork, name='home'),
    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
