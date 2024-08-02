// prob_004.rs

// Problem 4
//
// A palindromic number reads the same both ways.
// The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
//
// Find the largest palindrome made from the product of two 3-digit numbers.
//

// check if number reads the same both ways
fn palindrome(number: i64) -> bool {
    // get string from integer
    let num_string: String = number.to_string();
    // reverse string
    let num_string_reversed: String = num_string.chars().rev().collect();
    // check if string is equal to its reverse
    if num_string == num_string_reversed {
        return true;
    } else {
        return false;
    }
}

// Solve the problem
fn solve() -> i64 {
    println!("Running solve()...");
    
    // Since we plan to change result, we need to make it mutable using "mut".
    let mut result: i64 = 0;

    let mut num_products: i64 = 0; 
    let val_start: i64  = 100;
    let val_stop: i64   = 1000;

    for i in val_start..val_stop {
        for j in i..val_stop {
            num_products += 1;
            let product: i64 = i * j;
            let is_palindrome: bool = palindrome(product);
            //println!("(i, j) = ({i}, {j}): product = {product}, is_palindrome = {is_palindrome}");
            if is_palindrome {
                println!("(i, j) = ({i}, {j}): product = {product}, is_palindrome = {is_palindrome}");
                if product > result {
                    result = product;
                }
            }
        }
    }

    println!("num_products: {num_products}");
    result
}

// Run the calculation for this problem
pub fn run() {
    println!("Running run()... go go go!");
    let answer: i64 = solve();
    println!("answer: {answer}");
}
