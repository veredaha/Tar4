class Date:
  
  def __init__(self,day: int,month :int ,year:int) ->None:
    """
    function gets 3 parameters ,1 (day number between 1-31) int ,2 (month number between 1-12) int, 3 (year number (4 figures)) int.
    this function defines the date class
    :param day: int example - > 13
    :param month: int example - > 9
    :param year: int example - > 1998
    :return:None
    """
    self.day = day
    self.month = month
    self.year = year
   
  def __str__(self)->str: 
    """
    function prints the date that the function activates
    :return:None
    """
    return str(self.day) + '/' + str(self.month) + '/' + str(self.year)
  
  def isValid(self)-> bool: 
    """
    function checks weather the date is valid
    -date should be 3 seperate numbers
    - in months January, March, May, June, August, October, December - the number of the day should be betweeen 1- 31
    - in months Apil, July, September, Nuvember - the number of the day should be betweeen 1- 30
    - in fabuary the the day number should be between 1 -28 and evey 4 years 1 -29
    prints our if the date is valid or not
    :return: True,False
    """
    global max #to use in next function instead of writing again 
    if(self.month==1 or self.month==3 or self.month==5 or self.month==7 or self.month==8 or self.month==10 or self.month==12):
     max =31
    elif(self.month==4 or self.month==6 or self.month==9 or self.month==11):
     max =30
    elif(self.year%4==0  and self.year%100!=0 or self.year%400==0):
     max =29
    else:
     max=28
    if(self.month<1 or self.month>12):
     print("Date is invalid")
     #return false to use this in the next function instead of writing again
     return False
    elif(self.day<1 or self.day>max):
     print("Date is invalid")
      #return false to use this in the next function instead of writing again
     return False
    else:
     print("Date is valid")
      #return false to use this in the next function instead of writing again
     return True

  def getNextDay(self)->"Date": 
    """
    function returns the next day
    for example if date is 13/09/2018 it will return 14/09/2018
    return "The next day is: " + nextday
    """
    if self.isValid() == False :
        return "Please change the date"
    elif(self.day==max and self.month!=12):
     self.day=1
     self.month=self.month+1
     nextday = Date(self.day, self.month,self.year)
     return "The next day is: " + str(nextday)
    elif(self.day==31 and self.month==12):
     self.day=1
     self.month=1
     self.year = self.year +1
     nextday = Date(self.day, self.month,self.year)
     return "The next day is: " + str(nextday)
    else:
     self.day=self.day+1
     nextday = Date(self.day, self.month,self.year)
     return "The next day is: " + str(nextday)
    
  def getNextDays(self,daysToAdd:int)->"Date":
    """
    function adds days to the date
    for example if date is 13/09/2018 and daysToAdd is 7 it will return 20/09/2018
    :param daysToAdd: int example - > 7
    return "The next day is: " + nextdays
    """
    if self.isValid() == False :
        return "Please change the date"
    elif(self.day ==max and self.month!=12):
     self.day= daysToAdd 
     self.month=self.month+1
     nextdays = Date(self.day, self.month,self.year)
     return "The next day is: " + str(nextdays)
    elif(self.day==31 and self.month==12):
     self.day= daysToAdd
     self.month=1
     self.year = self.year +1
     nextdays = Date(self.day, self.month,self.year)
     return "The date is " + str(nextdays)
    elif(self.day + daysToAdd  > max and self.month!=12):
     self.day= ((self.day + daysToAdd) - max) 
     self.month=self.month+1
     nextdays = Date(self.day, self.month,self.year)
     return "The date is " + str(nextdays)
    elif(self.day + daysToAdd  > max and self.month==12):
     self.day= ((self.day + daysToAdd) - max) 
     self.month=1
     self.year = self.year +1
     nextdays = Date(self.day, self.month,self.year)
     return "The date is " + str(nextdays)
    else:
     self.day=self.day+ daysToAdd 
     nextdays = Date(self.day, self.month,self.year)
     return "The date is " + str(nextdays)
  
  def __sub__(self,otherday:int,othermonth:int,otheryear:int)->int:
     """
     function returns difference between 2 dates
     date input should be smaller than date object
     for example if date input  is 13/09/2018 and date object is 13/09/2019 the differnce is 365
     :param otherday: int example - > 7 (day in month)
     :param othermonth: int example - > 9 (month number)
     :param otheryeary: int example - > 1998 (year number)
     return "The difference between the years is " + dif
     """
     monthDays = [31, 28, 31, 30, 31, 30,31, 31, 30, 31, 30, 31]
     yeardd =0 
     if self.__lt__(otherday,othermonth,otheryear) == False:
        return "The date input should be smaller than date object"
     else:
      
      while otheryear < self.year:
          if (otheryear%4==0  and otheryear%100!=0 or otheryear%400==0):
           yeardd = yeardd +366
           otheryear = otheryear + 1
          else:
           yeardd = yeardd +365
           otheryear = otheryear + 1
    
      daysinother = sum(monthDays[:othermonth]) + otherday
      daysinself =sum(monthDays[:self.month]) + self.day
      dif = yeardd - daysinother + daysinself
      if (self.year%4==0  and self.year%100!=0 or self.year%400==0):
        dif =dif +1
      return "The difference between the years is " + str(dif)
  
  def __lt__(self,otherday:int,othermonth:int,otheryear:int)-> bool:
         """
     checks weather date object is lager than date input
     for example if date input  is 13/09/2018 and date object is 13/09/2019 it will return true
     :param otherday: int example - > 7 (day in month)
     :param othermonth: int example - > 9 (month number)
     :param otheryeary: int example - > 1998 (year number)
     return True, False
     """
         if self.year > otheryear :
            return True
         if self.year < otheryear :
            return False
         if self.year == otheryear :
          if self.month > othermonth :
            return True
          if self.month < othermonth :
            return False
         elif self.month == othermonth:
          if self.day > otherday :
            return True
          if self.day < otherday :
            return False

  def __eq__(self,otherday:int,othermonth:int,otheryear:int)-> bool:
    """
         checks weather date object and date input are the same
         for example if date input  is 13/09/2018 and date object is 13/09/2019 it will return false
         :param otherday: int example - > 7 (day in month)
         :param othermonth: int example - > 9 (month number)
         :param otheryeary: int example - > 1998 (year number)
          return True, False
     """
    if self.year == otheryear and self.month == othermonth and self.day == otherday:
        return True
    else:
        return False
 
  def __ne__(self,otherday:int,othermonth:int,otheryear:int)-> bool:

    if self.year != otheryear or self.month != othermonth or self.day != otherday:
        """
         checks weather date object and date input are the same
         for example if date input  is 13/09/2018 and date object is 13/09/2019 it will return true
         :param otherday: int example - > 7 (day in month)
         :param othermonth: int example - > 9 (month number)
         :param otheryeary: int example - > 1998 (year number)
          return True, False
     """
        return False
    else:
        return True
    
  def __gt__(self,otherday:int,othermonth:int,otheryear:int)-> bool:
         """
     checks weather date object is smaller than date input
     for example if date input  is 13/09/2018 and date object is 13/09/2019 it will return false
     :param otherday: int example - > 7 (day in month)
     :param othermonth: int example - > 9 (month number)
     :param otheryeary: int example - > 1998 (year number)
     return True, False
     """
         if self.year < otheryear :
            return True
         if self.year > otheryear :
            return False
         if self.year == otheryear :
          if self.month < othermonth :
            return True
          if self.month > othermonth :
            return False
         elif self.month == othermonth:
          if self.day < otherday :
            return True
          if self.day > otherday :
            return False
        
   
  
