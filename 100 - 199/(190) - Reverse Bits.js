/**
 * @param {number} n - a positive integer
 * @return {number} - a positive integer
 */
 var reverseBits = n => {
    let result = 0;
    let shamt = 31;
    for (let b = 31; b > 0; b--) {
        result += Math.abs(((2**(31-b)) & n) << shamt) + Math.abs(((2**b) & n) >> shamt);
        shamt -= 2;
    }
    return result;
};