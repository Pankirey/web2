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

class CompanyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer2

def company_vacancy(request, company_id):
    if request.method == "GET":
        try:
            vacancy_list = Vacancy.objects.all()
            vacancies = []
            for vacancy in vacancy_list:
                if(vacancy.company.id == company_id):
                    vacancies.append(vacancy.vacancy_to_json())
        except Company.DoesNotExist as e:
            return JsonResponse({'error': 'company doesn`t exist'})
        return JsonResponse(vacancies,safe=False)
    elif request.method == "POST":
        pass

@api_view(['GET', 'POST'])
def company_vacancies(request, company_id):
    if request.method == 'GET':
        vacancies = Vacancy.objects.filter(company = company_id)
        serializer = VacancySerializer(vacancies, many=True)

        return Response(serializer.data)

@api_view(['GET', 'POST'])
def vacancies_list(request):
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

@api_view(['GET', 'PUT', 'DELETE'])
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = VacancySerializer(vacancy)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        vacancy.delete()
        return Response({'deleted': True})


def top_vacancies(request):
    if request.method == "GET":
        vacancies = Vacancy.objects.all().order_by('-salary')[:10:1]
        vacancy_json = [vacancy.vacancy_to_json() for vacancy in vacancies]
        if (len(vacancy_json) == 0):
            return JsonResponse({'error': 'no vacancies'})
        else:
            return JsonResponse(vacancy_json, safe=False)
    elif request.method == "POST":
        pass
