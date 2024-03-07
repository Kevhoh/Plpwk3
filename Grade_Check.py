score = float(input("Enter The Score: "))

if score >= 80:
    performance = "Excellent"
elif score >= 70:
    performance = "Good Work"
elif score >= 60:
    performance ="Keep Up"
elif score >= 50:
    performance ="Fair"
elif score >= 40:
    performance ="Good Trial"
else:
    performance = "Fail"
    
print(f"The student's Performance is : {performance}")
