# Pesa Pulse Customer Data Analysis

## Project Overview

Pesa Pulse is a Python project that retrieves customer information from the JSONPlaceholder API, explores the data, and performs a simple analysis using Python data structures and pandas.

The goal is to understand the customer data, identify the cities customers come from, count email domains, and present the findings using CSV files and charts.

## Data Source

The project uses the JSONPlaceholder API:

https://jsonplaceholder.typicode.com/users

The API provides sample customer information, including names, usernames, email addresses, phone numbers, addresses, and company details.

## Tools and Libraries

- Python: Main programming language.
- Requests: Retrieves customer data from the API.
- Standard Python structures: Dictionaries, lists, sets, and dictionary comprehensions are used to explore and analyze the data.
- Pandas: Organizes the extracted information into a DataFrame and verifies the analysis.
- Matplotlib: Creates charts to show customer distributions.
- Pathlib: Handles output folder and file paths.

## Project Process

1. Retrieve data: The script sends a request to the API and retrieves the customer records.
2. Explore the data: It examines the keys and data types, including nested dictionaries.
3. Extract attributes: It collects useful customer information into a flat structure, including customer ID, name, email, email domain, city, ZIP code, latitude, longitude, company, and website.
4. Analyze the data: Sets identify unique cities and email domains, while dictionaries count customers in each category.
5. Use pandas: The extracted information is converted into a DataFrame. Its shape and data types are displayed, and pandas is used to verify the email-domain counts.
6. Visualize the results: Matplotlib creates charts showing the distribution of customers by city and email domain.

## Working with Nested Data

Some customer information is stored inside nested dictionaries. The project extracts values using attribute paths such as:

- `customer["address"]["city"]`
- `customer["address"]["zipcode"]`
- `customer["address"]["geo"]["lat"]`
- `customer["address"]["geo"]["lng"]`
- `customer["company"]["name"]`

These paths make it possible to access information stored several levels inside a customer record.

## Key Findings

The API returned 10 customer records.

- Total customers: 10
- Unique cities: 10
- Email domains: 10 different domains

The email-domain counts were:

Email Domain  Number of Customers

billy.biz         1

annie.ca          1

melissa.tv        1

jasper.info       1

april.biz         1

karina.biz        1

kory.org          1

dana.io           1

yesenia.net       1

rosalind.me       1

Each customer comes from a different city, so the number of unique cities is equal to the total number of customers. This means there is no repeated city in this sample.

The biz email domain appears most frequently, with three customers. The remaining seven domains each appear once.

The custom Python email-domain counts were also compared with pandas value_counts(). Both methods produced matching results, which helped verify the analysis.

## Output Files

The script saves the following files in the output folder:

- customers.csv – Contains the extracted customer information.
- city_counts.csv – Contains the number of customers in each city.
- customer_distribution.png - Shows the customer distribution by city.
- email_domain_distribution.png - Shows the customer distribution by email domain.

## Why the Charts Are Useful

The city chart makes it easier to see how customers are distributed across different cities. The email-domain chart helps identify which email providers or domains appear most frequently.

Of the two charts, I find the email-domain chart more useful because it makes it easier to identify the most common email domain. The city chart is also useful, but since every customer comes from a different city, it does not show much variation in this dataset.

Charts make the results easier to understand than looking at numbers in a CSV file alone.

## How to Run the Project

Install the required libraries:

```bash
pip install requests pandas matplotlib
```

Run the Python script:

```bash
python analysis.py
```

The script retrieves the data, performs the analysis, and saves the output files in the output folder.

## Conclusion

This project provided practical experience working with API data and Python data structures. It also showed how dictionaries and sets can be used for analysis before using pandas to organize and verify the results. Combining Python, pandas, and Matplotlib made it possible to turn raw customer data into useful information and visual summaries.