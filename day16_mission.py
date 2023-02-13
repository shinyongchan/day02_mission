#ch6-1
import random

def isStackFull():
	global SIZE, stack, top
	if (top >= SIZE-1):
		return True
	return False

def isStackEmpty():
	global SIZE, stack, top
	if (top == -1):
		return True
	return False

def push(data):
	global SIZE, stack, top
	if (isStackFull()):
		return
	top = top + 1
	stack[top] = data

def pop():
	global SIZE, stack, top
	if (isStackEmpty()):
		return
	data = stack[top]
	stack[top] = None
	top = top - 1
	return data


SIZE = 6
stack = [None for _ in range(SIZE)]
top = -1


if __name__ == '__main__':

	array=['빨강', '파랑', '초록', '노랑', '보라', '주황']
	random.shuffle(ston_array)


	print("과자집에 가는 길 : ", end = ' ')
	for ston in ston_array:
		push(ston)
		print(ston," -->", end=' ')
	print("과자집")

	print("우리집에 오는 길 : ", end=' ')
	while True:
		ston = pop()
		if ston == None:
			break
		print(ston," -->",end=' ')
	print("우리집")