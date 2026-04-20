| Keyword    | Use              |
| ---------- | ---------------- |
| subarray   | prefix / sliding |
| k times    | heap             |
| max/min    | greedy           |
| frequency  | Counter          |
| duplicates | set/dict         |

## 1.n ≤ 10^5
cannot use O(n²)

## 2.n ≤ 500
brute force OK

----------
subarray → prefix

k operations → heap

maximize/minimize → greedy

frequency → Counter

--------------
# How to recognize “simulate” questions

Look for words like:

“perform q queries”,
“apply operation”,
“update array”,
“assign values”,
“do this step by step”,

If you see this → just use loops
