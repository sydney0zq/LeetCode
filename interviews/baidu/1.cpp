#include<iostream>
#include<vector>
#include<map>
#include<stack>
using namespace std;
#include<math.h>



// m->rows
// n->cols

int main(){
    int rows,cols;
    cin>>rows>>cols;
    vector<vector<int>> img(rows,vector<int>(cols,0));
    // img create
    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++)
            cin>>img[i][j];
    }

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            int cnt = 1;
            int sum = img[i][j];
            if(i-1>=0){
                cnt++;
                sum += img[i-1][j];
            }
            if(i+1<rows){
                cnt++;
                sum += img[i+1][j];
            }
            if(j-1>=0){
                cnt++;
                sum += img[i][j-1];
            }
            if(j+1<cols){
                cnt++;
                sum += img[i][j+1];
            }
            img[i][j] = (int)round((double)sum/(double)cnt);
        }
    }

    for(int i=0;i<rows;i++){
        for(int j=0;j<cols;j++){
            cout << img[i][j];
            if(j != cols-1)
                cout << " ";
        }
        cout << endl;
    }
    return 0;
}