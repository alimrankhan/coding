#include<bits/stdc++.h>
int fib[15];
int generate_fibonaccis(int n) {

    fib[0] = 1;
    fib[1] = 1;
    for (int i = 2; i < n; ++i) {
        fib[i] = fib[i - 2] + fib[i - 1];
    }

}

int main() {
    int n = 10;
    generate_fibonaccis(n);
    for (int i = 0; i < n; i++) {
        std::cout << fib[i] << " ";
    }
    return 0;
}
