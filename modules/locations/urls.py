from django.urls import path
from modules.locations.views import home_page

urlpatterns = [
    path('home/', home_page, name='home_page'),

]