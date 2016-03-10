#!/usr/bin/env python

def sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            A[i+1] = A[i] # slide up
            i -= 1
        A[i+1] = key

if __name__ == '__main__':
    A = [3,5,2,4,6]
    print A
    sort(A)
    print A
