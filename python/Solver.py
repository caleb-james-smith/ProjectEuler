# Solver.py

import time

# solves problems
# - initialize with function and parameter
# - reports answer and time to solve
class Solver:
    def __init__(self, function, parameter):
        self.function  = function
        self.parameter = parameter

    def solve(self):
        start_time = time.time()
        x = self.function(self.parameter)
        end_time = time.time()
        
        run_time = end_time - start_time 
        
        print("answer: {0}".format(x))
        print("run time: {0:.3f} seconds".format(run_time))

