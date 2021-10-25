/**
 * @param {number} n
 * @return {boolean}
 */
 var isPowerOfFour = n => {
    if (n === 0) {
        return false;
    }
    while (n % 4 === 0) {
        n >>>= 2;
    }
    if (n === 1) {
        return true;
    } 
    return false
};