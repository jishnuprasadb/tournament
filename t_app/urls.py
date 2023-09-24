from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('registration',views.registration,name='registration'),
    path('team',views.team,name='team'),
    path('team_details/<int:id>',views.team_details,name='team_details'),
    path('fixture',views.fixture,name='fixture'),
    path('login_view',views.login_view,name='login_view'),
    path('admin_home',views.admin_home,name='admin_home'),
    path('score',views.score,name='score'),
]
