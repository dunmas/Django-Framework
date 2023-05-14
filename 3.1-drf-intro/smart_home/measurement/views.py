from rest_framework import generics
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializer, SensorDetailSerializer, MeasurementSerializer


class SensorsView(generics.ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

    def post(self, request):
        Sensor.objects.create(name=request.data['name'], description=request.data['description'])
        return Response({'detail': 'Sensor is added.'})


class SensorReadUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer

    def patch(self, request, pk):
        flag = Sensor.objects.filter(id=pk).update(description=request.data['description'])
        if flag != 0:
            return Response({'detail': f'Sensor №{pk} is updated.'})

        return Response({'detail': f'There is no sensor №{pk}.'})


class MeasurementView(generics.RetrieveUpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer

    def post(self, request):
        Measurement.objects.create(temperature=request.data['temperature'],
                                   sensor_id=request.data['sensor'])

        return Response({'detail': 'Added new measurement.'})
