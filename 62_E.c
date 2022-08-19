

int uniquePaths(int m, int n){
    int result = 1;
    int i, j;
    int Max, min;
    
    if(m > n){
        Max = m-1;
        min = n-1;
    }
    else{
        Max = n-1;
        min = m-1;
    }
    
    if(min == 0) return 1;
    
    int top[m+n-Max-2];
    int bottom[min];
    
    for(i=0; i<(m+n-Max-2); i++) top[i] = Max+min-i;
    for(i=0; i<min; i++) bottom[i] = min-i;
    
    for(i=0; i<min; i++){
        for(j=0; j<(m+n-Max-2); j++){
            if((top[j] % bottom[i]) == 0){
                top[j] /= bottom[i];
                bottom[i] = 1;
                break;
            }
        }
        if(j == (m+n-Max-2)){
            for(j=0; j<(m+n-Max-2); j++){
                if((bottom[i] % top[j]) == 0){
                    bottom[i] /= top[j];
                    top[j] = 1;
                }
                if(bottom[i] == 1) break;
            }
            if(bottom[i] != 1) i--;
        }
    }
    
    for(i=0; i<(m+n-Max-2); i++) result *= top[i];
    
    return result;
}