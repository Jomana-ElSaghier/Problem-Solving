class Solution:
    def cntSubarrays(self, arr, k):
        pre_sum_count={}
        count= 0
        pre_sum=0
        for num in arr:
            pre_sum+=num
            if pre_sum == k:
                count+=1
            if (pre_sum - k) in pre_sum_count:
                count+=pre_sum_count[pre_sum -k]
            pre_sum_count[pre_sum]=pre_sum_count.get(pre_sum,0)+1
        return count    
        