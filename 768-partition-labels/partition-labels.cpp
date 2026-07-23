class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> last(26, 0);
        
        // Record the last occurrence index of each character
        for (int i = 0; i < s.length(); i++) {
            last[s[i] - 'a'] = i;
        }

        vector<int> result;
        int start = 0, max_idx = 0;

        for (int i = 0; i < s.length(); i++) {
            max_idx = max(max_idx, last[s[i] - 'a']);
            
            // Reached the end of the current valid partition
            if (i == max_idx) {
                result.push_back(i - start + 1);
                start = i + 1;
            }
        }

        return result;
    }
};