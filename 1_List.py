# Let us say your expense for every month are listed below,
Expense = [2200,2350,2600,2130,2190]

#In Feb, how many dollars you spent extra compare to January?
Extra = Expense[1]- Expense[0]
print(Extra)

# Find out your total expense in first quarter (first three months) of the year.
Expenses = Expense[0] + Expense[1] + Expense[2]
print(Expenses)

#  Find out if you spent exactly 2000 dollars in any month
if 2000 in Expense:
  
  print("There is exactly 2000 dollars expense")

else:
  print('No 2000 dollars exact expense')


# June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
Expense.append(1980)
print("New list: ",Expense)

# You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# # based on this

Expense[3] = Expense[3] - 200

print("Correction of April Month: ", Expense[3])