#include <stdio.h>
#include <stdlib.h>

/*红黑树*/

// 红黑树节点结构体
    typedef struct Node
{
    int data;
    struct Node *parent;
    struct Node *left;
    struct Node *right;
    int color; // 0表示黑色，1表示红色
} Node;

// 红黑树结构体
typedef struct RedBlackTree
{
    Node *root;
    Node *nil; // NIL节点，用于代替NULL
} RedBlackTree;

// 创建节点
Node *createNode(int data)
{
    Node *newNode = (Node *)malloc(sizeof(Node));
    if (newNode != NULL)
    {
        newNode->data = data;
        newNode->left = NULL;
        newNode->right = NULL;
        newNode->parent = NULL;
        newNode->color = 1; // 新节点默认为红色
    }
    return newNode;
}

// 初始化红黑树
RedBlackTree *initializeRedBlackTree()
{
    RedBlackTree *tree = (RedBlackTree *)malloc(sizeof(RedBlackTree));
    tree->nil = createNode(-1); // 创建NIL节点
    tree->nil->color = 0;       // NIL节点为黑色
    tree->root = tree->nil;
    return tree;
}

// 左旋
void leftRotate(RedBlackTree *tree, Node *x)
{
    Node *y = x->right;
    x->right = y->left;
    if (y->left != tree->nil)
        y->left->parent = x;
    y->parent = x->parent;
    if (x->parent == tree->nil)
        tree->root = y;
    else if (x == x->parent->left)
        x->parent->left = y;
    else
        x->parent->right = y;
    y->left = x;
    x->parent = y;
}

// 右旋
void rightRotate(RedBlackTree *tree, Node *y)
{
    Node *x = y->left;
    y->left = x->right;
    if (x->right != tree->nil)
        x->right->parent = y;
    x->parent = y->parent;
    if (y->parent == tree->nil)
        tree->root = x;
    else if (y == y->parent->right)
        y->parent->right = x;
    else
        y->parent->left = x;
    x->right = y;
    y->parent = x;
}

// 红黑树插入修正
void insertFixup(RedBlackTree *tree, Node *z)
{
    while (z->parent->color == 1)
    {
        if (z->parent == z->parent->parent->left)
        {
            Node *y = z->parent->parent->right;
            if (y->color == 1)
            {
                z->parent->color = 0;
                y->color = 0;
                z->parent->parent->color = 1;
                z = z->parent->parent;
            }
            else
            {
                if (z == z->parent->right)
                {
                    z = z->parent;
                    leftRotate(tree, z);
                }
                z->parent->color = 0;
                z->parent->parent->color = 1;
                rightRotate(tree, z->parent->parent);
            }
        }
        else
        {
            Node *y = z->parent->parent->left;
            if (y->color == 1)
            {
                z->parent->color = 0;
                y->color = 0;
                z->parent->parent->color = 1;
                z = z->parent->parent;
            }
            else
            {
                if (z == z->parent->left)
                {
                    z = z->parent;
                    rightRotate(tree, z);
                }
                z->parent->color = 0;
                z->parent->parent->color = 1;
                leftRotate(tree, z->parent->parent);
            }
        }
    }
    tree->root->color = 0;
}

// 红黑树插入
void insertNode(RedBlackTree *tree, int data)
{
    Node *z = createNode(data);
    Node *y = tree->nil;
    Node *x = tree->root;
    while (x != tree->nil)
    {
        y = x;
        if (z->data < x->data)
            x = x->left;
        else
            x = x->right;
    }
    z->parent = y;
    if (y == tree->nil)
        tree->root = z;
    else if (z->data < y->data)
        y->left = z;
    else
        y->right = z;
    z->left = tree->nil;
    z->right = tree->nil;
    z->color = 1;
    insertFixup(tree, z);
}

// 中序遍历
void inOrderTraversal(Node *x)
{
    if (x != NULL)
    {
        inOrderTraversal(x->left);
        printf("%d ", x->data);
        inOrderTraversal(x->right);
    }
}

int main()
{
    RedBlackTree *tree = initializeRedBlackTree();

    insertNode(tree, 10);
    insertNode(tree, 20);
    insertNode(tree, 30);
    insertNode(tree, 40);
    insertNode(tree, 50);
    insertNode(tree, 60);

    printf("In-order traversal of the tree: ");
    inOrderTraversal(tree->root);
    printf("\n");

    return 0;
}
