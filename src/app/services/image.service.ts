import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ImageService {

  private apiUrl = 'http://127.0.0.1:8000/generate-image';

  constructor(
    private http: HttpClient
  ) { }
  generateImage(prompt: string): Observable<{ image_url: string }> {
    return this.http.post<{ image_url: string }>(this.apiUrl, { prompt });
  }
  
}
