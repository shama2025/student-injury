import { Component, OnInit } from '@angular/core';
import { LoginPageServiceService } from '../services/login-page-service.service';
import { HttpErrorResponse } from '@angular/common/http';
@Component({
    selector: 'app-login-page',
    templateUrl: './login-page.component.html',
    styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {
    constructor(private loginPageService: LoginPageServiceService) {}

    ngOnInit(): void {}

    /**
     * This function will pass the login infromation to the service
     * @param username
     * @param password
     */
    loginEvent(username: HTMLInputElement, password: HTMLInputElement): void {
        this.loginPageService.confirmLogin(username.value, password.value).subscribe(response => {
            if (response == 'Yes') {
                //Route to student-injury-form page
                console.log('Hooray');
            } else {
                //Display a popup box that user does not exist and encourage new account creation
                console.log('Boo');
            }
        });
    }
}
