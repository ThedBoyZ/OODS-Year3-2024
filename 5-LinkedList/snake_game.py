class DoublyLinkedNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

alive = True

class Snake:
    global alive

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoublyLinkedNode(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        cur_node = self.head
        while cur_node.next:
            cur_node = cur_node.next

        cur_node.next = new_node
        new_node.previous = cur_node
        self.tail = new_node

    def swap_nodes(self, node1, node2):
        if node1.data == node2.data:
            return

        prev1, next1 = node1.previous, node1.next
        prev2, next2 = node2.previous, node2.next


        node1.previous = node2
        node1.next = next2
        node2.previous = prev1
        node2.next = node1

        if prev1:
            prev1.next = node2
        else:
            self.head = node2

        if next2:
            next2.previous = node1
        else:
            self.tail = node1

    def swap_odd_even(self):
        if not self.head or not self.head.next:
            return

        if not self.head.next.next:
            self.delete_node(self.head.next)

        mom = self.head
        current = mom.next

        while current and current.next:
            new_current = current.next.next
            self.swap_nodes(current, current.next)
            current = new_current
            if not current:
                print("Swap success!")
                return
            if not current.next:
                prev_node = current.previous
                prev_node.next = None
                self.tail = prev_node

        print("Swap success!")

    def dad(self, number):
        mom = self.head
        current = mom.next
        width = mom.data

        while current:
            width += current.data
            current = current.next

        if number == 0:
            result = []
            current = self.tail
            while current.previous:
                pre_node = current.previous
                if current.data == 0:
                    result.append(0)
                    self.delete_node(current)
                else:
                    print(f'Play success!->{result}')
                    return
                current = pre_node

        if width < number:
            current = self.tail
            nodes = []
            result = []
            while current.previous:
                prev_node = current.previous
                if current.data == 0 and number != 0:
                    nodes.append(current)
                elif number % current.data == 0:
                    for i in nodes:
                        self.delete_node(i)
                        result.append(i.data)
                    result.reverse()
                    print(f'Play success!->{result}')
                    return
                else:
                    nodes.append(current)
                current = prev_node

            print("Play success!->[]")
            self.swap_head_tail()
        else:
            print("Play success!->[]")
            return

    def swap_head_tail(self):
        if not self.head.next:
            return

        if self.head.next == self.tail:
            head = self.head
            tail = self.tail
            self.swap_nodes(head, tail)
            return

        head, previous1, next1 = self.head, self.head.previous, self.head.next
        tail, previous2, next2 = self.tail, self.tail.previous, self.tail.next

        self.head = tail
        self.tail = head

        self.head.previous = previous1
        self.head.next = next1
        next1.previous = self.head

        self.tail.previous = previous2
        self.tail.next = next2
        previous2.next = self.tail

    def shake(self):
        mom = self.head
        current = mom.next
        result = []
        while current:
            next_node = current.next
            if current.data > mom.data:
                result.append(current.data)
                self.delete_node(current)
            current = next_node
        print(f'Shake success!->{result}')

    def steal(self, number):
        self.append(number)
        print(f"Steal success!->{number}")

    def delete_node(self, node):
        if not node:
            return

        if node == self.head:
            self.head = node.next
            if self.head:
                self.head.previous = None
            else:
                self.tail = None
            return

        if node == self.tail:
            self.tail = node.previous
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return

        node.previous.next = node.next
        if node.next:
            node.next.previous = node.previous

    def __str__(self):
        global alive
        if not self.head:
            return "List is empty"

        mom = self.head
        current_child = mom.next
        _list = []

        while current_child:
            _list.append(str(current_child.data))
            current_child = current_child.next
        if not _list:
            alive = False
        return f'({mom.data})->{"->".join(_list)}' if _list else f'({mom.data})->Empty'

snake = Snake()

command_string = input("Snake Game : ").split(",")
snake_data = command_string[0].split("/")

command_string.pop(0)
command_string.insert(0, snake_data[1])
snake_data = snake_data[0].split()

for i in snake_data:
    snake.append(int(i))

print(snake)

for i in command_string:
    command = i.split()
    action = command.pop(0)
    if not alive:
        break
    elif action == "SW":
        snake.swap_odd_even()
    elif action == "SH":
        snake.shake()
    elif action == "F":
        snake.steal(int(command.pop()))
    elif action == "D":
        snake.dad(int(command.pop()))
    print(snake)
    print("------------------------------")

if not alive:
    print("Mom is dead")
print("Snake Game : ")