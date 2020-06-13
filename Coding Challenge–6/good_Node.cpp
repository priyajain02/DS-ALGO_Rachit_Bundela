
// Q4. Numberof Good Nodes in Binary Tree

class Solution {
public:
    int ans =0;
    void solve(TreeNode* root, int mx){
        if(root == NULL) return;
        if(root->val >= mx){
            mx = root->val;
            ans++;
        }

        solve(root->left, mx);
        solve(root->right, mx);

    }



    int goodNodes(TreeNode* root) {
        if(root==NULL) return 0;

        solve(root, root->val);
        return ans;

    }
};
