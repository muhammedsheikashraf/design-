"""Question 7: 0/1 Knapsack using dynamic programming."""


def knapsack(weights, values, capacity):
    if len(weights) != len(values):
        raise ValueError("weights and values must have the same length")
    if capacity < 0 or any(weight < 0 for weight in weights):
        raise ValueError("capacity and weights must be non-negative")

    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        weight = weights[i - 1]
        value = values[i - 1]

        for current_capacity in range(capacity + 1):
            dp[i][current_capacity] = dp[i - 1][current_capacity]
            if weight <= current_capacity:
                dp[i][current_capacity] = max(
                    dp[i][current_capacity],
                    value + dp[i - 1][current_capacity - weight],
                )

    selected = []
    current_capacity = capacity
    for i in range(n, 0, -1):
        if dp[i][current_capacity] != dp[i - 1][current_capacity]:
            selected.append(i - 1)
            current_capacity -= weights[i - 1]

    selected.reverse()
    return dp[n][capacity], selected


if __name__ == "__main__":
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 5

    maximum_value, selected_items = knapsack(weights, values, capacity)
    print("Weights:", weights)
    print("Values:", values)
    print("Capacity:", capacity)
    print("Maximum value:", maximum_value)
    print("Selected item indices (0-based):", selected_items)
