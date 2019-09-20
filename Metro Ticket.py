#Choice based Project

def MetroProject():
  
  print("\t ~WELCOME TO MUMBAI METRO~")
  print('----- YOU ARE AT ANDHERI MERTO STATION -----')
  print('1: for single journey')
  print ('2: for reurn journey')
  print('3: for smart card purchase')
  print('4: for trip pass')
  print('5: checking balance')
  print('6: for refund')
  print('7: for renewal for smart card')
  print('0: to exit')
  ch=int(input('Enter the choice: '))
  try:
    if(ch==1):
      singlejourney()
    elif(ch==2):
      returnjourney()
    elif(ch==3):
      sm()
    elif(ch==4):
      tp()
    elif(ch==5):
      balance()
    elif(ch==6):
      refund()
    elif(ch==7):
      rn()
    elif(ch==0):
      exit()
    else:
      print('wrong choice')
      MetroProject()
  except:
    print('something went wrong')
    MetroProject()

def singlejourney():
  try :
    print(' 1: for WEH \n 2: for AIRPORT ROAD\n 3: for MAROL NAKA \n 4: for SAKI NAKA\n 5: for GHATKPOR\n')
    
    i=int(input('Enter Your destination: '))
    if(i==1):
      cost=10
      print("Cost for WEH: ",cost)
    elif(i==2):
      cost=15
      print("Cost for AIRPORT ROAD: ",cost)
    elif(i==3):
      cost=20
      print("Cost for MAROL NAKA: ",cost)
    elif(i==4):
      cost=30
      print("Cost for SAKI NAKA: ",cost)
    elif(i==5):
      cost=30
      print("Cost for GHATKPOR: ",cost)
    else:
      print('Sry!!! Invalid choice')
      singlejourney()
  except:
    print('something went wrong')
    singlejourney()
    MetroProject()

MetroProject()














  
    

    
