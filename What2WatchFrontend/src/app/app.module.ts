import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { HttpModule } from '@angular/http';
import { RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';


import { AppRoutingModule } from './app.routing';
import { ComponentsModule } from './components/components.module';

import { AppComponent } from './app.component';

import { DashboardComponent } from './explore/dashboard.component';
import { UserProfileComponent } from './profile/user-profile.component';
import { TableListComponent } from './collection/table-list.component';
import { TypographyComponent } from './theme/typography/typography.component';
import { IconsComponent } from './theme/icons/icons.component';
import { MapsComponent } from './theme/maps/maps.component';
import { NotificationsComponent } from './theme/notifications/notifications.component';
import { LogoutComponent } from './logout/upgrade.component';
import {
  AgmCoreModule
} from '@agm/core';
import { AdminLayoutComponent } from './layouts/admin-layout/admin-layout.component';
import { EmotionsService } from './services/emotions.service';

@NgModule({
  imports: [
    BrowserAnimationsModule,
    FormsModule,
    HttpModule,
    ComponentsModule,
    RouterModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  declarations: [
    AppComponent,
    AdminLayoutComponent,
  ],
  providers: [
    EmotionsService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
