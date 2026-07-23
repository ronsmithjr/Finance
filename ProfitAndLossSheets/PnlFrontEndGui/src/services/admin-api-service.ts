import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../environments/environment';
import { UserConfig } from '../models/userConfigsModel';



@Injectable({
  providedIn: 'root',
})
export class AdminApiService {
  private http: HttpClient = inject(HttpClient);
  private apiUrl: string = environment.apiUrl;

  
}
