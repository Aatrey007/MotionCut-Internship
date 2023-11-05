user = input("Enter Username: ")
print("Welcome " +str(user))
begin = input("Do You Wish to begin? ")

if begin.lower() == "yes":
    print("Good! Then Let The Games Begin!....")
    print("Greetings " + str(user) + "!!....")
    print("Your friend has been kidnapped, and you are being demanded to pay $500000.....")
    print("You have two options - Agree or Disagree...Choose wisely!")

    choice = input("What do you choose? ").lower()

    if choice == "disagree":
        print("You have lost your friend.....")
    elif choice == "agree":
        print("So you decided to give the money to save your friend...")
        print("The kidnapper wants you to meet at the tower at 9:30 pm tonight")
        print("You are skeptical of the situation...")
        print("Your options are - 1. Ask for proof of life, 2. Change location, 3. Deny the exchange")

        choice_1 = int(input("Enter your choice: "))

        if choice_1 == 1:
            print("Wise move " + str(user) + "!!")
            print("The kidnapper agreed to send proof of life but only after you reach the vicinity of the tower with the money....")
            print("Do you agree to this?")

            choice_2 = input("Enter your choice (yes/no): ").lower()

            if choice_2 == "yes":
                print("Congratulations you have successfully saved your friend!!!!")
            elif choice_2 == "no":
                print("You have lost your friend.....")
            else:
                print("Invalid choice")
        elif choice_1 == 2:
            print("The kidnapper grew impatient and decided to cancel the deal.... you lose , game over !!!!")
        elif choice_1 == 3:
            print("You have lost your friend.....")
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
else:
    print("Too Bad...")
