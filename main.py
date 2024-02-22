import theaterSeats as t

colums = ["A","B","C","D","E","F"]
#takes user input on number of pleople they are seating
def userInput():
  while True:
    count= int(input('Hello welcome to theater seat searcher\nhow many are we are seating today?\n> '))
    confirm= input(f'Are you sure you want to book {count} seats?(y/n) ')
  #confirm the number of people 
    if confirm.upper()=="Y" or confirm.upper()=="YES":
      break
  return count - 1
#check number of seats and where they might fit
def check_board(x,board):
  found_row= False
  list_row= []
  list_col= []
  for row in range(len(board)):
    for col in range(len(board[row])):
      if board[row][col]=='o':
        if (col+x)>= len(board):
            break
        if x>1:
          for check_row in range(x+1):
            found_row=True if board[row][col+check_row]=='o' else False
            if found_row is False:
              break
        else:    
          found_row=True if board[row][col+x]=='o' else False
        if found_row:
          y,z=interprit_datapoints(col,row,x)
          list_col.append(y)
          list_row.append(z)
  if len(list_row)==0 and len(list_col)==0:
    print(f'no open seats for {x+1} people')
    exit()
  return list_col,list_row




#convert(0,0)grid data to A1 B7 paterns 
#x colum first slot is in, y the row of seat, z total people  
def interprit_datapoints(x,y,z):
  col = colums[x-1]
  start= col+str(y)
  end= colums[x+z-1]+str(y)
  return start, end

#read out all posible rows combinations
def posible_rows(x,y):
  print("Posible seats-")
  for index in range(len(x)):
    print(f'- {x[index]}, {y[index]} ')
      
      


  
#to print out the seats so you can see them in the console
#This prints out the empty theater - Uncomment to see
def read_rows():
  for row in t.theater_seats:
    print(row)
  print("\n")
#this prints out the test theater - Uncomment to see
  for row in t.theater_seats2:
    print(row)


def main():
  read_rows()
  val = userInput()    # Added to capture the return value of userInput function
  print("seats in theater 1")
  start, end =check_board(val,t.theater_seats)
  posible_rows(start,end)
  print("seats in theater 2")
  start, end =check_board(val,t.theater_seats2)
  posible_rows(start,end)

main()
