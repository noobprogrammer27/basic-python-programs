import time
print("----------ATM MACHINE----------")
print("Welcome to  xxxx ATM")
print("Swipe Your Card please")
amount=10000
#your password is 2222

y="2222"
print("_________________")



x=input("enter your pin")
print("checking........................!!")
time.sleep(1)
if x==y:
  print("________________")
  print("1.Cash Withdrawl")
  print("2.check enquiry")
  print("3.check balance")
  print("4.print receipt")
  print("5.Mini Statement")
  print("6.Exit")
  print("________________")

  choice=int(input("enter your choice"))
  if choice==1:
     print("a.Current Account")
     print("b.Saving Account")
     print("________________")
     ch=input("choose between a and b")
     if ch=='a':
         
         
        wdraw=int(input("enter the amount to be withdraw:"))
        print("Transaction Successful")
        print("Collect Your Amount")
        print("your remain balance is",amount-wdraw)
        print("Thanks for using SBI ATM")            
     else:
        sdraw=int(input("enter the amount to be withdraw:"))
        print("Transaction Successful")
        print("collect your amount")
        print("your remain balance is",amount-wdraw)
        print("Thanks for using SBI ATM")
  elif choice==2:
     print(f"Your Current Balance is {amount}")
     print("Thanks For using SBI ATM")
  elif choice==3:
     print(f"Remaining Balance is {amount}")
     print("Thanks for using ATM")
  elif choice==4:
     yn=input("Would you want to print the receipt of remaining balance i.e.{amount} yes/no")
     if yn=='yes':
         
         print("collect your Receipt")
     elif yn=='no':
         print("thanks for using SBI ATM")
     else:
         print("error 404")           
         
     
        
  elif choice==5:
     print("collect your mini statement of your current balance")
     print("Thanks for using SBI ATM")

  elif choice==6:
     exit()             
     


  else:
      print("wrong choice")
                   
else:
  print("Wrong Pin ,Try After Sometime")
  
  
