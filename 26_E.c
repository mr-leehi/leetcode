

int removeDuplicates(int* nums, int numsSize){
    int tmp;
    int idx = 0;
    int i;
    
    tmp = nums[0];
    for(i = 1; i<numsSize; i++){
        if(tmp != nums[i]){
            nums[++idx] = nums[i];
            tmp = nums[i];
        }
    }
    
    return idx+1;
}