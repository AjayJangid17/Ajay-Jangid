import random,time

login = 1
while (login <=3):
    print("WELCOME TO HACKERS WORLD")
    username = 'hackersworld@kan.com'
    password = 8005
    print('-------------------------')
    u = input("enter your username: ")
    p = int(input("enter your password: "))
    print()
    if u == username and p == password:
        print("OTP Generating.......")
        print()
        time.sleep(3)
    else:
        print(login,"Attempt....Invalid Entry")
        print()
        if login == 3:
            print('Your 3 Attempt is over login again...')
        login +=1
        continue
        
        


    count = 1
    while (count<=3):
        otp = random.randrange(1000,9999)
        print(otp)
        num = int(input("enter OTP number: "))
        if num == otp:
            print("successfully login")
            print("Your data is hacked")
            break
        else:
            print('Invalid OTP...', count, 'Attempt')
            if count == 3:
                print('Exceeded your login limit ') 
            count += 1
    break
    

    
    
        
          


    
    
