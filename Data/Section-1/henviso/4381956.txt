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
#define EPS 1e-11
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

#define PI 3.14159265359
#define DEGtoRAD(x) (x * PI / 180.0)

typedef double real;

struct point{ 
	real x, y;
	point(){ };
	point(real _x, real _y){ x = _x; y = _y; }
	bool operator < (point other) const{
		if(fabs(x - other.x) >= EPS) return x < other.x;
		return y < other.y;
	}
	bool operator == (point other){
		return fabs(x - other.x) < EPS && fabs(y - other.y) < EPS;
	}
	double dist(point other){
		return hypot(x - other.x, y - other.y);		
	}
	point rotate(double theta){
		double rad = DEGtoRAD(theta);
		return point(x * cos(rad) - y * sin(rad), x * sin(rad) + y * cos(rad));
	}
	friend istream& operator >>(istream &is, point &p);
    friend ostream& operator <<(ostream &os, const point &p);
};

ostream& operator<<(ostream& os, const point& p){
	os << "(" << p.x << "," << p.y << ")";
}

istream& operator>>(istream& is, point& p){
	is >> p.x >> p.y;
}

int n;
point p[1000];
bitset<1000> bs; 
int a[4];

double area(int p0_, int p1_, int p2_, int p3_){
	point p0 = p[p0_], p1 = p[p1_], p2 = p[p2_], p3 = p[p3_];
	return 0.5 * (p0.x*p1.y + p1.x*p2.y + p2.x*p3.y + p3.x*p0.y - p0.y*p1.x - p1.y*p0.x - p2.y * p1.x - p3.y * p0.x); 
}

bool NotCons(){
	REP(i, 4){
		if(!bs[a[i]]){
			a[0] = a[i];
			return true;
		}
	}
	return false;
}

int main(){
	cin >> n;
	REP(i, n) cin >> p[i];
	
	bs.reset();
	a[0] = 0;
	double ans = -1.0;
	while(NotCons()){
		REP(i, n){
			REPP(j, i+1, n){
				REPP(k, j+1, n){
					double ar = area(a[0], i, j, k);
					if(fabs(ar - ans) > EPS){
						if(ar > ans){
							a[1] = i;
							a[2] = j;
							a[3] = k;
						}
					}
					else{  //EQ
						a[1] = i;
						a[2] = j;
						a[3] = k;
					}
					ans = max(ans, ar);
				}
			}
		}
		bs[a[0]] = true;	
	}
	if(ans < EPS) printf("0.0000000000\n");
	printf("%.10lf\n", ans);
	
}
