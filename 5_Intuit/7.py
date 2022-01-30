class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def canShip(capacity):
            days_needed = 1
            curr_wt = 0
            for w in weights:
                curr_wt += w
                
                if curr_wt > capacity:
                    days_needed += 1
                    curr_wt = w
            return days_needed <= D
            
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = low + (high-low)//2
            if canShip(mid):
                high = mid - 1
            else:
                low = mid + 1
        return high+1