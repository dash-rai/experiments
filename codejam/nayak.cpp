#include <iostream>
using namespace std;
long double counter=0;
int checker(int x,int y,int ex,int ey)
{
	if(x>ex||y>ey)
		return 1;
	else if(x==ex &&y==ey)
		counter++;
	checker(x+1,y,ex,ey);
	checker(x,y+1,ex,ey);
	return 1;
}
int main(int argc, char *argv[])
{
    int startx=1,starty=1,finishx,finishy;
	cout<<"enter total variable of the squre matrix"<<endl;
	cin>>finishx;
	finishy=finishx;
	checker(startx,starty,finishx,finishy);
	cout<<"The Value is "<<counter<<endl;
    return 0;
}
