from django.urls import path
from .views import RegisterView, LoginView, NoteListCreateView, NoteDetailView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger documentation
schema_view = get_schema_view(
   openapi.Info(
      title="Notes API",
      default_version='v1',
      description="Notes Management API",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('notes/', NoteListCreateView.as_view(), name='notes'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]