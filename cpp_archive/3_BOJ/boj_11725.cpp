/*
  c++ ==> boj 11725, 트리의 부모 찾기를 푼 정답 코드


  code from [http://blog.naver.com/PostView.nhn?blogId=kks227&logNo=220576195670&parentCategoryNo=271&categoryNo=302&viewDate=&isShowPopularPosts=false&from=postList]
*/
#include <iostream>
#include <cstring>
#include <vector>

using namespace std;

vector<int> adj[100000];
int parent[100000];

void DFS(int cur) {
  for(int next: adj[cur]) {
    if(parent[next] == -1) {
      parent[next] = cur;
      DFS(next);
    }
  }
}

int main(int argc, char **argv) {
  int N;
  cin >> N;

  for(int i=0; i<N-1; i++) {
    int a,b;
    cin >> a >> b;
    adj[a-1].push_back(b-1);
    adj[b-1].push_back(a-1);
  }
  // parent 배열을 -1로 초기화
  memset(parent, -1, sizeof(parent));
  DFS(0);

  std::cout << "------------------------" << endl;;
  for(int i=1; i<N; i++) {
    std::cout << parent[i]+1 << endl;
  }

  return 0;
}
