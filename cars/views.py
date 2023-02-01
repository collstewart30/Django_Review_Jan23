from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car
from .serializers import CarSerialzer
from rest_framework import status
from django.shortcuts import get_object_or_404

@api_view(['GET', 'POST'])
def cars_list(request):

    if request.method == 'GET':

        dealership_name = request.query_params.get("dealership")    # name of key used in url parameter
        print(dealership_name)
        
        cars = Car.objects.all()

        if dealership_name:
            cars=cars.filter(dealership__name=dealership_name)

        serializer = CarSerialzer(cars, many=True)
        # print(serializer.data)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = CarSerialzer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    if request.method == 'GET':
        serializer = CarSerialzer(car)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = CarSerialzer(car, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)