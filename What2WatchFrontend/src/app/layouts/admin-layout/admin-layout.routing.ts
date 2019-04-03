import { Routes } from '@angular/router';

import { DashboardComponent } from '../../explore/dashboard.component';
import { UserProfileComponent } from '../../profile/user-profile.component';
import { TableListComponent } from '../../collection/table-list.component';
import { TypographyComponent } from '../../theme/typography/typography.component';
import { IconsComponent } from '../../theme/icons/icons.component';
import { MapsComponent } from '../../theme/maps/maps.component';
import { NotificationsComponent } from '../../theme/notifications/notifications.component';
import { UpgradeComponent } from '../../theme/upgrade/upgrade.component';

export const AdminLayoutRoutes: Routes = [
    { path: 'explore',      component: DashboardComponent },
    { path: 'profile',   component: UserProfileComponent },
    { path: 'collection',     component: TableListComponent },
    { path: 'logout',        component: UpgradeComponent },
];
