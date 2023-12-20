import { Component, OnInit } from '@angular/core';

import { HttpClient } from '@angular/common/http';

@Component({
    selector: 'app-patient-outcome-reported-measure-table-page',
    templateUrl: './patient-outcome-reported-measure-table-page.component.html',
    styleUrls: ['./patient-outcome-reported-measure-table-page.component.css']
})
export class PatientOutcomeReportedMeasureTablePageComponent implements OnInit {
    constructor(private http: HttpClient) {}

    ngOnInit(): void {
        this.createTable();
    }

    tableForms: any;

    /**
     * This function will generate a table given x amount of PORM forms
     */
    createTable(): void {
        this.http.get('/assets/media.json').subscribe(response => {
            this.tableForms = response;
        });
    }

    /**
     * Searches the table for value contained in the search bar
     */
    search(): void {}

    /**
     * Filters the table by type of injury
     */
    filterInjuryBtn(): void {}

    /**
     * Filters if the file can be online or needs to be done by paper pencil
     */
    filterIsPenPaper(): void {}

    /**
     * Filters by Ascending or Descending alphabetically
     */
    filterASCDESC(): void {}
}
