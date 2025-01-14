#include<bits/stdc++.h>

using namespace std;
typedef struct student{
    int a;
    struct student *next;
}student;

int main(){
    student *head=nullptr;
    head = new student;
    head-> a=99;
    head->next = nullptr;
    student *second = new student;
    second-> a = 100;
    second -> next =nullptr;

    cout<<head->a <<endl<<second->a<<endl;
    return 0;
}
