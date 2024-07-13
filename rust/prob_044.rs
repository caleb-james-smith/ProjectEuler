// prob_044.rs

// Problem 44
// 
// Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. The first ten pentagonal numbers are:
// 
// 1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
// 
// It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 − 22 = 48, is not pentagonal.
// 
// Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal
// and D = |Pk − Pj| is minimised; what is the value of D?

// Calculate pentagonal number P(n)
fn P(n: i32) -> i32 {
    let result: i32 = n * (3 * n - 1) / 2;
    result
}

// Solve the problem
fn solve() -> i32 {
    println!("Go go go!");
    let max_n: i32  = 10;
    let result: i32 = 0;
    
    println!("max_n: {max_n}");
    
    // get pentagonal numbers
    //let mut pentagonal_nums: Vec<i32> = Vec::new();
    let mut pentagonal_nums: Vec<i32> = vec![];
    for n in 1..max_n+1 {
        pentagonal_nums.push(P(n));
    }
    
    // print pentagonal numbers
    for (i, p) in pentagonal_nums.iter().enumerate() {
        let n = i + 1;
        println!("P({n}) = {p}");
    }
    
    result
}

// This is the main function.
fn main() {
    let answer: i32 = solve();
    println!("answer: {answer}");
}

