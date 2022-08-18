

int maxArea(int* height, int heightSize){
    int maxArea = 0;
    int tmp = 0;
    int i=0, j=heightSize-1;
    
    while(j>i){
        if(height[i] <= height[j]){
            tmp = height[i]*(j-i);
            if(tmp > maxArea) maxArea = tmp;
            i++;
        }
        else{
            tmp = height[j]*(j-i);
            if(tmp > maxArea) maxArea = tmp;
            j--;
        }
    }
    
    return maxArea;
}