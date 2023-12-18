import { TestBed } from '@angular/core/testing';

import { SignUpPageServiceService } from './sign-up-page-service.service';

describe('SignUpPageServiceService', () => {
    let service: SignUpPageServiceService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(SignUpPageServiceService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
