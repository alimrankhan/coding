#include<bits/stdc++.h>
using namespace std;

int maxsub(int arr[]){
    int ans=0;
    int sum= 0;
    for(int i=0; i<5; i++){
        sum= max(arr[i], sum+arr[i]);
        ans= max(sum, ans);
    }
    return ans;
}
int main(){
    cout<<"hello"<<endl;
    int arr[]= {1,2,3,-1,20};
    cout<<maxsub(arr)<<endl;
}
