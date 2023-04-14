
import sympy 
from sympy import * 
from tkinter import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
import inputf


print(inputf.M)
v=[]
f=format(inputf.M)
n=0
for i in range(8,len(f)):
    o=ord(f[i])
    if(f[i]==']'):
        break
    if(o>=48 and o<=57):
        n=n+1
    

def intro():
   
    top = Tk()
    
    #top.configure(bg="rgb(2,0,36)")
    
    top.title("Input-Page")
    top.geometry('1500x1500')
    bg = PhotoImage(file = "ko.png")
  
# Create Canvas
    canvas1 = Canvas( top, width = 600,
                 height = 50)
  
    canvas1.pack(fill = "both", expand = True)
  
# Display image
    canvas1.create_image( 0, 0, image = bg, 
                     anchor = "nw")
  
# Add Text
   # canvas1.create_text( 200, 250, text = "Welcome")
    user_name = Label(top,
                  text = "ROWS").place(x = 40,
                                           y = 60) 
   
# the label for user_password 
    user_password = Label(top,
                      text = "COLUMNS").place(x = 40,
                                               y = 100) 
   

   
    user_name_input_area = Entry(top,
                             width = 30).place(x = 110,
                                               y = 60) 
   
    user_password_entry_area = Entry(top,
                                 width = 30).place(x = 110,
                                                   y = 100)
    b=Button(top,text="PROCEED",command=top.destroy).place(x=200,y=200)
    
    top.mainloop()
intro()

#print(len(M))

for i in range(0,len(inputf.M)):
    j=inputf.M[i]
    if(inputf.M[i]==')'):
        break
    if(inputf.M[i]==1 or inputf.M[i]==0 or inputf.M[i]==2 or inputf.M[i]==3 or inputf.M[i]==4 or inputf.M[i]==5 or inputf.M[i]==6 or inputf.M[i]==7 or inputf.M[i]==8 or inputf.M[i]==9 or inputf.M[i]<0):
        v.append(inputf.M[i])
for i in range(0,len(v)):
    if((i)%n==0):
        continue
        #print("\n")
    #print(v[i],end=' ')




    
    


# Use sympy.rref() method 
M_rref = inputf.M.rref()  
x=[];
b=0;
z=''
#print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
a=format(M_rref)
for i in range(0,len(a)):
    j=ord(a[i])
    if(a[i+1]=='/' or a[i-1]=='/'):
        continue
    if((j>=48 and j<=57)):
        x.append(a[i])
    
    if(a[i]=='/'):
        z=z+a[i-1]+a[i]+a[i+1]
        x.append(z)  
    if(a[i]==')'):
        break
    z=' '
for i in range(0,len(x)):
    if((i)%n==0):
        continue
       # print("\n")
    #print(x[i],end=' ')
c=0
p=5



#print(v)

def ans():
# Create Root Object
    root = Tk()
 
# Set Geometry(widthxheight)
    root.geometry('1700x1500')
   
    
    root.configure(bg="blue")
    root.title("main")
 
    l = Label(root, text = "This is root window")
 
# Create style Object
   # style = Style()


#btn1.grid(row = 0, column = 3, padx = 100)
 
# button 2
    c=0
    p=5

    for i in range(0,len(x)):
        if((i)%n==0 and i!=0):
            c=c+1
            p=5
        btn2 = Button(root, text =x[i])
        btn2.grid(row = 1+c, column = 3+p, pady = 20, padx = 20,ipadx=15,ipady=15)
        p=p+1
        

    
    root.mainloop()
    
root=Tk()
root.geometry('1700x1500')
root.title("Input-Array")
root.configure(bg="red")

  

btn2 = Button(root, text ='NEXT',command=root.destroy)
btn2.place(x=1300,y=100)


c=0
p=5
print(len(v))
for i in range(0,len(v)):
    if((i)%(n)==0 and i!=0):
            c=c+1
            p=5
    btn2 = Button(root, text =v[i])
    btn2.grid(row = 1+c, column = 3+p, pady = 20, padx = 20,ipadx=15,ipady=15)
    #btn2.place(x=50+c,y=50+p)
    
    p=p+1



ans() 




