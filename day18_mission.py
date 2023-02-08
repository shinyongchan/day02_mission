Ch9_1
class Graph:
	def __init__(self, size):
		self.SIZE = size
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


def print_graph(Graph):
	print("\t\t", end=' ')
	for v in range(Graph.SIZE):
		print("%9s" % store_ary[v][0], end=' ')
	print()
	for row in range(Graph.SIZE):
		print("%9s" % store_ary[row][0], end=' ')
		for col in range(Graph.SIZE):
			print("%8d" % Graph.graph[row][col], end=' ')
		print()

SIZE = 5

G1 = Graph(SIZE)
store_ary = [['GS25', 30], ['CU', 60], ['Seven11', 10], ['MiniStop', 90], ['Emart24', 40]]
stack = []
visited_ary =[]
G1.graph[0][1] = 1; G1.graph[0][2] = 1
G1.graph[1][0] = 1; G1.graph[1][2] = 1; G1.graph[1][3] = 1
G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1
G1.graph[3][1] = 1; G1.graph[3][4] = 1
G1.graph[4][3] = 1

if __name__ == "__main__":

	print_graph(G1)

	current = 0
	stack.append(current)
	visited_ary.append(current)
	max_store = 0
	max_count = store_ary[max_store][1]
	while (len(stack) != 0):
		next = None
		for vertex in range(SIZE):
			if G1.graph[current][vertex] == 1:
				if vertex in visited_ary:
					pass
				else:
					next = vertex
					break

		if next != None:
			current = next
			stack.append(current)
			visited_ary.append(current)
			if store_ary[next][1] > max_count:
				max_store = next
				max_count = store_ary[max_store][1]
		else:
			stack.pop()
			if len(stack) == 0:
				break
			current = stack[-1]

	print("허니버터칩 최대 보유 편의점(개수) -->", end=' ')
	print(store_ary[max_store])


