import { Component, OnInit } from '@angular/core';

declare const $: any;
declare interface RouteInfo {
    path: string;
    title: string;
    icon: string;
    class: string;
}

//WHERE SIDEBAR HAPPENS
export const ROUTES: RouteInfo[] = [
    { path: '/dashboard', title: 'Explore',  icon: 'dashboard', class: '' },
    { path: '/user-profile', title: 'Profile',  icon:'person', class: '' },
    { path: '/table-list', title: 'Collection',  icon:'content_paste', class: '' },
    { path: '/upgrade', title: 'Logout',  icon:'unarchive', class: 'active-pro' },
];

@Component({
  selector: 'app-sidebar',
  templateUrl: './sidebar.component.html',
  styleUrls: ['./sidebar.component.css']
})
export class SidebarComponent implements OnInit {
  menuItems: any[];

  constructor() { }

  ngOnInit() {
    this.menuItems = ROUTES.filter(menuItem => menuItem);
  }
  isMobileMenu() {
      if ($(window).width() > 991) {
          return false;
      }
      return true;
  };
}
