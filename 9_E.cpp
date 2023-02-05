// 難在將int轉成char

class Solution {
public:
    bool isPalindrome(int x) {
        char const *start;
        char const *end;

        string word = to_string(x);
        start = word.c_str();
        end = start + strlen(start)-1;

        while(start < end){
            if(*start != *end) return false;
            else{
                start++;
                end--;
            }
        }
        return true;
    }
};