l=[]
while True:
  c=int(input(
      '''
      Choose An Operation
      1. Enqueue
      2. Dequeue
      3. Peek Elements
      4. Display Queue
      5. Exit

      '''
  ))
  if c==1:
    n=input("\n\nEnter The Value :")
    l.append(n)
    print(l,"\n")
  elif c==2:
    if len(l)==0:
      print("\nEmpty Queue")
    else:
      p=l.pop(0)
      print("Deleted Element",p)
      print(l)
  elif c==3:
    if len(l)==0:
      print("Empty Queue")
    else:
      print("First Queue Element",l[0])
  elif c==4:
    print("Displaying Queue",l)
  elif c==5:
    break
  else:
    print("Invalid Input")
