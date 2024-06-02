# Lets say you are running a 5 km race. Write a program that,

# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

Distance = 5

for i in range(Distance):

    print(f"You ran {i+1} k.m. ")
    q = input("Are you tired? ").lower()
    if q == 'yes' :
        print("You didn\'t finish the race")
        break
    
if i == 4 :

    print("Congratulations you finished the race")
