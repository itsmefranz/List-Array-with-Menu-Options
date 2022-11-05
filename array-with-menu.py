#Write a python program that do the following:
#   - display the initial content of the array
#   - display a menu of options
#   - allow user to select item in the menu (check if valid)
#   - perform the selected option (you may prompt additional info to user when need)
#   - display the resulting values of the array

print(" \n.・。.・゜✭・.・✫・゜・。.・。.・゜✭・.・✫・゜・。.\n")
list_values=[5, 6, 7, 8, 9, 12, 14, 19, 20, 21]
#displays the content of the array
print(list_values)

print("\n┏━•❃°•°❀°•°❃°•°❀°•°❃°•°❀°•°❃°•°❀°•°❃•━┓")
print ("""
    Menu
    [1] ❀ Add an element
    [2] ✎ Insert an element
    [3] ✭ Modify an element
    [4] ✂ Delete an element
    [5] ▲ Arrange in ascending order
    [6] ▼ Arrange in descending order
    """)
print("┗━•❃°•°❀°•°❃°•°❀°•°❃°•°❀°•°❃°•°❀°•°❃°•━┛\n")

def menu_program():
    menu=input("What would you like to do? ")
    if menu=="1":
        add_value=int(input("What number would you like to add to the existing list? "))
        list_values.append(add_value)

        print(f'\nUpdated List {list_values}\n')

    elif menu=="2":
        insert_value=int(input("Please input a number you would like to insert to the list: "))
        index=int(input("At which position on the list would you like your number to appear? "))

        list_values.insert(index, insert_value)

        print(f'print("\nUpdated List {list_values}\n')
        
    elif menu=="3":
        modify_value=int(input("What number would you like to input on the list? "))
        modify_index=int(input("Which item would you like to be replaced by your number? "))

        list_values[modify_index] = modify_value

        print(f'\nModified List {list_values}\n')

    elif menu=="4":
        delete_value=int(input("Which element of the list you would like to remove? "))

        list_values.remove(delete_value)
        
        print(f'\nElement Removed List {list_values}\n')

    elif menu=="5":
        list_values.sort
        print(f'\n Ascending Sorted List {list_values}\n')

    elif menu=="6":
        list_values.sort(reverse=True)
        print(f'\nDescending Sorted List {list_values}\n')
    else:
        print("Not a valid menu option /ᐠ - ˕ -マ Please try again ૮ ˶ᵔ ᵕ ᵔ˶ ა \n")

def again():
    while True:
    #Loop for answer
        input_again = input("Do you wish to try again? (ㅅ´ ˘ `) Y/N: ")
        try_again = input_again.upper()
        if try_again == "Y":
            print("\n")
            menu_program()
        elif try_again == "N":
            print("\n.・。.・゜✭・.・✫・゜・。.・。.・゜✭・.・✫・゜・。.")
            print("See ya next time! Bye for now ◝(ᵔᵕᵔ)◜\n")
            break
        else:
            print("\nEnter Y if you want to start again, or N to exit the program.")

menu_program()
again()