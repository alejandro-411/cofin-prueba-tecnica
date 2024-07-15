import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-data-table',
  templateUrl: './data-table.component.html',
  styleUrls: ['./data-table.component.css']
})

export class DataTableComponent implements OnInit {
  data: any[] = [];
  statistics: any = {};

  constructor(private http: HttpClient) { }

  ngOnInit(): void {
  }


/**
 * Loads a CSV file and processes the data.
 */
 loadCSV(): void {
    this.http.get('assets/resultados_personales.csv', { responseType: 'text' })
      .subscribe(
        data => this.processData(data),
        error => console.error('Error loading CSV:', error)
      );
  } 

  

  /**
   * Processes the data by making an HTTP GET request to 'http://localhost:5000/process'.
   * It logs the response, loads the data, and loads the statistics.
   * If an error occurs, it logs the error message.
   */
  processData(): void {
    this.http.get('http://localhost:5000/process').subscribe(
      response => {
        console.log(response);
        this.loadData();
        this.loadStatistics();
      },
      error => console.error('Error processing data:', error)
    );
  }

  /**
   * Loads data from the server.
   */
  loadData(): void {
    this.http.get<any[]>('http://localhost:5000/data').subscribe(
      data => this.data = data,
      error => console.error('Error loading data:', error)
    );
  }


  /**
   * Loads the statistics data from the server.
   */
  loadStatistics(): void {
    this.http.get<any>('http://localhost:5000/statistics').subscribe(
      stats => this.statistics = stats,
      error => console.error('Error loading statistics:', error)
    );
  }
}