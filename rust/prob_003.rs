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

// Solve the problem
fn solve(max_n: i32) -> i32 {
    println!("Running solve()... go go go!");
    println!("max_n: {max_n}");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i32 = 0;
    
    println!("Completed solve()!");
    result
}

// This is the main function.
fn main() {
    let start_time  = Instant::now();
    let max_n: i32  = 1_000_000;
    let answer: i32 = solve(max_n);
    let end_time    = Instant::now();
    
    let run_time = end_time.duration_since(start_time);

    println!("answer: {answer}");
    println!("run time: {:.2?}", run_time);
}



