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
            if (response.ok) {
                //Route to student-injury-form page
                this.router.navigateByUrl(''); //navigate to student form site
            } else {
                //Display a popup box that user does not exist and encourage new account creation
                alert('ERROR: ' + response.status + ' ' + response.text);
                console.log('ERROR: ' + response.status + ' ' + response.text);
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
