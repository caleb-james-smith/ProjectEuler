// prob_005.rs

// Problem 5
//
// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
//
// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
//

// Solve the problem
fn solve(number: i64) -> i64 {
    println!("Running solve()...");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;
    let mut n: i64 = 1;
    let mut search: bool = true;

    while search {
        let mut divisible: bool = true;
        for i in 1..number {
            if n % i != 0 {
                divisible = false;
                break;
            }
        }
        if divisible {
            result = n;
            search = false;
        } else {
            n += 1;
        }
    }
    
    println!("Completed solve()!");
    result
}

// Run the calculation for this problem
pub fn run() {
    println!("Running run()... go go go!");
    let number: i64  = 20;
    let answer: i64 = solve(number);
    println!("answer: {answer}");
}
