#rewrite ex3_2 so that it can catch error

hours=input("how many hours did you work?")
rate=input("what is the rate ?")

try:
  if float(hours)>40:
  #rate= float(rate)*1.5
    ex=float(hours)-40
    pay= (40* float(rate) )+(ex*float(rate)*1.5) 
    print("pay= ", pay)
  elif float(hours)<=40:
    pay= float(hours) * float(rate)
    print("pay= ", pay)
except:
  print("ERROR! please enter a numeric value")
  quit()