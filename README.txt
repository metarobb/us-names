SSA Name Search

This is a Python script called ‘name.py’ that searches for a given name in the Social Security Administration's (SSA) National Data on the relative frequency of given names in the population of U.S. births.

The SSA data is tabulated based on Social Security records as of March 6, 2022, and provides information on the relative frequency of given names in the population of U.S. births where the individual has a Social Security Number. For each year of birth YYYY after 1879, the SSA has created a comma-delimited file called ‘yobYYYY.txt’. Each record in the individual annual files has the format "name,sex,number," where name is 2 to 15 characters, sex is M (male) or F (female), and "number" is the number of occurrences of the name. Each file is sorted first on sex and then on number of occurrences in descending order. When there is a tie on the number of occurrences, names are listed in alphabetical order. This sorting makes it easy to determine a name's rank. The first record for each sex has rank 1, the second record for each sex has rank 2, and so forth. To safeguard privacy, the list of names is restricted to those with at least 5 occurrences.


Usage:
To use the script, simply download the ‘name.py’ file and the ‘ssa_data’ directory and place them in a directory on your computer. Then, run the ‘name.py’ file and enter a name to search for when prompted. The script will search for the given name in each year from 1880 to 2022 and print a message for each year where the name was found. The message includes the year, the number of occurrences of the name, and the sex of the individuals who were given the name. After searching through all of the years, the script prints a message indicating whether or not the name was found and how many times it was found in total.
The script will continue to prompt the user to enter names to search for until the user manually interrupts the program by pressing "CONTROL+c".

Requirements:
This script requires Python 3.x and the following standard Python modules:

	•	os


License:
This script is released under the MIT License.
