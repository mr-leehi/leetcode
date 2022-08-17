// brute force
// worst case: O(mn),  m = len(haystack), n = len(needle)

int strStr(char * haystack, char * needle){
    char *pat = needle; // pattern
    char *rsu = haystack; // resource
    int cnt = 0;
    int res = 0; // result
    
    if(!needle) return 0;
    while(*(pat+cnt) && *(rsu+cnt)){
        if(*(pat+cnt) == *(rsu+cnt)){
            cnt++;
        }
        else{
            res++;
            rsu++;
            cnt = 0;
        }
    }
    if(!*(pat+cnt)) return res;
    else return -1;
}