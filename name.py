import os

# Define the folder path where the SSA data is stored
folder_path = "ssa_data"

# Loop indefinitely until the user manually interrupts the program
try:
    while True:
        # Prompt the user to enter a name to search for
        name = input("Please enter a name to search for (press CONTROL+c to exit): ")
        # Initialize a flag variable to track if the name was found
        name_found = False
        # Initialize a variable to store the total number of occurrences of the name
        total_occurrences = 0

        # Loop through each year from 1880 to 2022
        for year in range(1880, 2023):
            # Construct the file name for the given year
            file_name = "yob" + str(year) + ".txt"
            # Construct the file path for the given year
            file_path = os.path.join(folder_path, file_name)
            # Check if the file exists
            if os.path.exists(file_path):
                # Open the file for reading
                with open(file_path, "r") as file:
                    # Loop through each line in the file
                    for line in file:
                        # Split the line into its components (name, sex, number)
                        components = line.strip().split(",")
                        # Check if the name matches the given name and the sex is either M or F
                        if components[0].lower() == name.lower() and components[1] in ["M", "F"]:
                            # Increment the total number of occurrences of the name
                            total_occurrences += int(components[2])
                            # Set the name_found flag to True
                            name_found = True
                            # Print the year and the number of occurrences of the name
                            print(f"In {year}, {components[2]} {components[1]}'s were named {name}.")
        # Print a message indicating whether or not the name was found
        if name_found:
            print(f"{name} was found {total_occurrences} times in the data.")
        else:
            print(f"{name} was not found in the data.")
        # Print a blank line to separate the output for different names
        print()

# Catch the KeyboardInterrupt exception and exit the program cleanly
except KeyboardInterrupt:
    print("\nProgram exited.")
