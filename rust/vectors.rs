// This is a comment in Rust.

// This is the main function.
fn main() {
    // Statements here are executed when the compiled binary is called.

    // Print text to the console.
    println!("Bonjour!");
    println!("Here are some vector examples.");

    // Example vector
    let my_vec = vec![100, -10, 0, 3, 5, 30, 50, 15, 10, 1];

    println!("my_vec: {:?}", my_vec);
    
    // Find min and max values of vector
    let mut my_min_value = -999;
    let mut my_max_value = -999;
    //let min_value = my_vec.iter().min();
    //let max_value = my_vec.iter().max();
    let min_value: Option<&i32> = my_vec.iter().min();
    let max_value: Option<&i32> = my_vec.iter().max();

    // Set min value
    match min_value {
        Some(&min) => {
            println!("The minimum value is {}.", min);
            my_min_value = min;
        }
        None => println!("The vector is empty."),
    }
    
    // Set max value
    match max_value {
        Some(&max) => {
            println!("The maximum value is {}.", max);
            my_max_value = max;
        }
        None => println!("The vector is empty."),
    }
    
    println!("my_min_value: {:?}", my_min_value);
    println!("my_max_value: {:?}", my_max_value);
}
