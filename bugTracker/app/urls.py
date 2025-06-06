from django.urls import path
from app.views import UserView, ProjectView

urlpatterns = [
    path("users/", UserView.as_view(), name="User"),
    path("project/", ProjectView.as_view(), name="Project"),
]


