// primes.rs

// find divisors of a number
fn divisors(number: i32) -> Vec<i32> {
    let mut divs: Vec<i32> = Vec::new();
    for x in 1..(number/2 + 1) {
        if number % x == 0 {
            divs.push(x);
        }
    }
    divs.push(number);
    divs
}

// determine if a number is prime
fn is_prime(number: i32) -> bool {
    if number <= 1 {
        return false;
    }
    let divs = divisors(number);
    if divs.len() == 2 {
        return true;
    } else {
        return false;
    }
}

// Primes: test 1
fn primes_test_1(max_n: i32) {
    for n in 1..(max_n + 1) {
        let divs: Vec<i32> = divisors(n);
        let n_is_prime = is_prime(n);
        //println!("n: {:?}, divisors: {:?}, prime: {:?}", n, divs, n_is_prime);
        println!("n: {:?}, n_divs: {:?}, prime: {:?}", n, divs.len(), n_is_prime);
    }
}

// Primes: test 2
fn primes_test_2(max_n: i32) {
    let primes: Vec<i32> = get_primes_basic(max_n);
    println!("max_n: {:?}", max_n);
    println!("n_primes: {:?}", primes.len());
    //println!("primes: {:?}", primes);
}

// Get primes: basic method
fn get_primes_basic(max_n: i32) -> Vec<i32> {
    let mut primes: Vec<i32> = Vec::new();
    for n in 1..(max_n + 1) {
        if is_prime(n) {
            primes.push(n);
        }
    }
    primes
}

// This is the main function.
fn main() {    
    let max_n: i32 = 1_000_000;
    //primes_test_1(max_n);
    primes_test_2(max_n);
}
