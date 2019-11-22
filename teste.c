#include <stdio.h>



#include <stdlib.h>

#include <math.h>

char *combi(int n);

int imprimeini(char * vetor,int d,int ni,int nj);

int imprime(char * vetor,int d,int ni,int nj);

int ler(char*vetor);

char *uniao(char *coluna, char *princ, int i,int j,int ni,int d, int nj);

int main(){

int a;

char *vetor,o;



printf("-----------------------------------------------------\n");

printf("| Programa em linguagem C para transformacao de:    |\n");

printf("|                AFND para AFD                      |\n");

printf("-----------------------------------------------------\n");

printf("-----------------------------------------------------\n");

printf("| Kassio Romulo  -  Alan Moraes  - Nubia Cristine   |\n");

printf("|  cp09126-81        cp09121-76     cp09142-81      |\n");

printf("-----------------------------------------------------\n");

o=getchar();

system("cls");

a=ler(vetor);

system("pause");

}

int imprimeini(char * vetor,int d,int ni,int nj){

char tr='a',*matriz;

int z,k,p,l;

for(z=0; z<nj; z++) {

printf("         %c  ",tr);

tr++;

}

printf("\n");

for(z=0; z<d; z++) {

if(z<10)printf("q(0%d) | ",z);

else printf("q(%d) | ",z);

for(k=0; k<nj; k++){

printf("        |");

}

printf("\n");

}

printf("\n");

return 1;

}

//-----------------------------------------------------------------------------------------------------------------------------------------

int imprime(char * vetor,int d,int ni,int nj){

char tr='a';

int z,k,p,l;

for(z=0; z<nj; z++) {

printf("         %c  ",tr);

tr++;

}

printf("\n");

for(z=0; z<d; z++) {

if(z<10)printf("q(0%d) | ",z);

else printf("q(%d) | ",z);

for(k=0; k<nj; k++){

for(l=0;l<ni;l++){

//if(z<ni){                

p=l*d*nj+z*nj+k;

printf ("%c",vetor[p]);

}

printf("     |");

}

printf("\n");

}

printf("\n");

return 1;

}

//-----------------------------------------------------------------------------------------------------------------------------------------

int ler(char*vetor){

char *aux;

int a,ni,nj,d,j,i,k,l;

char es='a',str[2];

printf("possui quantas letras: \t\n");

scanf("%d",&nj);

printf("possui quantos estados:(no maximo 4): \t");

scanf("%d",&ni);



gets(str);

d=pow(2,ni)-1;



vetor=(char*)malloc(d*nj*ni*sizeof(char));

if(vetor!=NULL){

a=imprimeini(vetor,d,ni,nj);

for(i=0;i<ni;i++){

for(j=0;j<nj;j++){

printf("digite o estado final ou '-' para vazio(q%d)->",i);       

printf("%c\n",es);

es++;

for(l=0;l<ni;l++){      

k=l*d*nj+i*nj+j;

scanf("%c",&vetor[k]);       

gets(str);

}

}

es='a';

}

}

a=imprime(vetor,d,ni,nj);

aux=combi(ni);

for(i=0;i<d;i++){

for(j=0;j<ni;j++){

k=i*ni+j;

printf("%c",aux[k]);        

}

printf ("\n");

}

a=processamento(vetor,aux,ni,nj );

a=imprime(vetor,d,ni,nj);

}//------------------------------

char *combi(int n) {

char *v;

int i,d, j,x, k,l,m,t ;

int p;

char b[4] = {'0','1','2','3'}; /* elementos a serem combinados */



d=pow(2,n)-1;

//d--;

v=(char*)malloc(d*n*sizeof(char));

if(v!=NULL){

//  1 combinação



printf("Aguarde...\n\n");

for (i=0; i<n; i++){

x=i*n+0;

v[x]=b[i];v[x+1]='-';v[x+2]='-';v[x+3]='-';v[x+4]='-';v[x+5]='-';

}

//-----------------------------------

//  2 combinação

p=n;



for (i=0; i<n; i++){

for (j=(i+1); j<n; j++){

x=p*n+0;

v[x]=b[i];v[x+1]=b[j];v[x+2]='-';v[x+3]='-';v[x+4]='-';v[x+5]='-';



p++;

}

}

//-----------------------------------

//  3 combinação

if(n>3)p=2*n+2;

else p=2*n;

for (i=0; i<n; i++){

for (j=(i+1); j<n; j++){

for (k=(j+1); k<n;k++){

x=p*n+0;

v[x]=b[i];v[x+1]=b[j];v[x+2]=b[k];v[x+3]='-';v[x+4]='-';v[x+5]='-';

p++;

}

}

}

//------------------------------------

//  4 combinação

p=3*n+2;

for (i=0; i<n; i++){

for (j=(i+1); j<(n); j++){

for (k=(j+1); k<n;k++){

for (l=(k+1); l<n;l++){

x=p*n+0;

v[x]=b[i];v[x+1]=b[j];v[x+2]=b[k];v[x+3]=b[l];v[x+4]='-';v[x+5]='-';

p++;

}

}

}

}

return v;

}//fim do null

return NULL;

}

//----------------------------------------------------------------------------------------------------------------------------------------

int processamento(char *princ,char *coluna,int ni,int nj ){

int l,i,j,d,k,p,*cont;

char *a,*b;

system("cls");

cont=(int*)malloc(ni*sizeof(int));

a=(char*)malloc(ni*sizeof(char));

if(cont!=NULL && a!=NULL ){

d=pow(2,ni)-1;

for(i=ni;i<d;i++){



for(j=0;j<nj;j++){ 

a=uniao(coluna,princ,i,j,ni,d,nj);

for(l=0;l<ni;l++){

k=l*d*nj+i*nj+j;           

princ[k]=a[l];

}

}

}

return 1;

}

//return NULL;

}

char *uniao(char *coluna, char *princ, int i,int j,int ni,int d, int nj){

char *aux1,*b;

int contador,inteiro,e,k,l,x=0,p=0,flag=0;

aux1=(char*)malloc(2*ni*sizeof(char));

b=(char*)malloc(ni*sizeof(char));

if(aux1!=NULL)

{    

for(e=0;e<ni;e++){

k=i*ni+e;



if(coluna[k]!='-'){        

contador=coluna[k]-48;//contador recebe o indice da uniao



for(l=0;l<ni;l++){

k=l*d*nj+contador*nj+j;

aux1[x]=princ[k];

x++;

}

}

}

//----------------------------------------------------------------------------

for(i=0;i<ni;i++){//completa com - o vetor

b[i]='-';

}      

for(i=0;i<=2*ni;i++){

if(i==0){

b[p]=aux1[i];

p++;

}

if(i==2*ni+1){

b[p]='-';

p++;

}else{

for(j=0;j<p;j++){

inteiro=aux1[i];

if(aux1[i]!='-' && aux1[i]!=b[j] && inteiro > 44 && inteiro < 58 && inteiro != 46 && inteiro != 47){

flag=1;

}

else

flag=0;

}

if(flag==1){

b[p]=aux1[i];

p++;    

}

}

}

return b;      

}

return NULL;                    

} 