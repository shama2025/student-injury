import { Component, OnInit } from '@angular/core';
import { SignUpPageServiceService } from '../services/sign-up-page-service.service';
import { Router } from '@angular/router';
@Component({
    selector: 'app-sign-up-page',
    templateUrl: './sign-up-page.component.html',
    styleUrls: ['./sign-up-page.component.css']
})
export class SignUpPageComponent implements OnInit {
    constructor(
        private signUpService: SignUpPageServiceService,
        private router: Router
    ) {}

    ngOnInit(): void {}

    /**
     * Passes a newUser object to the service and handles response from api
     * @param username
     * @param password
     * @param email
     * @param name
     */
    createAccount(
        username: HTMLInputElement,
        password: HTMLInputElement,
        email: HTMLInputElement,
        name: HTMLInputElement
    ) {
        this.signUpService
            .confirmUserCreation(username.value, password.value, email.value, name.value)
            .subscribe((response: Response) => {
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
}
