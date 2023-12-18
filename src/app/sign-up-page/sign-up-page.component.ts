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
        const newUser = {
            username: username.value,
            password: password.value,
            email: email.value,
            name: name.value
        };
        this.signUpService.confirmUserCreation(newUser).subscribe((response: Response) => {
            if (response.ok) {
                this.router.navigateByUrl(''); //go to athlete table page
            } else {
                //alert user that something is wrong
                console.log(response.text);
                alert('ERROR:' + response.status + ' ' + response.text);
            }
        });
    }
}
