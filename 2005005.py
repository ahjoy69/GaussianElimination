import numpy as npy

def GaussianElimination(A, B, pivot=True, showall=True):

    f = len(A)
    if f !=len(B):
        print('Error!Number of rows in A and B should be same.Try again.')
        exit(1)

    c = npy.transpose(A,axes=None)
    for i in range(f):
        count_zeros =npy.count_nonzero(c[i])
        if count_zeros == 0 :
            print('Error!At least one Column of A contains all zeros')
            exit(1)



    AugMat = npy.zeros((f,f+1))
    for i in range(f):
        for j in range(f+1):
           if j!=f:
               AugMat[i,j] = A[i,j]
           else:
               AugMat[i,j]=B[i]
    if showall:
        print('Augmented Matrix : ')
        print(AugMat)
        print('\n')
#Elimination
    x =0
    swap = 0
    for i in range(f-1):
        if pivot :
            for j in range(i,f):
                if abs(AugMat[j,i]) > abs(AugMat[i,i]):
                    x=1
                    AugMat[[i,j]]=AugMat[[j,i]]
                    swap+=1
                else:
                    x=0
                    pass

            if showall and x==1:
                print('After partial pivoting : ')
                print(AugMat)
                print('\n')

        print(f'After elemination {i + 1} : ')
        for k in range(i+1,f):
            if(AugMat[i,i]==0):
                print("Error.May be divided by zero is creating error. Please set pivot = True.")
                exit(1)

            d = float(AugMat[k,i]/AugMat[i,i])

            for l in range(i,f+1):
                AugMat[k,l] -= d*AugMat[i,l]

            if showall:
                print(AugMat)
                print('\n')


    det = 1
    for i in range(f):
        det *= AugMat[i, i]
    if swap%2 !=0:
        det = -det
    if showall:
        print(f'Determinant of A = {det}\n')

    rslt = npy.zeros((f,1))
#BackSubstitution
    for i in range(f-1,-1,-1):
        neg = 0
        for j in range(i+1,f):
            neg+=AugMat[i,j]*rslt[j,0]
        if AugMat[i,i]==0:
            print('No solution.Try again.')
            exit(0)

        rslt[i,0] = float((AugMat[i,f]-neg)/AugMat[i,i])


    return rslt



def main():
    n = int(input())
    A = npy.zeros((n,n))
    B = npy.zeros(n)
    #input()
    for i in range(n):
        a = input().split(" ")
        if(len(a)!=n):
            print(f'Error! Input a {n}X{n} matrix ')
            exit(1)

        for j in range(n):
            A[i,j]= float(a[j])

    #input()
    for i in range(n):
        try:
          B[i]=float(input())
        except:
            print(f'Error! Input a {n}X{1} matrix ')
            exit(1)

    R = GaussianElimination(A, B)

    """npy.savetxt(sys.stdout,R,fmt="%.4f")"""
    for i in range(n):
       print("%.4f" %R[i,0])


main()

