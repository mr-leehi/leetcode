int romanToInt(char * s){
    int num = 0;
    while(*s!=0){
        if(*s == 'I'){   //1
            if(*(s+1) == 'V'){
                num += 4;
                s++;
            }
            else if(*(s+1) == 'X'){
                num += 9;
                s++;
            }
            else{
                num += 1;
            }
        }
        else if(*s == 'V'){  //5
            num += 5;
        }
        else if(*s == 'X'){  //10
            if(*(s+1) == 'L'){
                num += 40;
                s++;
            }
            else if(*(s+1) == 'C'){
                num += 90;
                s++;
            }
            else{
                num += 10;
            }
        }
        else if(*s == 'L'){  //50
            num += 50;
        }
        else if(*s == 'C'){  //100
            if(*(s+1) == 'D'){
                num += 400;
                s++;
            }
            else if(*(s+1) == 'M'){
                num += 900;
                s++;
            }
            else{
                num += 100;
            }
        }
        else if(*s == 'D'){  //500
            num += 500;
        }
        else if(*s == 'M'){  //1000
            num += 1000;
        }
        s++;
    }
    return num;
}