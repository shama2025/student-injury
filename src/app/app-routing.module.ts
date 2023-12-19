import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { PatientOutcomeReportedMeasureTablePageComponent } from './patient-outcome-reported-measure-table-page/patient-outcome-reported-measure-table-page.component';

const routes: Routes = [
    { path: '', component: LoginPageComponent },
    { path: 'sign/up', component: SignUpPageComponent },
    {path : 'patient-outcome-reported-measure', component:PatientOutcomeReportedMeasureTablePageComponent}
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule {}
