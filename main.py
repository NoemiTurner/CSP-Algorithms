# author: Noemi Turner
# date: June 2022
# class: CS 470
# assignment: CSP Project
# filename: main.py

import copy
import csv

numcolors = 1 # 0, 1, 2

# Big Map
num = 29
map1 = []
with open('CSPData.csv', newline='') as csvfile:
    file = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i, line in enumerate(file):
        if(i > 0):  
            row = []  
            for j, element in enumerate(line):
                if(j > 0):
                    if(element == ''):
                        row.append(0)
                    else:
                        row.append(int(element))
            map1.append(row)
solution = [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1] #29

# Small Map

# num = 5
#      0 1 2 3 4
# map1 = [[0,1,0,0,1], #0
#         [1,0,1,1,1], #1
#         [0,1,0,1,1], #2
#         [0,1,1,0,0], #3
#         [1,1,1,0,0]] #4

# solution = [-1,-1,-1,-1,-1]


def count_conflicts(m,sol):
    conflicts = 0
    for i in range(0,num): # row
        for j in range(i+1, num): # col
            if(m[i][j] == 1): # the regions are connected
                if(sol[i] == sol[j] and  sol[i] != -1 and sol[j] != -1): # they are the same color
                    conflicts += 1
    return conflicts


# very basic dfs
def solutionsearch(s,var):
    for c in range(0,numcolors):
        s2 = copy.deepcopy(s)
        s2[var] = c
        print(var,s2,count_conflicts(map1,s2))
        if(count_conflicts(map1, s2) == 0): # no conflicts, yet
            if(s2.count(-1) == 0): # checks if s2 is fully assigned (aka doesn't contain any -1's)
                return True
            else: 
                temp = solutionsearch(s2,var+1)
                if(temp == True):
                    return True
    return False # no solution found



def highestDegreeSearch(s, var, vertices):
    for c in range(0,numcolors):
        s2 = copy.deepcopy(s)
        s2[vertices[var][1]] = c
        print(var,s2,count_conflicts(map1,s2))
        if(count_conflicts(map1, s2) == 0): # no conflicts, yet
            if(s2.count(-1) == 0): # checks if s2 is fully assigned (aka doesn't contain any -1's)
                return True
            else: 
                temp = highestDegreeSearch(s2,var+1, vertices)
                if(temp == True):
                    return True
    return False # no solution found



    
vertices = [] # store the vertex indexes and their degrees in a list of tuples
for index, row in enumerate(map1):
    degree = row.count(1)
    vertices.append((degree, index))
vertices.sort(reverse=True)
print(highestDegreeSearch(solution, 0, vertices))


print(solutionsearch(solution, 0))


