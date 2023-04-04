# import sympy 
from sympy import * 
from tkinter import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk,Image
M = Matrix([[1, 0, 1, 3], [2, 3, 4, 7], [-1, -3, -3, -4]])
print("Matrix : {} ".format(M))
v=[]
n=4
 
print(len(M))

for i in range(0,len(M)):
    j=M[i]
    if(M[i]==')'):
        break
    if(M[i]==1 or M[i]==0 or M[i]==2 or M[i]==3 or M[i]==4 or M[i]==5 or M[i]==6 or M[i]==7 or M[i]==8 or M[i]==9 or M[i]<0):
        v.append(M[i])
for i in range(0,len(v)):
    if((i)%n==0):
        print("\n")
    print(v[i],end=' ')




    
    


# Use sympy.rref() method 
M_rref = M.rref()  
x=[];
b=0;
z=''
print("The Row echelon form of matrix M and the pivot columns : {}".format(M_rref))
a=format(M_rref)
for i in range(0,len(a)):
    j=ord(a[i])
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
        print("\n")
    print(x[i],end=' ')
c=0
p=5

def ans():
# Create Root Object
    root = Tk()
 
# Set Geometry(widthxheight)
    root.geometry('1700x1500')
    root = Tk()
    
    root.configure(bg="blue")
    root.title("main")
 
    l = Label(root, text = "This is root window")
 
# Create style Object
    style = Style()
    

 
    '''bg = ImageTk.PhotoImage(file="kol.jpg")

# Create a canvas
    my_canvas = Canvas(root, width=1500, height=1500)
    my_canvas.pack(fill="both", expand=True)

# Set image in canvas
    my_canvas.create_image(0,0, image=bg, anchor="nw")'''


#btn1.grid(row = 0, column = 3, padx = 100)
 
# button 2
    c=0
    p=5

    for i in range(0,len(x)):
        if((i)%n==0 and i!=0):
            c=c+1
            p=5
        btn2 = Button(root, text =x[i])
        btn2.grid(row = 1+c, column = 3+p, pady = 20, padx = 10,ipadx=10,ipady=10)
        p=p+1
        

    
    root.mainloop()
root=Tk()
root.geometry('1700x1500')
root.title("CHINESE")
root.configure(bg="red")
btn2 = Button(root, text ='NEXT',command=root.destroy)
btn2.place(x=1300,y=100)


c=0
p=5

for i in range(0,len(v
                     )):
    if((i)%n==0 and i!=0):
            c=c+1
            p=5
    btn2 = Button(root, text =v[i])
    btn2.grid(row = 1+c, column = 3+p, pady = 20, padx = 10,ipadx=10,ipady=10)
    p=p+1



root.mainloop()
ans()






