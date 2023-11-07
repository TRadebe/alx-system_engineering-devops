# Reddit API Project

This project aims to enhance your skills in working with the Reddit API, focusing on various aspects such as querying the 
number of subscribers, fetching the top posts, and creating a recursive function to retrieve all hot articles in a subreddit.

## Learning Objectives

Upon completion of this project, you should be able to:

- Read API documentation to identify endpoints.
- Use an API with pagination to handle large datasets.
- Parse JSON results obtained from an API.
- Make recursive API calls for more efficient data retrieval.
- Sort a dictionary by its values.

## Requirements

### General

- **Editors:** Allowed editors include vi, vim, and emacs.
- **Interpreter/Compiler:** All files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3 (version 3.4.3).
- **New Line:** Ensure that all your files end with a new line.
- **Shebang:** The first line of all your files should be exactly `#!/usr/bin/python3`.
- **Library Organization:** Organize imported libraries in alphabetical order.
- **README.md:** A README.md file at the root of the project folder is mandatory.
- **PEP 8 Style:** Your code should follow the PEP 8 style guide.
- **Executable Files:** All your files must be executable.
- **File Length:** The length of your files will be tested using `wc`.
- **Documentation in Modules:** All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
- **Requests Module:** Use the Requests module for sending HTTP requests to the Reddit API.

### Tasks

#### Task 0: How many subs?

Write a function (`number_of_subscribers`) that queries the Reddit API and returns the number of subscribers for a given subreddit. 
If an invalid subreddit is provided, the function should return 0.

**Requirements:**

- Prototype: `def number_of_subscribers(subreddit)`
- Return 0 if the subreddit is not valid.
- Handle potential errors related to Too Many Requests by setting a custom User-Agent.

```python
#!/usr/bin/python3
"""
0-subs
"""
import sys

if __name__ == '__main__':
    number_of_subscribers = __import__('0-subs').number_of_subscribers
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
```

#### Task 1: Top Ten

Write a function (`top_ten`) that queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit.

**Requirements:**

- Prototype: `def top_ten(subreddit)`
- Print None if the subreddit is not valid.

```python
#!/usr/bin/python3
"""
1-top_ten
"""
import sys

if __name__ == '__main__':
    top_ten = __import__('1-top_ten').top_ten
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
```

#### Task 2: Recurse it!

Write a recursive function (`recurse`) that queries the Reddit API and returns a list containing the titles of all hot articles 
for a given subreddit. Return None if no results are found.

**Requirements:**

- Prototype: `def recurse(subreddit, hot_list=[])`
- If the subreddit is not valid, return None.
- Use recursion for more efficient data retrieval.

```python
#!/usr/bin/python3
"""
2-recurse
"""
import sys

if __name__ == '__main__':
    recurse = __import__('2-recurse').recurse
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        result = recurse(sys.argv[1])
        if result is not None:
            print(len(result))
        else:
            print("None")
```
