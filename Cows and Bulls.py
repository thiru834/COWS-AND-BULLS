from random import randint
def random():
  while True:
    n=str(randint(100,999))
    if(not(n[0]==n[1] or n[1]==n[2] or n[2]==n[0])):
      return n

name =input("Welcome to the cows and bulls game\n please enter your name:")
print("hi",name)
chances=5
cows =0
bulls=0
num=str(random())
while chances>0:
  print("guess the number please")
  n = str(input("enter a number:"))
  if(num==n):
    print("Congratulations you have guessed it right")
    break
  else:
    for i in range(0,3):
      if num[i]==n[i] :
        bulls=bulls+1
      elif n[i] in num :
        cows=cows+1
    print("common you have ",bulls," bulls and ",cows," cows")
    bulls=0
    cows=0
    chances=chances-1

print("the right number is ",num)

