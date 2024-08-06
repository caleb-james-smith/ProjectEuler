// prob_007.rs

// Problem 7
//
// By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
//
// What is the 10 001st prime number?
//

// Import libraries and modules
use crate::primes;

// Solve the problem
fn solve(number: i64) -> i64 {
    println!("Running solve()...");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;

    // Get prime numbers up to a max value
    let max_n: i64 = 1_000_000;
    let prime_numbers: Vec<i64> = primes::get_primes_advanced(max_n);
    let n_primes: i64 = prime_numbers.len() as i64;

    println!("number: {number}");
    println!("n_primes: {n_primes}");

    // If number (index) >= number of primes in list, print error and return.
    if number >= n_primes {
        println!("ERROR: (number = {number}) >= (n_primes = {n_primes})");
        println!("FIX: More prime numbers need to calculated: increase max_n = {max_n}.");
        return result;
    }
    
    // Get prime number at index "number"
    result = prime_numbers[number as usize];

    println!("Completed solve()!");
    result
}

// Run the calculation for this problem
pub fn run() {
    println!("Running run()... go go go!");
    let number: i64  = 10_000;
    let answer: i64 = solve(number);
    println!("answer: {answer}");
}
