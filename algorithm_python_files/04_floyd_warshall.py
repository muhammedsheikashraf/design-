"""Question 4: Floyd-Warshall all-pairs shortest paths."""
INF = float("inf")


def floyd_warshall(graph):
    n = len(graph)
    distance = [row[:] for row in graph]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distance[i][k] != INF and distance[k][j] != INF:
                    distance[i][j] = min(
                        distance[i][j],
                        distance[i][k] + distance[k][j],
                    )

    # A negative diagonal entry indicates a negative-weight cycle.
    if any(distance[i][i] < 0 for i in range(n)):
        print("Warning: graph contains a negative-weight cycle.")

    return distance


if __name__ == "__main__":
    graph = [
        [0, 5, INF, 10],
        [INF, 0, 3, INF],
        [INF, INF, 0, 1],
        [INF, INF, INF, 0],
    ]

    result = floyd_warshall(graph)
    print("Shortest distance matrix:")
    for row in result:
        print(["INF" if value == INF else value for value in row])
