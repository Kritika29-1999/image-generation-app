import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { ImageService } from './services/image.service';
import { response } from 'express';
import { FormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { error } from 'node:console';


@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'image-generation-app';
  prompt: string = '';
  imageUrl: string | null = null;
  loading: boolean = false;

  constructor(private imageService: ImageService){

  }
  generateImage(){
    if(!this.prompt.trim())
      return;
    this.loading = true;
    this.imageService.generateImage(this.prompt)
  .subscribe(
    (response) => {
      console.log("API Response:", response); // Check if image_url is coming
      this.imageUrl = response.image_url;
    this.loading = false;
    },
    (error) => {
      console.error("Error generating image", error);
    }
  );

    
    
  }
}
