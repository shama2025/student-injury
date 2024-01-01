import { Component, OnInit } from '@angular/core';
import { AthleticTainerEmailServiceService } from '../services/athletic-tainer-email-service.service';
@Component({
    selector: 'app-athletic-trainer-email-form',
    templateUrl: './athletic-trainer-email-form.component.html',
    styleUrls: ['./athletic-trainer-email-form.component.css']
})
export class AthleticTrainerEmailFormComponent implements OnInit {
    constructor(private athleticTrainerEmailService: AthleticTainerEmailServiceService) {}

    ngOnInit(): void {}
    isVisible = true;

    /**
     * Pass the email information to the service
     * @param userEmail
     * @param trainerEmail
     * @param injuryFile
     */
    setEmail(userEmail: HTMLInputElement, trainerEmail: HTMLInputElement, injuryFile: HTMLInputElement): void {
        this.athleticTrainerEmailService
            .sendEmail(userEmail.value, trainerEmail.value, injuryFile.value) /*Change this to file type**/
            .subscribe((response: Response) => {
                if (JSON.stringify(response)) {
                    //Display confirmation text on screen
                    this.isVisible = false;
                } else {
                    //Post an alert for the user saying email error
                    alert('ERROR: ' + JSON.stringify(response));
                    console.log('ERROR: ' + JSON.stringify(response));
                }
            });
    }
}
