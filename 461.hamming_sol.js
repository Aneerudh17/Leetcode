/**
 * @param {number} x
 * @param {number} y
 * @return {number}
 */
var hammingDistance = function(x, y) {
    let d = x ^ y;
    let count = 0;
    while (d !== 0){
        d &= d -1;
        count ++;
    }
    return count;
    
};