from django.urls import include, path
from rest_framework import routers
from .views import TaskView

router = routers.DefaultRouter()
router.register(r"tasks", TaskView, basename="tasks")

urlpatterns = [
    path("", include(router.urls)),
]
