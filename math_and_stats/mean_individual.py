#simple program that can perform mean in individual series 
try:
    x=int(input("Enter the number of X element : "))
except ValueError:
    print("INVALID,USE ONLY INTEGER")
l=[]
sum=0
for i in range (x):
    try:
        n=int(input ("Enter the X elements :- "))
    except ValueError:
        print("INVALID,USE ONLY INTEGER")
    l.append(n)
    sum+=n

print("The Elements of X are",l)
print("The Summation of X is",sum)
mean=sum/x 
print("Mean is :-",mean)  

 
