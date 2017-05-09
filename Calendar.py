"""
 basic calendar that the user will be able to interact with from the command line. The user should be able to choose to:

View the calendar
Add an event to the calendar
Update an existing event
Delete an existing event
"""
from time import strftime, sleep

USER_FIRST_NAME = "Adrian"

calendar = {}

def welcome():
  print "Welcome," + USER_FIRST_NAME + "."
  print "Calendar starting..."
  sleep(1)
  print "Today is: " + strftime("%A %B %d, %Y")
  print strftime("%H:%M:%S")
  print "What would you like todo?"

def start_calendar():
  welcome()
  start = True
  while start:
    user_choice = raw_input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
    user_choice = user_choice.upper()
    if user_choice == 'V':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        print calendar
    elif user_choice == 'U':
      date = raw_input("What date?. ")
      update = raw_input("Enter the update: ")
      calendar[date] = update
      print "Update was successful"
    elif user_choice == 'A':
      event = raw_input("Enter event: ")
      date = raw_input("Enter date (MM/DD/YYYY): ")
      if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
        print "Invalid date was entered"
        try_again = raw_input("Try Again? Y for Yes, N for No: ")
        try_again = try_again.upper()
        if try_again == 'Y':
          continue
        else:
          start = False
      else:
        calendar[date] = event
    elif user_choice == 'D':
      if len(calendar.keys()) < 1:
        print "Calendar empty."
      else:
        event = raw_input("What event? ")
        for date in calendar.keys():
          if calendar[date] == event:
            del calendar[date]
            print "The event was successfully deleted"
          else:
            print "Incorrect event was specified."
    elif user_choice == 'X':
      start = False
    else:
      print "An invalid command was entered"


start_calendar()    
     
          
        
      
      
        
        
        
      
      
      
      
      
      
        
    
  
  
  
  


 

  

  
 







