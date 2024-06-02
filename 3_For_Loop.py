# Your monthly expense list (from Jan to May) looks like this,

# expense_list = [2340, 2500, 2100, 3100, 2980]
# Write a program that asks you to enter an expense amount and program should tell you in which month that expense occurred. If expense is not found then it should print that as well.

Month_list = ['Jan','Feb','Mar','April','May']

expense_list = [2340, 2500, 2100, 3100, 2980]

E = int(input("E: "))


j = -1 
for i in range(len(expense_list)) :

    if E == expense_list[i]:

        j = i 
        break

if j != -1 :
       print(f'You spent {E} in {Month_list[j]}')
else:
       print(f'You didn\'t spend {E} in any month')





