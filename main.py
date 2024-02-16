import theaterSeats as t

#to print out the seats so you can see them in the console
#This prints out the empty theater - Uncomment to see
#takes user input on number of pleople they are seating
def userInput():
  while True:
    count= int(input('Hello welcome to theater seat searcher how many are we are seating today?'))
    confirm= input(f'Are you sure you want to book {count} seats?(y/n) ')
  #confirm the number of people 
    if confirm.upper()=="Y" or confirm.upper()=="YES":
      break
  return count
#check number of seats and where they might fit
def check_board(x):
  found_row= False
  for row in range(len(t.theater_seats)):
    for col in range(len(t.theater_seats[row])):
      if t.theater_seats[row][col]=='o':
        for seat in range(x):
          found_row=True if t.theater_seats[row][col+seat]=='o' else False
        if found_row:
          return row,col 

#convert(0,0)grid data to A1 B7 paterns 
def interprit_datapoints():
  
  

def read_rows():
  for row in t.theater_seats:
    print(row)

#this prints out the test theater - Uncomment to see
  for row in t.theater_seats2:
    print(row)


def main():
  read_rows()




main()