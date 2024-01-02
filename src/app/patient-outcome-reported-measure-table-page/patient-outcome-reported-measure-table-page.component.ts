import { Component, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';
import { Router } from '@angular/router';

@Component({
    selector: 'app-patient-outcome-reported-measure-table-page',
    templateUrl: './patient-outcome-reported-measure-table-page.component.html',
    styleUrls: ['./patient-outcome-reported-measure-table-page.component.css']
})
export class PatientOutcomeReportedMeasureTablePageComponent implements OnInit {
    constructor(
        private http: HttpClient,
        private route: Router
    ) {}

    ngOnInit(): void {
        this.createTable();
    }
    //*Variable that holds the json file information/
    tableForms: any;

    /**
     * This function will generate a table given x amount of PORM forms
     */
    createTable(): void {
        this.http.get('/assets/patient-outcome-reported-measure-forms.json').subscribe(response => {
            this.tableForms = response;
        });
    }

    /**
     * Navigates to the email form page
     */
    navigateToEmailPage(): void {
        this.route.navigateByUrl('athletic/trainer/email/form');
    }
}
