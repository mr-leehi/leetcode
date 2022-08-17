

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* plusOne(int* digits, int digitsSize, int* returnSize){
    int i;
    bool cout = false; // carry out
    int *result = (int*)malloc(sizeof(int)*(digitsSize+1));
    
    result[digitsSize] = digits[digitsSize-1] + 1;
    if(result[digitsSize] > 9){
        cout = true;
        result[digitsSize] -= digits[digitsSize-1]+1;
    }
    if(digitsSize == 1){
        if(cout){
            result[0] = 1;
            *returnSize = 2;
        }
        else{
            *returnSize = 1;
            result[0] = result[1];
        }
        return result;
    }
    
    for(i=digitsSize-2; i>=0; i--){
        if(cout){
            digits[i]++;
            result[i+1] = digits[i];
            cout = false;
        }
        if(result[i+1] > 9){
            cout = true;
            result[i+1] -= digits[i];
            // printf("%d\n", result[i+1]);
        }
        else result[i+1] = digits[i];
    }
    if(cout){
        result[0] = 1;
        *returnSize = digitsSize+1;
    }
    else{
        for(i=1; i<digitsSize+1; i++){
            result[i-1] = result[i];
        }
        *returnSize = digitsSize;
    }
    
    return result;
}