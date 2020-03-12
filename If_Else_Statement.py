#If Else Statements
If_Else_Statement.py

#Boolean Expression

print(20 > 10)
print(20 == 10)
print(20 < 10)
print(bool("Hello World"))
print(bool(20))



Python Conditions 

Equals 					   ->  x == y
Not Equals 	 			   ->  x != y
Less than   		       ->  x <  y
Less than or equal to  	   ->  x <= y
Greater than               ->  x > y
Greater than or equal to   ->  x >= y
Boolean OR                 ->  x or y , x | y
Boolean AND                ->  x and y, x & y
Boolean NOT                ->  not x

x = 90
y = 45




if - 
else -

x = 10
if x == 0:
    print("x is zero")
elif x != 0:
   print("x is not equal to zero")			#because if the first is right, it doesn't jump to another
elif x < 20:
   print("x is 20")
elif x == 10:
   print("x is 10")
else:
   print("x is nothing")


#If Statement 

x = 70
y = 60

if x > y:
	print("x is greater than y ")


#Elif

x = 60
y = 70

if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")	
else:
	print("Default")

#Else

x = 50
y = 150
if x > y:
	print("x is greater than y")
elif x == y:
	print("x and y are equal")
else:
	print("x is less than y")		

#Short Hand If

if x < y: print("y is greater than x")	

#Short Hand If...Else

x = 50
y = 150
print(x) if x > y else print(y)


#And is logical operator

x = 50
y = 40
z = 100
if x > y and z > y or x > z:
	print("All Conditions are True")
else: 
	print("one condition is True")	

#Or is logical operator

x = 50
y = 40
z = 100

if x > y or z < y:
	print("one of the conditions is True")
elif x > y and z > y:
	print("All conditions are True")
else: 
	print("nothing else")	

#Nested If is if statements in if statements	

x = 15

if x > 10:
	print("x is ten")
	if x > 20:
		print("x is greater than 20")
		if x > 40 and x < 50 or x == 50:
			print("x is above 40 or equal to 50.")
		else:
			print("x is normal")	
	else:
		print("No,x is not greater than 20")
else:
	print("x is smaller than 10")


----------------------------------


if x > 10 and x != 10 or x > 20:
	print("x is greater than 10 and 20")	
else:
	print("x is not greater than 10 & 20")	


#Pass Statement

x = 100
y = 50

if x > y:
	pass


---------

x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

---------


int(input("Examination Result : "))
100 - 90	 - A
90 - 70 	 - B
70 - 60 	 - C
60 - 40 	 - D
40 - 0 	     - Fail
	
39










>>> Loops

if x >= 70 and x < 90 :
		print("Grade B")