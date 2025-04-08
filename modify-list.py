## This Prgram will allow user to modify specific element of list and change its value through user input ##

my_list = ['apple',33, 'orange', 45, 'pineapple']

print(my_list)

index_choice = int(input("please enter the index you want to change the value of :"))

value_choice = input("please enter your desired value you want to replace with :")

def change_list(index,value):
    my_list[index] = value

change_list(index_choice,value_choice)

print(f"updated list : {my_list}")


