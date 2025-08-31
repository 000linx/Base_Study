#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

int FindPos(int *arr, int begin, int end){
    int val = arr[begin];
    while(begin < end){
        while (begin < end && arr[end] >= val)
            --end;
        arr[begin] = arr[end];
        while(begin < end && arr[begin] <= val)
            begin++;
        arr[end] = arr[begin];
    }
    arr[begin] = val;
    return end;
}

void QuickSort(int *arr, int begin, int end){
    int pos;
    if(begin < end){
        pos = FindPos(arr, begin, end);
        QuickSort(arr, begin, pos - 1);
        QuickSort(arr, pos + 1, end);   
    }
}
int main(){
    int arr[10] = {1, 5, -5, 10, 6, 7, 9, 4, 2, 0};
    QuickSort(arr, 0, 9);
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", arr[i]);
    }
    return 0;
}
