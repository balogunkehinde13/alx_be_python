size = int(input("Enter the size of the pattern: "))

# Make sure the input is a positive integer
if size <= 0:
    print("Please enter a positive integer.")
else:
    # Initialize row counter
    row = 0
    
    # Use while loop to iterate through rows
    while row < size:
        # Use for loop to print asterisks side by side
        for col in range(size):
            print("*", end="")
        
        # Print newline after each row
        print()
        
        # Move to next row
        row += 1