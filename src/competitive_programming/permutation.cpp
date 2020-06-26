
#include <bits/stdc++.h>
using namespace std;


set<3> permutation = {1,2,3};
set<3> chosen = {false, false, false};
int n = 3;

void search() {
	if (permutation.size() == n) {
		cout<<permutation;
	} else {
		for (int i = 0; i < n; i++) {
			if (chosen[i]) continue;
			chosen[i] = true;
			permutation.push_back(i);
			search();
			chosen[i] = false;
			permutation.pop_back();
		}
	}
}


int main() {
	search();
	return 0;
}
