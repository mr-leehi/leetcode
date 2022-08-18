// dynamic programming

int climbStairs(int n){
    int cnt[n];
    int i;
    
    if(n < 2) return n;
    cnt[0] = 1;
    cnt[1] = 2;
    for(i=2; i<n; i++) cnt[i] = cnt[i-1]+cnt[i-2];
    
    return cnt[n-1];
}