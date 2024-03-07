#write a simple python code that can rate students performance
score = int(input("Enter The Students Score (0-100): "))

if score >=80:
    performance = "Distinction"
elif score >= 60:
    performance = "Credit"
elif score >= 40:
    performance = "Fair"
else:
    performance = "Fail"

print(f"The Student's performance is: {performance}")