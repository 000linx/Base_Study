#include<stdio.h>
int main(){
    int n,count=0;
    scanf("%d",&n);
    for(int a1=1;a1<=3;a1++){
        for(int a2=1;a2<=3;a2++){
            for(int a3=1;a3<=3;a3++){
                for(int a4=1;a4<=3;a4++){
                    for(int a5=1;a5<=3;a5++){
                        for(int a6=1;a6<=3;a6++){
                            for(int a7=1;a7<=3;a7++){
                                for(int a8=1;a8<=3;a8++){
                                    for(int a9=1;a9<=3;a9++){
                                        for(int a10=1;a10<=3;a10++){
                                            if(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10==n){
                                                count++;
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    printf("%d\n",count);
    for(int a1=1;a1<=3;a1++){
        for(int a2=1;a2<=3;a2++){
            for(int a3=1;a3<=3;a3++){
                for(int a4=1;a4<=3;a4++){
                    for(int a5=1;a5<=3;a5++){
                        for(int a6=1;a6<=3;a6++){
                            for(int a7=1;a7<=3;a7++){
                                for(int a8=1;a8<=3;a8++){
                                    for(int a9=1;a9<=3;a9++){
                                        for(int a10=1;a10<=3;a10++){
                                            if(a1+a2+a3+a4+a5+a6+a7+a8+a9+a10==n){
                                                printf("%d",a1);printf(" ");printf("%d",a2);printf(" ");
                                                printf("%d",a3);printf(" ");printf("%d",a4);printf(" ");
                                                printf("%d",a5);printf(" ");printf("%d",a6);printf(" ");
                                                printf("%d",a7);printf(" ");printf("%d",a8);printf(" ");
                                                printf("%d",a9);printf(" ");printf("%d",a10);printf(" ");printf("\n");
                                            }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
        return 0;
    }
