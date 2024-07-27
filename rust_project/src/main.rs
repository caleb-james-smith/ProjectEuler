// Import libraries and modules
use std::time::{Instant, Duration};
pub mod prob_003;
pub mod primes;

// This is the main function
fn main() {
    println!("---------------");
    println!("Running main().");
    println!("---------------");
    // Calculate run time
    let start_time: Instant = Instant::now();
    prob_003::run();
    let end_time: Instant = Instant::now();
    let run_time: Duration = end_time.duration_since(start_time);
    println!("run time: {:.2?}", run_time);
}
