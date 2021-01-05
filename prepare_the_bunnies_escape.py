'''

Prepare the Bunnies' Escape
===========================

Level 3.1

You're awfully close to destroying the LAMBCHOP doomsday device and freeing Commander Lambda's bunny prisoners, but once they're free of the prison blocks, the bunnies are going to need to escape Lambda's space station via the escape pods as quickly as possible. Unfortunately, the halls of the space station are a maze of corridors and dead ends that will be a deathtrap for the escaping bunnies. Fortunately, Commander Lambda has put you in charge of a remodeling project that will give you the opportunity to make things a little easier for the bunnies. Unfortunately (again), you can't just remove all obstacles between the bunnies and the escape pods - at most you can remove one wall per escape pod path, both to maintain structural integrity of the station and to avoid arousing Commander Lambda's suspicions. 

You have maps of parts of the space station, each starting at a prison exit and ending at the door to an escape pod. The map is represented as a matrix of 0s and 1s, where 0s are passable space and 1s are impassable walls. The door out of the prison is at the top left (0,0) and the door into an escape pod is at the bottom right (w-1,h-1). 

Write a function solution(map) that generates the length of the shortest path from the prison door to the escape pod, where you are allowed to remove one wall as part of your remodeling plans. The path length is the total number of nodes you pass through, counting both the entrance and exit nodes. The starting and ending positions are always passable (0). The map will always be solvable, though you may or may not need to remove a wall. The height and width of the map can be from 2 to 20. Moves can only be made in cardinal directions; no diagonal moves are allowed.

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]])
Output:
    7

Input:
solution.solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]])
Output:
    11

'''

def process(i, j, wall, visited, queue, map):
	if 0 <= i < len(map) and 0 <= j < len(map[0]) and wall - map[i][j] >= 0:
		if visited[i][j] == -1:
			visited[i][j] = wall - map[i][j]
			queue.append([i, j, wall-map[i][j]])
		elif visited[i][j] == 0:
			if wall - map[i][j] == 1:
				visited[i][j] = 1
				queue.append([i, j, 1])


def solution(map):
	queue = [[0, 0, 1]]
	step = 1
	rows = len(map)
	cols = len(map[0])

	visited = [[-1 for j in range(cols)] for i in range(rows)]
	visited[0][0] = 1
	end = [rows-1, cols-1]

	while queue:
		for i in range(len(queue)):
			neighbors = queue.pop(0)
			if neighbors[0] == end[0] and neighbors[1] == end[1]:
				return step

			process(neighbors[0]-1, neighbors[1], neighbors[2], visited, queue, map)
			process(neighbors[0]+1, neighbors[1], neighbors[2], visited, queue, map)
			process(neighbors[0], neighbors[1]-1, neighbors[2], visited, queue, map)
			process(neighbors[0], neighbors[1]+1, neighbors[2], visited, queue, map)

		step += 1

print(solution([[0, 1, 1, 0], [0, 0, 0, 1], [1, 1, 0, 0], [1, 1, 1, 0]]))
print(solution([[0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0]]))