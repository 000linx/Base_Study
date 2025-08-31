#include <stdio.h>
#include <stdlib.h>
#include <string.h>

//哈夫曼树以及哈夫曼编码
typedef struct Huffman
{
    int weight;
    int parent;
    int lchild;
    int rchild;
}HuffmanTree;


int main(){

    HuffmanTree tree[100];
    int n;
    scanf("%d",&n);
    //初始化哈夫曼树
    for(int i = 0; i < n; i++){
        //初始化哈夫曼树的权值

        scanf("%d",&tree[i].weight);
    }
    int m = 2 * n - 1;
    //初始化哈夫曼树的父节点，左子节点，右子节点
    for (int i = n; i < m; i++){
        tree[i].weight = 0;
        tree[i].parent = 0;
        tree[i].lchild = 0;
        tree[i].rchild = 0;
    }
    //创建哈夫曼树
    for (int i = 0; i < n - 1; i++) {
        int min1 = 0, min2 = 0;
        for (int j = 0; j < n + i; j++) {
            //找到权值最小的两个节点
            if (tree[j].weight != 0 && tree[j].parent == 0) {
                if (tree[j].weight < tree[min1].weight){
                    min2 = min1;
                    min1 = j;
                }
                else if (tree[j].weight < tree[min2].weight){
                    min2 = j;
                }
            }
            else{
                continue;
            }
        }
        //创建新节点

        tree[n + i].weight = tree[min1].weight + tree[min2].weight;
        tree[n + i].parent = 0;
        tree[n + i].lchild = min1;
        tree[n + i].rchild = min2;
        tree[min1].parent = n + i;
        tree[min2].parent = n + i;
    }
    for (int i = 0; i < m; i++) {
        if (tree[i].parent == 0) {
            printf("%d ", tree[i].weight);
        }
    }
    printf("\n");
    for (int i = 0; i < m; i++) {
        if (tree[i].parent != 0) {
            printf("%d %d %d\n", tree[i].parent, tree[i].lchild, tree[i].rchild);
        }
    }



    return 0;
}


