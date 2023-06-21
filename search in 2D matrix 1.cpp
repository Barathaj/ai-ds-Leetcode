class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
          int n=matrix.size();//row
          int m=matrix[0].size();//column
          int i=0;
          int j=m-1;//co
        while(i<n&&j>=0)//understand
        {
            if(matrix[i][j]==target)//[2][2]==target
            return true;
            else if(matrix[i][j]<target)
            {
                i++;
            }
            else
            {
                j--;
            }
        }
        return false;
    }
};
