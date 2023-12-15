import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
@Injectable({
    providedIn: 'root'
})
export class LoginPageServiceService {
    constructor(private http: HttpClient) {}

    private baseApiUrl = environment.apiBaseUrl;
    /**
     * This function sends a request to the flask api endpoint and returns a response
     * @param usernameValue
     * @param passwordValue
     * @returns HTTP Response
     */
    confirmLogin(usernameValue: string, passwordValue: string): Observable<any> {
        const loginUrl: string = `${this.baseApiUrl}/api/login?username=${usernameValue}&password=${passwordValue}`;
        return this.http.get(loginUrl);
    }
}
