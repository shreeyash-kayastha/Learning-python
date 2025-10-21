#write a program that repeateadly reads numbers until the user  enters "done". Once "done" is entered ,
#print out the total,count , and average of numbers . If the user enters anything other than a number ,
#detect their mistake using try and except and print an error message and skip to the next number.
y=0
z=0.0

while True :
  x=input("enter a number")
  if x=="done":
    print("the total is",z)
    print("the count is",y)
    m=z/y
    print("the average is",m)
    break
  try:
    x=float(x)
  except:
    print("error. enter a valid number")
    continue
  y=y+1
  z=z+x
  
  
  
  