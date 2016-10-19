#include<stdio.h>
#include<assert.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
int main(int argc, const char *argv[])
{
    if (argc != 2)
 {
    fprint(stderr,"bad number of arguments\n2 number of arguments are required\n");
    exit(1);    
 }
    FILE* fin;
    fin = fopen(*(argv+1),"r");
    int points[100][4];
    int i;
    char contin=0;
    int a,b;
    for (i=0;i<100;i++)
    fscanf(fin,"%d%d%d%d%d",points[i]+0,points[i]+1,points[i]+2,points[i]+3);
    while(!contin)
 {
    fprintf(stdout,"please enter any two indices?");
    fscanf(stdin,"%d%d",&a,&b);
    fprintf(stdout,"point %d %d %d %d\n",a,points[a][0],
                                           points[a][1],
                                           points[a][2],
                                           points[a][3]);
    fprintf(stdout,"point %d %d %d %d\n",b,points[b][0],
                                           points[b][1],
                                           points[b][2],
                                           points[b][3]);
    int *t=points[a],*q=points[b];
    fprintf(stdout,"answer=%lf\n",sqrt(pow(*t++-*q++,2)+
                                       pow(*t++-*q++,2)+
                                       pow(*t++-*q++,2)+
                                       pow(*t++-*q++,2)));
    fprintf(stdout,"do you wish to continue?(y)");
    fscanf(stdin,"%c%c",&contin,&contin);
    contin-='y';
 }
return 0;
}
                                                                          
                                                                                
    
    
