"""
- Link: https://app.codesignal.com/tournaments/ThyE5pQLXR6tqrGE8/A
"""

#Solution 1: 
def __mergeSort(sequence):
    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left + 1 == right:
            return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence


#Solution 2: clearly ---> python standard

def optimizedMergeSort(sequence):
    if len(sequence) > 1:
        mid = len(sequence) // 2
        left = sequence[:mid]
        right = sequence[mid:]

        optimizedMergeSort(left)
        optimizedMergeSort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sequence[k] = left[i]
                i += 1
            else:
                sequence[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            sequence[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            sequence[k] = right[j]
            j += 1
            k += 1

    return sequence    
    
if __name__ == "__main__":
    sequence = [100, 99]
    
    # print("After implementing merge sort: {}".format(__mergeSort(sequence)))
    print("{}".format(optimizedMergeSort(sequence)))