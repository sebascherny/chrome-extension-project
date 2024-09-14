from django.contrib import admin
from django.urls import path
from notification_app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("get-notification/", views.get_notification, name="get_notification"),
    path("log-event/", views.log_event, name="log_event"),
]
