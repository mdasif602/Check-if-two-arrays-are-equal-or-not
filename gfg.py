

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        
        #code here
        dict1={}
        dict2={}
        for i in A:
            if i not in dict1:
                dict1[i]=1
            else:
                dict1[i]+=1
        for i in B:
            if i not in dict2:
                dict2[i]=1
            else:
                dict2[i]+=1
        if dict1==dict2:
            return True
        else:
            return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
