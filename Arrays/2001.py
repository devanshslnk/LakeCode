class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        hmap={}
        for rectangle in rectangles:
            ratio=rectangle[1]/rectangle[0]
            hmap[ratio]=hmap.get(ratio,0)+1

        ans=0
        for key,value in hmap.items():
            ans+=(value*(value-1))//2
        return ans

    # Time Complexity O(n) Space Complexity O(n)
