'''#operators
 #1 average of 3num
a=int(input("enter"))
b=int(input("enter"))
c=int(input("enter"))
d=(a+b+c)//3
print(d)

#2area
r=int(input("enter"))
a=int(input("enter"))
h=int(input("enter"))
b=int(input("enter"))

d=3.14*(r*2)
e=a*2
t=(h*b)//2
print(d,e,t)

#3convert c to f
c=float(input("enter the centi"))
print((c*1.8)+32)



#4convert f to c
f=int(input("enter the fahren"))
g=((f-32)*(0.55))
print(g)



#5 simple inter
p=float(input("enter the p"))
r=float(input("enter the r"))
t=float(input("enter the t"))
si=(p*r*t)//100
print(si)


#6 compound int
p=float(input("enter the p"))
r=float(input("enter the r"))
t=float(input("enter the t"))
n=float(input("enter the n"))
a=(p*(1+(r//n)))
ta=a**(n*t)
ci=ta-p
print(ci)


#7swap with variable
a=int(input("enter the num"))
b=int(input("enter the num"))
c=a
a=b
b=c
print(a)
print(b)



#8swap without variable
a=int(input("enter the num"))

b=int(input("enter the num"))
a,b=b,a
print(a)
print(b)



#9 square root
a=int(input("enter the num"))
sq=a**0.5
print(sq)


#10 print last digit

a=int(input("enter the num"))
c=a%10
print(c)


#conditions


#1
m=int(input("enter the num"))
n=int(input("enter the num"))
if(m>n):
    print ("quotient",m//n)
    print ("remainder",m%n)
    


#2

a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
d=int(input("enter the num"))
e=int(input("enter the num"))
avg=(a+b+c+d+e)//5
if(avg>=90):
    print("grade a")
elif(avg<90 and avg>=80):
    print("grade b")
else:
    print("fail")




#3
a=int(input("enter the num"))
if(a>0):
    print("positive")
elif(a==0):
    print("neither postive or negative")
else:
    print("negative")

if (a%2==0):
    print("even")
else:
    print("odd")

if(a%400==0):
    print("its leap")
else:
    print("its not")



#4


a=input("enter the letter")
if a in "aeiou":
    print("vowel")
else:
    print("consonants")


 
#5
a=int(input("enter the num"))
b=int(input("enter the num"))
c=int(input("enter the num"))
if(a>b and a>c):
    print(a)
elif(b>c):
    print(b)
else:
    print(c)



#7
month=int(input("enter the num"))
year=int(input("enter the num"))
if(month in [1,3,5,7,8,10,12]):
    print("31 days")
elif month==2:
    if(year%400==0):
        print("29 days")
    else:
        print("28 days")
else:
    print("30 days")
    


#8

a=int(input("enter the num"))
if a%5==0:
    print("hello")
else:
    print("bye")



#9

t=float(input("enter the celius"))
if(t>100):
    print("its boiling")
else:
    print("its not")
    

#10

a=int(input("enter the num of days"))
if a<=5:
    print("charge",a*2)

elif a>=6 and a<=10:
    print("charge",a*3)

elif a>=11 and a<=15:
    print("charge",a*4)
else:
    print("charge",a*5)
    
    


 
#11

a=int(input("enter the age"))
b=int(input("enter the hieght"))
if (a>=18 and a<=30) and b>165:
    print("he can")
else:
    print("he cant")


#12

a=float(input("enter the salary"))
b=double(input("enter the bonus "))
c=b//100
print(c)
tb=a*c
t=tb+a
print(t)

#13
a=int(input("enter the num of electric units"))
if a<=100:
    print("charge",a*2)

elif a>=101 and a<=200:
    print("charge",a*3)

elif a>=201 and a<=300:
    print("charge",a*4)
else:
    print("charge",a*5)
    
'''

#14

a=(input("enter the new password"))


    
for char in a:
    if 48<= ord(char)<=57 in a:
        pass
    else:
        print("enter digit")
    if 65<= ord(char)<=90:
        pass
    else:
        print("enter upper case")
    if 97<= ord(char)<=122:
        pass
    else:
        print("enter lower case")












