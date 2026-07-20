class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sorted_cars = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        fleets = 1
        time = (target - sorted_cars[0][0]) / sorted_cars[0][1]
        for i in sorted_cars[1:]:
            current = (target - i[0]) / i[1]
            if current > time:
                fleets += 1
                time  = current
        return fleets