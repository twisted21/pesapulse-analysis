"""
Day 1 - API Data Analysis Using Python Structures
Squad Python Specialization - Data Science, AI & Analytics
"""
import json
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import requests

API_URL = "https://jsonplaceholder.typicode.com/users"


def get_customers(url: str = API_URL) -> list[dict]:
    """Fetch the customer list. Report failures clearly instead of crashing."""
    try: 
        response = requests.get(url)#request customer data
        response.raise_for_status()#check for errors
        customers = response.json()#convert json to python data
        return customers

    except requests.exceptions.RequestException as e:
        print("could not retrieve data from API:", e) #show the error
        return [] #return an empty list if there was an error
    
        


def explore(record: dict, indent: int = 0) -> None:
    """Print every key in a (possibly nested) record with its type, indented by depth."""
    for key, value in record.items():# go through each key and value
        print(" " * indent + f"{key}: {type(value).__name__}")# print key and type


        if type(value) == dict:# if the value is a dictionary, call explore recursively
            explore(value, indent + 2)# explore the nested dictionary with increased indentation


def extract_attributes(customers: list[dict]) -> list[dict]:
    """Return one flat dict per customer with the attributes listed in the task."""
    rows = [] #store customer information 
    for customer in customers: #go through each customer
        address = customer["address"] #get the address of the customer
        geo = address["geo"] #get the geo information of the customer
        company = customer["company"] #get the company information of the customer  


        row = { #create a new dictionary with the required attributes
           "customer_id": customer["id"],
            "name": customer["name"],
            "username": customer["username"],
            "email": customer["email"],
            "email_domain": customer["email"].rsplit(".", 1)[-1],
            "phone": customer["phone"],
            "city": address["city"],
            "zipcode": address["zipcode"],
            "latitude": float(geo["lat"]),
            "longitude": float(geo["lng"]),
            "company": company["name"],
            "website": customer["website"],
        }


        rows.append(row) #add the new dictionary to the list of rows
    return rows #return the list of rows or customers with the required attributes



def unique_cities(customers: list[dict]) -> set[str]:
    """Return the set of distinct cities."""

    cities = set() #create an empty set to store unique cities a set does not kee duplicates 
    for customer in customers: #go through each customer
        cities.add(customer["address"]["city"]) #add the city of the customer to the set
    return cities #return the set of unique cities



def city_counts(customers: list[dict]) -> dict[str, int]:
    """Count customers per city using a loop and/or a dict comprehension (no Counter, no pandas)."""
    counts = {} #create an empty dictionary to store the counts of customers per city
    for customer in customers: #go through each customer
        city = customer["address"]["city"] #get the city of the customer
        if city in counts: #if the city is already in the dictionary, increment the count
            counts[city] += 1
        else: #if the city is not in the dictionary, add it with a count of 1
            counts[city] = 1
    return counts #return the dictionary of counts of customers per city


def email_domain_counts(customers: list[dict]) -> dict[str, int]:
    """Count customers per email top-level domain (e.g. 'biz', 'tv')."""
    counts = {} #create an empty dictionary to store the counts of customers per email domain
    for customer in customers: #go through each customer
        email = customer["email"] #get the email of the customer
        domain = email.rsplit(".", 1)[-1] #get the ending of email
        
        
        if domain in counts: #if the domain is already in the dictionary, increment the count
            counts[domain] += 1
        else: #if the domain is not in the dictionary, add it with a count of 1
            counts[domain] = 1
    
    
    return counts #return the dictionary of counts of customers per email domain


def to_dataframe(rows: list[dict]) -> pd.DataFrame:
    """Convert a list of dicts to a pandas DataFrame."""
    return pd.DataFrame(rows) #convert the list of dictionaries to a pandas DataFrame and return it


def plot_distribution(counts: dict[str, int], path: Path) -> None:
    """Save a labelled chart of the distribution to path."""
    labels = list(counts.keys()) #get the labels for the chart from the keys of the counts dictionary
    values = list(counts.values()) #get the values for the chart from the values of

    plt.figure(figsize=(10, 6)) #create a new figure with a specified size
    plt.bar(labels, values) #create a bar chart with the labels and values

    plt.title("customer distribution by city")#add a title to the chart
    plt.xlabel("City")#add a label to the x-axis
    plt.ylabel("Number of Customers")#add a label to the y-axis

    plt.xticks(rotation=45, ha="right")#rotate the x-axis labels for better readability

    plt.tight_layout()#prevents lavels from beig cut off
    plt.savefig(path)#save chart as an image to the specified path
    plt.close()#close the chart





if __name__ == "__main__":
    customers = get_customers()
    print(f"Retrieved {len(customers)} customers") # count customers


    if customers:
        explore(customers[0])  # Explore the first customer

if __name__ == "__main__":
    customers = get_customers()  # Retrieve customer data

    cities = unique_cities(customers)  # Find unique cities

    print("Unique cities:", len(cities))  # Count unique cities
    print(cities)  # Display the cities


if __name__ == "__main__":
    customers = get_customers()  # Retrieve customer data

    domains = email_domain_counts(customers)  # Count email endings

    print("Email domains:", domains)  # Display the counts


if __name__ == "__main__":
    customers = get_customers()
    print("Number of customers:", len(customers))
    print("First customer:", customers[0] if customers else "No data")



if __name__ == "__main__":
    # Retrieve customer data
    customers = get_customers()

    # Create the output folder if it does not exist
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)

    # Prepare the customer data
    rows = extract_attributes(customers)
    df = to_dataframe(rows)

    # Save customer information to CSV
    df.to_csv(output_folder / "customers.csv", index=False)

    # Count customers in each city
    counts = city_counts(customers)

    # Sort cities by customer count, then alphabetically
    sorted_counts = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    # Create and save the city counts table
    city_df = pd.DataFrame(
        sorted_counts,
        columns=["city", "customer_count"]
    )
    city_df.to_csv(output_folder / "city_counts.csv", index=False)

    # Create and save the chart
    plot_distribution(counts, output_folder / "customer_distribution.png")

    # Count unique cities and email endings
    cities = unique_cities(customers)
    domains = email_domain_counts(customers)

    # Print the findings
    print("Customers retrieved :", len(customers))
    print("Unique cities       :", len(cities))

    if sorted_counts:
        city, count = sorted_counts[0]
        print("Most common city    :", f"{city} ({count})")

    print("Email domains       :", domains)
    print("Chart saved to      :", output_folder / "customer_distribution.png")





    