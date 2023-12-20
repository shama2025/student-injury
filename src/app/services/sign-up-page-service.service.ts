import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from 'src/environments/environment';
import { Observable } from 'rxjs';
import { User } from '../user';
@Injectable({
    providedIn: 'root'
})
export class SignUpPageServiceService {
    constructor(private http: HttpClient) {}

    private baseApiUrl = environment.apiBaseUrl;

    /**
     * Sends a put request to the backend with the user object
     * @param user
     * @returns
     */
    confirmUserCreation(username: string, password: string, email: string, name: string): Observable<any> {
        const loginUrl = `${this.baseApiUrl}/api/new/account?username=${username}&password=${password}&name=${name}&email=${email}`;
        return this.http.get(loginUrl, { responseType: 'text' });
    }
}
