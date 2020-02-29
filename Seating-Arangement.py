import csv
import random
import json 

bank = [] # an array of all the students in the school 
Worked_before = [] #array of the current waiters and kitchen crew 
tableNumber = 1 

def removal_function(): #function that removes the waiters and kitchen crew out of the bank
    bank.remove(row) 

def retrieval_function(): 
    Kitchen_crew = random.sample(bank, 7) # 7 random people are chosen out of the bank array and put into the variable Kitchen_crew 
    print('Kitchen_crew members are:',Kitchen_crew)
    for row in Kitchen_crew: # cant put a function in a function 
        # all 7 people's fist and last names as well as the label "Kitchen_crew" is added to the "worked_before" array 
        Worked_before.append(((row[0],row[1]), 'Kitchen_crew'))  
        bank.remove(row) #their names are removed from the bank array
    
    waiters = random.sample(bank,31) # 31 random people are chosen out of the bank array and put into the variable waiters 
    print('waiters are:', waiters)
    tableNumber = 0 
    
    for row in waiters:
        tableNumber += 1  # the tablenumber increases 
        # all 31 people's fist and last names as well as the label "w" is added to the "worked_before" array 
        Worked_before.append((row[0],row[1],str(tableNumber) + 'w'))  
        bank.remove(row) #their names are removed from the bank array

with open('Dinner Seating - Student List 2018-19.csv', 'r') as csv_file: 
    csv_reader = csv.reader(csv_file) 

    for row in csv_reader:
        bank.append((row[0],row[1])) 

#1rst seating
#   
    print(len(bank
    ))
    retrieval_function() # the kitchen_crew and waiters are taken out 
    tableNumber = 1 # tableNumber is set to 1 
    random.shuffle(bank) # the people left in the bank are shuffle  

    for i in range (0, 27, 9): #the first 27 people are grouped into 3 groups of nine and get seated at the first 3 tables 
        for row in bank[i:i+9]:
            print(f'row is {row}, table is {tableNumber}') 
        tableNumber += 1 

    for i in range(28, len(bank), 8): # the remainder of the students are grouped 8 per table 
        for row in bank[i:i+8]:
            print(f'first seating row is {row}, table is {tableNumber}')  
        tableNumber += 1 

    
# #2rd seating - how do i write the previous label and the new table assignment
    
#     print('2nd seating')

#     random.shuffle(bank) # the people left in the bank are shuffle 
#     tableNumber = 1 # tableNumber is set to 1 
#     print(len(Worked_before))

#     for i in range (0, 27, 9): # assign the previous workers to tables first 
#         for row in Worked_before[i:i+9]: # the first 27 people are put into groupss of 9 
#             Worked_before.append(((row[0],row[1]), tableNumber)) # new seats are added to the array 
#             print(f'second seating row is {row}, table {tableNumber}') 
#         tableNumber += 1 
#     # the error is here - repeats 
    
#     for i in range (28, len(Worked_before), 8): #the rest of the waiters and kitchen_crew are grouped by 8 
#         for row in Worked_before[i:i+8]:
#             Worked_before.append(((row[0],row[1]), tableNumber)) 
#             print(f'second seating row {row}, table {tableNumber}') 
#         tableNumber += 1

#     # new waiters and kitchen_crew are chosen 
#     retrieval_function() 
   
#     print('second set of waiters and kitchen_crew:', Worked_before) 

#     # there is a table of two from the worked_before array - this loops adds people to that table 
#     for i in range (0,6,1):
#         for row in bank[i:i+1]:
#             tableNumber = 5 
#             print(f'second seating row is {row}, table is {tableNumber}')  

#     tableNumber = 6 # tableNumber is set to 6 because we just ended on 5 

#     for i in range(7, len(bank), 8): # the remainder of the students in the bank array are grouped 8 per table 
#         for row in bank[i:i+8]:
#             print(f'second seating row is {row}, table is {tableNumber}') 
#         tableNumber += 1 

# #3rd seating 
#     print('3rd seatings') 
    
#     random.shuffle(bank) # the people left in the bank are shuffle 
#     tableNumber = 1 # tableNumber is set to 1 
#     random.shuffle(Worked_before) #the Worked_before array is shuffle so the same tables are created again  

#     for i in range (0, 27, 9): # assign the previous workers to tables first 
#         for row in Worked_before[i:i+9]: # the first 27 people are put into groupss of 9 
#             Worked_before.append(((row[0],row[1]), tableNumber)) # new seats are added to the array 
#             print(f'third seating row is {row}, table is {tableNumber}') 
#         tableNumber += 1 
    
#     for i in range (28, len(Worked_before), 8): #the rest of the waiters and kitchen_crew are grouped by 8 
#         for row in Worked_before[i:i+8]:
#             print(f'people left in third seating row is {row}, table is {tableNumber}') 
#         tableNumber += 1
    
#     retrieval_function() #  takes out the 3rd round of waiters and kitchen_crew 

#     print('third set of waiters and kitchen_crew:', Worked_before) 

#     tableNumber = 10 
    
#     for i in range(0, len(bank), 8): # the remainder of the students are grouped 8 per table 
#         for row in bank[i:i+8]:
#             print(f'third seating rows are {row}, table is {tableNumber}') 
#         tableNumber += 1 