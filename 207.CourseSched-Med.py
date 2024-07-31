class Solution: # O(N^2) Time & O(N) Space. 
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(numCourses)}
        # Map each prereq to associated course. 
        for course1, course2 in prerequisites: 
            adjList[course1].append(course2)

        visited = set()

        def dfs(crs):
            # Check for a cycle. 
            if crs in visited: 
                return False
            # If it's not in our adj list not pre reqs. 
            if adjList[crs] == []:
                return True 
            # Add to visited. 
            visited.add(crs)
            # Look thru each of the courses pre reqs. 
            for preReq in adjList[crs]: 
                if not dfs(preReq):
                    return False
            # Remove it from visited. After we traversed the path.   
            visited.remove(crs)
            # Now we can return to base case because we have covered all pre reqs. 
            adjList[crs] = []
            return True 
            


        for course in range(numCourses): 
            if not dfs(course):
                return False 

        return True 
    