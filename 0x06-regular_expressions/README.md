# Regular Expression - DevOps

## Overview

This repository contains the solutions to the Regular Expression project in the DevOps course. 
The project aims to test your knowledge and skills in using Regular Expressions with the Oniguruma library, which is commonly used in Ruby.

## Concepts

In this project, you will learn about:
- Regular Expressions
- Oniguruma library
- Using regex in Ruby

## Requirements

- Operating System: Ubuntu 20.04 LTS
- Editors: vi, vim, emacs
- All files should end with a new line
- All Bash scripts must be executable
- The first line of each Bash script should be `#!/usr/bin/env ruby`
- The regex must be built for the Oniguruma library

## Tasks

The project consists of several tasks, where i am required to create Ruby scripts that match specific regular expression patterns. 
Each task comes with clear requirements and examples.

## Resources

To help you with the project, you can refer to the following resources:
- [Regular Expressions - Basics](https://example.com/regex_basics)
- [Regular Expressions - Advanced](https://example.com/regex_advanced)
- [Rubular - Regular Expression Testing](https://rubular.com/)
- [Use a regular expression against a problem: now you have 2 problems](https://example.com/regex_problem)
- [Learn Regular Expressions with simple, interactive exercises](https://example.com/regex_exercises)

## Getting Started

1. Clone this repository to your local machine.
2. Go to the appropriate directory for the task you want to work on.
3. Open the Ruby script and replace `/your-regex-goes-here/` with your regular expression code.
4. Run the Ruby script with appropriate arguments to test your regex.

## Example

For Task 0, you can use the provided Ruby script `0-simply_match_school.rb` as follows:
```bash
$ ./0-simply_match_school.rb School | cat -e
School$
$ ./0-simply_match_school.rb "Best School" | cat -e
School$
$ ./0-simply_match_school.rb "School Best School" | cat -e
SchoolSchool$
$ ./0-simply_match_school.rb "Grace Hopper" | cat -e
$
```

## Auto Review

An auto review will be launched at the deadline to ensure that your solutions meet the requirements.

## Conclusion

Regular expressions are powerful tools for pattern matching and text manipulation. By completing this project, 
you will improve your regex skills and gain confidence in using them in your future DevOps projects.

Good luck with the tasks!

---
**Note:** This README provides an overview of the project. Please refer to the individual task files for detailed instructions and requirements.
