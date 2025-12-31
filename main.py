from art import logo
from game_data import data
print(logo)
p=0
t=""
k=0
s=len(data)
ans=' '
for i in range(0,(s-2)):
    print(data[i]["name"])
    print(data[i]["description"])
    print(data[i]["country"])
    t=int((data[i]["follower_count"]))
    print("person a")
    print(data[i+1]["name"])
    print(data[i+1]["description"])
    print(data[i+1]["country"])
    print("person b")
    k = int(data[i+1]["follower_count"])
    ans=''
    g=input("who has more followers, type 'a' or b'")
    if(t>k):
        ans='a'
    elif(t<k):
        ans='b'
    if(g==ans):
        p=p+1
    else:
        break
    print("your current score is",p)
    t=0
    k=0

print ("final score",p)
