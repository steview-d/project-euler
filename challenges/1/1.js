function counter(n) {
    // create array of numbers [1, n]
    const rng = [...Array(n).keys()];
    counter = 0;

    rng.forEach(i => {
        // for every multiple of 3 or 5,
        // add this number to the counter
        if (i % 3 === 0 || i % 5 === 0) {
            counter += i;
        }
    });

    console.log(counter);
}

counter(1000);
