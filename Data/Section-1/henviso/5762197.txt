#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <cstdlib>
#include <stack>
#include <algorithm>
#include <cctype>
#include <vector>
#include <queue>
#include <tr1/unordered_map>
#include <cmath>
#include <map>
#include <bitset>
#include <set>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef pair<int,int> ii;
///////////////////////////////UTIL/////////////////////////////////
#define ALL(x) (x).begin(),x.end()
#define CLEAR0(v) memset(v, 0, sizeof(v))
#define CLEAR(v, x) memset(v, x, sizeof(v))
#define INRANGE0(x, n) ((x) > -1 && (x) < n)
#define INRANGE(x, a, b) ((x) >= a && (x) <= b)
#define COPY(a, b) memcpy(a, b, sizeof(a))
#define CMP(a, b) memcmp(a, b, sizeof(a))
#define REP(i,n) for(int i = 0; i<n; i++)
#define REPP(i,a,n) for(int i = a; i<n; i++)
#define REPD(i,n) for(int i = n-1; i>-1; i--)
#define REPDP(i,a,n) for(int i = n-1; i>=a; i--)
#define pb push_back
#define pf push_front
#define sz size()
#define mp make_pair
/////////////////////////////NUMERICAL//////////////////////////////
#define INCMOD(a,b,c) (((a)+b)%c)
#define DECMOD(a,b,c) (((a)+c-b)%c)
#define ROUNDINT(a) (int)((double)(a) + 0.5)
#define INF 0x3f3f3f3f
#define EPS 1e-9
/////////////////////////////BITWISE////////////////////////////////
#define CHECK(S, j) (S & (1 << j))
#define CHECKFIRST(S) (S & (-S))  //PRECISA DE UMA TABELA PARA TRANSFORMAR EM INDICE
#define SET(S, j) S |= (1 << j)
#define SETALL(S, j) S = (1 << j)-1  //J PRIMEIROS
#define UNSET(S, j) S &= ~(1 << j)
#define TOOGLE(S, j) S ^= (1 << j)
///////////////////////////////64 BITS//////////////////////////////
#define LCHECK(S, j) (S & (1ULL << j))
#define LSET(S, j) S |= (1ULL << j)
#define LSETALL(S, j) S = (1ULL << j)-1ULL  //J PRIMEIROS
#define LUNSET(S, j) S &= ~(1ULL << j)
#define LTOOGLE(S, j) S ^= (1ULL << j)
//scanf(" %d ", &t);

int n, m;

int main(){
	scanf(" %d %d ", &n, &m);
	int row, col;
	set<int> rocked;
	ii ent[100010];
	REP(i, m) scanf(" %d %d ", &ent[i].first, &ent[i].second);
	sort(ent, ent+m);
	vector< ii > r[2]; r[0].push_back(ii(1, n));
	int act = 1, lst = 0;
	int ult = 0, pos = 0;
	while(pos < m){
		int i = ent[pos].first;
		//cout << " I EH " << i << endl;
		//REP(i, r[lst].size()) cout << "(" << r[lst][i].first << "," << r[lst][i].second << ") ";
		//cout << endl;
		
		r[act].clear();
		if(i-ult > 1){ 
			int aux = (r[lst][0]).first; 
			r[lst].clear(); 
			r[lst].push_back(ii(aux, n)); 
		}
		
		
		int lo = 0, rock;
		while(ent[pos].first == i){
			rock = ent[pos].second;
			int p = lower_bound(r[lst].begin(), r[lst].end(), ii(rock+1, -INF)) - r[lst].begin();
			//cout << "ROCK EH " << rock << " P EH " << p << endl;
			if(p != lo){
				if(r[lst][lo].first <= rock-1) r[act].push_back(ii(r[lst][lo].first, rock-1));
				lo = p;
			}
			pos++;
			
		}
		//cout << " LO EH " << lo << endl;
		int beg = INF;
		if(r[lst][lo-1].second >= rock+1) beg = rock+1;
		if(lo < r[lst].size()) beg = r[lst][lo].first;
		if(beg <= n) r[act].push_back(ii(rock+1, n)); 
		
		swap(act, lst);
		ult = i;
	}
	
	//REP(i, r[lst].size()) cout << "(" << r[lst][i].first << "," << r[lst][i].second << ") ";
		
	int ans = r[lst].empty() ? INF : (r[lst][0]).first;
	if(ans <= n) printf("%d\n", 2*(n-1));
	else printf("-1\n");
}
