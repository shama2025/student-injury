import { Injectable } from '@angular/core';
import { Observable, timer } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Form } from '@angular/forms';

@Injectable({
    providedIn: 'root'
})
export class AthleticTainerEmailServiceService {
    constructor(private http: HttpClient) {}
    private baseApiUrl = environment.apiBaseUrl;
    private formData: FormData = new FormData();
    sendEmail(userEmail: string, trainerEmail: string, injuryForm: File | null | undefined): Observable<any> {
        this.formData.append('userEmail', userEmail);
        this.formData.append('trainerEmail', trainerEmail);

        if (injuryForm) {
            this.formData.append('injuryForm', injuryForm, injuryForm.name);
        }
        const emailUrl: string = `${this.baseApiUrl}/api/at/email`;
        return this.http.post(emailUrl, this.formData);
    }
}
