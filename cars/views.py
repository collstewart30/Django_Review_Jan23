from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerialzer

@api_view(['GET'])
def cars_list(request):
    cars = Car.objects.all()

    serializer = CarSerialzer(cars, many=True)

    print(serializer.data)

    return Response(serializer.data)