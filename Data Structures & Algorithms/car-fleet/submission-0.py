class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleet_time = None
        fleets = 0

        cars = sorted(zip(position, speed), reverse=True)

        for p, s in cars:
            time = (target - p) / s

            if not fleet_time or fleet_time < time:
                fleet_time = time
                fleets += 1
        return fleets

        