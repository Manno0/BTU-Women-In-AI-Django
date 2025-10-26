from django.urls import path
from my_second_app.views import home, HomeView , current_datetime

urlpatterns = [
    path('home/', home, name='home'),
    path('class_home_page', HomeView.as_view(), name="class_home_page"),
    path('current_datetime', current_datetime, name='current_datetime'),
]