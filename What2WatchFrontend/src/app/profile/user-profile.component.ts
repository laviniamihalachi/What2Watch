import { Component, OnInit } from '@angular/core';
import { EmotionsService } from '../services/emotions.service';

@Component({
  selector: 'app-user-profile',
  templateUrl: './user-profile.component.html',
  styleUrls: ['./user-profile.component.css'],
  providers: [EmotionsService]
})
export class UserProfileComponent implements OnInit {

  constructor(
    private emotionsService: EmotionsService,
  ) {
    this.emotionsService.getEmotions().subscribe(res => {
      console.warn(res);
    });
  }

  ngOnInit() {
  }

}
