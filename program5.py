# Fractional Knapsack and Job Scheduling

from typing import List

# 1. Fractional Knapsack

def fractional_knapsack(weights: List[int], values: List[int], capacity: int) -> float:

    items = []

    for i in range(len(weights)):
        ratio = values[i] / weights[i]
        items.append((ratio, weights[i], values[i]))

    items.sort(reverse=True)

    profit = 0

    for ratio, weight, value in items:

        if capacity >= weight:
            profit += value
            capacity -= weight

        else:
            profit += ratio * capacity
            break

    return profit

# 2. Job Scheduling

class Job:
    def __init__(self, id, deadline, profit):
        self.id = id
        self.deadline = deadline
        self.profit = profit


def job_scheduling(jobs: List[Job]) -> List[int]:

    jobs = sorted(jobs, key=lambda x: x.profit, reverse=True)

    max_deadline = max((job.deadline for job in jobs), default=0)

    slots = [-1] * max_deadline

    for job in jobs:

        for j in range(job.deadline - 1, -1, -1):

            if slots[j] == -1:
                slots[j] = job.id
                break

    return [x for x in slots if x != -1]


# Main Program

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Fractional Knapsack")
print("Maximum Profit:", fractional_knapsack(weights, values, capacity))


jobs = [
    Job(1, 2, 100),
    Job(2, 1, 19),
    Job(3, 2, 27),
    Job(4, 1, 25),
    Job(5, 3, 15)
]

sequence = job_scheduling(jobs)

total_profit = sum(job.profit for job in jobs if job.id in sequence)

print("\nJob Scheduling")
print("Optimal Job Sequence:", sequence)
print("Maximum Profit:", total_profit)
