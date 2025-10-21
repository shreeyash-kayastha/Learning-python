greatest=-1
print('greatest before:',greatest)
for i in [1,5,34,20,70,19]:
  print('greatest so far is ',greatest,'and i is',i)
  if greatest<i:
    greatest=i

print('greatest after:',greatest)
