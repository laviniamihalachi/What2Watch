import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-table-list',
  templateUrl: './table-list.component.html',
  styleUrls: ['./table-list.component.css']
})
export class TableListComponent implements OnInit {

  constructor() { }

  statusesList: any[] = ["all", "watched", "recommended", "on watch list"];
  selectedStatus: string = "all";

  changeStatus(event) {
    if (event.isUserInput == true) {
      this.selectedStatus = event.source.value;
    }
  }

  collectionCardsList = [
    {
      movieTitle: "Movie Title",
      status: "watched",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "recommended",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "on watch list",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "watched",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "recommended",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "on watch list",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "watched",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "recommended",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "on watch list",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "watched",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "recommended",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "on watch list",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "watched",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "recommended",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
    {
      movieTitle: "Movie Title",
      status: "on watch list",
      image: "https://m.media-amazon.com/images/M/MV5BMjUyNjg1ODIwMl5BMl5BanBnXkFtZTgwNjMyOTYzNzM@._V1_SY1000_CR0,0,640,1000_AL_.jpg",
    },
  ];

  ngOnInit() {
  }

}
