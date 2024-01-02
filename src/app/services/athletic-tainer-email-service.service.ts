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

    sendEmail(userEmail: String, trainerEmail: String, injuryForm: String): Observable<any> {
        return this.http.get(this.baseApiUrl);
    }
}
