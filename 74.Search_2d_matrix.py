class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[-1] >= target:
                for i in row:
                    if i == target:
                        return True
        return False
    
'''
optional rust solution
impl Solution {
    pub fn search_matrix(matrix: Vec<Vec<i32>>, target: i32) -> bool {
        for row in matrix {
            if row.is_empty() {
                continue;
            }

            let last = row[row.len() - 1];
            if last >= target {
                return row.binary_search(&target).is_ok();
            }
        }
        false
    }
}
'''