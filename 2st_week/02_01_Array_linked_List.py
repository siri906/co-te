# Array 같은 경우 조회에서  시간복잡도가 적고  [캡슐 호텔방 생각하기]
# Linked List 중간 삽입 삭제할 경우에는 삽입삭제 할경우 사용 [기차 생각하기 [기관실]-[1호차]-[2호차]]

# 파이썬의 list 는 Array, linkedList 둘다 사용가능한 효율적인 자료구조이다


# Class란?
# 객체를 정의한 설계도 또는 틀
# ex) 클래스가 사람이라면 객체는 나, 너, 우리 이렇게 될 수 있다
# ex) 클래스가 동물이라면 객체는 강아지, 고양이, 새 이렇게 될수 있다 
# class Person:
#   def __init__(self, name_param):
#     self.name = name_param
#     print('hehje ' , self, self.name)

#   def talk(self):
#     print('안녕하세요 저는', self.name ,'입니다')
    

# person_1 = Person("유재석")
# person_2 = Person("박명수")

# print(person_1.talk())

# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None


# first_node = Node(5) # [5] 라는 기차칸 생성
# second_node = Node(12) # [12] 라는 기차칸 생성
# first_node.next = second_node # [5] - [12] 라는 기차칸 연결

# class LinkedList:
#   def __init__(self, value):
#     self.head = Node(value)

#   def append(self, value):
#     cur = self.head

#     while cur.next is not None:
#       cur = cur.next
#     cur.next = Node(value)

#   def print_all(self):
#     cur1 = self.head
#     while cur1.next is not None:
#     # print(cur)
#     # print(self.head,'self')
#       print(cur1.data)


# linked_list = LinkedList(9)
# # print(linked_list.head.data, 'head')

# linked_list.append(10)
# linked_list.append(150)

# linked_list.print_all()


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
            cur = self.head
            print(cur)
            while cur is not None:
                print(cur.data)
                cur = cur.next
        

linked_list = LinkedList(5)
linked_list.append(12)
linked_list.print_all()