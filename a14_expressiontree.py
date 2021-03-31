import tokenize

operator = ["+", "-", "*", "/", "%", "//", "**"]


class Node (object):
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None


class Stack (object):
    def __init__(self):
        self.stack = []

    def push(self, token: Node):
        self.stack.append(token)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack[-1]

    def size(self):
        return len(self)

    def is_empty(self):
        return len(self.stack) == 0


class Tree (object):
    def __init__(self):
        self.root = Node()
        self.prefix = ""
        self.postfix = ""

    def create_tree(self, expr: str):
        curNode = self.root
        stack = Stack()
        tokens = expr.split()

        for token in tokens:
            if token == "(":
                curNode.left = Node()
                stack.push(curNode)
                curNode = curNode.left
            elif token == ")":
                if not stack.is_empty():
                    curNode = stack.pop()
            elif token in operator:
                curNode.value = token
                curNode.right = Node()
                stack.push(curNode)
                curNode = curNode.right
            else:
                curNode.value = token
                curNode = stack.pop()

    def evaluate(self, aNode: Node):
        if aNode == None:
            return 0
        elif aNode.left == None and aNode.right == None:
            return int(aNode.value)
        else:
            lValue = int(self.evaluate(aNode.left))
            rValue = int(self.evaluate(aNode.right))

            if aNode.value == "+":
                return lValue + rValue
            elif aNode.value == "-":
                return lValue - rValue
            elif aNode.value == "*":
                return lValue * rValue
            elif aNode.value == "/":
                return lValue / rValue
            elif aNode.value == "%":
                return lValue % rValue
            elif aNode.value == "//":
                return lValue // rValue
            elif aNode.value == "**":
                return lValue ** rValue

    def pre_order(self, aNode: Node):
        if aNode and aNode.value:
            self.prefix += aNode.value + " "
            self.pre_order(aNode.left)
            self.pre_order(aNode.right)

    def post_order(self, aNode: Node):
        if aNode and aNode.value:
            self.post_order(aNode.left)
            self.post_order(aNode.right)
            self.postfix += aNode.value + " "


def main():
    infix = input()
    tree = Tree()
    tree.create_tree(infix)
    tree.pre_order(tree.root)
    tree.post_order(tree.root)
    print(infix + " = " + str(tree.evaluate(tree.root)))
    print("Prefix Expression: " + tree.prefix)
    print("Postfix Expression: " + tree.postfix)


main()