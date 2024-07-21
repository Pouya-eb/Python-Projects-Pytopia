# Happy Numbers

This script checks whether a given number is a "happy" number. A happy number is a number which eventually reaches 1 when replaced by the sum of the square of each digit, and this process is repeated for the resulting numbers. If the process results in a cycle that does not include 1, the number is not happy.

For example, 19 is a happy number. Here's why:

- 1² + 9² = 82
- 8² + 2² = 68
- 6² + 8² = 100
- 1² + 0² + 0² = 1

## Project Structure

```
Happy-Numbers/
│
├── src/
│   ├── main.py - The main checker file
│   ├── main.ipynb
│
├── README.md - This file
```

## Requirements

- Python 3.7+
- A basic understanding of Python and its core concepts

## Running the Code

```python
python src/main.py
```
