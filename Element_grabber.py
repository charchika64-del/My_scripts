my_list=[1,2,3,4,5,6,7,8,9,10]
print("Type 1 for indexing ,2 for slicing and 3 to exit: ")
while True:
    try:
        num=int(input("Enter number: "))
        if num==1:
             index=int(input("Enter index: "))
             print("The element is",my_list[index])
        elif num==2:
            initial_index=int(input("Enter the starting index: "))
            final_index=int(input("Enter the last index: "))
            print("Here are the elements:",my_list[initial_index:final_index])
        elif num==3:
             print("Program finished")
             break
        else:
           print("Type 1 or 2")
    except ValueError:
          print("Please type in something valid.")
    except IndexError:
          print("This index item is not available.")
