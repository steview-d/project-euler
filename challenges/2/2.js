function fibonacci_evens(limit) {
    var fs = [1, 2];

    // create array of all fibonacci numbers below limit param
    while (fs[fs.length - 1] + fs[fs.length - 2] < limit) {
        fs.push(fs[fs.length - 1] + fs[fs.length - 2]);
    }

    // filter out odd numbers, then sum all array elements
    return fs.filter(idx => idx % 2 == 0).reduce((a, b) => a + b, 0);
}

console.log(fibonacci_evens(4000000));
