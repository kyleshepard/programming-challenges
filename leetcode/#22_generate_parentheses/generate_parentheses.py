class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        stack = ["("]
        countLeft = 1
        countRight = 0

        def recur(countLeft, countRight):
            # base case: if we have both n left and right parentheses, we are done
            if countLeft == countRight == n:
                output.append("".join(stack)) 
                return
            
            # place left parentheses first until we have reached n left parentheses
            if countLeft < n:
                stack.append("(")
                recur(countLeft + 1, countRight)
                stack.pop()
            
            # make sure our right count doesn't exceed our left count, otherwise we get an invalid combination
            if countRight < countLeft:
                stack.append(")")
                recur(countLeft, countRight + 1)
                stack.pop()

        recur(countLeft, countRight)

        return output

