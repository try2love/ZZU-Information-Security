#include<stdio.h>
#include<string.h>
#include <stdlib.h>
 
const int max=2e4;
int size;
int miwen[max];//为加密后的数字密文
char mingwen[max]; 
 
//判断两个数是否互为素数  eg:p和q e和 t 
bool gcd(int p,int q)
{
	int m,n;
	if(q<p)
	{
		m=p;  p=q;  q=m;  //将p换成p和q之间那个小的数 
		m=q%p;  n=q/p;  //辗转相除法求两个数的最大公因数 
	}
	while(m!=0)
	{
		q=p; p=m;  //将p换成p和q之间那个小的数
		m=q%p;  n=q/p;		
	} 
	if(m==0&&n==q)
	{
		printf("符合条件！\n");
			return true;
	}
	else{
		printf("不符合条件！请重新输入：\n");
	    	return false;
	}
} 
//判断输入的p和q是不是素数 
bool sushu(int s){
	for(int i=2;i<s;i++){
		if(s%i==0) 
		return false;
	}
	return true;
}
//求私钥d
int siyao(int e,int t)  //t:欧拉函数 
{
	int d;
	for(d=0;d<t;d++)
	    if(e * d % t==1)
	       return d;
}
//随机生成与 t互质的数e
int getrand(int p,int q)
{
	int t=(p-1)*(q-1);
	while(1)
	{
		int e=rand() % t;
		if(gcd(e,t)==1)
		return e;
	//	if(e<=2)
	//	e=3;
	}
}
void jiami(int e,int n) 
{
	//先将符号明文转换成字母所对应的ascii码。 
	char mingwen[100];    //符号明文 
	printf("请输入明文：\n");
	scanf("%s",mingwen);
	size=strlen(mingwen);
	int ming[strlen(mingwen)];   //定义符号明文 
	for(int i=0;i<strlen(mingwen);i++)
	{
	   ming[i]=mingwen[i];        //将字母转换成对应的ascii码。 
	//printf("%d",mingwen[i]);  //将字母转换成对应的ascii码。可以不输出 
	} 
	int flag=1;    //miwen为加密后的数字密文 
	for(int i=0;i<strlen(mingwen);i++)
	{
	    for(int j=0;j<e;j++)
		{
		    flag=flag*ming[i]%n; 
	    }
	    miwen[i]=flag; 
	    flag=1;
	} 
	printf("加密密文为：\n");
	for(int i=0;i<strlen(mingwen);i++) 
	printf("%d",miwen[i]); 
}
void jiemi(int d,int n)
{
	int de_mingwen[size],flag=1;//解密后得到的数字明文（即ascii码） 
	char de_ming[size];//解密后得到的字符串明文 
	for(int i=0;i<size;i++)
	{
	   for(int j=0;j<d;j++)
	   {
	   	  flag=flag*miwen[i]%n;
	   }
	   de_mingwen[i]=flag; 
	   flag=1;
	} 
	printf("解密后的明文为：\n");
	for(int i=0;i<size;i++)
	{
		de_ming[i]=de_mingwen[i];
		printf("%c",de_ming[i]);
	}
}
int main()
{
	int p,q,e,d,n,t,tep;
	while(1)
	{
		printf("请输入p:",p);
		scanf("%d",&p);
		tep=sushu(p);
		if(tep==0)
		{
			printf("p不是素数，请重新输入p！\n");
		    continue;
		} 
		printf("请输入q:",q);
		scanf("%d",&q);
	    tep=sushu(q);
	    if(tep==0)
		{
		printf("q不是素数，请重新输入q！\n");
		printf("请输入q:",q);
		scanf("%d",&q);
		tep=sushu(q);
		}
		int n=p*q;
		int t=(p-1)*(q-1);
		tep=gcd(p,q);
		if(tep==0)   continue;
		printf("t=(q-1)*(p-1)=%d\n",t);
		e=getrand(p,q);
		printf("公钥(e=%d n=%d)\n",e,n);
		tep=(e,t);
		d=siyao(e,t);
		printf("私钥d=%d",d);
		int a=0;
		while(a!=3)
		{
			printf("\n-------------------------\n");
			printf("1、加密\n");
	        printf("2、解密\n");
	        printf("3、退出");
	        printf("\n-------------------------\n");
	        scanf("%d",&a);
	        getchar();
	        if(a==1)
	        {
	        	jiami(e,n);
	        }
	        else if(a==2)
	        {
	        	printf("请输入密钥：");
		        scanf("%d",&d);
		        jiemi(d,n);
	        }
	        else 
			     return 0;
		}		
    }
    return 0;
}
