#include<stdio.h>
#include<stdint.h>
#include<time.h>
#include<math.h>
#include <cstdlib>
#include<string.h>
char m[100],*m_tmp;
int c[100];
int n,e,len,d;
int gcd(int a,int b){
	if(b==0){
		return a;
	}
	else{
		return gcd(b,a%b);
	}
}
void egcd(int a,int b,int &x,int &y)
{
	if(b==0||a==0){
		x=1;
		y=0;
	}
	else{
	if(a<b){
		egcd(a,b%a,x,y);
		x=(int)(b*y+1)/a;
	}
	else{
		egcd(a%b,b,x,y);
		y=(int)(a*x-1)/b;
	}
	}
}
void RSAInit(){
	int p,q,N,Y;
	int o=1;
	printf("请输入素数p和q：");//需要一个p和q的判断
	while(o){
		scanf("%d %d",&p,&q);
		int k1=sqrt(p);
		int k2=sqrt(q);
		int flag1=1,flag2=1;
		for(int i=2;i<=k1;i++){
			if(p%i==0){
				flag1=0;
				break;
			}
		}
		for(int j=2;j<=k2;j++){
			if(q%j==0){
				flag2=0;
				break;
			}
		}
		if(flag1==1&&flag2==1){
			o=0;
		}
		else{
			printf("p，q不全为素数，请重新输入素数p，q：");
		}
	}
	
	n=p*q;
	N=(p-1)*(q-1);
	
	srand(time(NULL));
	int r;
	
	while(1){
		r=rand();
		if(r<=0||r>=N)
			continue;
		if(gcd(r,N)==1)
			break;
	}
	e=r;
	printf("公钥对PU={e=%d,n=%d}\n",e,n);
	egcd(e,N,d,Y);
	printf("私钥对PR={d=%d,n=%d}\n",d,n);	
}
void En(){
	len=strlen(m);
	printf("密文：\n");
	for(int i=0;i<len;i++){
		int C=1;
		for(int j=0;j<e;j++){
			C=(C*m[i])%n;
		}
		c[i]=C;
		printf("%d ",c[i]);
	}
	printf("\n");
}//加密函数
void De(){
	m_tmp=(char *)malloc(len*sizeof(int));
	printf("明文：\n");
	for(int i=0;i<len;i++){
			int C=1;
			for(int j=0;j<d;j++){
				C=(C*c[i])%n;
			}
			m_tmp[i]=C;
			printf("%c",m_tmp[i]);//缺少ascii转化字符操作
		}	
}//解密函数
int main(){
	printf("请输入明文：");
	gets(m);
	RSAInit();
	En();
	printf("\n");
	De();
	return 0;
}
