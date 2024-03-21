# # class Stack:

# #     def __init__(self, items = [], limit = 100):
# #         pass

# #     def isEmpty(self):
# #         pass

# #     def push(self, item):
# #         pass

# #     def pop(self):
# #         pass

# #     def peek(self):
# #         pass
    
# #     def size(self):
# #         pass

# #     def full(self):
# #         pass

# #     def search(self, target):
# #         pass
# class Stack:
#     def __init__(self, limit=None):
#         self.stack = []
#         self.limit = limit

#     def push(self, item):
#         if self.limit is None or len(self.stack) < self.limit:
#             self.stack.append(item)
#         else:
#             raise Exception("Stack is full")
# # 
#     def pop(self):
#         if not self.empty():
#             return self.stack.pop()
#         else:
#             raise Exception("Stack is empty")

#     def peek(self):
#         if not self.empty():
#             return self.stack[-1]
#         else:
#             return None

#     def size(self):
#         return len(self.stack)

#     def empty(self):
#         return len(self.stack) == 0

#     def full(self):
#         if self.limit is None:
#             return False
#         return len(self.stack) == self.limit

#     def search(self, value):
#         if not self.empty():
#             for i in range(len(self.stack) - 1, -1, -1):
#                 if self.stack[i] == value:
#                     return len(self.stack) - 1 - i
#         return -1
class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items else []
        self.limit = limit

    def push(self, item):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(item)
        else:
            raise Exception("Stack is full")

    def pop(self):
        if not self.empty():
            return self.items.pop()
        else:
            raise Exception("Stack is empty")

    def peek(self):
        if not self.empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

    def empty(self):
        return len(self.items) == 0

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) == self.limit

    def search(self, value):
        if not self.empty():
            for i in range(len(self.items) - 1, -1, -1):
                if self.items[i] == value:
                    return len(self.items) - 1 - i
        return -1
