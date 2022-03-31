from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .serializers import CarSerializer
from .models import Car
from cars import serializers

@api_view(['GET'])
def cars_list(request): 
    cars = Car.objects.all()

    serializer = CarSerializer(cars, many = True)
    
    return Response('ok')