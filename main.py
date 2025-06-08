from tracker import add_job, view_jobs, edit_job, delete_job, search_jobs

def main():
    while True:
        print("\nJob Tracker Menu:")
        print("\n1. Add a new job application")
        print("\n2. View all job applications")
        print("\n3. Edit a job application")
        print("\n4. Delete a job application")
        print("\n5. Search job applications")
        print("\n6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            edit_job()
        elif choice == "4":
            delete_job()
        elif choice == "5":
            search_jobs()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print ("Invalid option. Try again.")

if __name__ == "__main__":
    main()