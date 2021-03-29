
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

int main(){
    string ss;
    getline(cin,ss);
    int n = ss.length();
    vector<int> index(n,0);
    int count = 0;
    for(int i=0;i<n;){
        while(ss[i]!='G' && i<n){
            i++;
        }
        if(i==n){
            break;
        }else{
            int j = i+1;
            while(j<n && (ss[j]!='o' || index[j] ==1)){
                j++;
            }
            if(j==n){
                break;
            }
            else{
                index[j] = 1;
                int k = j+1;
                while(k<n && (ss[k]!='o' || index[k] ==1)){
                    k++;
                }
                if(k==n){
                    break;
                }
                else{
                    index[k] = 1;
                    int z = k+1;
                    while(z<n && (ss[z]!='d' || index[z] ==1)){
                        z++;
                    }
                    if(z==n){
                        break;
                    }
                    else{
                        index[z] = 1;
                        count+=1;
                        i+=1;
                    }
                }
            }
        }
    }
    cout<<count;
    return 0;
}
