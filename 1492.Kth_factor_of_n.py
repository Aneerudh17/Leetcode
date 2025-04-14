class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factor = []
        for i in range(1, n + 1):  
            if n % i == 0:
                factor.append(i)

        if k <= len(factor): 
            return factor[k - 1]
        else:
            return -1
        
'''
optional rust solution:
impl Solution {
    pub fn kth_factor(n: i32, k: i32) -> i32 {
        let mut factor = Vec::new();
        for i in 1..=n{
            if n % i == 0{
                factor.push(i);
            }
        }
        if (k as usize) <= factor.len(){
            return factor[(k-1)as usize];
        }
        else{
            return -1;
        }
        
    }
}
'''