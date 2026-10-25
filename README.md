# prime-factors_check
A robust, interactive command-line interface (CLI) tool written in Python to evaluate prime numbers and calculate mathematical factors, featuring specific exception handling for seamless user interaction
# Prime & Factor Checker CLI

An interactive command-line application built in Python that allows users to seamlessly check if a number is prime and generate a complete list of its mathematical factors. The project highlights foundational logic, structured modular functions, and robust exception handling.

## 🚀 Features
* **Prime Number Validator:** Checks if a given integer is a prime or composite number.
* **Factor Generator:** Automatically computes and displays all positive factors of a number.
* **Robust Input Validation:** Utilizes specific exception handling (`ValueError`) to prevent program crashes due to invalid input formats or empty strings.
* **Persistent CLI Loop:** Runs inside a continuous loop, letting you switch between operations or type `stop` at any prompt to safely exit.

## 🛠️ Built With
* **Python 3.x**

## 📦 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   ```

2. **Navigate into the project directory:**
   ```bash
   cd YOUR_REPOSITORY_NAME
   ```

3. **Execute the script:**
   ```bash
   python main.py
   ```

## 📖 Code Highlights: Specific Exception Handling
Unlike bare `except:` clauses that mask hidden syntax bugs or restrict system termination commands (like `Ctrl+C`), this tool targets exact potential exceptions:

```python
try:             
    num = int(num)
    # core numerical logic...
except ValueError:
    invalid() # Safely catches formatting errors without breaking the environment
```
