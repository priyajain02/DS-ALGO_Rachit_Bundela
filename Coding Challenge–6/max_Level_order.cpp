

// Q2. Largest Value in Each Row

class Solution {
public:

    vector<int> largestValues(TreeNode* root) {
        vector<int> ans;
        if(root == NULL) return ans;

        int mx = INT_MIN;
        queue <TreeNode*> q;
        q.push(root);


        q.push(NULL);

        while(!q.empty()){


            TreeNode* temp = q.front() ;

            q.pop();
            mx = max(mx, temp->val);
            if(temp->left != NULL) q.push(temp->left);
            if(temp->right != NULL) q.push(temp->right);
            if(q.front() == NULL){
                q.pop();
                ans.push_back(mx);
                mx = INT_MIN;
                if(q.empty()) break;
                q.push(NULL);
            }

        }
        return ans;

    }
};
