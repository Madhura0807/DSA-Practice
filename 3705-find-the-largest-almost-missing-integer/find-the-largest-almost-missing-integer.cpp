#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>

class Solution {
public:
    int largestInteger(std::vector<int>& nums, int k) {
        int n = nums.size();
        std::unordered_map<int, std::unordered_set<int>> subarray_counts;

        for (int i = 0; i <= n - k; ++i) {
            for (int j = i; j < i + k; ++j) {
                subarray_counts[nums[j]].insert(i);
            }
        }

        int ans = -1;
        for (const auto& [num, sub_indices] : subarray_counts) {
            if (sub_indices.size() == 1) {
                ans = std::max(ans, num);
            }
        }

        return ans;
    }
};