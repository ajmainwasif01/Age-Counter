def age_checker():
    try:
        
        age = int(input("Enter your age: "))

        if age < 0:
            raise ValueError("Age cannot be negative.")
        
        if age % 2 == 0:
            print(f"The age {age} is even.")
        else:
            print(f"The age {age} is odd.")

    except ValueError as e:

        print(f"Invalid input: {e}")
    except Exception as e:

        print(f"An error occurred: {e}")

age_checker()
