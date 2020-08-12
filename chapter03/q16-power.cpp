

/* 剑指Offer P129
 * 题目：实现函数 doublePower（doublebase，intexponent），求 base 的 exponent 次方。不得使用库函数，同时不需要考虑大数问题。
 * 要考虑exponent是负数的情况
 */

#include <iostream>
#include <cmath>

bool g_InvalidInput = false;
bool equal(double num1, double num2);
double Power(double base, int exponent);
double PowerWithUnsignedExpoent(double base, unsigned int expoent);


double Power(double base, int exponent){
    g_InvalidInput = false;
    if (equal(base, 0.0) && exponent < 0){
        g_InvalidInput = true;
        return 0.0;
    }

    unsigned int absExponent = (unsigned int) (exponent);
    if (exponent < 0)
        absExponent = (unsigned int) (-exponent);
    
    double result = PowerWithUnsignedExpoent(base, absExponent);
    if (exponent < 0)
        result = 1.0 / result;
    return result;
}


double PowerWithUnsignedExpoent(double base, unsigned int expoent){
    // Recursive, high efficient
    // if (expoent == 0)   return 1;
    // if (expoent == 1)   return base;

    // double result = PowerWithUnsignedExpoent(base, expoent >> 1);
    // result *= result;
    // if ((expoent & 0x1) == 1)        // odd/even
    //     result *= base;
    // return result;

    // Iterative, low efficient
    double result = 1.0;
    for (int i=0; i < expoent; i++){
        result *= base;        
    }
    // printf("%f\n", result);
    return result;
}


bool equal(double num1, double num2){
    if ((num1-num2 > -0.0000001) && (num1-num2 < 0.0000001))
        return true;
    else
        return false;
}

void Test(const char* testName, double base, int exponent, double expectedResult, bool expectedFlag){
    double result = Power(base, exponent);
    if (equal(result, expectedResult) && g_InvalidInput == expectedFlag){
        std::cout << testName << " passed" << std::endl;
    }else{
        std::cout << testName << " FAILED" << std::endl;
    }
}




int main(int argc, char* argv[])
{
    Test("Test1", 2, 3, 8, false);
    Test("Test2", -2, 3, -8, false);
    Test("Test3", 2, -3, 0.125, false);
    Test("Test4", 2, 0, 1, false);
    Test("Test5", 0, 0, 1, false);
    Test("Test6", 0, 4, 0, false);
    Test("Test7", 0, -4, 0, true);

    return 0;
}





