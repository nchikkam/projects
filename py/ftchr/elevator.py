import unittest
""" No of stops a Lift has to stop given
    weights: an array of weights of a person in the queue
    targets: an array of destination floors a person want to get out
    floors: total no of floors the lift supports
    people_capacity: no of people the lift can accomodate
    total_weight: total weight the lift can accomodate
    return: no of stops the lift stops to complete the given
    queue of users.
"""

def solution(weights, targets, floors, people_capacity, total_weight):
    total_stops = 0
    while len(weights)  != 0:
        persons = 0
        weight = 0
        stops = 1
        elevator = {x:0 for x in range(floors+1)}

        while len(weights)  != 0 and persons < people_capacity and (weight+weights[0]) <= total_weight:
            flr = targets[0]
            elevator[flr] += 1  # drop at targets

            weight += weights[0]
            persons+= 1

            weights.pop(0)  # remove from queue
            targets.pop(0)

        for floor in elevator:
            if elevator[floor] != 0:
                stops += 1
        total_stops += stops

    return total_stops

class ElevatorTest(unittest.TestCase):
    def test_cases(self):
        self.assertEqual(solution([60, 80, 40], [2, 3, 5], 5, 2, 200), 5)
        self.assertEqual(solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 5, 3, 200), 6)
        self.assertEqual(solution([40, 40, 100, 80, 20], [3, 3, 2, 2, 3], 3, 5, 200), 6)

if __name__ == "__main__":
    unittest.main()
