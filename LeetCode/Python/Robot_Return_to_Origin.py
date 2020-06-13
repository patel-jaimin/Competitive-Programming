# 657. Robot Return to Origin
# There is a robot starting at position (0, 0), the origin, on a 2D plane. 
# Given a sequence of its moves, judge if this robot ends up at (0, 0) after it completes its moves.

# The move sequence is represented by a string, and the character moves[i] represents its ith move. 
# Valid moves are R (right), L (left), U (up), and D (down). 
# If the robot returns to the origin after it finishes all of its moves, return true. Otherwise, return false.

# Example 1:

# Input: "UD"
# Output: true 
# Explanation: The robot moves up once, and then down once. 
# All moves have the same magnitude, so it ended up at the origin where it started. 
# Therefore, we return true.
 

# Example 2:

# Input: "LL"
# Output: false
# Explanation: The robot moves left twice. It ends up two "moves" to the left of the origin. 
# We return false because it is not at the origin at the end of its moves.

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        UpDown=0
        LeftRight=0
        for i in range(len(moves)):
            if moves[i]=='U':
                UpDown+=1
            elif moves[i]=='D':
                UpDown-=1
            elif moves[i]=='L':
                LeftRight+=1
            elif moves[i]=='R':
                LeftRight-=1
        if UpDown==0 and LeftRight==0:
            return True
        return False