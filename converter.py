print("This is a Temperature Unit Converter")
choice=(input("Enter conversion (F_to_C/C_to_F): "))         #C is Celsius and F is Fahrenheit
temp = int(input("Enter the Temperature: "))
if (choice == "F_to_C"):
    c = (temp - 32)/1.8
    print( temp ,"degrees in fahrenheit is :", c, "degress in celsius")
elif (choice == "C_to_F"):
    f = (temp*1.8) + 32
    print( temp ,"degrees in celsius is :", f, "degress in fahrenheit")
else :
    print("invalid")

    
    
