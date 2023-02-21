def de(arr,s):
    if len(arr)==4:
    
        return arr[0]*arr[3]-arr[1]*arr[2]
    
 
    sum =0
    sign =1
    z =0
    for i in range(0,len(arr) ,s):
        l =[]
       
    

        for k in range(len(arr)):
     
            if k%s!=0 and (k>=s+i or k<i):
                l.append(arr[k])
   
 
  
    
 

        if z%2==0:
            sign =-1
        else:
            sign =+1
        det =sign*arr[i]*de(l,s-1)
    
        sum+=det
        
    
        z +=1
 

    return sum
    
        
  
     
    

    


     
        
 
   

      
        
  
 


   






def main():
    arr =[1,4,2,1,-1,-1,3,2,0,5,7,-4,2,1,-3,2]
    arr1 =[1,1,1,-1,1,1,-1,1,1,-1,1,1,-1,1,1,1]

    print(de(arr,4))

main()