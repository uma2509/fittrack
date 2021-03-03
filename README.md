from tkinter import*
m= Tk()
n=Tk()

def homepg():
	l1= Label(m, text="WELCOME TO _______ ").grid(row=1, column=1)
	b1= Button(m, text="Login", command= login).grid(row=2,column=1)
	b2= Button(m, text="Signup", command= signup).grid(row=3,column=1)

def login():
    def gsearch(x):
        f1 = open("file.txt", "r")
        if x in f1:
            print("found")
        f1.close()
    l2= Label(m,text="Enter your name: ").grid(row=5, column=1)
    e1= Entry(m)
    e1.grid(row=5,column=2) 
    ef1= e1.get()
    b3= Button(m, text="Submit", command= gsearch(ef1) ).grid(row=5,column=3)        
    l3= Label(m,text="Enter your password: ").grid(row=6, column=1)
    e2= Entry(m,show="*")
    e2.grid(row=6,column=2)
    ef2= e2.get()
    b4= Button(m, text="Submit", command= gsearch(ef2)).grid(row=6,column=3)
    l4= Label(m,text="WELCOME BACK").grid(row=9, column=1)
    b5= Button(m, text="Continue", command= mainmenu).grid(row=10,column=1)   

def signup():
	def ginput(x):
        f1 = open("file.txt", "w")
        f1.write(x)
        f1.close()
    l2= Label(m,text="Enter your name: ").grid(row=5, column=1)
    e1= Entry(m)
    e1.grid(row=5,column=2)
    ef1= e1.get()
    b3= Button(m, text="Submit", command= ginput(ef1)).grid(row=5,column=3)        
    l3= Label(m,text="Enter your password: ").grid(row=6, column=1)
    e2= Entry(m,show="*")
    e2.grid(row=6,column=2)
    ef2= e2.get()
    b4= Button(m, text="Submit", command= ginput(ef2)).grid(row=6,column=3)  
    l4= Label(m,text="WELCOME").grid(row=9, column=1)
    b5= Button(m, text="Continue", command= mainmenu).grid(row=10,column=1)
    
def mainmenu():
    l1= Label(n,text="CHOOSE: ").grid(row=1, column=1)
    b1= Button(n, text="BMI", command= bmi).grid(row=3,column=1)
    b2= Button(n, text="Pulse/ Heart Rate", command= phrate).grid(row=5,column=1)
    b3= Button(n, text="Calories burnt - Exercise", command= exercise).grid(row=7,column=1)
    b4= Button(n, text="Calories consumed - Food", command= food).grid(row=9,column=1)
    

homepg()
	
m.mainloop()
