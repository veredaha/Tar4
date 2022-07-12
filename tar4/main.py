import  module as m
def main():
 date = m.Date(12,3,2022)
 date.__str__()
 date.isValid()
 print(date.getNextDay())
 print(date.getNextDays(5))
 print(date.__sub__(13,12,2012))
 print(date.__lt__(13,12,2022))
 print(date.__eq__(13,12,2022))
 print(date.__ne__(13,12,2022))
 print(date.__gt__(13,12,2022))


 

if __name__ == "__main__":
    main()