#include<bits/stdc++.h>
#define llt long long
using namespace std;

struct pint
{
	int x,y;
} a[100010];
set<int> S;
int n,m,num,ans;

bool cmp(pint p,pint q){return p.x==q.x?p.y<q.y:p.x<q.x;}

int main()
{
    printf("runiing");
	cin.tie(0);
	ios::sync_with_stdio(false);
	cin>>n>>m>>num;
	for(int p,q,i=1;i<=num;i++)
	{
		cin>>p>>q;
		a[i]={p,q};
	}
	
	sort(a+1,a+num+1,cmp);
	S.insert(0); S.insert(m+1);
	for(int i=1;i<=num;i++)
	{
		auto it = S.lower_bound(a[i].y+1);
		it--;
		if(*it==0)
		{
			ans++;
			S.insert(a[i].y);
		}
		else
		{
			S.erase(it);
			S.insert(a[i].y);
		}
	}
	cout<<ans;
}