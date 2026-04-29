class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #sort the array
        result = [] # initialize an empty list

        for i,a in enumerate(nums): #traverse through the list
            if i>0 and a==nums[i-1]: #skip through duplicates
                continue
            l,r = i+1, len(nums)-1 #set left and right pointers
            while l<r: #the usual 2pointer loop
                ts = nums[l]+nums[r]+a #cursum
                if ts>0: 
                    r-=1
                elif ts<0:
                    l+=1
                else:
                    result.append([a,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
        return result
        