from tkinter import *
from tkinter import ttk as ttk





class User:  #Class
     
    def __init__(self):
        self.name = "null"
        self._Dates_Present = []
        self._Dates_Absent = []

        

    def add_present(self, date):
        self._Date = date
        
        self._Dates_Present.append(self._Date)
        
        if self._Date in self._Dates_Absent:
            self._Dates_Absent.remove(self._Date)
            
        print(self._Dates_Present,self._Dates_Absent)
        

    def add_absent(self, date):
        self._Date = date
        
        if self._Date in self._Dates_Present:
            self._Dates_Present.remove(self._Date)
        
        self._Dates_Absent.append(self._Date)

        print(self._Dates_Present,self._Dates_Absent)
        
            
    def add_name(self, name):
        self.name = name
        print(self.name)
        
    
def add(date, holder, button): #function test
    
    if date in holder._Dates_Absent:
        holder.add_present(date)
        button.config(bg='green')
    else:
        holder.add_absent(date)
        button.config(bg='red')
        
        

dates_between = []



#User Initialization
UserOne = User() 
UserTwo = User()
UserThree = User()
UserFour = User()
UserFive = User()
UserSix = User()
UserSeven = User()
UserEight = User()
UserNine = User()
UserTen = User()
UserEleven = User()







def placeholder():
    print("placeholder")


classList = [UserOne, UserTwo, UserThree, UserFour, UserFive, UserSix, UserSeven, UserEight, UserNine, UserTen, UserEleven]
name = []

def export():
    
    with open('masterfile.txt', 'a') as f:
        for x in range(len(classList)):
         name.append(classList[x].name)
         
         
        charmax = max(name, key = len)
        charmax = len(charmax)
        
        print("""format:
Name: 
Dates List:
Dates Present:
Dates Absent:
Total Days Present:
Total Days Absent:
""", file= f)
        
        for z in range(len(classList)):
            
            print("\nName: ",classList[z].name, file = f)
            print("Dates Recorded: ", dates_between, file = f)
            print("Present: ",classList[z]._Dates_Present, file = f)
            print("Absent: ", classList[z]._Dates_Absent, file = f)
            print("Total Days Present: ", len(classList[z]._Dates_Present), file = f)
            print("Total Days Absent:  ", len(dates_between) - len(classList[z]._Dates_Present), end='\n' ,file = f)
    

        



    
    

"""How to make the calendar thingy:
1. cry in my sleep
2. cry in my sleep
3. cry in my sleep
4. have them input the days one by one (brain dead option)
5. have them put the starting and ending days:
    How to make it possible?
        Use calendar ig, calculate by days in between
        then store in a tuple
        call tuple action
        then use the stored data in tuple as an added days
            but then theres the problem if its only less than 15 days
                I can make it a case only of 15 days?
                what if I just append 0s then make the output code not read tuple values that are 0?
                
            solution might be: take the start date and end date
                end date - start date = total dates + 2
                    store all inside values using range on total dates
                        then iterate using that in button test class
                            note that total dates should not be a private or there is no way that the button class can access it
                                damn
                                    What about if less than 16 days?
                                
                 

"""

