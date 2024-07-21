// prob_003.rs

// Problem 3
// 
// Largest Prime Factor
// 
// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// 

// import standard library types
use std::time::Instant;

// import modules
use crate::primes;

// Solve the problem
fn solve(number: i64) -> i64 {
    println!("Running solve()... go go go!");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;
    
    // get prime numbers up to a max value
    // may have to clone to pass to function: prime_numbers.clone()
    // may have to change types due to overflow
    let max_n: i64 = 1_000_000;
    let prime_numbers: Vec<i64> = primes::get_primes_advanced(max_n);
    let prime_factors: Vec<i64> = primes::get_prime_factors(number, prime_numbers.clone());

    // figure out how to get max value of vector

    println!("number: {number}");
    println!("prime factors: {:?}", prime_factors);
    
    println!("Completed solve()!");
    result
}

// This is the main function.
pub fn main() {
    let start_time  = Instant::now();
    let number: i64  = 600851475143;
    let answer: i64 = solve(number);
    let end_time    = Instant::now();
    
    let run_time = end_time.duration_since(start_time);

    println!("answer: {answer}");
    println!("run time: {:.2?}", run_time);
}
