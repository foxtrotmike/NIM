# -*- coding: utf-8 -*-
"""
Created on Thu Aug 03 00:03:37 2017

@author: Dr. Fayyaz Minhas (http://faculty.pieas.edu.pk/fayyaz/)
"""
import numpy as np
global count 
count = 0
def successors(s):
    """
    Generate successors of state s
        input: s (tuple)   
        return: a successor state of 
    """
    global count
    count+=1
    x = set([])
    for i in range(len(s)):
        n = s[i]
        for j in range(n/2+1,n):
            e = s[:i]+(j,n-j)+s[i+1:]            
            x.add(tuple(sorted(e))) #to prevent duplication
    return x
    
def isTerminal(s):
    """
    Is s a terminal state?
    """
    return np.max(s)<=2

def minimax(s):
    best = None
    val = -np.inf
    for x in successors(s):
        v = minv(x)
        if v>val:
            val = v
            best = x
    return best
            
def minv(s):
    if isTerminal(s):
        return +1
    v = np.inf
    for x in successors(s):
        v = min(v,maxv(x))
    return v
    
def maxv(s):
    if isTerminal(s):
        return -1
    v = -np.inf
    for x in successors(s):
        v = max(v,minv(x))        
    return v
    
if __name__=='__main__':
    v = (13,)
    # for a computer vs. computer game    
    w = True
    while v:
        print w,v
        v = minimax(v)
        w = not(w)
    print "Winner:",w
    print "States:",count