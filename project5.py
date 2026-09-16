print("==========SECURE LOGIN SYSTEM==========")
username = input("\nEnter Username:")
password = "admin@123"
attempts = 3
pw = input("\nEnter Password:")
if pw == password:
    print("\nLogin Credentials verified!")
elif pw != password:
    print("\nincorrect password")
otp = 583214
print("\nyour OTP is:",otp)

for i in range(attempts):
    enterotp = int(input("\nEnter OTP:"))
    if enterotp == otp:
        print("\nOTP Verification Successful!")
        print("\n==========LOGIN SUCCESSFUL!==========")
        print("\nWelcome",username)
        break
    elif enterotp != otp:
        print("\n incorrect otp")
else:
    print("\nclose")
   
                    
    
    
    


