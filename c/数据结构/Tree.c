#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct Binary_TreeNode{
    int data;
    struct Binary_TreeNode *left;
    struct Binary_TreeNode *right;
}TreeNode;

 TreeNode *CreatTree(TreeNode *root, int val){
    //判断当前节点是否为空
    if(root == NULL){
        root = (TreeNode *)malloc(sizeof(TreeNode));
        root->data = val;
        return root;
    }

    //如果不为空就进行判断，比根节点小的放左边，比根节点大的放右边
    if(root->data > val){
        root->left = CreatTree(root->left, val);
    }else if(root->data < val){
        root->right = CreatTree(root->right, val);
    }

    return root;
 }

int main(){
    
    return 0;
}