#!/usr/bin/env python

import sys

def merge(A,start,lower_end,end):
    left = A[start:lower_end+1]
    right = A[lower_end+1:end]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i = 0
    j = 0
    for k in range(start,end):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
    return A

        
