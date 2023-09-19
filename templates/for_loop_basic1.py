#print all the intergers from 0-100

def my_function():
  print("Hello from a function")
  for x in range(101):
   print(x)
my_function()   

#Print all the multiples of 5 from 5 to 1,000

def five_onit():
  print("I got five on it")
  for x in range(5,1001,5):
   print(x)
five_onit()
  

#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo"

def five_orten():
    print("This or That")
    for x in range(101):
        if x%10 ==0:
            print("Coding Dojo")
        elif x%5 ==0:
            print("Coding")
        else:
            print(x)


five_orten()

#Add odd integers from 0 to 500,000, and print the final sum

def odds_and_end():
    oddsum=0
    print("i'm working here")
    for x in range(0,500000):
        if x%2 !=0:
            oddsum=oddsum+x
            print(oddsum)
odds_and_end()

#Print positive numbers starting at 2018, counting down by fours.

def minusfour():
  print("what art thou four")
  for x in range(2018,0,-4):
   print(x)
minusfour()

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers 
#that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

def three_likeme():
    print("threes")
    lownum=0
    highnum=3000
    mult=3
    for i in range(lownum,highnum):
        if i%mult==0:
            print(i)
three_likeme()