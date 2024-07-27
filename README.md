# ProjectEuler

Solutions to Project Euler problems.

See Project Euler at https://projecteuler.net/ .

Example of running python code:
```
python3 python/prob_003.py
```

Example of running Rust code using rustc to compile.
Here, we are using the compiler flags `-O -C opt-level=3 -C lto` to optimize performance.
```
cd rust
rustc -O -C opt-level=3 -C lto prob_044.rs
./prob_044
```

Example of running Rust code using cargo to compile and run.
```
cd rust_project
cargo run
```

Example of running C++ code.
Here we put the executable in the directory "bin".
```
mkdir -p bin
g++ --std=c++20 -o bin/prob_003 src/prob_003.cpp src/Primes.cpp
./bin/prob_003
```

For GCC version 9 and earlier:
```
mkdir -p bin
g++ --std=c++2a -o bin/prob_003 src/prob_003.cpp src/Primes.cpp
./bin/prob_003
```

Example of running java code.
Note that you need to be in the java directory to compile and run java when multiple files are being used.
```
cd java
javac prob_003.java Primes.java ArrayAppend.java
java prob_003.java Primes.java ArrayAppend.java
```

For Ubuntu:
```
cd java
javac prob_003.java Primes.java ArrayAppend.java
java prob_003
```

