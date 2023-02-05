// 參考網路上演算法 https://www.issacc.com/implement-a-square-root-function/

int mySqrt(int x){
    if(x==0 || x==1) return x;
    
    int start = 1;
    int end = x;
    
    while(start+1 < end){
        int mid = start + (end - start)/2;
        
        if(mid == x/mid) return mid;
        else if(mid > x/mid) end = mid;
        else start = mid;
    }
    
    return start;
}