#include <vector>
#include <string>

using namespace std;

struct TrieNode {
    TrieNode* children[26] = {nullptr};
    int count = 0;
};

class Solution {
public:
    vector<int> sumPrefixScores(vector<string>& words) {
        TrieNode* root = new TrieNode();

        // Step 1: Insert all words into the Trie and increment prefix counts
        for (const string& word : words) {
            TrieNode* curr = root;
            for (char ch : word) {
                int idx = ch - 'a';
                if (!curr->children[idx]) {
                    curr->children[idx] = new TrieNode();
                }
                curr = curr->children[idx];
                curr->count++;
            }
        }

        // Step 2: Calculate the sum of prefix scores for each word
        vector<int> ans;
        ans.reserve(words.size());

        for (const string& word : words) {
            TrieNode* curr = root;
            int score = 0;
            for (char ch : word) {
                int idx = ch - 'a';
                curr = curr->children[idx];
                score += curr->count;
            }
            ans.push_back(score);
        }

        return ans;
    }
};