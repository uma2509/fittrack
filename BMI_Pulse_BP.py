#BMI
def bmi(weight,height): #In kg and m respectively
	bmi=weight/(height**2)
	print("Your BMI is ",bmi)
	if bmi<25:
		print("You are underweight")
	else:
		print("You are overweight")
		
#Heart Rate (Pulse)
def heart_condition(hbpm): #Heart Beats Per Minute
	if hbpm>100:
		return "Tachycardia"
	elif hpbm<60:
		return "Bradycardia"
	else:
		return "Normal Heart Rate"

#Blood Pressure
def blood_pressure(sys_bp,dia_bp): #Systolic/Diastolic Blood pressure
	if sys_bp>120: #In mm of Hg
		return "High BP"
	elif dia_bp<80:
		return "Low BP"
	else:
		return "Normal Blood Pressure"
