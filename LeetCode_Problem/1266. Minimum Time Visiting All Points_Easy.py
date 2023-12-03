class Solution:
    def minTimeToVisitAllPoints(self, points):
        ans = 0
        n = len(points)

        for i in range(1, n):
            diffx = abs(points[i][0] - points[i - 1][0])
            diffy = abs(points[i][1] - points[i - 1][1])
            ans += max(diffx, diffy)
        
        return ans