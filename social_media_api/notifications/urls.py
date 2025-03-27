from django.urls import path, include
from . import views

urlpatterns = [
    path("notifications/", views.NotificationListView.as_view(), name="notifications"),
    path("notifications/read/", views.MarkNotificationsReadView.as_view(), name="mark-notifications-read"),
]
