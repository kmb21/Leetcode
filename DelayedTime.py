def findDelayedArrivalTime(self, arrivalTime: int, delayedTime: int) -> int:
        arrival = arrivalTime + delayedTime
        if arrival>=24:
            return arrival-24
        else:
            return arrival