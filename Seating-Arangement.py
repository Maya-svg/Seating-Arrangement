import csv
import random

bank = [] # an array of all the students in the school 
tableNumber = 0 
Worked_before = [] #array of the current waiters and kitchen crew 

def removal_function(): #function that removes the waiters and kitchen crew out of the bank
        bank.remove(row) 


with open('Dinner Seating - New Student List 2018-19.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file) 

    for row in csv_reader:

        bank.append((row[0],row[1]))
    del bank[0] #deletes the header in the file 

    Kitchen_crew = random.sample(bank, 7) # 7 random people are chosen out of the bank array and put into the variable Kitchen_crew
   
    for row in Kitchen_crew:
        # all 7 people's fist and last names as well as the label "Kitchen_crew" is added to the "worked_before" array 
        Worked_before.append(((row[0],row[1]), 'Kitchen_crew')) 
        removal_function() #their names are removed from the bank array

    waiters = random.sample(bank,31) # 31 random people are chosen out of the bank array and put into the variable waiters 

    for row in waiters:
        tableNumber += 1  # the tablenumber increases 
        # all 31 people's fist and last names as well as the label "w" is added to the "worked_before" array 
        Worked_before.append((row[0],row[1],str(tableNumber) + 'w'))  
        removal_function() #their names are removed from the bank array
    print(Worked_before) 
    tableNumber = 1 #tablenumber is reset to 1
    random.shuffle(bank) # the people left in the bank are shuffle 

    for i in range (0, 27, 9): #the first 27 people are grouped into 3 groups of nine and get seated at the first 3 tables 
        for row in bank[i:i+9]:
            print(f'row is {row}, table is {tableNumber}') 
        tableNumber += 1 

    for i in range(28, len(bank), 8): # the remainder of the students are grouped 8 per table 
        for row in bank[i:i+8]:
            print(f'row is {row}, table is {tableNumber}') 
        tableNumber += 1 
