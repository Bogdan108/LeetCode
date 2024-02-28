class Pair:
     def __init__(self, a:int, b:int):
       self.left = a
       self.right = b

class MinStack:

    def __init__(self):
        self.stack_list = []


    def push(self, val: int) -> None:
        if len(self.stack_list) > 0:
            if self.stack_list[-1].right > val:
                self.stack_list.append(Pair(val,val))
            else:
                self.stack_list.append(Pair(val,self.stack_list[-1].right))
        else:
            self.stack_list.append(Pair(val,val))

    def pop(self) -> None:
        if  len(self.stack_list) > 0:
             self.stack_list.pop()

    def top(self) -> int:
         return self.stack_list[-1].left

    def getMin(self) -> int:
         return self.stack_list[-1].right
def main():
    minStack =  MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())

if __name__ == "__main__":
    main()