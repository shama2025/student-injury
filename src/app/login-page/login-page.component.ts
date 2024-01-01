import { Component, OnInit } from '@angular/core';
import { LoginPageServiceService } from '../services/login-page-service.service';
import { Router } from '@angular/router';

@Component({
    selector: 'app-login-page',
    templateUrl: './login-page.component.html',
    styleUrls: ['./login-page.component.css']
})
export class LoginPageComponent implements OnInit {
    constructor(
        private loginPageService: LoginPageServiceService,
        private router: Router
    ) {}

    ngOnInit(): void {}

    /**
     * This function will pass the login infromation to the service
     * @param username
     * @param password
     */
    loginEvent(username: HTMLInputElement, password: HTMLInputElement): void {
        this.loginPageService.confirmLogin(username.value, password.value).subscribe((response: Response) => {
            if (JSON.stringify(response)) {
                //Route to student-injury-form page
                this.router.navigateByUrl('patient-outcome-reported-measure'); //navigate to student form site
            } else {
                //Display a popup box that user does not exist and encourage new account creation
                alert('ERROR: ' + JSON.stringify(response));
                console.log('ERROR: ' + JSON.stringify(response));
            }
        });
    }

    /**
     * Route to the sign-up-page componenet
     */
    newUser(): void {
        this.router.navigateByUrl('sign/up');
    }
}
