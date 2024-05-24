# I have a string variable called s='maine 200 banana khaye'. This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'. Replace incorrect words in original strong form

s='maine 200 banana khaye'
s_1 = s.replace("200","10").replace('banana','samosa')
print(s_1)

print('maine 200 banana khaye'.replace("200","10").replace('banana','samosa'))