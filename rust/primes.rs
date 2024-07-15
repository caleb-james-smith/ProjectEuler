// primes.rs

// find divisors of a number
fn divisors(number: i32) -> Vec<i32> {
    let mut divs: Vec<i32> = Vec::new();
    for x in 1..(number/2 + 1) {
        if number % x == 0 {
            divs.push(x);
        }
    }
    divs.push(number);
    divs
}

// This is the main function.
fn main() {
    let number: i32 = 24;
    let divs: Vec<i32> = divisors(number);
    println!("number: {:?}, divisors: {:?}", number, divs);
}
