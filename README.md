# leetcode

Twenty-one problems, solved once and left where they fell. No write-ups, no second passes, no "optimal" rewrite when the first one already returned the right answer. The filename is the problem number; that's the whole filing system.

## What it does

It holds solutions, by problem number, in two languages — sixteen Python files and five SQL ones. A slow drip over time: some easy, some medium, nothing chosen to look clever. Each file is one answer that worked the day it was written. The point was never the best solution to problem 135. It was getting 135 to pass and moving on.

There's no application here. The directory is flat, the names tell you what's inside, and the only running code is the one script that checks the archive hasn't rotted.

## The index

| # | problem | language |
|---|---|---|
| 1   | two sum                              | py  |
| 76  | minimum window substring             | py  |
| 135 | candy                                | py  |
| 177 | nth highest salary                   | sql |
| 182 | duplicate emails                     | sql |
| 183 | customers who never order            | sql |
| 196 | delete duplicate emails              | sql |
| 231 | power of two                         | py  |
| 326 | power of three                       | py  |
| 344 | reverse string                       | py  |
| 406 | queue reconstruction by height       | py  |
| 595 | big countries                        | sql |
| 647 | palindromic substrings               | py  |
| 771 | jewels and stones                    | py  |
| 806 | number of lines to write string      | py  |
| 819 | most common word                     | py  |
| 836 | rectangle overlap                    | py  |
| 838 | push dominoes                        | py  |
| 856 | score of parentheses                 | py  |
| 890 | find and replace pattern             | py  |
| 893 | groups of special equivalent strings | py  |

## Verify

This is an archive, not a live app. The useful check is that every
committed solution still parses and every SQL answer is non-empty:

```bash
python scripts/validate_archive.py
```

Expected output:

```text
validated 16 python file(s) and 5 sql file(s)
```

Twenty-one in, twenty-one out. If the count ever drops, something rotted.

## Colophon

Archived. Not actively maintained. If you came looking for the canonical answer to problem `638`, it isn't here — that one never got solved, which is its own kind of entry.

[the basement, room 7](https://github.com/AthenaTheOwl)
