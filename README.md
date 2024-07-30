# GCD/HCF of 2 Numbers using Euclid's Algorithm

Euclid's Algorithm is a method for finding the Greatest Common Divisor (GCD) of two integers. The algorithm follows these steps:

1. **Start with two integers**, `a` and `b`, where `a ≥ b`.

2. **Compute the remainder** of `a` divided by `b`, denoted as `r` (i.e., `r = a mod b`).

3. **Replace `a` with `b`** and `b` with `r`.

4. **Repeat the process** until `b` becomes `0`. The non-zero remainder at this step is the GCD of `a` and `b`.

## Features

- **Step-by-Step Explanation**: Outputs each step of the Euclidean Algorithm for clarity.
- **Error Handling**: Includes basic error handling for invalid integer inputs.

## Sample Output
```
    GCD or HCF of 2 numbers using EUCLID'S ALGORITHM

    value of A:56
    value of B:98

    EUCLID'S ALGORITHM STEPS

    Step 1 : 98 = 56 * 1 + 42
    Step 2 : 56 = 42 * 1 + 14
    Step 3 : 42 = 14 * 3 + 0

    GCD/HCF of 56 and 98 = 14
    LCM 392.0
```

## To Run This Script

1. Clone the repository:

   ```sh
   git clone https://github.com/bheematgithub/Euclidean_Algorithm.git
   ```
2. Navigate to the project directory:

   ```sh
   cd Euclidean_Algorithm
   ```
3. Run the script using Python:

    ```sh
    python Euclidean_Algorithm.py
    ```

