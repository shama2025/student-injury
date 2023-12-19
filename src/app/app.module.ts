import { NgModule, importProvidersFrom } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { SignUpPageComponent } from './sign-up-page/sign-up-page.component';
import { PatientOutcomeReportedMeasureTablePageComponent } from './patient-outcome-reported-measure-table-page/patient-outcome-reported-measure-table-page.component';

@NgModule({
    declarations: [AppComponent, LoginPageComponent, SignUpPageComponent, PatientOutcomeReportedMeasureTablePageComponent],
    imports: [BrowserModule, AppRoutingModule, HttpClientModule],
    providers: [],
    bootstrap: [AppComponent]
})
export class AppModule {}
