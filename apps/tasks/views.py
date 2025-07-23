from rest_framework import viewsets
from .serializer import TaskSerializer
from .models import Task

from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import JsonResponse
from django.utils.decorators import method_decorator

# Vista principal de las tareas
class TaskView(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# Vista que configura la cookie CSRF en el navegador
@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({'message': '✅ CSRF cookie set'})
