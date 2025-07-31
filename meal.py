'''a program that prompts the user for a time and outputs whether it’s breakfast time,
 lunch time, or dinner time. 
 If it’s not time for a meal, don’t output anything at all. 
 Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##.
   And assume that each meal’s time range is inclusive. 
   For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.'''

def main():
    time = input("what time is it? ")
    convert(time)
    
    

def convert(time):
    hours,min = time.strip().split(':')
    if (hours == "7" and int(min) <60) or (hours == "8" and int(min) == 0):
        print("breakfast time")
    elif (hours == "12" and int(min) <60) or (hours == "13" and int(min) == 0):
        print("lunch time")
    elif (hours == "18" and 0 <=int(min) <60) or (hours == "19" and int(min) == 0):
        print("dinner time")
    


if __name__ == "__main__":
    main()
