#  Fails due to time limit exceeded, need to work on  but passes 31/39 testcases

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Input: n = 6, headID = 2, manager = [2,2,-1,2,2,2], informTime = [0,0,1,0,0,0]
        # Output: 1
        # Explanation: The head of the company with id = 2 is the direct manager 
        # of all the employees in the company and needs 1 minute to inform them all.
        # The tree structure of the employees in the company is shown.
        # https://assets.leetcode.com/uploads/2020/02/27/graph.png
        # In example above HeadID is used to match who the manager is in the manager array
        # so everyone with the number 2 in manager array means that they report to the manager with headID of 2
        
        # I need to use headID to find the head of company
        # Have totalTime variable start at 0, then with each recursive call add corresponding informTime until 
        # but only  if totalTime < variable that is adding informTimes

        total = 0
        # for first call id = headId, pass time = 0
        def backtrack(id, time):
            nonlocal total
            # print(id, "ID CALL")
            # check manager array see if anyone reports to current id
            for employee in range(n):
                # print(employee, "EMPLOYEE CALL")
                if manager[employee] == id:
                    # print(informTime[id], "this gets added to time")
                    backtrack(employee, time + informTime[id])
                elif time > total:
                    total = time

        backtrack(headID, 0)
        # print(total, "FINISH CASE")
        return total