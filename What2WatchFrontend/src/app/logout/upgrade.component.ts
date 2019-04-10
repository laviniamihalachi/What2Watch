import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-logout',
  templateUrl: './upgrade.component.html',
})
export class LogoutComponent implements OnInit {

  constructor() { }

  ngOnInit() {
    alert("Esti blocat pe veci in aceasta pagina!");
  }

}