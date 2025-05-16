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