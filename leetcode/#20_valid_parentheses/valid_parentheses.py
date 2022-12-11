class Solution:
    def isValid(self, s: str) -> bool:

        # directional pairing of parentheses, if given a left, return the right. None if given anything else
        hashmap = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []

        for i in s:
            pair = hashmap.get(i)

            # if its a right bracket, check that the head of the stack is a matching left bracket. return false if invalid
            if pair == None:
                if (len(stack) < 1 or i != stack[-1]):
                    return False
                
                stack.pop()
            # if its a left bracket, add the matching right bracket to the stack
            else:
                stack.append(pair)


        # default true
        return len(stack) < 1