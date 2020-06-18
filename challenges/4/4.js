function find_palindrome(num_digits_a, num_digits_b) {
    /*
        Find the largest palindrome made from the product of two n-digit numbers.

        Args:
            num_digits_a (int): number of digits in number
            num_digits_b (int): number of digits in number

        Returns:
            largest (int): The largest palindrome found
    */

    a = 10**num_digits_a-1
    b = 10**num_digits_b-1
    largest = 0

    for (let x = a; x >= 0; x--) {
        for (let y = b; y >= 0; y--) {
            if (is_palindrome(x*y) && x*y > largest) {
                largest = x*y
            }
        }
    }
    return largest
}


function is_palindrome(n) {
    /*
        Check if n is a palindrome

        Args:
            n (int): The number to check

        Returns: Boolean
    */

    // get number of digits in n, halved
    h = parseInt(n.toString().length / 2)

    fr = n.toString().slice(0, h)
    bk = n.toString().slice(-h).split("").reverse().join("")

    var result = fr === bk ? true : false
    return result
}


console.log(find_palindrome(3, 3))
