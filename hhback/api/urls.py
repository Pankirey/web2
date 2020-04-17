from django.contrib import admin
from django.urls import path

from api.views import CompanyListAPIView, CompanyDetailAPIView
from api.views import vacancies_list, vacancy_detail, top_vacancies, company_vacancies
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:pk>/', CompanyDetailAPIView.as_view()),
    path('vacancies/', vacancies_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('companies/<int:company_id>/vacancies', company_vacancies),
    path('vacancies/top_ten', top_vacancies)
]