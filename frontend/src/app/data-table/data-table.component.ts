import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-data-table',
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.css']
})
export class DataTableComponent implements OnInit {
  data: any[] = [];
  statistics: any[] = [];

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
   this.http.get('')
  }

}
