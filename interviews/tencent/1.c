#include<iostream>
#include<cmath>
#include<cstring>
using namespace std;
int main()
{
int N,n;
int dp[200][200]={0};
cin>>N;
while(N--)
{
char a[200]={0};
cin>>a;
n=strlen(a);
for(int i=0;i<n;i++)
dp[i][i]=1;
for(int i=1;i<n;i++)
for(int j=0;j<=i;j++)
{
dp[j][i]=dp[j][i-1]+1;
for(int k=j;k<=i-1;k++)
{
if(a[k]+1==a[i]||a[k]+2==a[i])
dp[j][i]=min(dp[j][i],dp[j][k-1]+dp[k+1][i-1]);
}
}
// cout<<dp[0][n-1]<<endl;
printf("%d", dp[0][n-1]);
}
return 0;
}