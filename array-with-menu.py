#Write a python program that do the following:
#   - display the initial content of the array
#   - display a menu of options
#   - allow user to select item in the menu (check if valid)
#   - perform the selected option (you may prompt additional info to user when need)
#   - display the resulting values of the array

print("\n.・。.・゜✭・.・✫・゜・。.・。.・゜✭・.・✫・゜・。.\n")
list_values=[5, 6, 7, 8, 9, 12, 14, 19, 20, 21]
#displays the content of the array
print(list_values)
menu=True
while menu:
    print("\n.・。.・゜✭・.・✫・゜・。.・。.・゜✭・.・✫・゜・。.")
    print ("""
    Menu
    [1] ❀ Add an element
    [2] ✎ Insert an element
    [3] ✭ Modify an element
    [4] ✂ Delete an element
    [5] ▲ Arrange in ascending order
    [6] ▼ Arrange in descending order
    """)

    menu=input("What would you like to do? ")
    if menu=="1":
        add_value=input("What number would you like to add to the existing list? ")
        list_values.append(add_value)

        print(f'\nUpdated List {list_values}\n')
    elif menu=="2":
        insert_value=input("Please input a number you would like to insert to the list: ")
        index=int(input("At which position on the list would you like your number to appear? "))

        list_values.insert(index, insert_value)

        print(f'\nUpdated List {list_values}\n')
        
    elif menu=="3":
        modify_value=int(input("What number would you like to input on the list? "))
        modify_index=int(input("Which item would you like to be replaced by your number? "))

        list_values[modify_index] = modify_value

        print(f'\nUpdated List {list_values}\n')

    elif menu=="4":
        delete_value=(input("Which element of the list you would like to remove? "))

        list_values.remove(delete_value)
        
        print(f'\nUpdated List {list_values}\n')

    elif menu=="5":
        list_values.sort
        print(f'\nUpdated List {list_values}\n')

    elif menu=="6":
        list_values.sort(reverse=True)
        print(f'\nUpdated List {list_values}\n')
    break

    