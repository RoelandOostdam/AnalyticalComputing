def formatPrint(matrix):
    for x in range(0,len(matrix)):
        print(matrix[x])

def checkSolution(matrix, t):
    a, b, c, \
    d, e, f, \
    g, h, i = matrix[0][0], \
                matrix[0][1], \
                matrix[0][2], \
                matrix[1][0], \
                matrix[1][1], \
                matrix[1][2], \
                matrix[2][0], \
                matrix[2][1], \
                matrix[2][2]
    if(a+b+c==t and d+e+f==t and g+h+i==t and a+d+g==t and b+e+h==t and c+f+i==t and a+e+i==t and g+e+c==t):
        return 1
    else:
        return 0


def solve(matrix, t):
    a, b, c, \
    d, e, f, \
    g, h, i = matrix[0][0], \
                matrix[0][1], \
                matrix[0][2], \
                matrix[1][0], \
                matrix[1][1], \
                matrix[1][2], \
                matrix[2][0], \
                matrix[2][1], \
                matrix[2][2]
    #Horizontal 0
    if(a==0 and b and c):
        a = t-b-c
    if (b==0 and a and c):
        b = t-a-c
    if (c==0 and a and b):
        c = t-a-b
    #Horizontal 1
    if (d==0 and e and f):
        d = t-e-f
    if (e==0 and d and f):
        e = t-d-f
    if (f==0 and d and e):
        f = t-d-e
    #Horizontal 2
    if (g==0 and h and i):
        g = t-h-i
    if (h==0 and g and i):
        h = t-g-i
    if (i==0 and g and h):
        i = t-g-h
    #Vertical 0
    if (a==0 and d and g):
        a = t-d-g
    if (d==0 and a and g):
        d = t-a-g
    if (g==0 and a and d):
        g = t-a-d
    #Vertical 1
    if (b==0 and e and h):
        b=t-e-h
    if (e==0 and b and h):
        e=t-b-h
    if (h==0 and b and e):
        h=t-b-e
    #Vertical 2
    if (c==0 and f and i):
        c=t-f-i
    if (f==0 and c and i):
        f=t-c-i
    if (i==0 and c and f):
        i=t-c-f
    #Diagonal 0
    if (a==0 and e and i):
        a=t-e-i
    if (e==0 and a and i):
        e=t-a-i
    if (i==0 and a and e):
        i=t-a-e
    #Diagonal 1
    if (g==0 and e and c):
        g=t-e-c
    if (e==0 and g and c):
        e=t-g-c
    if (c==0 and g and e):
        c=t-g-e

    newMatrix = [
        [a,b,c],
        [d,e,f],
        [g,h,i],
    ]

    return newMatrix

matrix = [
    [5,0,0],
    [0,0,4],
    [0,0,6]
]

for constant in range(1,100000):
    constant = round(constant*0.1,1)
    print(constant)
    matrix_temp = matrix
    while(matrix_temp!=solve(matrix_temp,constant)):
        matrix_temp = solve(matrix_temp,constant)
    if(checkSolution(matrix_temp,constant)):
        print("Solved with constant:",constant)
        formatPrint(matrix_temp)
        break