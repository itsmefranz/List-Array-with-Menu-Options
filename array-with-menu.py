#Write a python program that do the following:
#   - display the initial content of the array
#   - display a menu of options
#   - allow user to select item in the menu (check if valid)
#   - perform the selected option (you may prompt additional info to user when need)
#   - display the resulting values of the array

print(".・。.・゜✭・.・✫・゜・。.")
list_values=[5, 6, 7, 8, 9, 12, 14, 19, 20, 21]
#displays the content of the array
print(list_values)
menu=True
while menu:
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

        print(f'Updated List {list_values}')
    elif menu=="2":
        insert_value=input("Please input a number and an index you would like to put your number at: ")
        list_values.insert(insert_value)

        print(f'Updated List {list_values}')
        
