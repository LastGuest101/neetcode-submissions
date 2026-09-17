class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # for each car in the list
        stack = []
        cars = sorted(zip(position, speed), reverse=True)
        for pos, spd in (cars):
        # find the time it takes to reach the destination
            time = ((target - pos) / spd)
            if stack:
                prev_time = stack.pop()
                if time <= prev_time:
                    stack.append(prev_time)
                else:
                    stack.append(prev_time)
                    stack.append(time)
            else:
                stack.append(time)
        
        return len(stack)

        # check if stack is empty and pop from the stack
        # if the current time is less than the stack == part of car fleet.
        # append pop time to stack.
        # current time is greater than popped time -> append popped time and current time 
        # calculate the number of items in the stack and return.


