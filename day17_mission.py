#Ch8_1
import random
class tree_node:
    def __init__(self, data):
        self.left = None
        self.data = data
        self.right = None

def preorder(node):
    if node == None:
        return
    print(node.data, end=' ')
    preorder(node.left)
    preorder(node.right)


root = None
data_array = ['바나나맛우유', '레쓰비', '츄파츕스', '도시락', '삼각김밥', '코카콜라', '삼다수',]
sell_array = [random.choice(data_array) for _ in range(20)]

if __name__ == "__main__":

    node = tree_node(sell_array[0])
    root = node
    for sell in sell_array[1:]:
        node = tree_node(sell)

        current = root
        while True:
            if sell < current.data:
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            elif sell == current.data:
                break
            else:
                if current.right == None:
                    current.right = node
                    break
                current = current.right
    print("오늘 판매된 물건(중복O) : ", end=' ')
    print(sell_array)
    print()
    print("이진 탐색 트리 구성 완료!")
    print()
    print("오늘 판매된 종류(중복X) : ", end=' ')
    preorder(root)
