from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer


# Create your views here.

class NotificationListView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.all().order_by("-timestamp")

class MarkNotificationsReadView(generics.UpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, *args, **kwargs):
        notifications = request.user.notifications.filter(is_read=False)
        notifications.update(is_read=True)
        return Response({"message": "All notifications marked as read."})
