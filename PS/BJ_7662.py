import heapq
import sys

def dual_priority_queue(operations, n):
    min_heap, max_heap = [], [] 
    check = [1] * n
    for i in range(n):
        op, num = operations[i].split()
        num = int(num)

        if op == 'I':
            heapq.heappush(min_heap, (num, i))
            heapq.heappush(max_heap, (-num, i))
        else:
            if num == 1:
                if max_heap:
                    check[heapq.heappop(max_heap)[1]] = 0
            elif num == -1:
                if min_heap:
                    check[heapq.heappop(min_heap)[1]] = 0
        
        while min_heap and check[min_heap[0][1]] == 0:
            heapq.heappop(min_heap)
        while max_heap and check[max_heap[0][1]] == 0:
            heapq.heappop(max_heap)
    
    if min_heap == []:
        print("EMPTY")
    else:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")

def main():
    input = sys.stdin.readline
    T = int(input().strip())
    for _ in range(T):
        k = int(input().strip())
        operations = [input().strip() for _ in range(k)]
        dual_priority_queue(operations, k)

if __name__ == "__main__":
    main()