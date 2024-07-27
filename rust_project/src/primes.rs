// primes.rs

// import standard library types
use std::time::Instant;

// find divisors of a number
fn divisors(number: i64) -> Vec<i64> {
    let mut divs: Vec<i64> = Vec::new();
    for x in 1..(number/2 + 1) {
        if number % x == 0 {
            divs.push(x);
        }
    }
    divs.push(number);
    divs
}

// determine if a number is prime
fn is_prime(number: i64) -> bool {
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
fn primes_test_1(max_n: i64) {
    println!("Running primes_test_1().");
    for n in 1..(max_n + 1) {
        let divs: Vec<i64> = divisors(n);
        let n_is_prime = is_prime(n);
        //println!("n: {:?}, divisors: {:?}, prime: {:?}", n, divs, n_is_prime);
        println!("n: {:?}, n_divs: {:?}, prime: {:?}", n, divs.len(), n_is_prime);
    }
}

// Primes: test 2
fn primes_test_2(max_n: i64) {
    println!("Running primes_test_2().");
    let primes: Vec<i64> = get_primes_basic(max_n);
    println!("max_n: {:?}", max_n);
    println!("n_primes: {:?}", primes.len());
    //println!("primes: {:?}", primes);
}

// Primes: test 3
fn primes_test_3(max_n: i64) {
    println!("Running primes_test_3().");
    let primes: Vec<i64> = get_primes_advanced(max_n);
    println!("max_n: {:?}", max_n);
    println!("n_primes: {:?}", primes.len());
    //println!("primes: {:?}", primes);
}

// Prime factors: test 1
fn prime_factors_test_1(max_n: i64) {
    println!("Running prime_factors_test_1().");
    let primes: Vec<i64> = get_primes_advanced(max_n);
    for n in 1..(max_n + 1) {
        let prime_factors: Vec<i64> = get_prime_factors(n, primes.clone());
        println!("n: {:?}, prime factors: {:?}", n, prime_factors);
    }
}

// Get primes: basic method: counting divisors
pub fn get_primes_basic(max_n: i64) -> Vec<i64> {
    let mut primes: Vec<i64> = Vec::new();
    for n in 1..(max_n + 1) {
        if is_prime(n) {
            primes.push(n);
        }
    }
    primes
}

// Get primes: advanced method: Sieve of Eratosthenes
pub fn get_primes_advanced(max_n: i64) -> Vec<i64> {
    let mut primes: Vec<i64> = Vec::new();
    
    // Start with all numbers assigned True for prime.
    // Assign False to numbers that are divisible by a prime.
    // At the end, numbers still assigned True are prime.
    let mut is_prime_list: Vec<bool> = vec![true; (max_n + 1) as usize];
    is_prime_list[0] = false;
    is_prime_list[1] = false;
    // Start with the first prime number, 2.
    // Keep iterating as long as i^2 <= max_n.
    let mut i: i64 = 2;
    while i*i <= max_n {
        //println!("i: {}", i);
        if is_prime_list[i as usize] {
            for j in ((i*i)..(max_n+1)).step_by(i as usize) {
                is_prime_list[j as usize] = false;
            }
        }
        i += 1;
    }

    // Collect primes.
    for (i, &is_p) in is_prime_list.iter().enumerate() {
        //println!("i: {}, is_p: {}", i, is_p);
        if is_p {
            primes.push(i as i64);
        }
    }

    primes
}

// get prime factors of a number
// only keep one of each prime factor; do not record power of each prime
pub fn get_prime_factors(number: i64, primes: Vec<i64>) -> Vec<i64> {
    let mut prime_factors: Vec<i64> = Vec::new();
    let mut i: i64 = 0;
    while (i as usize) < primes.len() && primes[i as usize] <= number {
        if number % primes[i as usize] == 0 {
            prime_factors.push(primes[i as usize]);
        }
        i += 1;
    }
    prime_factors
}

// This is the main function.
fn main() {
    let start_time  = Instant::now();
    let max_n: i64  = 100;
    //let max_n: i64  = 1_000_000;
    //let max_n: i64  = 1_000_000_000;
    //primes_test_1(max_n);
    //primes_test_2(max_n);
    //primes_test_3(max_n);
    prime_factors_test_1(max_n);
    let end_time    = Instant::now();

    let run_time = end_time.duration_since(start_time);

    println!("run time: {:.2?}", run_time);
}
