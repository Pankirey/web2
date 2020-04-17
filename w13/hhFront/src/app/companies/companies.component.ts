import { CompanyService } from './../Company.service';
import { Company } from './../Company';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-companies',
  templateUrl: './companies.component.html',
  styleUrls: ['./companies.component.css']
})
export class CompaniesComponent implements OnInit {

  companies: Company[] = [];

  constructor(public companyService: CompanyService) { }

  ngOnInit() {
    this.getCompanies();
  }

  getCompanies():void{
    this.companyService.getCompanies().subscribe(companies => this.companies = companies);
  }

}
