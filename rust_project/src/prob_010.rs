// prob_010.rs

// Problem 10
//
// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
//
// Find the sum of all the primes below two million.
//

// Import libraries and modules
use crate::primes;

// Solve the problem
fn solve(number: i64) -> i64 {
    println!("Running solve()...");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;

    // Get prime numbers up to a max value
    let prime_numbers: Vec<i64> = primes::get_primes_advanced(number);
    let n_primes: i64 = prime_numbers.len() as i64;
    
    println!("number: {number}");
    println!("n_primes: {n_primes}");
    
    // Get sum of primes
    for p in prime_numbers {
        result += p;
    }

    println!("Completed solve()!");
    result
}

// Run the calculation for this problem
pub fn run() {
    println!("Solving Problem 10.");
    println!("Running run()...");
    let number: i64  = 2_000_000;
    let answer: i64 = solve(number);
    println!("answer: {answer}");
}
