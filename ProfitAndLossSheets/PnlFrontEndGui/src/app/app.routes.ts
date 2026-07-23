import { Routes } from '@angular/router';
import { UserConfigs} from '../Admin/user-configs/user-configs';
import { Home } from '../home/home';




export const routes: Routes = [
    {path: "home", component: Home },
    {path: "user-configs", component: UserConfigs},
    {path: "", redirectTo: '/home', pathMatch: "full"},
    {path: "**", redirectTo: '/home'}
];
