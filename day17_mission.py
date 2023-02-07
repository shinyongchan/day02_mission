#Ch7_2


def enqueue(data):
    global SIZE, front, rear
    if (rear+1) % SIZE == 0:
        print("큐가 꽉찼습니다.")
    rear = (rear+1) % SIZE
    queue[rear] = data


def dequeue():
    global SIZE, front, rear
    if rear == front:
        print("큐가 비었습니다.")
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data


def calc_time():
    time_sum = 0
    for i in range((front+1) % SIZE,(rear+1) % SIZE):
        time_sum = time_sum + queue[i][1]
    return time_sum

SIZE = 6
queue = [None for _ in range(SIZE)]
front = 0
rear = 0

if __name__ == "__main__":
    wait_call = [('사용', 9), ('고장', 3), ('환불', 4), ('환불', 4), ('고장', 3)]


    for call in wait_call:
        print(f'귀하의 대기 예상시간은 {calc_time()}분 입니다.')
        print(f'현재 대기 콜 --> {queue}')
        print()
        enqueue(call)

    print(f'최종 대기 콜 --> {queue}')
    print("프로그램 종료!")