from django.urls import include, path

from .views import ListProductView, DetailProductView

urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('product/', ListProductView.as_view()),
    path('product/<int:pk>/', DetailProductView.as_view()),
]
