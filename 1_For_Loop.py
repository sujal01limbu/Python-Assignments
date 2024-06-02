# After flipping a coin 10 times you got this result,
# result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
# Using for loop figure out how many times you got heads


result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for items in result:
    if items == "heads":
        count = count + 1
print(count)