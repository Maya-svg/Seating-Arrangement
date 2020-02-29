import json
from http.server import BaseHTTPRequestHandler, HTTPServer
import csv


# the Student List csv file is opened with commas as the seperators 
with open('Dinner Seating - Student List 2018-19.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # variables are stated here 
    current_table = 0
    person_number = 1
    waiter = False
    studentDict = {}
    # for every row in the csv file a new student dictionary is created 
    for row in csv_reader:
        studentDict[str(row[1] +' '+ row[0])] = dict()
        # the waiters boolean is true only if the person_number is 9
        if person_number == 9:
            waiter = True
        else:
            # or else everyone else are waiters 
            waiter = False
        if current_table == 0:
            # if the table number is 0 which it is in the begining, those people are assinged as kitchen crew members 
            studentDict[str(row[1] +' '+ row[0])].update({'name': row[1]+' '+row[0], 'seating': 'kitchen crew', 'isWaiter': 'no' })        
        else:
            # if the waiter boolean is true then those rows are assigned a table to wait on 
            if waiter == True:
                studentDict[str(row[1] +' '+ row[0])].update({'name': row[1]+' '+row[0], 'seating': str(current_table), 'isWaiter': 'yes'})
            else:
                #if the ewaiter boolean is still false then those students in those rows are just assigned tables to sit at. They are also told they are not waiters. 
                studentDict[str(row[1] +' '+ row[0])].update({'name': row[1]+' '+row[0], 'seating': str(current_table), 'isWaiter': 'no'})
        if current_table < 31: # if the tableNumber is less thean 31 then the numbers continue to increase by 1 
            current_table += 1
        else:
            #if the table number is greatter than 31 than the current_table vaiable is reset to 0 and the person_nu,ber is increase by 1. 
            current_table = 0
            person_number += 1
print(studentDict) # the entire dictionary of students is printed 
class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        requestPath = self.path
        
        # this function removes the %20 in the person's name 
        if '%20'in requestPath: 
            key = '%20'
            newUrl = requestPath.replace(key, '+')
            keyword = newUrl.replace('+', ' ')
            # the %20 is switched to a space 

        # this function removes the ""/"" in the person's name  
        if '/'in requestPath:   
            key = '/' 
            title = keyword.replace(key, '+')
            name = title.replace('+', '')
            requestPath = name 
            print(requestPath)
            # the name now matches the name from the student dictionaries 

        #Log to us
        
        print(f'\n----- GET Request Start ----->\n')
        print(f'Request path: {requestPath}')
        print(f'Request headers:\n')
        for line in self.headers:
            print(f'  > {line}: {self.headers[line]}')
        print(f'\n<----- GET Request End -----\n')
        
        #Answer 200 => OK Status
        self.send_response(200)
        #Add Headers if any needed
        #self.send_header("Set-Cookie", "cate=true")
        self.end_headers()
        
        # function to get the people at the same table as the serched name 
        if requestPath in studentDict:
            #the number of found students at the table starts at 0 
            studentNum = 0 
            # looks through the studentDict for the name searched and is put into the varible "student"
            student = studentDict[requestPath]
            # the table the searched person is sitting at becomes the stored value for the variable placement 
            placement = studentDict[requestPath]['seating']
            # a new table dictionary is created 
            tableDict = {}
            #this function looks through each student in the studentDict 
            for student in studentDict:
                #if there table number matches the placement value 
                if studentDict[student]['seating'] == placement:
                    #then the additional student at is increased by 1 
                    studentNum += 1
                    # a new table dictionary is created with each student that has the same seating number 
                    tableDict['student'+str(studentNum)] = dict()
                    #the student is added to that new table dictionary that was created in their name 
                    tableDict['student'+str(studentNum)].update(studentDict[student])
            # if there aren't 10 people in the dictionary then the statement is false 
            if ('student10' in tableDict) == False:
                #a new table dictionary is created 
                tableDict['student10'] = dict()
                #we are told no one is at seat 10 and so all the variables are empty 
                tableDict['student10'].update({'name': "empty", 'seating': 'empty', 'isWaiter': 'no'})

            print(tableDict) #the table dictionaries are printed 

            # Marshall `student' to JSON and send it
            marshaled = json.dumps(tableDict)
            print(marshaled)
            self.wfile.write(marshaled.encode('utf_8'))
        else:
            # there was an error!
            print("oh no")
        
# Listen on Port 80
port = 80
print('Listening on localhost:%s' % port)
server = HTTPServer(('', port), RequestHandler)
print(server)
server.serve_forever()