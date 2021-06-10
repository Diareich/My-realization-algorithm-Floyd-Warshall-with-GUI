# Floyd Warshall Algorithm in python


# The number of vertices
nV = 4

INF = 999


# Algorithm implementation
def floyd_warshall(G):
	distance = list(map(lambda i: list(map(lambda j: j, i)), G))

	# Adding vertices individually
	for k in range(nV):
		for i in range(nV):
			for j in range(nV):
				distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

	return print_solution(distance)


# Printing the solution
def print_solution(distance):

	solve = list ()

	for i in range(nV):

		lol = list ()

		for j in range(nV):
			if(distance[i][j] == INF):
				lol.append("INF")
			else:
				lol.append(distance[i][j])

		solve.append(lol)

	return (solve)

if __name__ == '__main__':
	G = [[0, 3, INF, 5],
			 [2, 0, INF, 4],
			 [INF, 1, 0, INF],
			 [INF, INF, 2, 0]]
	
	print (floyd_warshall(G))