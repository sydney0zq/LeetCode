int main(){
   int n,m;cin>>n>>m;
   vector<vector<int>> matrix(n,vector<int>(m,0));
   vector<vector<int>> re(n,vector<int>(m,0));
   for(int i=0;i<n;i++){
       for(int j=0;j<m;j++){
           cin>>matrix[i][j];
       }
   }
   int res = 0;
   for(int i=1;i<n;i++){
       for(int j=1;j<m;j++){
           if(matrix[i][j]>matrix[i][j-1]){
               matrix[i][j] = max(matrix[i][j-1]+1,matrix[i][j]);
           }
           if(matrix[i][j]>matrix[i-1][j]){
               matrix[i][j] = max(matrix[i-1][j]+1,matrix[i][j]);
           }
           res = max(res,matrix[i][j]);
       }
   }
   cout<<res<<endl;
   return 0;
}