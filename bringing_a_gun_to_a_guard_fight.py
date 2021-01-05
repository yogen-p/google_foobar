'''

Bringing a Gun to a Guard Fight
===============================

Level 4.1

Uh-oh - you've been cornered by one of Commander Lambdas elite guards! Fortunately, you grabbed a beam weapon from an abandoned guard post while you were running through the station, so you have a chance to fight your way out. But the beam weapon is potentially dangerous to you as well as to the elite guard: its beams reflect off walls, meaning you'll have to be very careful where you shoot to avoid bouncing a shot toward yourself!

Luckily, the beams can only travel a certain maximum distance before becoming too weak to cause damage. You also know that if a beam hits a corner, it will bounce back in exactly the same direction. And of course, if the beam hits either you or the guard, it will stop immediately (albeit painfully). 

Write a function solution(dimensions, your_position, guard_position, distance) that gives an array of 2 integers of the width and height of the room, an array of 2 integers of your x and y coordinates in the room, an array of 2 integers of the guard's x and y coordinates in the room, and returns an integer of the number of distinct directions that you can fire to hit the elite guard, given the maximum distance that the beam can travel.

The room has integer dimensions [1 < x_dim <= 1250, 1 < y_dim <= 1250]. You and the elite guard are both positioned on the integer lattice at different distinct positions (x, y) inside the room such that [0 < x < x_dim, 0 < y < y_dim]. Finally, the maximum distance that the beam can travel before becoming harmless will be given as an integer 1 < distance <= 10000.

For example, if you and the elite guard were positioned in a room with dimensions [3, 2], your_position [1, 1], guard_position [2, 1], and a maximum shot distance of 4, you could shoot in seven different directions to hit the elite guard (given as vector bearings from your location): [1, 0], [1, 2], [1, -2], [3, 2], [3, -2], [-3, 2], and [-3, -2]. As specific examples, the shot at bearing [1, 0] is the straight line horizontal shot of distance 1, the shot at bearing [-3, -2] bounces off the left wall and then the bottom wall before hitting the elite guard with a total shot distance of sqrt(13), and the shot at bearing [1, 2] bounces off just the top wall before hitting the elite guard with a total shot distance of sqrt(5).

Test cases
==========
Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

-- Python cases --
Input:
solution.solution([3,2], [1,1], [2,1], 4)
Output:
	7

Input:
solution.solution([300,275], [150,150], [185,100], 500)
Output:
	9

'''

from math import sqrt, atan2, ceil
from copy import deepcopy


class GuardFight:
	def __init__(self, dim, pos, guard_pos, distance):
		self.room_x = dim[0]
		self.room_y = dim[1]
		self.self_x = pos[0]
		self.self_y = pos[1]
		self.guard_x = guard_pos[0]
		self.guard_y = guard_pos[1]
		self.max_distance = distance
		self.max_x = self.self_x + distance + 1
		self.max_y = self.self_y + distance + 1

	def get_dist(self, point_x, point_y):
		distance = sqrt((point_x - self.self_x) ** 2 + (point_y -
													  self.self_y) ** 2)
		return distance

	def get_angle(self, point_x, point_y):
		angle = atan2(point_y - self.self_y, point_x - self.self_x)
		return angle

	def get_first_quadrant(self):
		num_x_copies = ceil(self.max_x / self.room_x)
		num_x_copies = int(num_x_copies)
		num_y_copies = ceil(self.max_y / self.room_y)
		num_y_copies = int(num_y_copies)

		new_self_x = []
		new_self_y = []
		new_guard_x = []
		new_guard_y = []

		for i in range(0, num_x_copies + 1, 1):
			temp_self_y_list = []
			temp_guard_y_list = []
			nrx = self.room_x * i

			if len(new_self_x) == 0:
				nsx = self.self_x
			else:
				nsx = (nrx - new_self_x[-1][0]) + nrx
			new_self_x.append([nsx, self.self_y, 1])

			if len(new_guard_x) == 0:
				ngx = self.guard_x
			else:
				ngx = (nrx - new_guard_x[-1][0]) + nrx
			new_guard_x.append([ngx, self.guard_y, 7])

			for j in range(1, num_y_copies + 1, 1):
				nry = self.room_y * j
				if len(temp_guard_y_list) == 0:
					ngy = (nry - self.guard_y) + nry
					temp_guard_y_list.append(ngy)
				else:
					ngy = (nry - temp_guard_y_list[-1]) + nry
					temp_guard_y_list.append(ngy)
				new_guard_y.append([ngx, ngy, 7])

				if len(temp_self_y_list) == 0:
					nsy = (nry - self.self_y) + nry
					temp_self_y_list.append(nsy)
				else:
					nsy = (nry - temp_self_y_list[-1]) + nry
					temp_self_y_list.append(nsy)
				new_self_y.append([nsx, nsy, 1])

		return new_self_x + new_guard_x + new_self_y + new_guard_y

	def other_quadrants(self, matrix):
		quad2 = deepcopy(matrix)
		quad2t = [-1, 1]
		quad2f = []
		for j in range(len(quad2)):
			list = [quad2[j][i] * quad2t[i] for i in range(2)]
			dist = self.get_dist(list[0], list[1])

			if dist <= self.max_distance:
				list.append(matrix[j][2])
				quad2f.append(list)

		quad3 = deepcopy(matrix)
		quad3t = [-1, -1]
		quad3f = []
		for j in range(len(quad3)):
			list = [quad3[j][i] * quad3t[i] for i in range(2)]
			dist = self.get_dist(list[0], list[1])

			if dist <= self.max_distance:
				list.append(matrix[j][2])
				quad3f.append(list)

		quad4 = deepcopy(matrix)
		quad4t = [1, -1]
		quad4f = []
		for j in range(len(quad3)):
			list = [quad4[j][i] * quad4t[i] for i in range(2)]
			dist = self.get_dist(list[0], list[1])

			if dist <= self.max_distance:
				list.append(matrix[j][2])
				quad4f.append(list)

		return quad2f, quad3f, quad4f

	def filter_target_hit(self, matrix):
		target = {}
		for i in range(len(matrix)):
			dist = self.get_dist(matrix[i][0], matrix[i][1])
			angle = self.get_angle(matrix[i][0], matrix[i][1])
			test_a = self.max_distance >= dist > 0
			test_b = angle not in target
			test_c = angle in target and dist < target[angle][1]
			if test_a and (test_b or test_c):
				target[angle] = [matrix[i], dist]

		return target


def return_count(dict):
	count = 0
	for key in dict:
		if dict[key][0][2] == 7:
			count += 1
	return count


def solution(dimensions, your_position, guard_position, distance):
	gf = GuardFight(dimensions, your_position, guard_position, distance)
	first_quadrant = gf.get_first_quadrant()
	quad2, quad3, quad4 = gf.other_quadrants(first_quadrant)
	final_list = first_quadrant + quad2 + quad3 + quad4
	final_dict = gf.filter_target_hit(final_list)
	count = return_count(final_dict)
	return count
