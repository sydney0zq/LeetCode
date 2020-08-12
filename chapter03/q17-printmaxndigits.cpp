#include <cstdio>
#include <memory>


bool Increment(char* number);
void PrintNumber(char * number);
void Print1ToMaxOfNDigits(int n);


bool Increment(char* number){   // Increase 1 to a char-struct number
    bool isOverflow = false;    // Identify whether the number is out of range
    int nTakeOver = 0;          // Carry bit
    int nLength = strlen(number);

    for (int i=nLength-1; i >= 0; i--){
        int nSum = number[i] - '0' + nTakeOver;

        if (i == nLength-1)
            nSum ++;        // add 1
        
        if (nSum >= 10){
            if (i == 0){
                isOverflow = true;
            }else{
                nTakeOver = 1;
                number[i] = '0';
            }
        }else{
            number[i] = '0' + nSum;
            break;               // This break means the previous number will not be changed
        }
    }
    return isOverflow;
}

void PrintNumber(char * number){
    bool isBeginning0 = true;
    int nLength = strlen(number);
    
    for (int i=0; i<nLength; i++){
        if (isBeginning0 && number[i] != '0')
            isBeginning0 = false;
        
        if (!isBeginning0)
            printf("%c", number[i]);
    }
    printf("\t");
}


void Print1ToMaxOfNDigits(int n){
    if (n <= 0) return;

    char* number = new char[n+1];
    memset(number, '0', n);     // set 0~n-1 char to '0'
    number[n] = '\0';

    while (!Increment(number)){
        PrintNumber(number);
    }
    delete[] number;
}




void Test(int n)
{
    printf("Test for %d begins:\n", n);
    Print1ToMaxOfNDigits(n);
    printf("\nTest for %d ends.\n", n);
}


int main(int argc, char* argv[])
{
    Test(1);
    Test(2);
    Test(3);
    Test(0);
    Test(-1);

    return 0;
}




















