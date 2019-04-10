import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { last } from "@angular/router/src/utils/collection";

@Injectable() 
export class EmotionsService {
  constructor(private http: HttpClient) {

  }
  baseUrl: string = "api/MovieEmotions";

  getEmotions() {
    return this.http.get<any[]>(this.baseUrl);
  }

}