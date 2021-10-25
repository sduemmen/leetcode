/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
    let sum = 0;
    let conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    };
    let order = ["I", "V", "X", "L", "C", "D", "M"]

    let i = s.length-1;
    let chain = "";
    while (i >= 0) {
        if (i !== 0 && s[i] === s[i-1]){
            chain += s[i];
        } else {
            if (i > 0 && order.indexOf(s[i-1]) < order.indexOf(s[i])){ //case IV IX ...
                sum += (conversion[s[i]] - conversion[s[i-1]]);
                i--;
            } else {
                sum += conversion[s[i]];
            }
        }
        i--;
    }
    for (const c of chain) {
        sum += conversion[c];
    }
    return sum
}

console.log(romanToInt("MMCDXXV"));