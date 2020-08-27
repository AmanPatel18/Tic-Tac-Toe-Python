from tkinter import *
from tkinter import messagebox
win=Tk()
win.title('Tic-Tac-Toe')
win.config(bg='black')
win.resizable(0,0)
sign=True # if sign is True it means it is X else O
count=0
status=None

def reset():
    global status,count,sign
    count=0
    status=None
    b1.config(text="",bg="gold")
    b2.config(text="",bg="gold")
    b3.config(text="",bg="gold")
    
    b4.config(text="",bg="gold")
    b5.config(text="",bg="gold")
    b6.config(text="",bg="gold")
    
    b7.config(text="",bg="gold")
    b8.config(text="",bg="gold")
    b9.config(text="",bg="gold")


def check_winner():
    global count,status
    # winner condition for case: X

    if  b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":

        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X has won the game...!")
    
    elif  b7["text"]=="X" and b8["text"]=="X" and b9["text"]=="X":
        
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    elif  b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    elif  b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":

        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X has won the game...!")
    
    elif  b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    elif  b3["text"]=="X" and b5["text"]=="X" and b7["text"]=="X":
        
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! X has won the game...!")
    
    # winner condition for case: O
    
    elif  b1["text"]=="O" and b2["text"]=="O" and b3["text"]=="O":
        
        b1.config(bg="green")
        b2.config(bg="green")
        b3.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":

        b4.config(bg="green")
        b5.config(bg="green")
        b6.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe", "Congratulations! O has won the game...!")
    
    elif  b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        
        b7.config(bg="green")
        b8.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    elif  b1["text"]=="O" and b4["text"]=="O" and b7["text"]=="O":
        
        b1.config(bg="green")
        b4.config(bg="green")
        b7.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    elif  b2["text"]=="O" and b5["text"]=="O" and b8["text"]=="O":
        
        b2.config(bg="green")
        b5.config(bg="green")
        b8.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":

        b3.config(bg="green")
        b6.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe", "Congratulations! X has won the game...!")
    
    elif  b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        
        b1.config(bg="green")
        b5.config(bg="green")
        b9.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    elif  b3["text"]=="O" and b5["text"]=="O" and b7["text"]=="O":
        
        b3.config(bg="green")
        b5.config(bg="green")
        b7.config(bg="green")
        status=messagebox.showinfo("Tic-Tac-Toe","Congratulations! O has won the game...!")
    
    else:
        if count==9:
            status=messagebox.showinfo("Tic-Tac-Toe", "Game has been Draw!")
    
    if status=="ok":
        reset()



def btn_click(b):
    global sign,count
    if sign==True and b["text"]=="":
        b["text"]="X"
        sign=False
        count+=1

    elif sign==False and b["text"]=="":
        b["text"]="O"
        sign=True
        count+=1

    check_winner()
    


b1=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b1))
b2=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b2))
b3=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b3))

b4=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b4))
b5=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b5))
b6=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b6))

b7=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b7))
b8=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b8))
b9=Button(win,text="",bg="gold",font=("Helvetica 20 bold"),height=2,width=4,command=lambda:btn_click(b9))


b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)

win.mainloop()
