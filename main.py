import itertools
import pprint
import pandas as pd
import numpy as np
import random
from itertools import combinations
cartList ={}
masterdict = {}
logTracker=[]
hexnum = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}
decnum = []
ansList = []
alphabet = []
primenums = []
#user start currency
userCurr= 12000
#user start bag of Hex gems
userGems=["A","A","A","A","C","E","D","E","A","A","A","E","E","B","A","E","C","F","C","A","A","C","C","A","F","E","D","E","A","A","A","E","E","B","A","E","C","F","C","A","A","C","C","A","F","E","D","E","A","A","A","E","E","B","A","E","C","F","C","A",]
# shopping
chLst = {"Weightless Wiz Robe(+15 int)":116,
"Spider Silk Armor(+17 agi)":199,
"Brachiosaurus Hide Armor(+10 agi)":100,
"Steel of the Sea Armor(+10 str)":202,
"Grill Master Robe(+3 int)":5}

heLst={"Professor Chaos Helm(+7 str)":62,
"Kinda Okay Helm(+1 int)":10,
"Mysterion Mask(+5 agi)":77,
"Mask of Madness(+4 agi)":56,
"Cast Iron Bowl(1+ str)":3}

poLst={"Ludacris Healing Potion":30,
"Ludacris Mana Potion":30,
"Strength Boost Potion":20,
"Agility Boost Potion":20,
"Intelligence Boost Potion":20}

weLst={"Sword of 1000 Truths(+20str, +20agi, +20int)":9999,
"Twig Bow(+1 agi)":3,
"Man Bear Pig Claws(+17 agi)":136,
"Vantablack Staff of Magic(+18 int) ":240,
"Goober Sword(+2 str)":12}

boLst={"Arctic Bear Boots(+10 str)": 55,
"Gym Shoes(+1 agi)":3,
"Golden Toes Sandle(+6 int)":74,
"Super Cereal Boots(7 str)":82,
"Marty Mcfly Shoes(+10 agi)":93}
#11 shopping interactions
def userInH():
  count =1
  print("\n=== HELMS MENU ===\n")
  for keys,values in heLst.items():
    print(str(count) + " "+ keys + " = $"+str(values))
    count+=1
  console = int(input("\nChoose the item you like to purchase\nInput: "))
  dupCheck(console,heLst)
  if console==1:
    cartList.update({"Professor Chaos Helm(+7 str)":62}) 
    logTracker.append(1)   
  elif console == 2:
    cartList.update({"Kinda Okay Helm(+1 int)":10})
    logTracker.append(2)   
  elif console ==3:
    cartList.update({"Mysterion Mask(+5 agi)":77})
    logTracker.append(3)   
  elif console==4:
    cartList.update({"Mask of Madness(+4 agi)":56})
    logTracker.append(4)   
  elif console==5:
    cartList.update({"Cast Iron Bowl(1+ str)":3})
    logTracker.append(5)
  console = input("\nWould you like to purchase another helm?\nInput (y/n): ")
  if console.upper() =="Y":
    userInH()  #recursion
  else:
    inventory()
#11 shopping interactions
def userInC():
  count =6
  print("\n=== BODY ARMORS MENU ===\n")
  for keys,values in chLst.items():
    print(str(count) + " "+ keys + " = $"+str(values))
    count+=1
  console = int(input("\nChoose the item you like to purchase\nInput:  "))
  dupCheck(console,chLst)
  if console==6:
    cartList.update({"Weightless Wiz Robe(+15 int)":16}) 
    logTracker.append(6)   
  elif console == 7:
    cartList.update({"Spider Silk Armor(+17 agi)":199})
    logTracker.append(7)   
  elif console ==8:
    cartList.update({"Brachiosaurus Hide Armor(+10 agi)":100})
    logTracker.append(8)   
  elif console==9:
    cartList.update({"Steel of the Sea Armor(+10 str)":202})
    logTracker.append(9)   
  elif console==10:
    cartList.update({"Grill Master Robe(+3 int)":5})
    logTracker.append(10)   
  console = input("\nWould you like to purchase another body armor?\nInput (y/n): ")
  if console.upper() =="Y":
    userInC() #recursion
  else:
    inventory()
#11 shopping interactions
def userInP():
  console=input('\n"My potions are too strong for you Traveler and can not drink more than 3 potions at a time" \n\nDo you want to see all possible triple potion combinations?\nInput (y/n): ')
  if console=="y":
    poComb()
  count =11
  print("\n=== POSTIONS MENU ===\n")
  for keys,values in poLst.items():
    print(str(count) + " "+ keys + " = $"+str(values))
    count+=1
  console = int(input("\nChoose the item you like to purchase\nInput:  "))
  dupCheck(console,chLst)
  if console==11:
    cartList.update({"Ludacris Healing Potion":30}) 
    logTracker.append(11)   
  elif console == 12:
    cartList.update({"Ludacris Mana Potion":30,})
    logTracker.append(12)   
  elif console ==13:
    cartList.update({"Strength Boost Potion":20})
    logTracker.append(13)   
  elif console==14:
    cartList.update({"Agility Boost Potion":20})
    logTracker.append(14)   
  elif console==15:
    cartList.update({"Intelligence Boost Potion":20})
    logTracker.append(15)   
  console = input("\nWould you like to purchase another potion?\nInput (y/n): ")
  if console.upper() =="Y":
    userInP() #recursion
  else:
    inventory()
#11 shopping interactions
def userInW():
  count =16
  print("\n=== WEAPONS MENU ===\n")
  for keys,values in weLst.items():
    print(str(count) + " "+ keys + " = $"+str(values))
    count+=1
  console = int(input("\nChoose the item you like to purchase\nInput:  "))
  dupCheck(console,chLst)
  if console==16:
    print("\nInsuffcient funds to buy this item\n") 
    logTracker.append(16)   
  elif console == 17:
    cartList.update({"Twig Bow(+1 agi)":3})
    logTracker.append(17)   
  elif console ==18:
    cartList.update({"Man Bear Pig Claws(+17 agi)":136})
    logTracker.append(18)   
  elif console==19:
    cartList.update({"Vantablack Staff of Magic(+18 int) ":240})
    logTracker.append(19)   
  elif console==20:
    cartList.update({"Goober Sword(+2 str)":12})
    logTracker.append(20)   
  console = input("\nWould you like to purchase another weapon?\nInput (y/n): ")
  if console.upper() =="Y":
    userInW() #recursion
  else:
    inventory()
#11 shopping interactions
def userInB():
  count =21
  print("\n=== BOOTS ===\n")
  for keys,values in boLst.items():
    print(str(count) + " "+ keys + " = $"+str(values))
    count+=1
  console = int(input("\nChoose the item you like to purchase\nInput:  "))
  dupCheck(console,chLst)
  if console==21:
    cartList.update({"Arctic Bear Boots(+10 str)": 25}) 
    logTracker.append(21)   
  elif console == 22:
    cartList.update({"Gym Shoes(+1 agi)":3})
    logTracker.append(22)   
  elif console ==23:
    cartList.update({"Golden Toes Sandle(+6 int)":74})
    logTracker.append(23)   
  elif console==24:
    cartList.update({"Super Cereal Boots(7 str)":82})
    logTracker.append(24)   
  elif console==25:
    cartList.update({"Marty Mcfly Shoes(+10 agi)":93})
    logTracker.append(25)   
  console = input("\nWould you like to purchase another pair of boots?\nInput (y/n): ")
  if console.upper() =="Y":
    userInB() #recursion
  else:
    inventory()
    
#inventory display (#9 finite state machine)
def inventory():
  console=input("\nWhich menu catagory would you like to view?\n1 Helmet Armor\n2 Body Armor\n3 Potions\n4 Boot Armor\n5 Determine Hex gem value\n6 Weapons\n7 Chance to win legendary item\n8 View shopping cart\n9 Pay for items in shopping cart\n\nType Menu number to view catagory items\nInput:  ")
  if console == "1":#8 finite state machine
    userInH() #12 menu
  if console == "2":#8 finite state machine
    userInC()#12 menu
  if console == "3":#8 finite state machine
    userInP()#12 menu
  if console == "4":#8 finite state machine
    userInB()#12 menu
  if console == "5":#8 finite state machine
    print("\nIn your Hex gem bag you currently have: \n"+str(userGems)+"\n")
    print('\n"Yes this is true, I am a Hex gem enthusiast and I can help determine the values of your Hex gems"\n')
    findGems()
  if console == "6":#8 finite state machine
    userInW()#12 menu
  if console =="7":
    print('\n"The Sword of 1000 Truths(+20str, +20agi, +20int) is the most legendary sword around and Im going to give you a chance to win it! Here is how to win, roll 5 dice 20 times and if the all five dice roll the same number on one of the turn you win the prize."\n')
    playGame(masterdict)
  if console =="8":    #8 finite state machine
    sCart()#12 menu
    console=input("\nWhat would you like to do?\n1 Back to menu \n9 Checkout\nInput:  ")
    if console=="1":
      inventory() #recursion
  if console=="9":#8 finite state machine
    diffH = heLst.keys() - cartList.keys()  #3 set theory
    diffC = chLst.keys() - cartList.keys()  #3 set theory
    diffL = poLst.keys() - cartList.keys()  #3 set theory
    diffW = weLst.keys() - cartList.keys()  #3 set theory
    diffB = boLst.keys() - cartList.keys()  #3 set theory
    print('\n"Can I interest you in these other items?"')
    fh = pd.DataFrame(diffH, columns=["=== HELMS ==="])
    fc = pd.DataFrame(diffC, columns=["=== BODY ARMOR ==="])
    fl = pd.DataFrame(diffL, columns=["=== POTIONS ==="])
    fw = pd.DataFrame(diffW, columns=["=== WEAPONS ==="])
    fb = pd.DataFrame(diffB, columns=["=== BOOTS ==="])
    temp=[fh,fc,fl,fw,fb]
    for i in range(len(temp)):
      print(temp[i])
      print("\n")
    console=input("Input (y/n):  ").upper()
    if console =="Y":
      inventory()  #recursion
    checkout()
    butWait()
 #shopping cart (# 10 stats scores)
def sCart():
  intersH = heLst.keys() & cartList.keys()  #3 set theory
  intersC = chLst.keys() & cartList.keys()  #3 set theory
  intersL = poLst.keys() & cartList.keys()  #3 set theory
  intersW = weLst.keys() & cartList.keys()  #3 set theory
  intersB = boLst.keys() & cartList.keys()  #3 set theory
  print("\nHere is what you have in your shopping cart\n ")
  he = pd.DataFrame(intersH, columns=["=== HELM ==="])
  ch = pd.DataFrame(intersC, columns=["=== BODY ARMOR ==="])
  le = pd.DataFrame(intersL, columns=["=== POTIONS ==="])
  we = pd.DataFrame(intersW, columns=["=== WEAPONS ==="])
  bo = pd.DataFrame(intersB, columns=["=== BOOTS ==="])
  temp=[he,ch,le,we,bo]
  for i in range(len(temp)):
    print(temp[i])
    print("\n")

# (#5 probibility)
def playGame(masterdict):
  rolls = 20
  print("Rolls\t\tResults\t\tProb\n")
  track=False
  while rolls > 0:
    fH =0
    straight=0
    count=0
    string = "\tNone"
    result=sorted(np.random.randint(1, 7, size=5))
    masterdict[rolls] = result
    if result[4]- result[3]==0:
      if result[3]- result[2]==0:
        if result[2]- result[1]==0:
          if result[1]- result[0]==0:
            string = "All numbers match!"
            track=True
    rolls-=1
    print(str(rolls+1)+"\t"+ str(result)+ "\t"+ string)
  if track==True:
    cartList.update({"Sword of 1000 Truths(+20str, +20agi, +20int)":9999}) 
    print("Sword of 1000 Truths added to your shopping cart!")
    inventory()
  else:
    console=input('"Looks like you didnt win this time"\nTry again?\nInput (y/n):  ').upper()
    if console=="Y":
      playGame(masterdict) #recursion
    else:
      inventory()
    
# potion combinations (#4 permutation/combinations)
def poComb():
  trioFaceSpades = combinations(poLst, 3)
  for i in list(trioFaceSpades):
    print(i)

# (#8 BST)
class Node():
  def __init__(self, key, desc):
    self.key = key
    self.left = None
    self.right = None
    self.desc = desc

def insert(root, node):
	if root is None:
		root = node 
	else:
		if root.key < node.key:
			if root.right is None:
				root.right = node 
			else:
				insert(root.right, node)
		else:
			if root.left is None:
				root.left = node
			else:
				insert(root.left, node)

r = Node(35, "keyNum")
arr = [75,25,62,10,13,9,33,8,14,15,30,29,34,61,60,63,64,100,99]
for i in arr:
  insert(r,Node(i, "keyNum"+str(i)))

def printPreorder(root): 
  if root: 
    print(root.key), 
    printPreorder(root.left) 
    printPreorder(root.right) 

def searchBST(root, key): #9 BST search
  while root != None: 
    if key > root.key:  
      root = root.right 
    elif key < root.key: 
      root = root.left  
    else: 
      return True
  return False
#checkout
def checkout():
  change=userCurr-sum(cartList.values())
  print("\nCurrent balance: $"+str(userCurr))
  print("Total comes to: $"+str(sum(cartList.values())))
  print("Change: $"+ str(change))      

#generates currency (#10 stats scores)
def genCurr():
  input("\nYou currently have $"+ str(userCurr)+" and these types of Hex gems in your inventory bag: \n"+ str(userGems)+"\n\n*Press [Enter] key to continue*")
  print('\n\n"Greetings traveler! I have many rare finds for trade"\n')

def butWait():
  console=int(input('\n"Wait! Before you leave I want to make a deal with you. \nIn my binary search tree are a group of numbers that range from 1-100.  \nIf you can in one try guess one of the numbers in my binary search tree I will let you have everything in your shopping cart for free!"\nEnter your guess:  '))
  if searchBST(r,console) == True:
    print('\n"'+str(console)+' Found in BST! CONGRATS ALL YOUR ITEMS ARE FREE!!"')
    print('\nGrand Total: $0.00!!\n\n\n"Goodbye Traveler"')
  else:
    print('\n"'+str(console)+' Not found in BST, but I will still give you your items for FREE!!"\nGrand Total: $0.00!!\n\n\n"Goodbye Traveler"')

#check for duplicates
def dupCheck(con, lst):
  for i in range(len(logTracker)):
    if con == logTracker[i]:
      print("\n***Item already in shopping cart. Pick another item***\n")
      return True

#sort Hex gems (#6 algorithms)
def bubbleSort(randlist):
  for i in range(len(randlist)-1,0,-1):
    for j in range(i):
      if randlist[j] > randlist[j+1]:
        temp = randlist[j]
        randlist[j] = randlist[j+1]
        randlist[j+1] = temp
  print("\nYour Hex gem bag sorted from least to most valuable:\n "+str(randlist)+"\n")

# determine Hex gem value (#1 number conversion)
def currConv(x):
  for i in x:
  	if i in hexnum.keys():
  		decnum.append(hexnum.get(i))
  print("\nYour Hex gems are worth: \n" + str(decnum)+"\n")

def findGems():
  console=input("1 Determine value of gems\n2 Determine value and sort all Hex gems in your Hex gem bag\n3 Back to Menu\nInput:  ")
  if console == "1":
    console=input("Enter letter(s) of Hex gem you like to determine the value of\nInput (A-F):  ").upper()
    currConv(console)
    findGems() #recursion
  if console=="2":
    currConv(userGems)
    bubbleSort(decnum)
    findGems() #recursion
  if console=="3":
    inventory()

############ ADMIN #################################################
#admin sign in password: nsc   #11 interactions  #12 menu
def admin():
  fullLst= chLst.keys() | heLst.keys() | weLst.keys() | poLst.keys() | boLst.keys() #set theory
  console=input("\nEnter number to select from menu option\n1 List all items in inventory\n2 List all numbers in BST\n3 Add a number to BST\n4 Delete a number from BST\n5 Exit admin menu\nInput:  ")
  if console == "1": #finite state 
    print(fullLst)
    admin()  #recursion
  if console =="2": #finite state 
    print("Here are the numbers in the BST:\n")
    printPreorder(r)
    admin()#recursion 
  if console=="3": #finite state 
    addBst()
    admin()#recursion
  if console=="4": #finite state 
    delBst()
    admin()#recursion
  if console=="5":
    genCurr()
    inventory()


#(#2 prime nums) admin sign in
def isPrime(num):
  if num >= 2:
    for i in range(2, num):
      if not (num % i):
        return False
  else:
    return False
  return True
for i in range(2, 103):
  result = isPrime(i)
  if result == True:
    primenums.append(i)  
for i in range(97, 123):
  alphabet.append(chr(i))
cipher = dict(zip(alphabet, primenums))
def SASPrimeCipher(word):
  total=0
  for i in word.lower():
    res = cipher.get(i)
    ansList.append(res)
    numpyArr = np.array(ansList)
    total = np.prod(numpyArr)
  if total == 14405:
    print("\nWelcome Admin!")
    admin()
  else:
    print("Incorrect Password")
    inventory()
print("\n")

# store front
def startUp():
  console=input("Would you like to log in as an Admin?\nInput (y/n):  ").upper()
  if console == "Y":
    console = input("Enter Admin Password: ")
    SASPrimeCipher(console)
  else:
    genCurr()
    inventory()

def minValueNode(node):
	current = node  
	# loop down to find the leftmost leaf
	while(current.left is not None):
		current = current.left 
	return current

def deleteNode(root, key):
# key = node we want to delete
# Base case  
  if root is None:
    return root
  # Traverse until find node to be deleted 
  if key < root.key:
    root.left = deleteNode(root.left, key)
  elif key > root.key:
    root.right=deleteNode(root.right,key)
  else:
    if root.left is None:
      temp=root.right
      root=None
      return temp
    elif root.right is None:
      temp=root.left
      root=None
      return temp
    temp=minValueNode(root.right)
    root.key=temp.key
    root.right=deleteNode(root.right,temp.key)
  return root
#9 add to BST
def addBst():
  console=int(input("\nEnter number you like to add: "))
  insert(r,Node(console, "addBST"))
  print(str(console)+" added to BST")
#9 del from BST
def delBst():
  console=int(input("\nEnter number you like to delete: "))
  deleteNode(r,console)
  print(str(console)+" deleted from BST")



#main
startUp()

