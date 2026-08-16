class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars =list(zip(position, speed))
        cars.sort(reverse = True)
        fleets = 1
        time = (target - cars[0][0]) / cars[0][1]
        for i, j in cars[1: ]:
            if self.timeNeeded(i, j, target) > time:
                fleets += 1
                time = self.timeNeeded(i, j, target)
        return fleets

    def timeNeeded(self, position, speed, target):
        return (target - position) / speed