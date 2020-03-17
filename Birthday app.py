dict={}
while True:
    print("----------Birthday LIST-----------\n")
    print("Note:Here you can add your favorite people birthdays")
    print("1.Show Birthday Date")
    print("2.Add To Birthday List")
    print("3.EXIT")
    choice=input("Enter Your Choice:")
    if choice=='1':
        if len(dict.keys())==0:
               print("nothing to show \n i did not attach any database for this program  to store data.\n if you have already stored then \n a text file will be created in your system.\n Please check there")
        else:
               name=input("enter name to look for birthday")
               birthday=dict.get(name,"No Data Found")
               print(birthday)
    elif choice=='2':
               name=input("Enter Friend's name:")
               date=input("Enter Birthday's date:")
               dict[name]=date
               print("Birthday Added")
               file=open("birthdaylist.txt","w")
               file.write(name+"\n")
               file.write(date)
               file.close()
    elif choice=='3':
        
              print("press enter to exit")
              exit()
    else:
        print("Choose a valid Option")

