bool isValid(char * s){
    char buffer[5000];
    int top = 0;
    char tmp;
    while(*s){
        switch(*s){
            case '(':
                buffer[top++] = *s;
                break;
            case ')':
                if(top <= 0) return false;
                else{
                    tmp = buffer[--top];
                    if(tmp != '(') return false;
                }
                break;
            case '{':
                buffer[top++] = *s;
                break;
            case '}':
                if(top <= 0) return false;
                else{
                    tmp = buffer[--top];
                    if(tmp != '{') return false;
                }
                break;
             case '[':
                buffer[top++] = *s;
                break;
            case ']':
                if(top <= 0) return false;
                else{
                    tmp = buffer[--top];
                    if(tmp != '[') return false;
                }
                break;
        }
        s++;
    }
    if(top == 0) return true;
    else return false;
}