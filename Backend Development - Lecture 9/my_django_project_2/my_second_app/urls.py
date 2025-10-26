from django.urls import path
from my_second_app.views import home, HomeView

urlpatterns = [
    path('home/', home, name='home'),
    path('class_home_page', HomeView.as_view(), name="class_home_page")# Maps the root URL to the home view
]