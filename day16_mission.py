#ch5-2
import random
import math

class Node:
	def __init__(self, data):
		self.data = data
		self.plink = None
		self.nlink = None
def print_node(start):
	current = start
	print("정방향 -->", end=' ')
	print(current.data, end=' ')
	while current.nlink != None:
		current = current.nlink
		print(current.data, end=' ')
	print()
	print("역방향 -->", end=' ')
	print(current.data, end=' ')
	while current.plink != None:
		current = current.plink
		print(current.data, end=' ')


data_array = ['다현', '정연', '쯔위', '사나', '지효']
head, current, pre = None, None, None


if __name__ == '__main__':
	node = Node(data_array[0])
	head = node

	for data in data_array[1:]:
		pre = node
		node = Node(data)
		pre.nlink = node
		node.plink = pre

	print_node(head)