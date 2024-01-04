import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
@Injectable({
    providedIn: 'root'
})
export class AthleticTainerEmailServiceService {
    constructor(private http: HttpClient) {}
    private baseApiUrl = environment.apiBaseUrl;

    sendEmail(userEmail: String, trainerEmail: String, injuryForm: File | null | undefined): Observable<any> {
        const emailUrl: string = `${this.baseApiUrl}/api/at/email?userEmail=${userEmail}&trainerEmail=${trainerEmail}&injuryForm=${injuryForm}`;
        return this.http.get(emailUrl);
    }
}
