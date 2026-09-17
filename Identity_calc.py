print("------------Welcome to identity calculator---------------")
square=lambda x:x**2
whole_square=lambda a,b: square(a)+square(b)+2*a*b
sub_square=lambda a,b: square(a)+square(b)-2*a*b
diff_squares=lambda a,b: square(a)-square(b)
sum_squares=lambda a,b: square(a)+square(b)
cube=lambda x:x**3
whole_cube=lambda a,b: cube(a)+cube(b)+3*square(a)*b+3*a*square(b)
sub_cube=lambda a,b: cube(a)-cube(b)-3*square(a)*b+3*a*square(b)
diff_cubes=lambda a,b: cube(a)-cube(b)
sum_cubes=lambda a,b: cube(a)+cube(b)
print(""" 
          Type 1 to calculate (a+b)²
          Type 2 to calculate (a-b)²
          Type 3 to calculate a²-b²
          Type 4 to calculate a²+b²
          Type 5 to calculate (a+b)³
          Type 6 to calculate (a-b)³
          Type 7 to calculate a³-b³
          Type 8 to calculate a³+b³
          """)
calculate=input("Would you like to calculate?(y/n) ").lower()
while calculate=="y":
    try:
        what_to_calc=int(input("Enter a number "))
        num1=float(input("Enter a's value "))
        num2=float(input("Enter b's value "))
        if num1 == int(num1) and num2 == int(num2):
            num1 = int(num1)
            num2 = int(num2)
        if what_to_calc==1:
            value=whole_square(num1,num2)
            print(f"({num1}+{num2})²={value}")
        elif what_to_calc==2:
            value=sub_square(num1,num2)
            print(f"({num1}-{num2})²={value}")
        elif what_to_calc==3:
            value=diff_squares(num1,num2)
            print(f"({num1})²-({num2})²={value}")
        elif what_to_calc==4:
            value=sum_squares(num1,num2)
            print(f"({num1})²+({num2})²={value}")
        elif what_to_calc==5:
            value=whole_cube(num1,num2)
            print(f"({num1}+{num2})³={value}")
        elif what_to_calc==6:
            value=sub_cube(num1,num2)
            print(f"({num1}-{num2})³={value}")
        elif what_to_calc==7:
            value=diff_cubes(num1,num2)
            print(f"({num1})³-({num2})³={value}")
        elif what_to_calc==8:
            value=sum_cubes(num1,num2)
            print(f"({num1})³+({num2})³={value}")
        else:
            print("Please type a number according to identity")
    except Exception:
        print("Type a number!!!!!!")
         #Restart the loop if the datatype is invalid
        #Avoids creating extra while loop
        continue
    calculate=input("Calculate again?(y/n) ").lower()
 
print("Bye,user ")     
        
