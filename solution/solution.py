from typing import List

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        next_idle_time = 0  # Tracks when the chef will be free to take the next order
        net_wait_time = 0   # Accumulates total wait time for all customers

        for arrival, prep_time in customers:
            # The next idle time for the chef is the maximum of the customer's arrival time and
            # the chef's current idle time, plus the preparation time for the current order.
            next_idle_time = max(arrival, next_idle_time) + prep_time

            # The wait time for the current customer is the difference between the finish time
            # and the customer's arrival time.
            net_wait_time += next_idle_time - arrival

        # Calculate the average wait time by dividing total wait time by the number of customers.
        average_wait_time = net_wait_time / len(customers)
        return average_wait_time

# Example usage
solution = Solution()

# Example 1
customers1 = [[1, 2], [2, 5], [4, 3]]
print(solution.averageWaitingTime(customers1))  # Output: 5.00000

# Example 2
customers2 = [[5, 2], [5, 4], [10, 3], [20, 1]]
print(solution.averageWaitingTime(customers2))  # Output: 3.25000
