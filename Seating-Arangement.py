import csv
import random

bank = []
tableNumber = 0 
Worked_before = [] 

def removal_function():  
        bank.remove(row) 


with open('Dinner Seating - New Student List 2018-19.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file) 

    for row in csv_reader:

        bank.append((row[0],row[1]))
    del bank[0]

    Kitchen_crew = random.sample(bank, 7) 
   
    for row in Kitchen_crew:
        Worked_before.append(((row[0],row[1]), 'Kitchen_crew'))
        removal_function() 

    waiters = random.sample(bank,31) 

    for row in waiters:
        tableNumber += 1  
        Worked_before.append((row[0],row[1],str(tableNumber) + 'w'))  
        removal_function() 
    
    tableNumber = 1
    random.shuffle(bank)

    for i in range (0, 27, 9): #make this a function? 
        for row in bank[i:i+9]:
            print(f'row is {row}, table is {tableNumber}') 
        tableNumber += 1 

    for i in range(28, len(bank), 8):
        for row in bank[i:i+8]:
            print(f'row is {row}, table is {tableNumber}') 
        tableNumber += 1 
