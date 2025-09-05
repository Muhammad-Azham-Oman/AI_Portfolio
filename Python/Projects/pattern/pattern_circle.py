# if n = 7
  

   ####    
 ##    ##  
##      ## 
##      ## 
##      ## 
##      ## 
 ##    ##  
   ####
 
# if n = 5 
 
   
   ####  
 ##    ## 
##      ##
 ##    ## 
   ####  




n = int(input("Enter the number:"))

for i in range(1,n+1):
    if(i==1 or i==n):
        print(" "*3,end="")
        print("#"*4,end="")
        print(" ")
    elif(i==2 or i==n-1):
        print(" "*1,end="")
        print("#"*2,end="")
        print(" "*4,end="")
        print("#"*2,end="")
        print(" ")
    else:
        print("#"*2,end="")
        print(" "*6,end="")
        print("#"*2,end="")
        print(" ")