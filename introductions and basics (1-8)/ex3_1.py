#rewrite the pay so that the pay is 1.5 times entered amount if the work is >40 hours
hours=input("how many hours did you work?")
rate=input("what is the rate ?")
if float(hours)>40:
  #rate= float(rate)*1.5
  ex=float(hours)-40
  pay= (40* float(rate) )+(ex*float(rate)*1.5) 
  print("pay= ", pay)
elif float(hours)<=40:
  pay= float(hours) * float(rate)
  print("pay= ", pay)
