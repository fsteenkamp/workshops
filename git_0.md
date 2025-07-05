# Git Level 0

Introduction to git.

---

## Scales of Git
On a scale of 0..9, how good are you at git?

           0                                                     9
           |-----------------------------------------------------|

"I've heard of Github"                "I use git bisect to find the commit that introduced a bug"

---

```python
def add(a, b):
    return a+b

print(add(4, 9))

```

---
## Looking at the problem

```go
package main

import "fmt"
import "time"

func main() {
  fmt.Println("Execute code directly inside the slides")
  fmt.Println(time.Now())
}
```
=====

=>
---
## Looking at the problem

```python
import boto3
import pyarrow.compute as pc

try:
    session = boto3.Session(
        aws_access_key_id:="AHjdflhah9875a",
        aws_secret_access_key:="halksdfoa876s8df5a8s5df8a",
        region_name="af-south-1",
    )
    s3 = boto3.client("s3")

    resp = s3.get_object(Bucket="my-bucket", Key="my-file.txt")
    with open("/Users/ferdz/Desktop/workshops/output/my-file.txt") as f:
        f.write(resp["Body"])

    trip_df = duckdb.sql("""
SELECT id, first_name, last_name, trip_date, distance FROM
parquet("my_bucket/my_key.parquet")
ORDER BY
    triP_date;
""").arrow()

    print(trip_df.schema())

    distance_col = trip_df.col("distance")
    print(pc.sum(distance_col))

except Exception as e:
    print(e)
```

---
## What is git?


> Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

git-scm.com

---

## Everything happens in your terminal
Create slides and present them without ever leaving your terminal.

---

## Code execution
```go
package main

import "fmt"

func main() {
  fmt.Println("Execute code directly inside the slides")
}
```

You can execute code inside your slides by pressing `<C-e>`,
the output of your command will be displayed at the end of the current slide.

---

## Pre-process slides

You can add a code block with three tildes (`~`) and write a command to run *before* displaying
the slides, the text inside the code block will be passed as `stdin` to the command
and the code block will be replaced with the `stdout` of the command.

```
~~~graph-easy --as=boxart
[ A ] - to -> [ B ]
~~~
```

The above will be pre-processed to look like:

┌───┐  to   ┌───┐
│ A │ ────> │ B │
└───┘       └───┘

For security reasons, you must pass a file that has execution permissions
for the slides to be pre-processed. You can use `chmod` to add these permissions.

```bash
chmod +x file.md
```
