from django.urls import path

from measurement.views import SensorsView, SensorReadUpdateView, MeasurementView

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorReadUpdateView.as_view()),
    path('measurements/', MeasurementView.as_view()),
]
