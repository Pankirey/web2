import { CompanyService } from './../Company.service';
import { Component, OnInit } from '@angular/core';
import { Vacancy } from './../Company';

@Component({
  selector: 'app-vacancies',
  templateUrl: './vacancies.component.html',
  styleUrls: ['./vacancies.component.css']
})
export class VacanciesComponent implements OnInit {

  vacancies: Vacancy[] = [];

  constructor(private companyService: CompanyService) { }

  ngOnInit() {
    this.getVacancies();
  }

  getVacancies():void{
    this.companyService.getVacancies().subscribe(vacancies => this.vacancies = vacancies);
  }

}
