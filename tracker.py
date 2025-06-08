import pandas as pd
import os

DATA_FILE = 'data/application.csv'

def add_job():
    company = input("Company: ")
    title = input("Job Title: ")
    status = input("Status (Applied, Interview, Offer, etc.): ")

    new_entry = {
        "Company": company,
        "Title": title,
        "Status": status
    }

    # If file exists, load it; if not, create a new one.
    if os.path.exists(DATA_FILE):
        df = pd.read_csv(DATA_FILE)
        df = df.append(new_entry, ignore_index=True)
    else:
        df = pd.DataFrame([new_entry])

    df.to_csv(DATA_FILE, index=False)
    print("Job application added.")

def view_jobs():
    if not os.path.exists(DATA_FILE):
        print("No job applications found.")
        return
    
    df = pd.read_csv(DATA_FILE)
    print("\nYour job applications:")
    print(df.to_string(index=False))

def edit_job():
    if not os.path.exists(DATA_FILE):
        print("No job applications found.")
        return
    
    df = pd.read_csv(DATA_FILE)
    print(df.to_string())

    try:
        index = int(input("Enter the index of the job you want to edit: "))
        if index < 0 or index >= len(df):
            print("Invalid index.")
            return
        print("Leave blank to keep current value.")
        company = input(f"Company [{df.loc[index, 'Company']}]: ") or df.loc[index, 'Company']
        title = input(f"Job Title [{df.loc[index, 'Title']}]: ") or df.loc[index, 'Title']
        status = input(f"Status [{df.loc[index, 'Status']}]: ") or df.loc[index, 'Status']

        df.loc[index] = [company, title, status]
        df.to_csv(DATA_FILE, index=False)
        print("Job application updated.")
    except ValueError:
        print("Please enter a valid number.")

def delete_job():
    if not os.path.exists(DATA_FILE):
        print("No job applications found.")
        return
    
    df = pd.read_csv(DATA_FILE)
    print(df.to_string())

    try:
        index = int(input("Enter the index of the job you want to delete: "))
        if index < 0 or index >= len(df):
            print("Invalid index.")
            return
        confirm = input(f"Are you sure you want to delete this job? (y/n): ")
        if confirm.lower() == "y":
            df = df.drop(index).reset_index(drop=True)
            df.to_csv(DATA_FILE, index=False)
            print("Job application deleted.")
        else:
            print("Deletion canceled.")            
    except ValueError:
        print("Please enter a valid number.")

def search_jobs():
    try: 
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No data found.")
        return
    keyword = input("Enter a keyword to search (company, title, status etc.): ").lower()

    # Search across all columns
    matches = df[df.apply(lambda row: keyword in row.astype(str).str.lower().to_string(), axis=1)]

    if matches.empty:
        print("No matching job applications found.")
    else:
        print("\nMatching Job Applications:\n")
        print(matches.to_string(index=False))