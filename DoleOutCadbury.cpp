#include<bits/stdc++.h>
using namespace std;



int square(int a,int b){

    if(b == 1)
       return a;
    if(a==b)
       return 1;
    int p = a-b;
    return 1+ square(max(a-b,b),min(a-b,b));
}

int main(){

	int P; //min length
	int Q; //max length
	int R; //min widthh
	int S; //max width
	cin>>P>>Q>>R>>S;
	int count;
	for(int i =P; i<=Q; i++){
		for(int j = R; j<= S; j++){
			count += square(max(i,j), min(i,j));
		}
	}

	cout<<count;

	return 0;
}
