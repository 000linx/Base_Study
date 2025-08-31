#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>

//链表队列
typedef struct Node{
    int data;
    struct Node *next;
}Node;

typedef struct queue{
    Node *front;
    Node *rear;

}queue;

// 初始化队列
void InitQueue(queue *q) {
    q->front = NULL;
    q->rear = NULL;
}

// 判断队列是否为空
bool IsEmpty(queue *q) {
    return q->front == NULL;
}

// 入队
void EnQueue(queue *q, int data) {
    Node *newNode = (Node *)malloc(sizeof(Node));
    newNode->data = data;
    newNode->next = NULL;
    if (IsEmpty(q)) {
        q->front = newNode;
        q->rear = newNode;
    } else {
        q->rear->next = newNode;
        q->rear = newNode;
    }
    printf("入队成功\n");
    printf("入队数据为：%d\n", data);

}

// 出队
void DeQueue(queue *q) {
    if (IsEmpty(q)) {
        printf("队列为空");
        return;
    }
    Node *temp = q->front;
    q->front = temp->next;
    printf("%d", temp->data);
    free(temp);
    printf("出队成功\n");
}


// 打印队列
void PrintQueue(queue *q) {
    if (IsEmpty(q)) {
        printf("队列为空");
        return;
    }
    Node *temp = q->front;
    while (temp != NULL)
    {
        printf("%d", temp->data);
        temp = temp->next;
    }
    
}

// 队列长度
int QueueLength(queue *q) {
    int length = 0;
    Node *temp = q->front;
    while (temp != NULL)
    {
        length++;
        temp = temp->next;
    }
    return length;
}

// 队列头元素
int QueueFront(queue *q) {
    if (IsEmpty(q)) {
        printf("队列为空");
        return -1;
    }
    return q->front->data;
}

// 队列尾元素
int QueueRear(queue *q) {
    if (IsEmpty(q)) {
        printf("队列为空");
        return -1;
    }
    return q->rear->data;
}


int main(){
    queue q;
    InitQueue(&q);
    EnQueue(&q, 1);
    EnQueue(&q, 2);
    EnQueue(&q, 3);
    PrintQueue(&q);
    printf("\n");
    printf("队列长度为：%d\n", QueueLength(&q));
    printf("队列头元素为：%d\n", QueueFront(&q));
    printf("队列尾元素为：%d\n", QueueRear(&q));
    DeQueue(&q);
    DeQueue(&q);
    DeQueue(&q);
    return 0;

}