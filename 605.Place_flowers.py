class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        size = len(flowerbed)
        if flowerbed[0] == 0 and (size == 1 or flowerbed[1]==0):
            flowerbed[0] = 1
            count += 1
        
        if flowerbed[size-1] == 0 and (size == 1 or flowerbed[size-2] == 0):
            flowerbed[size-1] = 1
            count += 1

        for i in range(1,size-1):
            if flowerbed[i] == 0 and flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                count += 1
        return count >= n

'''
alternative rust solution:
impl Solution {
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, n: i32) -> bool {
        let mut count = 0;
        let mut size = flowerbed.len();
        
        if flowerbed[0] == 0 && (size == 1 || flowerbed[1]==0){
            flowerbed[0] = 1;
            count += 1;
        }
        if flowerbed[size-1] == 0 && (size ==1 || flowerbed[size-2]==0){
            flowerbed[size-1] =1 ;
            count += 1;
        }
        for i in 1..size-1{
            if flowerbed[i] == 0 && flowerbed[i - 1] == 0 && flowerbed[i + 1] == 0{
                flowerbed[i] = 1;
                count += 1;
            }
        }
        return count >= n;
    }
}
'''