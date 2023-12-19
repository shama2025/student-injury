import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PatientOutcomeReportedMeasureTablePageComponent } from './patient-outcome-reported-measure-table-page.component';

describe('PatientOutcomeReportedMeasureTablePageComponent', () => {
  let component: PatientOutcomeReportedMeasureTablePageComponent;
  let fixture: ComponentFixture<PatientOutcomeReportedMeasureTablePageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PatientOutcomeReportedMeasureTablePageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(PatientOutcomeReportedMeasureTablePageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
