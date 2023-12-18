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
    confirmUserCreation(user: User): Observable<any> {
        const loginUrl = `${this.baseApiUrl}/api/new/account`;
        return this.http.post(loginUrl, user);
    }
}
