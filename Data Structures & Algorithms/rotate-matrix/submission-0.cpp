class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        mirror(matrix);
        flipy(matrix);
    }

    void mirror(vector<vector<int>>& matrix){
        for (int i = 0; i < matrix.size(); i++){
            for(int j = i+1; j < matrix[i].size(); j++){
                std::swap(matrix[i][j], matrix[j][i]);
            }
        }
    }

    void flipy(vector<vector<int>>& matrix){
        int n = matrix.size();
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n / 2; j++){
                std::swap(matrix[i][j], matrix[i][std::abs(j-n+1)]);
            }
        }
    }
};
