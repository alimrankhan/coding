//triple_sum //hackerrank
#include<bits/stdc++.h>
using namespace std;

int main() {
    int a,b,c;
    int ans=0;
    cin>>a>>b>>c;
    int ara[a], arb[b], arc[c];
    for(int i= 0;i< a;i++)
        cin>>ara[i];
    for(int i=0; i<b; i++)
        cin>>arb[i];
    for(int i=0; i<c; i++)
        cin>>arc[i];
    for(int i=0; i<b; i++){
        if(i>0 && arb[i]==arb[i-1])
            continue;
        int sa=0,sc=0;
        for(int j=0;j<a;j++){
            if(ara[j]<=arb[i])
                sa++;
        }
        for(int k=0;k<c;k++){
            if(arc[k]<=arb[i])
                sc++;
        }
        ans+= (sa*sc);
    }
    cout<<ans<<endl;

    return 0;
}
