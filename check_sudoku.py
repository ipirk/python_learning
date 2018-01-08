'''
Created on 21/12/2017

@author: it
'''
import copy
from time import time


def union(p,q):
    for e in q:
        if e not in p:
            p.append(e)
            
            
correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

def check_sudoku2(p):
    n=len(p)
    digit=1
    while digit <=n:
        i=0
        while i<n:
            row_count=0
            col_count=0
            j=0
            while j<n:
                if p[i][j]==digit:
                    row_count=row_count+1
                if p[j][i]==digit:
                    col_count=col_count+1
                j+=1
            if row_count !=1 or col_count!=1:
                return False
            i=i+1
        digit=digit+1
    return True

def check_table(sudoku):
    
    size= len(sudoku)
    y=0
    x=0
    temp=copy.deepcopy(sudoku)
    check=1
    while y <= size-1:
        x=0
        temp[y].sort()
        if temp[y][0]==1:
            while x < size:
                #print sudoku[y][x]
                if temp[y][x] <> x+1:
                    check=0
                x+=1
        else:
            check=0
        y+=1
    return check

def transpose(sudoku):
    size= len(sudoku)
    x=0
    y=0
    result=[]
    resultx=[]
    while x<size:
        while y<size:
            resultx.append(sudoku[y][x])
            y+=1
        x+=1
        y=0
        result.append(resultx)
        resultx=[]
    return result

def check_sudoku(p):
    check=check_table(p)  

    if check==1:     
        transposto=transpose(p)
        check=check_table(p) 
    return check  
a=time()
print check_sudoku(correct)
print time()-a

a=time()
print check_sudoku2(correct)
print time()-a



 
