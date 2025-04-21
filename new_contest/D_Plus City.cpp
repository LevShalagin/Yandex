#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

int n, m, d;
vector<string> grid;
vector<vector<int>> dist;
vector<vector<int>> prefix;

bool is_valid(int i, int j, int k) {
    if (i + k > n || j + k > m) {
        return false;
    }
    int total = prefix[i + k][j + k] - prefix[i][j + k] - prefix[i + k][j] + prefix[i][j];
    return total == k * k;
}

int main() {
    cin >> n >> m >> d;
    grid.resize(n);
    for (int i = 0; i < n; ++i) {
        cin >> grid[i];
    }

    dist.assign(n, vector<int>(m, INT_MAX));
    queue<pair<int, int>> q;

    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (grid[i][j] == 'x') {
                dist[i][j] = 0;
                q.push({i, j});
            }
        }
    }

    vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
    while (!q.empty()) {
        auto [x, y] = q.front();
        q.pop();
        for (auto [dx, dy] : directions) {
            int nx = x + dx;
            int ny = y + dy;
            if (nx >= 0 && nx < n && ny >= 0 && ny < m && dist[nx][ny] == INT_MAX) {
                dist[nx][ny] = dist[x][y] + 1;
                q.push({nx, ny});
            }
        }
    }

    prefix.assign(n + 1, vector<int>(m + 1, 0));
    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= m; ++j) {
            prefix[i][j] = prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1] + (dist[i-1][j-1] >= d ? 1 : 0);
        }
    }

    int left = 0;
    int right = min(n, m);
    int best_k = 0;
    while (left <= right) {
        int mid = (left + right) / 2;
        bool found = false;
        for (int i = 0; i <= n - mid; ++i) {
            for (int j = 0; j <= m - mid; ++j) {
                if (is_valid(i, j, mid)) {
                    found = true;
                    break;
                }
            }
            if (found) {
                break;
            }
        }
        if (found) {
            best_k = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    cout << best_k << endl;

    return 0;
}