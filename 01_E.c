int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i,j;
    bool flag = false;
    int* result =(int*) malloc(sizeof(int)*2);
    for(i = 0; i<numsSize; i++){
        for(j = i+1; j<numsSize; j++){
            if((nums[i]+nums[j]) == target){
                result[0] = i;
                result[1] = j;
                flag = true;
                break;
            }
        }
    }
    if(flag) *returnSize = 2;
    else *returnSize = 0;
    return result;
}