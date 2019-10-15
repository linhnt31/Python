from pythonds.basic.stack import Stack
from pythonds.trees.binaryTree import BinaryTree
import operator

def build_parse_tree(exp):
    fplist = exp.split()
    pStack = Stack()
    eTree = BinaryTree('') #initialize empty Tree
    pStack.push(eTree)
    currentTree = eTree

    for i in fplist:
        if i == '(':
            currentTree.insertLeft('')
            pStack.push(currentTree)
            currentTree  = currentTree.getLeftChild()
        elif '0' <= i <= '9':
            currentTree.setRootVal(int(i))
            parent = pStack.pop()
            currentTree = parent
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = pStack.pop()
        else:
            raise ValueError
    
    return eTree

def evaluate(parseTree):
    opers = {
        '+':operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC), evaluate(rightC))
    else:
        return parseTree.getRootVal()


if __name__ == "__main__":
    exp = "( ( 10 + 5 ) * 3 )"
    print(evaluate(build_parse_tree(exp)))
