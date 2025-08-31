#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>


//队列
/*
    队列：
        先进先出
        队头：队头出队
        队尾：队尾入队
    队列的实现：
        数组实现
        链表实现
*/

//队列数组实现
typedef struct queue
{
    int data[100];
    int front;
    int rear;
}queue;

//初始化
void InitQueue(queue *q) {
    q->front = 0;
    q->rear = 0;
}

//判断队列是否为空
bool IsEmpty(queue *q) {
    if(q->front == q->rear)
    {
        return true;
    }
    else
        return false;
}

//入队
void EnQueue(queue *q, int x) {
    if(q->rear == 100)
    {
        printf("队列已满");
        return;
    }
    q->data[q->rear] = x;
    q->rear++;
}

//出队
void DeQueue(queue *q) {
    q->front++;
    if(q->front == 100)
    {
        printf("队列已空");
        return;
    }
}

//获取队头元素
int GetFront(queue *q) {
    return q->data[q->front];
}

//获取队尾元素
int GetRear(queue *q) {
    return q->data[q->rear-1];
}

//获取队列长度
int GetLength(queue *q) {
    return q->rear - q->front;
}


int main() {
    
    queue q;
    InitQueue(&q);
    EnQueue(&q, 1);
    EnQueue(&q, 2);
    EnQueue(&q, 3);
    EnQueue(&q, 4);
    EnQueue(&q, 5);
    printf("%d", GetFront(&q));
    printf("%d", GetRear(&q));
    printf("%d", GetLength(&q));
    DeQueue(&q);
    printf("%d", GetFront(&q));

    return 0;
}