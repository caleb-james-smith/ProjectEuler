// prob_003.rs

// Problem 3
// 
// Largest Prime Factor
// 
// The prime factors of 13195 are 5, 7, 13 and 29.
// 
// What is the largest prime factor of the number 600851475143 ?
// 

// Import libraries and modules
use crate::primes;

// Solve the problem
fn solve(number: i64) -> i64 {
    println!("Running solve()...");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;
    
    // Get prime numbers up to a max value
    // May have to clone to pass to function: prime_numbers.clone()
    // May have to change types due to overflow
    let max_n: i64 = 1_000_000;
    let prime_numbers: Vec<i64> = primes::get_primes_advanced(max_n);
    let prime_factors: Vec<i64> = primes::get_prime_factors(number, prime_numbers.clone());

    println!("number: {number}");
    println!("prime factors: {:?}", prime_factors);

    // get max value of vector
    let max_value: Option<&i64> = prime_factors.iter().max();
    // set result to the max value
    match max_value {
        Some(&max) => {
            println!("The maximum value is {}.", max);
            result = max;
        }
        None => println!("The vector is empty."),
    }

    println!("Completed solve()!");
    result
}

// Run the calculation for this problem
pub fn run() {
    println!("Running run()... go go go!");
    let number: i64  = 600851475143;
    let answer: i64 = solve(number);
    println!("answer: {answer}");
}
