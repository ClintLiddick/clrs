#!/usr/bin/env python

import sys

def merge(A,start,lower_end,end):
    left = A[start:lower_end]
    right = A[lower_end:end]
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

def sort(A,start=None,end=None):
    if start is None:
        start = 0
    if end is None:
        end = len(A)

    if end <= start + 1:
        return
    else:
        mid = (start + end) / 2
        sort(A,start,mid)
        sort(A,mid,end)
        merge(A,start,mid,end)
        return
