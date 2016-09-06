# Genetic-Algorithm
This is a simple genetic algorithm written in Python3. I wrote this script based on the AI Junkie article, which you can read here: http://www.ai-junkie.com/ga/intro/gat1.html

## What does it do?
This script solves the problem presented in the AI Junkie Genetic Algorithm article:

"Given the digits 0 through 9 and the operators +, -, * and /,  find a sequence that will represent a given target number. The operators will be applied sequentially from left to right as you read." (page 3)

Additional information:

1. Result follows the pattern: number -> operator -> number -> operator -> number...
2. Invalid genes are ignored
3. Divide by zero is solved by ignoring '0' when following a '/'

### Example output:
Randomly generated number: 710

Possible solution: 5 * 7 + 1 + 1 + 1 - 8 + 8 * 4 + 0 * 7 * 6 * 1 + 6 / 9 = 710.0

Note: This is an actual result from this script. It is not optimized for short solutions.

## How to Use:
```py geneticalgorithm.py```

This script is not meant to be used as a module. I wrote this for learning purposes. The code is messy and tied to the problem presented in the AI Junkie article.
