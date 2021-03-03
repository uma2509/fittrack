#bmi
def bmi(weight,height):
	bmi=weight/(height**2)
	print("Your BMI is ",bmi)
	if bmi<25:
		print("You are underweight")
	else:
		print("You are overweight")
		
#heart condition
def heart_condition(hbpm): #Heart Beats Per Minute
	if hbpm>100:
		return "Tachycardia"
	elif hpbm<60:
		return "Bradycardia"
	else:
		return "Normal Heart Rate"
