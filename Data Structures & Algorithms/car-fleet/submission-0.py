class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Zip them as cars and sort by position, reversed so
        # closest to target (highest position) is at 0
        # Add to stack: if that car and the car below it 
        # are going to meet before target using the formula
        # position = (a,b) speeds = (v1, v2), 
        # will meet before target if 
        # (target - b)/ v2 <= (target - a)/ v1 where a, v1 car is 
        # closer to the target (in stack already). if true, then 
        # dont add the second car to the stack. If not true, add the second car
        # return size of the stack
        # i[0] = position
        # i[1] = speed
        # i is a tuple (position, speed)
        sorted_cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        stack = [sorted_cars[0]]
        for i in sorted_cars[1:]: 
            if (target - i[0]) / i[1] > (target - stack[-1][0]) / stack[-1][1]:
                stack.append(i)
    
        return len(stack)


