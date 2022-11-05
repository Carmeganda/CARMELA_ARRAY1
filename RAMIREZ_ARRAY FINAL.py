#Write a python program that do the following:

#display the initial content of the array
#display a menu of options
#allow user to select item in the menu (check if valid)
#perform the selected option (you may prompt additional info to user when need)
#display the resulting values of the array


#Note:
#The program has an array variable containing 10 random numbers
#You may add other options and features
#Your program should be uploaded to github before 1:30pm
#Record a demo presenting your program
#Send the demo directly to Sir Danilo's messenger

array= [12, 16, 21, 18, 24, 26, 32, 18, 17, 36]
def menu():
    print("--------------------------")
    print("Index: [12, 16, 21, 18, 24, 26, 32, 18, 17, 36]")
    print(f"   Array: {array}")
    print("[Option 1] Add an element in array")
    print("[Option 2] Insert an element at a particular index")
    print("[Option 3] Remove the given element from the array")
    print("[Option 4] Modify an element")
    print("[Option 5] Arrange in ascending order")
    print("[Option 6] Arrange in descending order")
    print("--------------------------")
menu()
option= int(input("What do you want to do?"))

if option == 1:
   num=int(input("what is the number to add?"))
   array.append(num)
   Add = array.append(num)
   print("The Numbers has been Added")
   print(array)

elif option == 2:
    num=int(input("What number do you want to insert?"))
    location=int(input("What is the location to insert? "))
    array.insert(location, num)
    print("The numbers has been inserted")
    print(array)

elif option == 3:
    num= int(input("What number do you want to delete? "))
    array.remove(num)
    print(array)

elif option == 4:
      location= int(input("What is the position you want to delete?"))
      num = int(input("What number do you want to add?"))
      array.pop(location)
      array.insert(location, num)
      print("The element has been Modify")
      print(array)

elif option == 5:
        num = array.sort()
        print("The element has been arrange to ascending order")
        print(array)

elif option == 6:
        num= array.reverse()
        print("The element has been arrange to descending order")
        print(array)
