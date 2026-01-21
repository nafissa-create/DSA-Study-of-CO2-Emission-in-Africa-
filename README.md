# CO₂ Emissions Analysis in Africa

## Context
This project was developed as part of the course **Data Structures and Algorithms** .  
It focuses on analyzing CO₂ emissions data across African countries using algorithmic logic, data structures, and user-driven queries.

## Objective
The objective of this project is to analyze CO₂ emissions in Africa and provide flexible ways to explore the data by country, year, sector, and emission trends, while applying appropriate data structures and algorithmic reasoning.

## Dataset Overview
The dataset contains CO₂ emissions data for African countries from **2000 to 2020**, including:
- Total CO₂ emissions
- Emissions by sector (energy, transportation, manufacturing, land-use change, etc.)
- Country and year identifiers

## Project Features
The program allows users to interact with the dataset through several functionalities:

1. **Search emissions by country, year, and sector**  
   - View CO₂ emissions by sector for a selected country  
   - Option to view data for all years or a specific year  

2. **Compute total CO₂ emissions across Africa**  
   - Calculates total emissions for all African countries  
   - Allows querying a specific year or viewing totals across all years  

3. **Identify the highest emitting country**  
   - Determines the country with the highest CO₂ emissions for a given year  
   - Option to view results across all years  

4. **Aggregate emissions by sector**  
   - Displays emissions for all sectors in a tabular format  
   - Allows analysis of a specific sector across years or for a specific year  

5. **Track emission trends by country**  
   - Displays year-by-year emission trends for a selected country  
   - Option to query a specific year  

6. **Insert new emission records (simulation)**  
   - Simulates real-time data entry by allowing user input  
   - Automatically handles missing and numeric values  
   - Appends the new record to the dataset  

7. **Undo last insertion**  
   - Removes the most recently added emission record  
   - Restores the dataset to its previous state  

## Methodology
- Data loading and manipulation using pandas  
- Use of dictionaries to store and retrieve emissions efficiently  
- Iterative processing of dataset records  
- Input validation and error handling  
- Algorithmic aggregation and comparison of emission values  

## Tools and Technologies
- Python  
- pandas  

## Results
The project produces:
- Tabular emission summaries  
- Country-level and sector-level insights  
- Identification of emission trends and top emitters  
- A flexible command-line interface for interactive data exploration  

## How to Run

1. Clone the repository:
```bash
git clone https://github.com/nafissa-create/DSA-Study-of-CO2-Emission-in-Africa-.git
cd DSA-Study-of-CO2-Emission-in-Africa-
pip install pandas
python applicationName.py

