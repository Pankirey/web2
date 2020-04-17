from django.urls import path

from api.views import company_vacancy, vacancy_list, company_detail
from api.views import CompanyListAPIView

from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:company_id>/', company_detail),
    path('companies/<int:company_id>/vacancies', company_vacancy),
    path('vacancies/',vacancy_list),
]