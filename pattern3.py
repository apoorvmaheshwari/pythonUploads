num=int(input("Enter Number of rows: "))

for i in range(num,0,-1):
    print(" "*(num-i),"*"*i)
    
    
    
def sayhello(name1,name2,name3="Harbhajan"):
    print("Hi "+name1+" "+name2+" "+name3)
    
    
sayhello(name1="Sachin",name2="Saurav")