
// # 3721. Longest Balanced Subarray II


// # You are given an integer array nums.

// # A subarray is called balanced if the number of distinct even numbers in the subarray is equal to the number of distinct odd numbers.

// # Return the length of the longest balanced subarray.

 

// # Example 1:

// # Input: nums = [2,5,4,3]

// # Output: 4

// # Explanation:

// # The longest balanced subarray is [2, 5, 4, 3].
// # It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [5, 3]. Thus, the answer is 4.
// # Example 2:

// # Input: nums = [3,2,2,5,4]

// # Output: 5

// # Explanation:

// # The longest balanced subarray is [3, 2, 2, 5, 4].
// # It has 2 distinct even numbers [2, 4] and 2 distinct odd numbers [3, 5]. Thus, the answer is 5.
// # Example 3:

// # Input: nums = [1,2,3,2]

// # Output: 3

// # Explanation:

// # The longest balanced subarray is [2, 3, 2].
// # It has 1 distinct even number [2] and 1 distinct odd number [3]. Thus, the answer is 3.
 

// # Constraints:

// # 1 <= nums.length <= 105
// # 1 <= nums[i] <= 105

// CXODE ?


#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    struct Node {
        int l, r;
        int mn, mx;
        int lazy;
    };

    struct SegTree {
        int n;
        vector<Node> tr;

        SegTree(int n_) : n(n_), tr(4 * (n + 1)) {
            build(1, 0, n); // positions 0..n
        }

        void build(int u, int l, int r) {
            tr[u].l = l; tr[u].r = r;
            tr[u].mn = tr[u].mx = 0;
            tr[u].lazy = 0;
            if (l == r) return;
            int mid = (l + r) >> 1;
            build(u << 1, l, mid);
            build(u << 1 | 1, mid + 1, r);
        }

        void apply(int u, int v) {
            tr[u].mn += v;
            tr[u].mx += v;
            tr[u].lazy += v;
        }

        void pushdown(int u) {
            if (tr[u].lazy != 0) {
                int v = tr[u].lazy;
                apply(u << 1, v);
                apply(u << 1 | 1, v);
                tr[u].lazy = 0;
            }
        }

        void pushup(int u) {
            tr[u].mn = min(tr[u << 1].mn, tr[u << 1 | 1].mn);
            tr[u].mx = max(tr[u << 1].mx, tr[u << 1 | 1].mx);
        }

        // range add [L, R] by v
        void modify(int u, int L, int R, int v) {
            int l = tr[u].l, r = tr[u].r;
            if (L <= l && r <= R) {
                apply(u, v);
                return;
            }
            pushdown(u);
            int mid = (l + r) >> 1;
            if (L <= mid) modify(u << 1, L, R, v);
            if (R > mid)  modify(u << 1 | 1, L, R, v);
            pushup(u);
        }

        // find earliest index where value == target
        int queryEarliest(int u, int target) {
            if (tr[u].mn > target || tr[u].mx < target) return -1;
            if (tr[u].l == tr[u].r) return tr[u].l;
            pushdown(u);
            int leftAns = queryEarliest(u << 1, target);
            if (leftAns != -1) return leftAns;
            return queryEarliest(u << 1 | 1, target);
        }
    };

    int longestBalanced(vector<int>& nums) {
        int n = (int)nums.size();
        SegTree st(n);

        unordered_map<int,int> last; // value -> last index (1..n)
        last.reserve(n * 2);

        int now = 0; // current distinctOdd - distinctEven for prefix [1..i]
        int ans = 0;

        for (int i = 1; i <= n; i++) {
            int x = nums[i - 1];
            int det = (x & 1) ? 1 : -1; // odd:+1 even:-1

            auto it = last.find(x);
            if (it != last.end()) {
                int p = it->second;
                st.modify(1, p, n, -det); // remove old contribution
                now -= det;
            }

            last[x] = i;
            st.modify(1, i, n, det); // add new contribution
            now += det;

            int pos = st.queryEarliest(1, now); // earliest prefix-cut with same balance
            if (pos != -1) ans = max(ans, i - pos);
        }
        return ans;
    }
};