#Time complexity: O(n)
#Space complexity: O(1)

def sequential_search(alist, item)->bool:
    pos = 0 
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
        
    return found

if __name__ == "__main__":
    alist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequential_search(alist, 8))
    print(sequential_search(alist, 10))