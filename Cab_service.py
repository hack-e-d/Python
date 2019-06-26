#Program for Uber application
c=0
count=1
t=0
cq=1
o=0
a=input("Enter the passanger Name:")
while cq==1 :

  try:
    s=float(input("Enter the start point:"))
    if(s<0):
      print("Enter a start point greater than 0")
      continue
    e=float(input("Enter the stop point:"))
    if(e<0):
      print("Enter a end point greater than 0")
      continue
  except:
    print("Invalid Intput Reenter the inputs")
    continue
  d=e-s
  if(d>0):
    while True:
      o=int(input("Enter the ride choise 1.MINI 2.MICRO 3.AUTO:"))
      d=(e-s)
      if(d>0):
        if(o==1):
          c=d*10
          break
        elif(o==2):
          c=d*15
          break
        elif(o==3):
          c=d*8
          break
        else:
          print("Invalid option Reenter details")
      else:
        print("Start and stop are same reenter:") 
        break   
  else:
    print("Distance is negative:") 
  if(o<=3 and d!=0 and d>0):
    t+=c
    print("____INVOICE______")
    print("Passanger name:",a)
    print("Ride No:",count)
    print("Cost of ride:",t)
    cq=int(input("Enter 1 to continue the rides:"))
    if(cq==1):
      count+=1
    



