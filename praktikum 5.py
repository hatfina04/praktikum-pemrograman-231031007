## TULIS KELAS Node DI SINI ##
    ## TULIS NODE CONSTRUCTOR DI SINI ##
class Node:
    def __init__(self, nilai):
            self.value = nilai
            self.next = None
                                     
    
## TULIS KELAS LinkedList DI SINI ##
    ##  TULIS LL CONSTRUCTOR DISINI  ##
class linkedlist:
    def __init__(self, nilai):
            new_node = Node (nilai)
            self.head = new_node
            self.tail = new_node 
            self.lengght = 1

    ## TULIS FUNGSI APPEND DI SINI ##
    def append(self, value) :
        new_node = Node (value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node 
        else:
            self.tail.next = new_node 
            self.tail = new_node
        self.length += 1

            


    ## TULIS FUNGSI PRINT_LIST DI SINI ##
    def print_list(self):
        temp = self.head
        while temp is not None:
              print(temp.value)
              temp = temp.next 


    ## TULIS FUNGSI POP DI SINI ##
    def pop(self):
        if self.lenght == 0:
              return None 
        temp = self.head 
        pre = self.head 
        while(temp.next):
              pre = temp
              temp = temp.next 
        self.tail = pre 
        self.tail.next = None 
        self.lenght -= 1
        if self.lenght == 0:
             self.head = None
             self.head = None 
        return temp 


    ## TULIS FUNGSI PREPEND DI SINI ##
    def prepend(self, value):
        new_node = Node(value)
        if self.lenght == 0:
              self.head = new_node
              self.tail = new_node
        else:
             new_node.next = self.head
             self.head = new_node
        self.lenght += 1
        return True 


    ## TULIS FUNGSI POP FIRST DI SINI ##
    def pop_first(self):
        if self.lenght == 0:
              return None 
        temp = self.head = self.head.next
        temp.next = None
        self.lenght -= 1
        if self.lenght == 0:
              self.tail = None 
        return temp 

    ## TULIS FUNGSI GET DI SINI ##
    def get(self, index):
        if index < 0 or index >= self.length:
             return None
        temp = self.head 
        for _ in range(index):
             temp = temp.next
             return temp 


## 01 Membuat Linked List
print("01 Membuat Linked List")
# Tulis kode program di sini
print("01 membuat linked list")
LL = linkedlist(7)
print('Head:', LL.head.value)
print('Tail:', LL.tail.value)
print('Lenght:', LL.lenght)

## 02 Append (Menambahkan Node Di Akhir)
print("\n02 Append Node")
# Tulis kode program di sini
LL.append(2)
LL.append(2)
LL.append(1)
LL.append(0)
LL.append(1)
LL.append(1)
LL.append(0)
LL.append(9)

## 03 Pop (Menghapus Node Terakhir)
print("\n03 Pop Node")
# Tulis kode program di sini
print('Linkdlist setelah append')
LL.print_list()

## 04 Prepend (Menambahkan Node Di Awal)
print("\n04 Prepend Node")
# Tulis kode program di sini
LL.append('Jian jenistiani')
print('Linked List setelah prepend')
LL.print_list

## 05 Pop First (Menghapus Node Pertama)
print("\n05 Pop First Node")
# Tulis kode program di sini
print(LL.pop_first().value)
print('linked List setelah pop first:')
LL.print_list()

## 06 Get Node (Mengakses Node Berdasarkan Indeksnya)
print("\n06 Get a Node")
# Tulis kode program di sini
print(LL.get(1).value)