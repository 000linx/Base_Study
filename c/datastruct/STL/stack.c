#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/*栈*/
/*
定义：一种可以实现“先进后出”的存储结构
分类：
    静态栈
    动态栈
算法：
    出栈
    入栈
    单调栈
*/

typedef struct StackNode{
    int data;
    struct StackNode *next;
}Node;

typedef struct Stack{
    //分别指向栈的顶部和底部
    Node *Top;
    Node *Bottom;//它是最后一个有效元素的下一个节点，没有实际含义，是为了方便操作栈而构造的
}Stack;

void initStack(Stack *stack){
    stack->Top = (Node *)malloc(sizeof(Node));
    if(stack->Top == NULL){
        printf("分配内存失败");
    }
    stack->Bottom = stack->Top;
    stack->Top->next = NULL;
}

bool is_empty(Stack *stack){
    if(stack->Top != stack->Bottom)
    {
        return false;
    }
    else
        return true;
}

void Push(Stack *stack, int val){
    Node *node = (Node *)malloc(sizeof(Node));
    node->data = val;
    node->next = stack->Top ;
    stack->Top = node;
    return;
}

bool Pop(Stack *stack){
    if(is_empty(stack)){
        printf("出栈失败\n");
        return false;
    }
    else{ 
        Node *node = stack->Top;
        stack->Top = stack->Top->next;
        free(node);
        node = NULL;
        return true;
    }
}

Node *Top(Stack *stack){
    return stack->Top;
}

void traverse_stack(Stack *stack){
    Node *p = stack->Top;
    while(p != stack->Bottom){
        printf("%d ", p->data);
        p = p->next;
    }
    return;
}

int size_stack(Stack *stack){
    Node *p = stack->Top;
    int cnt = 0;
    while(p->next != NULL){
        cnt++;
        p = p->next;
    }
    return cnt;
}

void Clear(Stack *stack){
    while(stack->Top != stack->Bottom){
        Node *node = stack->Top;
        stack->Top = stack->Top->next;
        free(node);
    }
    return;
}
int main(){
    Stack stack;
    initStack(&stack);
    if(is_empty(&stack)){
        printf("栈空\n");
    }
    printf("栈中元素个数为:%d\n", size_stack(&stack));
    Push(&stack, 1);
    Push(&stack, 5);
    Push(&stack, 6);
    Push(&stack, 2);
    Push(&stack, -1);
    Push(&stack, 10);
    printf("栈中元素个数为:%d\n", size_stack(&stack));
    printf("栈顶元素为:%d\n", Top(&stack)->data);
    traverse_stack(&stack);
    Pop(&stack);
    printf("\n");
    traverse_stack(&stack);
    printf("\n");
    Clear(&stack);
    printf("栈中元素个数为:%d\n", size_stack(&stack));
}