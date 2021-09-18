from django.urls import path, re_path
from apps.Skill import views
import apps

urlpatterns = [

    # The home page
    path('/skill', views.SkillsLearning, name='home'),

    # Matches any html file
    # re_path(r'^.*\.*', apps.app.views.pages, name='pages'),

]