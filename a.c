#include <stdio.h>

int main(void) {
	// your code goes here
	int t;
	scanf("%d", &t);
	while(t--){
	    int n,k;
	    scanf("%d %d", &n, &k);
	    printf("%d\n", n%k);
	}
	return 0;
}

