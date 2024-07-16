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
fn isPrime(number: i32) -> bool {
    if number == 1 {
        return false;
    }
    let divs = divisors(number);
    if divs.len() == 2 {
        return true;
    } else {
        return false;
    }
}

// Test primes
fn testPrimes(max_n: i32) {
    for n in 1..(max_n + 1) {
        let divs: Vec<i32> = divisors(n);
        let is_prime = isPrime(n);
        println!("n: {:?}, divisors: {:?}, prime: {:?}", n, divs, is_prime);
    }
}

// This is the main function.
fn main() {
    // let number: i32 = 24;
    // let divs: Vec<i32> = divisors(number);
    // let is_prime = isPrime(number);
    // println!("number: {:?}, divisors: {:?}, prime: {:?}", number, divs, is_prime);
    
    let max_n: i32 = 100;
    testPrimes(max_n);
}
