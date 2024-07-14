// prob_001.rs

// Problem 1
// 
// If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
// The sum of these multiples is 23.
// 
// Find the sum of all the multiples of 3 or 5 below 1000.
// 

// import standard library types
use std::time::Instant;

// Solve the problem
fn solve(max_val: i32) -> i32 {
    println!("Go go go!");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i32 = 0;
    
    for n in 1..max_val {
        if n % 3 == 0 || n % 5 == 0 {
            result += n;
        }
    }
    result
}

// This is the main function.
fn main() {
    let start_time = Instant::now();
    let max_val: i32 = 1_000;
    let answer: i32  = solve(max_val);
    let end_time = Instant::now();
    
    let run_time = end_time.duration_since(start_time);

    println!("answer: {answer}");
    println!("run time: {:.2?}", run_time);
}

