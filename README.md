# Pesa Pulse Customer Analysis

## Project Overview

This project retrieves customer data from an API, explores the data, and performs a simple customer analysis using Python.

The project focuses on customer locations and email domains. It also saves the cleaned customer data and analysis results as CSV files and creates a bar chart showing the distribution of customers by city.

## Tools and Libraries

- Python
- Requests: retrieves customer data from the API.
- Pandas: organizes customer data into tables and saves CSV files.
- Matplotlib: creates the bar chart.
- uv: manages project dependencies and the Python environment.

## Data Source

The project uses the JSONPlaceholder Users API:

https://jsonplaceholder.typicode.com/users

## Project Outputs

The program creates the following files in the `output/` folder:

- `customers.csv`: flattened customer information, including names, email domains, locations, and company details.
- `city_counts.csv`: customer counts for each city, sorted by customer count and city name.
- `customer_distribution.png`: a bar chart showing the number of customers in each city.

## How to Run

1. Clone or download the project.
2. Open the project folder in a terminal.
3. Install the project dependencies using uv:

   ```bash
   uv sync
   ```

4. Run the analysis:

   ```bash
   uv run python analysis.py
   ```

## Analysis Summary

The program reports the total number of customers retrieved, the number of unique cities, the most common city, and the distribution of email domains.

## Purpose

This project demonstrates basic API data retrieval, data exploration, data transformation, descriptive analysis, CSV file generation, and data visualization using Python.