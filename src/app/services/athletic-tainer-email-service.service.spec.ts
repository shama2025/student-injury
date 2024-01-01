import { TestBed } from '@angular/core/testing';

import { AthleticTainerEmailServiceService } from './athletic-tainer-email-service.service';

describe('AthleticTainerEmailServiceService', () => {
    let service: AthleticTainerEmailServiceService;

    beforeEach(() => {
        TestBed.configureTestingModule({});
        service = TestBed.inject(AthleticTainerEmailServiceService);
    });

    it('should be created', () => {
        expect(service).toBeTruthy();
    });
});
