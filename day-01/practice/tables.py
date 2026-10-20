choice = input("Press 'Q' to quit or any other key to continue: ").lower()

while choice != 'q':
    try:
        num = int(input("Enter the number you want the table for: "))
        for i in range(1, 11):
            value = num * i
            print(f"{num} * {i} = {value}")
    except ValueError:
        print("Please enter a valid number.")

    # Update choice at the end of every loop iteration
    choice = input("\nPress 'Q' to quit or any other key to continue: ").lower()

print("Goodbye!")