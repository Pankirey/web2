import { CompanyService } from './../Company.service';
import { Component, OnInit } from '@angular/core';
import { Company, Vacancy } from './../Company';
import { ActivatedRoute } from '@angular/router';
import { Location } from '@angular/common';

@Component({
  selector: 'app-company_details',
  templateUrl: './company_details.component.html',
  styleUrls: ['./company_details.component.css']
})
export class Company_detailsComponent implements OnInit {

  company: Company;
  vacancies: Vacancy[] = [];

  constructor(
    private companyService: CompanyService,
    private route: ActivatedRoute,
    private location: Location
  ) { }

  ngOnInit() {
    this.getCompany();
    this.getVacanciesByCompany();
  }

  getCompany(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getCompany(id).subscribe(company => this.company = company);
  }

  getVacanciesByCompany(){
    const id = +this.route.snapshot.paramMap.get('id');
    this.companyService.getVacanciesOfCompany(id).subscribe(vacancies => this.vacancies = vacancies);
  }

  goBack(){
    this.location.back();
  }

}
