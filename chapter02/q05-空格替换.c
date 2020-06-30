#include<stdio.h>
#include<stdlib.h>

/* 剑指Offer P70
 * 要从后向前替换，先算出总体需要的长度，然后再用两个指针替换
 */


char* replaceSpace(char* s){
    int num_blank = 0;
    int len_s = 0;
    char * p = s;
    // count how many blanks in s and the length of s
    for (int i=0; 1; i++){
        if (s[i] != NULL){
            if (s[i] == ' '){
                num_blank += 1;
            }
        }else{
            len_s = i+1;
            break;
        }
    }
    int len_new_s = len_s + num_blank * 2;
    char * new_s = (char *)malloc(len_new_s*sizeof(char));
    int p1;
    int p2;
    p1 = len_s-1;
    p2 = len_new_s-1;
    for (; p1 >= 0; p1--){
        if (s[p1] != ' '){
            new_s[p2] = s[p1];
            p2 -= 1;
        }else{
            new_s[p2] = '0';
            new_s[p2-1] = '2';
            new_s[p2-2] = '%';
            p2 -= 3;
        }
    }

    //printf("len_s=%d, num_blanks=%d\n", len_s, num_blank);

    return new_s;
}

int main(){
    char s[] = "hello world";
    printf("%s\n", s);
    printf("%s\n", replaceSpace(s));
}
