from tkinter import *
from tkinter.messagebox import showinfo
y =""
x =2
player1= []
player2 = []

def define_sign(number):

  
  global x,y
  global player1,player2
  from itertools import permutations
  set1 = permutations([1,2,3])
  set2 = permutations([3,5,7])
  set3 = permutations([1,5,9])
  set4 = permutations([4,5,6])
  set5 = permutations([7,8,9])
  set6 = permutations([1,4,7])
  set7 = permutations([2,5,8])
  set8 = permutations([3,6,9])
  for _ in set1,set2,set3,set4,set5,set6,set7,set8:
    for j in list(_):
      plyr1 = all(elem in player1 for elem in j)
      plyr2 = all(elem in player2 for elem in j)
      if plyr1 == True:
        #print("player 1 Won !")
        showinfo("game result",'player 1 has won')
        break
      elif plyr2 == True:
        #print("player 2 Won !")
        showinfo("game result",'player 2 has won')
        break
      else:
        pass
  if number == 1:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      ##print(player2)
    b1.config(text = y)
    x = x+1

  if number == 2:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      ##print(player2)
    b2.config(text = y)
    x = x+1

  if number == 3:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b3.config(text = y)
    x = x+1

  if number == 4:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b4.config(text = y)
    x = x+1

  if number == 5:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b5.config(text = y)
    x = x+1

  if number == 6:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b6.config(text = y)
    x = x+1

  if number == 7:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b7.config(text = y)
    x = x+1

  if number ==8:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b8.config(text = y)
    x = x+1

  if number == 9:
    if x%2 == 0:
      y = 'x'
      player1.append(number)
      #print(player1)
    elif x%2 != 0:
      y = 'o'
      player2.append(number)
      #print(player2)
    b9.config(text = y)
    x = x+1



root = Tk()
l1 = Label(root,text= "player 1 : x",font="times 15")
l1.grid(row = 0, column = 1)
l2 = Label(root,text= "player 2 : o",font="times 15")
l2.grid(row = 0, column = 2)


b1 = Button(root , width =20,height = 10,command = lambda : define_sign(1))
b1.grid(row =1,column = 1 )

b2 = Button(root , width =20,height = 10,command = lambda : define_sign(2))
b2.grid(row =1,column = 2 )

b3 = Button(root , width =20,height = 10,command = lambda : define_sign(3))
b3.grid(row =1,column = 3 )

b4 = Button(root , width =20,height = 10,command = lambda : define_sign(4))
b4.grid(row =2,column = 1 )

b5 = Button(root , width =20,height = 10,command = lambda : define_sign(5))
b5.grid(row =2,column = 2 )

b6 = Button(root , width =20,height = 10,command = lambda : define_sign(6))
b6.grid(row =2,column = 3 )

b7 = Button(root , width =20,height = 10,command = lambda : define_sign(7))
b7.grid(row =3,column = 1 )

b8 = Button(root , width =20,height = 10,command = lambda : define_sign(8))
b8.grid(row =3,column = 2 )

b9 = Button(root , width =20,height = 10,command = lambda : define_sign(9))
b9.grid(row =3,column = 3 )

root.mainloop()
