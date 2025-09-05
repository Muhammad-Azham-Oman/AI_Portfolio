print("______WELCOME TO CONTACTS MANNAGEMENT SYSTEM_______")
print("click '1' to add a new contact.")
print("click '2' to view all the contacts.")
print("click '3' to view a specific contact.")
print("click '4' to delete a specific contact.")
print("Click '5' to update the contact.")
print("click '6' to Exit.")
while True:
  choice = int(input("Enter your choice (1to5):"))

  if (choice==6):
    print("Goodbye,See you again.")
    break

  elif (choice==1):
    print("Click '1' if you want add a phone number.")
    print("Click '2' if you want add an E-mail.")
    choice_1 = int(input("Enter your choice (1 or 2):"))
    if (choice_1 == 1):
        n = input("Enter the name: ")
        p = int(input("Enter the number:"))
        with open("contacts/phone","a") as f:
            f.write(f"\n{n}:0{p}")
        print("Phone number added successfully.")
    elif(choice_1 == 2):
        name = input("Enter the name: ")
        email = input("Enter the email:")
        with open("contacts/email","a") as f:
            f.write(f"\n{name}:{email}")
        print("Email added successfully.")
    else:
        ("Invalid.")

  elif (choice==2):
    with open("contacts/phone","r") as f:
        contant = f.read()
        print("PHONE NUMBERS:\n")
        print(f"{contant}\n")
    with open ("contacts/email") as f:
        contant = f.read()
        print("E-MAILS:\n")
        print(f"{contant}\n")

  elif (choice == 3):
    print("Click '1' if you want to view a phone number.")
    print("Click '2' if you want to view an E-mail.")
    choice_2 = int(input("Enter your choice (1 or 2):"))
    if (choice_2 == 1):
        n = input("Enter the name of contact you want to view: ")
        with open ("contacts/phone") as f:
            lines = f.readlines()
            for line in lines:
               if (n in line):
                  print(line)
                  break

    elif (choice_2 == 2):
        n = input("Enter the name of contact you want to view: ")
        with open ("contacts/email") as f:
            lines = f.readlines()
            for line in lines:
               if (n in line):
                  print(line)
                  break


  elif(choice==4):
     print("Click '1' if you want to delete a phone number.")
     print("Click '2' if you want to delete an E-mail.")
     choice_3 = int(input("Enter your choice:"))
     if(choice_3==1):
        n = input("Enter the name of contact you want to delete:")
        with open ("contacts/phone") as f:
            lines = f.readlines()
            for line in lines:
               if (n not in line):
                  with open ("contacts/phone","w") as f:
                     f.write(line)
     elif(choice_3==2):
        n = input("Enter the name of contact you want to delete:")
        with open ("contacts/email") as f:
            lines = f.readlines()
            for line in lines:
               if (n not in line):
                  with open ("contacts/email","w") as f:
                     f.write(line)

  elif(choice==5):
     print("Click '1' if you want to update a phone number.")
     print("Click '2' if you want to update an E-mail.")
     choice_4 = int(input("Enter your choice:"))
     if choice_4 == 1:
        b = input("Enter the name of contact you want to update:")
        name = input("Enter the new name:")
        phone = int(input("Enter the new phone number:"))
        with open ("contacts/phone") as f:
            contant = f.read()
            if b not in contant:
               print("Contact not found.")
            elif b in contant:
              with open ("contacts/phone","r") as f:
                 lines = f.readlines()
              with open ("contacts/phone","w") as f:
               for line in lines:
                if (b not in line):
                     f.write(line)
              with open ("contacts/phone","a") as f:
                 f.write(f"\n{name}:0{phone}")
     
     if choice_4 == 2:
        c = input("Enter the name of contact you want to update:")
        name = input("Enter the new name:")
        phone = int(input("Enter the new E-mail:"))
        with open ("contacts/email") as f:
            contant = f.read()
            if c not in contant:
               print("Contact not found.")
            elif c in contant:
              with open ("contacts/email","r") as f:
                 lines = f.readlines()
              with open ("contacts/email","w") as f:
               for line in lines:
                if (c not in line):
                     f.write(line)
              with open ("contacts/email","a") as f:
                 f.write(f"\n{name}:0{phone}")