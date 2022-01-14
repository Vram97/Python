#! /usr/bin/env python
'''Solution to problem set for solving a string of mathematical expression'''

def isdigit(element):  
   """Function that checks if incoming element is a digit"""
   try:
      element=int(element)
      return True
   except:
      return False

def value(opp):  
  """Function that checks if incoming element is a digit"""
  op=["*","/","+","-"]
  try:
   x=op.index(opp)
   if(x==0 or x==1):
       return 2
   elif(x==2 or x==3):
       return 1
  except:
      return 0

def calc(org_string):     
    """Function to which you feed in a string expression and in turn solves the problem"""
    operators=[]       #Array that stores operators
    operands=[]        #Array that stores operands
    points=[]          #Array to track positions of elements inside brackets
    val=0
    op=["*","/","+","-"]  #Array of acceptable operators
    for i in range(len(org_string)):
     if(i not in points):
       current=org_string[i]
       if(isdigit(current)==True):
          val=val*10+int(current)  # To store multi digit numbers
          if(i==len(org_string)-1):
            while(len(operators)!=0):
               num1=operands.pop()
               num2=val
               t=operators.pop()
               if(t=="*"):
                   ans=num1*num2
               elif(t=="/"):
                   ans=num1/num2
               elif(t=="+"):
                   ans=num1+num2
               else:
                   ans=num1-num2
               val=ans

       elif(current in op):    #For processing operators
          if(len(operators)==0 and len(operands)==0):
            operators.append(current)
            operands.append(val)
            val=0
          else:
            if(value(current)>value(operators[-1])): #Checking if incoming operator has a greater priority than existing operator
               operands.append(val)
               operators.append(current)
               val=0
            else:
               num1=operands.pop()
               num2=val
               j=operators.pop()
               if(j=="*"):
                   ans=num1*num2
               elif(j=="/"):
                   ans=num1/num2
               elif(j=="+"):
                   ans=num1+num2
               else:
                   ans=num1-num2
               operators.append(current)
               operands.append(ans)
               val=0
       elif(current=="("):     #Processing brackets
          brack_string="" 
          tracker=1  #variable to track the number of brackets
          for h in range(1,100):
              if(org_string[i+h]=="("):
                  tracker+=1
              elif(org_string[i+h]==")"):
                   tracker-=1
              if(tracker!=0):
                brack_string=brack_string+org_string[i+h]
                points.append(i+h)
              else:
                break   
          temp=calc(brack_string)   #Using recursion to process what is inside a bracket
          val=int(temp)
          while(len(operators)!=0): 
               num1=operands.pop()
               num2=val
               t=operators.pop()
               if(t=="*"):
                   ans=num1*num2
               elif(t=="/"):
                   ans=num1/num2
               elif(t=="+"):
                   ans=num1+num2
               else:
                   ans=num1-num2
               val=ans

    return val
              


if(__name__=="__main__"):
    numstr=input("Enter the mathematical equation: ")
    final=calc(numstr)
    print("The answer is: ", final)
            

