#include<stdio.h>
#include<stdlib.h>

//构建二叉树结点
typedef struct Node{
    int data;
    struct Node *left;
    struct Node *right;
}node;

//前序遍历
void pre_order(node *root) {
    if(root == NULL){
        return;
    }
    printf("%d", root->data);
    pre_order(root->left);
    pre_order(root->right);
}

//中序遍历
void in_order(node *root) {
    if(root == NULL){
        return;
    }
    in_order(root->left);
    printf("%d", root->data);
    in_order(root->right);

}

//后序遍历
void post_order(node *root) {
    if(root == NULL){
        return;
    }
    post_order(root->left);
    post_order(root->right);
    printf("%d", root->data);
}

//层序遍历
void level_order(node *root) {
    if(root == NULL){
        return;
    }
    //创建队列
    node *queue[100];
    int front = 0;
    int rear = 0;
    //让根节点入队
    queue[rear++] = root;
    //进行遍历
    while (front < rear)
    {
        node *temp = queue[front++];
        printf("%d", temp->data);
        if (temp->left != NULL)
        {
            queue[rear++] = temp->left;
        }
        if (temp->right != NULL)
        {
            queue[rear++] = temp->right;
        }
    }
    printf("\n");  
}

// 计算二叉树的高度
int height(node *root) {
    if(root == NULL){
        return 0;
    }
    int left_height = height(root->left);
    int right_height = height(root->right);
    return left_height > right_height ? left_height + 1 : right_height + 1;
}

// 计算二叉树的节点数
int count(node *root) {
    if(root == NULL){
        return 0;
    }
    int left_count = count(root->left);
    int right_count = count(root->right);
    return left_count + right_count + 1;
}

// 计算二叉树的叶子数
int leaf_count(node *root) {
    if (root == NULL) {
        return 0;
    }
    if (root->left == NULL && root->right ==NULL) {
        return 1;
    }
    int left_leaf_count = leaf_count(root->left);
    int right_leaf_count = leaf_count(root->right);
    return left_leaf_count + right_leaf_count;

}

int main() {

    //创建根节点
    node *root = (node * )malloc(sizeof(node));
    root->data = 1;
    root->left = NULL;
    root->right = NULL;

    //创建左子节点
    node *left = (node * )malloc(sizeof(node));
    left->data = 2;
    left->left = NULL;
    left->right = NULL;
    root->left = left;
    
    //创建右子节点
    node *right = (node * )malloc(sizeof(node));
    right->data = 3;
    right->left = NULL;
    right->right = NULL;
    root->right = right;

    //前序遍历
    pre_order(root);
    printf("\n");
    //中序遍历
    in_order(root);
    printf("\n");
    //后序遍历
    post_order(root);
    printf("\n");
    //层序遍历
    level_order(root);
    //计算二叉树的高度
    int h = height(root);
    printf("二叉树的高度为：%d\n", h);
    //计算二叉树的节点数
    int c = count(root);
    printf("二叉树的节点数为：%d\n", c);
    //计算二叉树的叶子数
    int l = leaf_count(root);
    printf("二叉树的叶子数为：%d\n", l);

    return 0;
}


