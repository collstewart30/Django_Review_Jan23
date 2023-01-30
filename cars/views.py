from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerialzer
from rest_framework import status

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':
        cars = Car.objects.all()
        serializer = CarSerialzer(cars, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
