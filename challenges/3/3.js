function is_prime(n) {
    // check if n is a prime, return bool
    for (let i = 2; i < Math.ceil(n ** 0.5) + 1; i++) {
        if (n % i == 0) {
            return false;
        }
    }
    return true;
}

function prime_list(n) {
    // create an array of primes up to value n
    primeList = [2];
    for (let i = 2; i < (n+1); i++) {
        if (is_prime(i)) {
            primeList.push(i);
        }
    }
    return primeList;
}

function prime_factor(n, pl) {
    /*
        n:  number to find largest prime factor for
        pl: create a list of all prime numbers that fall
            within the range of 1 and this value
    */

    // create list of primes, upto & including value of pl
    prime_nums = prime_list(pl)

    // return largest prime factor by returning
    // 1st factor in a reversed list of primes
    for (let i = prime_nums.length - 1; i >= 0; i--) {
        if (n % prime_nums[i] == 0) {
            return prime_nums[i]
        }
    }
}

console.log(prime_factor(600851475143, 10000))
