Ch7_1

def dequeue():
    global SIZE, front, rear
    if rear == -1:
        print("큐가 비었습니다.")
        return
    front = front + 1
    data = queue[front]
    queue[front] = None
    for i in range(front+1,SIZE):
        queue[i-1] = queue[i]
        queue[i] = None
    rear = rear - 1
    front = - 1
    return data




SIZE = 5
queue = ['정국', '뷔', '지민', '진', '슈가']
front = -1
rear = 4

if __name__ == "__main__":
    for _ in range(SIZE):
        print(f'대기 줄 상태 : {queue}')
        print(f'{dequeue()} 님 식당에 들어감')
    print(f'대기 줄 상태 : {queue}')
    print("식당 영업 종료!")


