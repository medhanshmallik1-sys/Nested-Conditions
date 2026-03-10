medical_cause = str(input("Did you have a medical cause? (Y/N)"))
if medical_cause == 'Y':
    print ("You are allowed")
else:
    atten = int(input("Enter Attendece Percentage:"))
    if atten >= 75:
        print(" Allowed")
    else:
        print(" Not allowed")