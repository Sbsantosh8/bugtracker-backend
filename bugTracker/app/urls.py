from django.urls import path
from app.views import UserView, ProjectView, TicketView

urlpatterns = [
    path("users/", UserView.as_view(), name="User"),
    path("project/", ProjectView.as_view(), name="Project"),
    path("project/<int:pk>/", ProjectView.as_view(), name="Project"),
    path("ticket/", TicketView.as_view(), name="Ticket"),
]
