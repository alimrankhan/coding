//subset generating //pdf
#include<bits/stdc++.h>
using namespace std;

vector <int> sub_arr;
int n=3;
void fun(int k){
    if(k==(n+1)){
for(auto i:sub_arr){
cout<<i;}
cout<<endl;

    }
    else{
        sub_arr.push_back(k);
        fun(k+1);
        sub_arr.pop_back();
        fun(k+1);
    }
}
int main() {
    fun(1);
    for(auto i= sub_arr.begin();i<sub_arr.end();i++){
        cout<<*i<<endl<<n ;
    }

    return 0;
}
