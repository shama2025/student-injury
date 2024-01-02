import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AthleticTrainerEmailFormComponent } from './athletic-trainer-email-form.component';

describe('AthleticTrainerEmailFormComponent', () => {
    let component: AthleticTrainerEmailFormComponent;
    let fixture: ComponentFixture<AthleticTrainerEmailFormComponent>;

    beforeEach(async () => {
        await TestBed.configureTestingModule({
            declarations: [AthleticTrainerEmailFormComponent]
        }).compileComponents();

        fixture = TestBed.createComponent(AthleticTrainerEmailFormComponent);
        component = fixture.componentInstance;
        fixture.detectChanges();
    });

    it('should create', () => {
        expect(component).toBeTruthy();
    });
});
