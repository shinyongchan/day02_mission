#ch5-1
import random
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.link = None
		self.dist = math.sqrt(data[1]*data[1] + data[2]*data[2])

def pirnt_node(start):
	current = start
	print(f'{current.data[0]}편의점, 거리 : {current.dist}')
	while current.link != start:
		current = current.link
		print(f'{current.data[0]}편의점, 거리 : {current.dist}')



def makeList(store):
	global head, current, pre

	node = Node(store)

	if head == None:
		head = node
		node.link = head
		return
	if head.dist > node.dist:
		node.link = head
		last = head
		while last.link != head:
			last = last.link
		last.link = node
		head = node
		return


	current = head
	while current.link != head:
		pre = current
		current = current.link
		if current.dist > node.dist:
			pre.link = node
			node.link = current
			return
	current.link = node
	node.link = head




head, current, pre = None, None, None
memory = []

if __name__ == '__main__':

	store_array = []
	store_name = 'A'
	for _ in range(10):
		store = (store_name, random.randint(1, 100), random.randint(1, 100))
		store_array.append(store)
		store_name = chr(ord(store_name) + 1)

	for store in store_array:
		makeList(store)

	pirnt_node(head)