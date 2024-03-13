A=[
[2,3,4],
[4,5,3],
[3,4,5]
]

B=[
[4,3,5],
[4,3,2],
[3,7,6]
]

result=[
[0,0,0],
[0,0,0],
[0,0,0]
]

for i in range(len(A)):
    for j in range(len(B[0])):

     result[i][j]=A[i][j]+B[i][j]

for r in result:
    print(r)