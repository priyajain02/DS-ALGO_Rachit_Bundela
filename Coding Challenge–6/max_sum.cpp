
// Q1. Maximum path sum between two Nodes.


class Solution {
public:
    int max_sum_include;
    int ms_root;
    int result = INT_MIN;

    int solve(TreeNode* root) {
        if(root == NULL)
            return 0;

        int left = solve(root->left);
        int right = solve(root->right);

        max_sum_include = max(max(left, right) + root->val, root->val);
        ms_root = max(max_sum_include, left + right + root->val);
        result = max(result, ms_root);

        return max_sum_include;

    }
    int maxPathSum(TreeNode* root){
        int a = solve(root);
        return result;

    }
};
