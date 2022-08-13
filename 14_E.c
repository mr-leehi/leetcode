char * longestCommonPrefix(char ** strs, int strsSize){
    int minlen = strlen(strs[0]);
    int i, j;
    char *res = strs[0];
    int cnt;
    int end = 0;
    
    for(i = 0; i<strsSize; i++){
        if(strlen(strs[i]) < minlen){
            minlen = strlen(strs[i]);
        }
    }
    //printf("%d", minlen);
    for(i = 0; i<minlen; i++){
        cnt = 0;
        for(j = 0; j<strsSize-1; j++){
            if(strs[j][i] == strs[j+1][i]){
                cnt++;
                continue;
            }
            else break;
        }
        if(cnt == strsSize-1){
            end++;
        }
        else break;
    }
    res[i] = '\0';
    return res;
}