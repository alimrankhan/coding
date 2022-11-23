// Online C compiler to run C program online
#include <stdio.h>

int main() {
    // matrix multiplication
    printf("Matrix Multiplication\n");
    int n,m,r1,c1,r2,c2;
    int i,j,k,l;
    int a[r1][c1];
    int b[r2][c2];
    scanf("%d %d", &r1, &c1);
    scanf("%d %d", &r2, &c2);
    for(i=0;i<r1;i++){
        for(j=0;j<c1;j++){
            scanf("%d", &a[i][j]);
        }
    }
    for(i=0;i<r2;i++){
        for(j=0;j<c2;j++){
            scanf("%d", &b[i][j]);
        }
    }
    
    int mul[r1][c2];
    for(i=0;i<r1;i++){
        for(j=0;j<c2;j++){
            mul[i][j]=0;
        }
    }
    for(i=0;i<r1;i++){
        for(j=0;j<c2;j++){
            for(k=0;k<c1;k++){
                mul[i][j]+= a[i][k]*b[k][j];
            }
            //printf("%d ", mul[i][j]);
            
        }
    }
    for(i=0;i<r1;i++){
        for(j=0;j<c2;j++){
            printf("%d\t", mul[i][j]);
        }
        printf("\n");
    }
    

    return 0;
}