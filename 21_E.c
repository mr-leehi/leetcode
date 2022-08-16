/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// 解題方向為讓list2接到list1上

struct ListNode* mergeTwoLists(struct ListNode* list1, struct ListNode* list2){
    struct ListNode* head;
    struct ListNode* tmp;
    struct ListNode* prev = NULL;
    
    if(list1 && list2 && list1->val > list2->val) head = list2;
    else if(list1 && list2) head = list1;
    else if(list1) return list1;
    else return list2;
    
    while(list1 && list2){
        if(list1->val <= list2->val){
            prev = list1;
            list1 = list1->next;
        }
        else{
            if(prev){
                tmp = list2;
                list2 = list2->next;
                prev->next = tmp;
                tmp->next = list1;
                prev = tmp;
            }
            else{
                tmp = list2;
                list2 = list2->next;
                tmp->next = list1;
                prev = tmp;
            }
        }
    }
    if(list2) prev->next = list2;
    
    return head;
}