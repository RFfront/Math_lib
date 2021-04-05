from matrix import Matrix
a=[
[1,2,3],
[1,3,5],
[6,1,6]
]
b=[
[-9,1,3],
[12,7,1],
[0,10,-5]
]
c=[
[5,0,2],
[4,1,5],
[3,1,-1]
]


mat=Matrix(a)
mat2=Matrix(b)
print(mat.det())

#print(mat*mat2)
