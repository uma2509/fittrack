'''
This code for fitness tracker provides the user, detailed report of their health condition using Python's tkinter gui. It also keeps track of calories consumed and burned.
'''
from tkinter import * #Importing tkinter module from standard Python Library

#--------------------------------------------------------------------------------------------------------------
#Code for the home page
m= Tk()
home_l1 = Label(m, text="FITNESS TRACKER",font=('Arial',30))
home_l1.grid(row=1, column=2)
home_l1_1 = Label(m, text="")
home_l1_1.grid(row=2)


home_l2 = Label(m, text="Enter your NAME",font=('Arial',15))
home_l2.grid(row=3, column=2)
def ip_home_name():
    global name
    name = home_e1.get()
home_e1 = Entry(m)
home_e1.grid(row=4,column=2)


home_l3 = Label(m, text="Enter your AGE",font=('Arial',15))
home_l3.grid(row=6, column=2)
def ip_home_age():
    global age
    age = int(home_e2.get())
home_e2 = Entry(m)
home_e2.grid(row=7,column=2)


home_l4 = Label(m, text="Enter your WEIGHT",font=('Arial',15))
home_l4.grid(row=9, column=2)
def ip_home_weight():
    global weight
    weight = int(home_e3.get())
home_e3 = Entry(m)
home_e3.grid(row=10,column=2)


home_l5 = Label(m, text="Enter your HEIGHT(in cm) ",font=('Arial',15))
home_l5.grid(row=11, column=2)
def ip_home_height():
    global height
    height = int(home_e4.get())
home_e4 = Entry(m)
home_e4.grid(row=12,column=2)


def ip_home():
    ip_home_name()
    ip_home_age()
    ip_home_weight()
    ip_home_height()
    m.destroy()
home_l1_2 = Label(m, text="")
home_l1_2.grid(row=13)
b1= Button(m, text="Submit", command= ip_home)
b1.grid(row=14,column=2)
home_Ll1 = Label(m,text = "").grid(row=14,column=1)
m.mainloop()
print(name,age,weight,height)

#--------------------------------------------------------------------------------------------------------------
# Code for BMI
bmi=weight/((height/100)**2)
bmistr=str(bmi)
n= Tk()
bmi_Ll1 = Label(n,text = "").grid(row=5,column=1)
bmi_Ll2 = Label(n,text = "").grid(row=5,column=3)
bmi_L = Label(n, text="BMI",font=('Arial',20)).grid(row = 1, column = 2)
bmi_L1 = Label(n,text = "Your BMI is "+ bmistr).grid(row=4,column=2)
if bmi<25 and bmi>18:
    bmi_Ll2 = Label(n,text = "You are NORMAL").grid(row=7,column=2) 
elif bmi<18:
    bmi_L2 = Label(n,text = "You are UNDERWEIGHT").grid(row=7,column=2)
else:
    bmi_L3 = Label(n,text = "You are OVERWEIGHT").grid(row=7,column=2)
def close_1():
    n.destroy()
bmi_b1= Button(n, text="Close", command= close_1)
bmi_b1.grid(row=10,column=2)
bmi_Ll3 = Label(n,text = "").grid(row=11,column=1)
n.mainloop()

#--------------------------------------------------------------------------------------------------------------
#Code for user's heart rate condition
q=Tk()
hbpm_Ll1 = Label(q,text = "").grid(row=5,column=1)
hbpm_Ll2 = Label(q,text = "").grid(row=5,column=3)
hbpm_l1 = Label(q, text = "Heart Rate",font=('Arial',20)).grid(row = 1, column = 2)
hbpm_l2 = Label(q, text="Enter your heartbeat per minute")
hbpm_l2.grid(row=4, column=2)
def hbpm_ip():
    global hbpm
    hbpms = hbpm_e1.get()
    hbpm = int(hbpms)
hbpm_e1 = Entry(q)
hbpm_e1.grid(row=7,column=2)

def close_2():
    hbpm_ip()
    q.destroy()

hbpm_b1= Button(q, text="Submit", command= close_2)
hbpm_b1.grid(row=10,column=2)
hbpm_Ll4 = Label(q,text = "").grid(row=11,column=1)
q.mainloop()
c1=Tk()
label1 = Label(c1,text="QUICK REPORT",font=('Arial',20)).grid(row=1,column=2)
if hbpm>100:
    hbpm_l3 = Label(c1,text = "Tachycardia").grid(row=2,column=2)
elif hbpm<60:
    hbpm_l4 = Label(c1,text = "Bradycardia").grid(row=2,column=2)
else:
	hbpm_l5 = Label(c1,text = "Normal Heart Rate").grid(row=2,column=2)
def hbpm_h_1():
    c1.destroy()
hbpm_b2= Button(c1, text="Close", command= hbpm_h_1)
hbpm_b2.grid(row=5,column=2)
hbpm_Ll3 = Label(c1,text = "").grid(row=6,column=1)
c1.mainloop()


#--------------------------------------------------------------------------------------------------------------
#Code for user's BP condition
j=Tk()
bp_l1 = Label(j, text="BLOOD PRESSURE ",font=('Arial',15)).grid(row = 1, column = 2)
bp_l2 = Label(j, text="Enter your systolic blood pressure: ").grid(row = 3, column = 2)
def sysbp_ip():
    global sysbp
    sysbp = int(bp_e1.get())
bp_e1 = Entry(j)
bp_e1.grid(row=4,column=2)
bp_l3 = Label(j, text="Enter your diastolic blood pressure: ").grid(row = 6, column = 2)
def diabp_ip():
    global diabp
    diabp = int(bp_e2.get())
def ip_pressure():
    sysbp_ip()
    diabp_ip()
    j.destroy()
bp_e2 = Entry(j)
bp_e2.grid(row=7,column=2)
bp_b1= Button(j, text="Submit", command= ip_pressure)
bp_b1.grid(row=8,column=2)
j.mainloop()
j1=Tk()
label2 = Label(j1,text="QUICK REPORT",font=('Arial',20)).grid(row=1,column=2)
if sysbp>140 or diabp>80: 
	bp_l4=Label(j1, text = "High BP").grid(row = 3, column = 2)
elif sysbp<90 or diabp<70:
    bp_l5=Label(j1, text ="Low BP").grid(row = 3, column = 2)
else:
    bp_l6=Label(j1, text = "Normal Blood Pressure").grid(row = 3, column = 2)
def close_3():
    j1.destroy()
hbpm_b1= Button(j1, text="Close", command= close_3)
hbpm_b1.grid(row=6,column=2)
j1.mainloop()

#--------------------------------------------------------------------------------------------------------------
#Code for user's calorie burnt amount
o=Tk()
exl1 = Label(o, text = "CALORIES BURNT",font=('Arial',15)).grid(row = 1, column = 1)
i=0
calories = 0
r=weight/60
totalcal=0

ex_l1= Label(o, text="CHOOSE ").grid(row=2,column=1)
lb = Listbox(o,width=40,height=30) 
lb.grid(row=3,column=1)
scb = Scrollbar(o) 
scb.grid(row=3,column=40) 

file = open("exercise.txt","r")
global b,c
activity_done='yoga'
b = file.read()
c = eval(b)

for i5 in c.keys():
    lb.insert(END,i5 )
'''
lb.insert(END, "aerobic dancing - high impact") 
lb.insert(END, "aerobic dancing - low impact")
lb.insert(END, "basketball")
lb.insert(END, "bodyweight exercises - moderate effort")
lb.insert(END, "bodyweight exercises - vigorous effort")
lb.insert(END, "bowling")
lb.insert(END, "boxing - punching bag")
lb.insert(END, "boxing - sparring")
lb.insert(END, "cleaning")
lb.insert(END, "cycling - fast")
lb.insert(END, "cycling - moderate")
lb.insert(END, "cycling - slow")
lb.insert(END, "football")
lb.insert(END, "gardening")
lb.insert(END, "gymnastics")     
lb.insert(END, "hockey")
lb.insert(END, "hiking")
lb.insert(END, "horseback riding")
lb.insert(END, "ice skating")
lb.insert(END, "inline skating")
lb.insert(END, "martial arts")
lb.insert(END, "pilates")
lb.insert(END, "rock climbing")
lb.insert(END, "roller skating")
lb.insert(END, "running at 6min/mile")
lb.insert(END, "running at 7min/mile")
lb.insert(END, "running at 8min/mile")
lb.insert(END, "running at 9min/mile")
lb.insert(END, "running at 10min/mile")
lb.insert(END, "running at 11min/mile")
lb.insert(END, "running at 12min/mile")
lb.insert(END, "scuba diving")
lb.insert(END, "skateboarding")
lb.insert(END, "skiing")
lb.insert(END, "skipping - fast")
lb.insert(END, "skipping - moderate")
lb.insert(END, "skipping - slow")
lb.insert(END, "squash")
lb.insert(END, "stretching")
lb.insert(END, "surfing")
lb.insert(END, "swimming - fast")
lb.insert(END, "swimming - moderate")
lb.insert(END, "table tennis")
lb.insert(END, "tennis")
lb.insert(END, "volleyball")
lb.insert(END, "walking- brisk")
lb.insert(END, "walking- moderate")
lb.insert(END, "walking- slow")
lb.insert(END, "weightlifting - moderate effort")
lb.insert(END, "weightlifting - vigorous effort")
lb.insert(END, "wrestling")
lb.insert(END, "yoga")
lb.config(yscrollcommand = scb.set) 
scb.config(command = lb.yview) 
'''


ex_l2= Label(o, text="Enter the activities from the list above(comma after each activity): ")
ex_l2.grid(row=34,column=1)
ex_e1= Entry(o)
ex_e1.grid(row = 44, column = 1) 


def ip_act_activity_done():
    global activity_done
    activity_done=ex_e1.get()
    activity_done=activity_done.lower()


ex_l3= Label(o, text="Enter the number of minutes(comma after each activity): ")
ex_l3.grid(row=45,column=1)
ex_e2= Entry(o)
ex_e2.grid(row = 46, column = 1)


def ip_act_activity_time():
    global activity_time
    activity_time=ex_e2.get()
    
    
def ip_act():
    ip_act_activity_done()
    ip_act_activity_time()
    o.destroy()
    
    
ex_l2_1= Label(o, text="")
ex_l2_1.grid(row=48,column=1)
ex_b1=Button(o,text="Submit",command=ip_act).grid(row = 49, column = 1)
o.mainloop()


activity_done_each=activity_done.split(",")
activity_time_each=activity_time.split(",")
for x in activity_done_each:
    time = int(activity_time_each[i])
    calories=int(c[x.lower()])
    v=calories*time*r
    totalcal+=v
    i+=1
print("Total Calorie Burnt: ",totalcal)

#--------------------------------------------------------------------------------------------------------------
#Code for user's calorie consumption

p=Tk()
foodl1 = Label(p, text = "CALORIE INTAKE",font=('Arial',15)).grid(row = 1, column = 1)
user_calorie=0
food_l1= Label(p, text="CHOOSE ").grid(row=2,column=1)
lb1 = Listbox(p,width=40,height=30) 
lb1.grid(row=3,column=1)
scb1 = Scrollbar(p) 
scb1.grid(row=3,column=40) 

file = open("Calorie_Intake.txt","r")
b = file.read()
c = eval(b)
food_consumed='apple'

for i7 in c.keys():
    lb1.insert(END,i7 )
'''
lb1.insert(END, "apple")
lb1.insert(END, "pear")
lb1.insert(END, "banana")
lb1.insert(END, "chickoo")
lb1.insert(END, "cherries")
lb1.insert(END, "dates")
lb1.insert(END, "grapes-black")
lb1.insert(END, "guava")
lb1.insert(END, "kiwi fruit")
lb1.insert(END, "litchies")
lb1.insert(END, "mangoes")
lb1.insert(END, "orange")
lb1.insert(END, "papaya")
lb1.insert(END, "peach")
lb1.insert(END, "pears")
lb1.insert(END, "pineapple")
lb1.insert(END, "plums")
lb1.insert(END, "strawberries")
lb1.insert(END, "watermelon")
lb1.insert(END, "pomegranate")
lb1.insert(END, "butter")
lb1.insert(END, "buttermilk")
lb1.insert(END, "cheese")
lb1.insert(END, "cream")
lb1.insert(END, "ghee")
lb1.insert(END, "milk")
lb1.insert(END, "coffee")
lb1.insert(END, "tea")
lb1.insert(END, "chapatti")
lb1.insert(END, "bread")
lb1.insert(END, "paratha")
lb1.insert(END, "burger")
lb1.insert(END, "pizza")
lb1.insert(END, "samosa")
lb1.insert(END, "kachori")
lb1.insert(END, "pakoda")
lb1.insert(END, "potato chips")
lb1.insert(END, "chicken")
lb1.insert(END, "fish")
lb1.insert(END, "egg")
lb1.insert(END, "omelette")
lb1.insert(END, "rice")
lb1.insert(END, "tea")
lb1.insert(END, "coffee")
lb1.insert(END, "rasam")
lb1.insert(END, "sambar")
lb1.config(yscrollcommand = scb1.set) 
scb1.config(command = lb1.yview) 
'''

fo_l2= Label(p, text="Enter the food from the list above(comma after each activity): ")
fo_l2.grid(row=34,column=1)
fo_e1= Entry(p)
fo_e1.grid(row = 44, column = 1) 


def ip_fo_food_consumed():
    global food_consumed
    food_consumed=fo_e1.get()  

    
def ip_fo():
    ip_fo_food_consumed()
    p.destroy()
    
    
fo_l2_1= Label(p, text="")
fo_l2_1.grid(row=47,column=1)
fo_b1=Button(p,text="Submit",command=ip_fo).grid(row = 48, column = 1)
p.mainloop()


food_consumed_each=food_consumed.split(",")
for x in food_consumed_each:
    user_calorie+=c[x.lower()]  
print("Total Calorie consumed: ",user_calorie)

#--------------------------------------------------------------------------------------------------------------
#Code for the final report page
tcc = user_calorie - totalcal
bp = str(sysbp)+'/'+str(diabp)

b=Tk()
sum_l1= Label(b, text="").grid(row = 1, column = 1)
sum_l2= Label(b, text="").grid(row = 1, column = 3)
sum_l3= Label(b, text="FINAL REPORT", font=('Arial',15)).grid(row = 1, column = 1)
sum_l4= Label(b, text = "Name: ").grid(row = 3, column = 1)
sum_l5= Label(b, text = name).grid(row = 3, column = 2)
sum_l6= Label(b, text = "Age: ").grid(row = 5, column = 1)
sum_l7= Label(b, text = age).grid(row = 5, column = 2)
sum_l8= Label(b, text = "Height: ").grid(row = 7, column = 1)
sum_l9= Label(b, text = height).grid(row = 7, column = 2)
sum_l10= Label(b, text = "Weight: ").grid(row = 9, column = 1)
sum_l11= Label(b, text = weight).grid(row = 9, column = 2)
sum_l12= Label(b, text = "BMI: ").grid(row = 11, column = 1)
sum_l13= Label(b, text = bmi).grid(row = 11, column = 2)
sum_l14= Label(b, text = "Heart Rate Per Minute: ").grid(row = 13, column = 1)
sum_l15= Label(b, text = hbpm).grid(row = 13, column = 2)
sum_l16= Label(b, text = "Blood Pressure: ").grid(row = 15, column = 1)
sum_l17= Label(b, text = bp).grid(row = 15, column = 2)
sum_l18= Label(b, text = "Total Calories Burnt: ").grid(row = 17, column = 1)
sum_l19= Label(b, text = totalcal).grid(row = 17, column = 2)
sum_l20= Label(b, text = "Total Calories Gained: ").grid(row = 19, column = 1)
sum_l21= Label(b, text = user_calorie).grid(row = 19, column = 2)
sum_l22= Label(b, text = "Overall Calorie Gain(+) or Loss(-): ").grid(row = 21, column = 1)
sum_l23= Label(b, text = tcc).grid(row = 21, column = 2)
sum_l24= Label(b, text="").grid(row = 22, column = 2)
sum_l24= Label(b, text = "THANK YOU!", font=('Arial',15)).grid(row = 24, column = 1)
b.mainloop()

#--------------------------------------------------------------------------------------------------------------