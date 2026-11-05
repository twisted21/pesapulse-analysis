"""
Day 1 - API Data Analysis Using Python Structures
Squad Python Specialization - Data Science, AI & Analytics
"""
import json
from pathlib import Path #import Path from pathlib to handle file paths

import matplotlib.pyplot as plt #plotting library for creating visualizations
import pandas as pd #data analysis library for handling tabular data
import requests #library for making HTTP requests to APIs

API_URL = "https://jsonplaceholder.typicode.com/users"


def get_customers(url: str = API_URL) -> list[dict]:
    """Fetch the customer list. Report failures clearly instead of crashing."""
    try: 
        response = requests.get(url, timeout=10)#request customer dataand wait upto 10 seconds for a response
        
        response.raise_for_status()#check for errors
        
        customers = response.json()#convert json to python data
        
        return customers

    except requests.exceptions.RequestException as e:
        
        print("could not retrieve data from API:", e) #show the error if the API requests fails
        
        return [] #return an empty list if there was an error
    
        


def explore(record: dict, indent: int = 0) -> None:
    """Print every key in a (possibly nested) record with its type, indented by depth."""
    
    for key, value in record.items():# go through each key and value
        
        print(" " * indent + f"{key}: {type(value).__name__}")# print key and type


        if isinstance(value, dict):# if the value is a dictionary, call explore recursively
            
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
            "email_domain": customer["email"].rsplit(".", 1)[-1], #extract the email domain by splitting the email string at the last dot and taking the last part
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

    cities = set() #create an empty set to store unique cities a set does not keep duplicates 
   
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
       
        else: #if the city is not in the dictionary, adds th city as new key in the dictionary with a count of 1
            counts[city] = 1
    
    return counts #return the dictionary of counts of customers per city


def email_domain_counts(customers: list[dict]) -> dict[str, int]:
    """Count customers per email top-level domain (e.g. 'biz', 'tv')."""
    # Create a set containing only unique email endings
    domains = {
        customer["email"].split("@")[-1]
        for customer in customers
    }

    # Create a dictionaryusing dictionary comprehension where each email domain is a key
    #each domain becomes a key in the dictionary and the value is the count of customers with that domain
    # sum() counts how many customers have that particular domain
    counts = {domain: sum(
        # For each customer, add 1 if their email domain matches the current domain
        1 for customer in customers
            if customer["email"].split("@")[-1] == domain
        )
        for domain in domains
    }
    return counts #Return the dictionary containing email domain counts


def to_dataframe(rows: list[dict]) -> pd.DataFrame:
    """Convert a list of dicts to a pandas DataFrame."""

    return pd.DataFrame(rows) #convert the list of dictionaries to a pandas DataFrame and return it


def plot_distribution(counts: dict[str, int], path: Path, title:str, xlabel:str ) -> None:
    """Save a labelled chart of the distribution to path."""
    labels = list(counts.keys()) #get the labels for the chart from the keys of the counts dictionary
    values = list(counts.values()) #get the values for the chart from the values of

    plt.figure(figsize=(10, 6)) #create a new figure with a specified size
    plt.bar(labels, values) #create a bar chart with the labels and values

    plt.title(title)#add a title to the chart
    plt.xlabel(xlabel)#add a label to the x-axis
    plt.ylabel("Number of Customers")#add a label to the y-axis

    plt.xticks(rotation=45, ha="right")#rotate the x-axis labels for better readability

    plt.tight_layout()#prevents lavels from beig cut off
    plt.savefig(path)#save chart as an image to the specified path
    plt.close()#close the chart



#main program execution starts here, 
# only runs if the script is executed directly

if __name__ == "__main__":
    # 1. Retrieve customer data only once
    customers = get_customers()

    # Stop the program if no customer data was retrieved
    if not customers:
        raise SystemExit("No customer data retrieved. Stopping analysis.")

    # Display the number of customers retrieved
    print(f"Retrieved {len(customers)} customers")



    # 2. Explore the structure of the first customer
    print("\nExploring the first customer:")
    explore(customers[0])


    # 3. Find unique cities
    cities = unique_cities(customers) 

    # Display the number and names of unique cities
    print("\nUnique cities:", len(cities)) # Count unique cities
    print(cities) #display the cities

    # 4. Count customers by email domain
    domains = email_domain_counts(customers)

    # Display email domain counts
    print("\nEmail domains:", domains)


    # 5. Access the existing output folder
    # Create it only if it does not already exist
    output_folder = Path("output")
    output_folder.mkdir(exist_ok=True)



    # 6. Prepare and flatten customer information
    rows = extract_attributes(customers)

    # 7. Convert customer information into a pandas DataFrame
    df = to_dataframe(rows)

    # 8. Save customer information to a CSV file
    df.to_csv(output_folder / "customers.csv", index=False)

    # 9. Display the shape of the DataFrame
    # Shape shows the number of rows and columns
    print("\nDataFrame shape:")
    print(df.shape)

    # Display the data type of each column
    print("\nDataFrame data types:")
    print(df.dtypes)

    # 10. Count customers in each city
    counts = city_counts(customers)

    # Sort cities by customer count first, then alphabetically
    sorted_counts = sorted(
        counts.items(),
        key=lambda item: (-item[1], item[0])
    )

    # 11. Create a DataFrame for city counts
    city_df = pd.DataFrame(
        sorted_counts,
        columns=["city", "customer_count"]
    )

    # Save the city counts to a CSV file
    city_df.to_csv(output_folder / "city_counts.csv", index=False)

    # 12. Create and save the city distribution chart
    plot_distribution(
        counts,
        output_folder / "customer_distribution.png",
        "Customer Distribution by City",
        "City"
    )

    # 13. Create and save the email domain distribution chart
    plot_distribution(
        domains,
        output_folder / "email_domain_distribution.png",
        "Customer Distribution by Email Domain",
        "Email Domain"
    )

    # 14. Verify email domain counts using pandas
    # value_counts() counts how frequently each email domain appears
    pandas_counts = df["email_domain"].value_counts().to_dict()

    # Display counts calculated using our Python dictionary
    print("\nEmail counts using our Python dictionary:")
    print(domains)

    # Display counts calculated using pandas
    print("\nEmail counts using pandas value_counts():")
    print(pandas_counts)

    # Compare both methods to check whether their results agree
    print("\nDo both counting methods agree?")
    print(domains == pandas_counts)

    # 15. Display the final findings
    print("\nFINAL FINDINGS")

    print("Customers retrieved:", len(customers))
    print("Unique cities:", len(cities))

    # Find and display the city with the highest customer count
    if sorted_counts:
        city, count = sorted_counts[0]
        print("Most common city:", f"{city} ({count})")

    print("Email domains:", domains)

    # Display the location of all saved output files
    print("\nFiles saved successfully:")
    print(output_folder / "customers.csv")
    print(output_folder / "city_counts.csv")
    print(output_folder / "customer_distribution.png")
    print(output_folder / "email_domain_distribution.png")




    


