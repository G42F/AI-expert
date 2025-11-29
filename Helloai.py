print("Hello I am ai bot What is your name?")
name=input()
print("Hello " + name + " nice to meet you!")
print("How are you felling today ?")
mood=input().lower()
if mood=="good" or mood=="great" or mood=="fine":
    print("I am happy to hear that " + name)
elif mood=="bad" or mood=="sad" or mood=="not good":
    print("I am sorry to hear that " + name + " I hope your day gets better!")
else:
    print("I see " + name + " I hope you have a good day!")