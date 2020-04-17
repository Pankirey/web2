import json
from django.shortcuts import render
from rest_framework import generics
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from api.models import Company, Vacancy
from rest_framework.views import APIView

from api.serializers import CompanySerializer, CompanySerializer2, VacancySerializer
from rest_framework.permissions import IsAuthenticated

class CompanyListAPIView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2

@api_view(['GET', 'PUT', 'DELETE'])
def company_detail(request, company_id):
    try:
        company = Company.objects.get(id=company_id)
    except Company.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CompanySerializer2(instance=company, data=request.data)
        if serializer.is_valid():
            serializer.save()  # update function in serializer class
            return Response(serializer.data)
        return Response({'error': serializer.errors})
    elif request.method == 'DELETE':
        company.delete()
        return Response({'deleted': True})

@api_view(['GET', 'POST'])
def company_vacancy(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company = company_id)
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)

@api_view(['GET', 'POST'])
def vacancy_list(request):
    if request.method == 'GET':
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # create function in serializer class
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)





