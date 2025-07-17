# git - level 0

Introduction to git.

---
## scales of Git

On a scale of 0..9, how good are you at git?

           0                                                     9
           |-----------------------------------------------------|

          🤷‍♂️                                                    🚀
"I've heard of Github"                        "I use git bisect to to debug my code"
---
## my teaching style

- bottom up
- building blocks & tools
- conversational
- example driven, for example:
```python
import datetime

print(f"The time is {datetime.datetime.now()}")
```

---
## covering today

- problems
- intro
- language
- git for agentic ai
- init
- hash
- commit
- staging
- navigation
- ref
- branch
- tag
- merge
- conflict
- remote
- clone
- workflows
- resources


---
## what problems are we trying to solve?

Does this look familiar?

```
/Users/ferdz/Dev/my_data_proj/

- script.py
- script_working_version.py
- script_cleanup.py
- final_script.py
- final_script_v2.py
```
---
## what problems are we trying to solve?

Does this look familiar?

```python
import boto3

try:
    session = boto3.Session(
        aws_access_key_id:="AHjdflhah9875a",
        aws_secret_access_key:="halksdfoa876s8df5a8s5df8a",
        region_name="af-south-1",
    )
    s3 = session.client("s3")

    resp = s3.get_object(Bucket="my-bucket", Key="my-file.txt")

    with open("/Users/ferdz/Dev/workshops/dump/my-file.txt", "w") as f:
        file_bytes = resp["Body"].read()
        f.write(file_bytes)

except Exception as e:
    print(f"ERROR: {e}")
```

---
## what problems are we trying to solve?

* Complexity of managing versions of our code.
* Difficulty of collaborating on code.

---
## what is git?
### according to the Docs

> git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency. - [docs](https://git-scm.com)
---
## what is git?
### practically

> Git is a little programme that mostly just keeps track of changes in your files. It allows you to create *snapshots* of your files at different points in time. It also enables you to travel back & forth between snapshots, as well as sync those snapshots to other machines. Should your snapshots look different to your colleague's snapshot, git will try its very best to fix the differences. If git can't fix the differences, it might ask you to help a bit. - Ferdi

---
## what is git?
### another mental model

I like to think of git as a little database that lives right by my code. Let's go poke around in the database.

---
```
~~~bash
pwd
~~~
```

```bash
ls
```

---

```
~~~bash
pwd
~~~
```

```bash
ls -a
```

---
```
~~~bash
pwd
~~~
```

```bash
ls .git
```

---
Why getting started with git sucks...
## the language
- tag
- diff
- push
- pull
- HEAD
- hash
- fetch
- merge
- branch
- remote
- rebase
- bisect
- reflog
- commit
- origin
- staging
- checkout
- conflict
- detached HEAD state

---
## git for agentic ai

Why do we need git when agents can do all the coding for us?

---
## init

To get started, run `git init`.

---
## ignore

Why do we want to exclude things from git?

---
## the hash

> A hash function is a mathematical algorithm that maps data of any size to a fixed-size value, called a hash value or hash, ensuring that even small changes in the input result in a significantly different output

---
## the hash

```python
import hashlib

def print_hash(data):
    hash = hashlib.sha1()
    hash.update(bytes(data))
    digest = hash.digest()
    print(digest.hex())

print_hash([100, 210, 150, 0, 132])
print_hash([100, 210, 150, 1, 132])
print_hash([100, 210, 150, 1, 132, 184, 21, 42, 89, 101, 132, 45])
print_hash([100, 210, 150, 0, 132])


```

---
## the hash

Does the python file contain any data?

```python
with open("main.py", "rb") as f:
    file_bytes = f.read()
    print(list(file_bytes))
```


---
## the hash

```python
import hashlib

hash = hashlib.sha1()

with open("main.py", "rb") as f:
    hash.update(f.read())
    digest = hash.digest()
    print(digest.hex())
```

---
## the commit

```
┌────────────────────────────────────────────────┐
│                       c2                       │
│                                                │
│    ca9be885d9c7cf84790a46c06609d19b3e635b4d    │
└────────────────────────────────────────────────┘
                         │                            ┌────────────────────────┐
                         ▼                            │                        │
┌────────────────────────────────────────────────┐    │- files                 │
│                       c1                       │    │- author                │
│                                                │    │- timestamp             │
│    19dfdb250bc2e51be26ce19e57255fce4b8e47fe    │    │- parent commit(s)      │
└────────────────────────────────────────────────┘    │- message               │
                         │                            │                        │
                         ▼                            └────────────────────────┘
┌────────────────────────────────────────────────┐
│                       c0                       │
│                                                │
│    dbc6712ff0968b604fd02293f4676f32de1b030e    │
└────────────────────────────────────────────────┘
```
---
## What's in a hash?
```
┌───────────┐
│   files   │───┐
└───────────┘   │
┌───────────┐   │
│  author   │───┤
└───────────┘   │   ┌──────────────────┐
┌───────────┐   │   │                  │       ┌──────────────────────────────────────────┐
│ timestamp │───┼──▶│    sha1 hash     │──────▶│ ca9be885d9c7cf84790a46c06609d19b3e635b4d │
└───────────┘   │   │                  │       └──────────────────────────────────────────┘
┌───────────┐   │   └──────────────────┘
│ parent(s) │───┤
└───────────┘   │
┌───────────┐   │
│  message  │───┘
└───────────┘
```

---
## Staging

```
┌───working directory────┐              ┌─────── staging ────────┐              ┌───────repository ──────┐
│                        │              │                        │              │                        │
│                        │              │                        │              │        ┌───┐           │
│   ┌────────────────┐   │              │      ┌────────────┐    │              │        └─┬─┘           │
│   └────────────────┘   │              │    ┌─┴──────────┐ │    │              │          │             │
│   ┌────────────┐       │              │    │            │ │    │              │          ▼             │
│   └────────────┘       │              │    │  snapshot  │ │    │              │        ┌───┐           │
│   ┌──────────────┐     │─────add─────▶│    │            │ │    │─────commit──▶│        └─┬─┘           │
│   └──────────────┘     │              │    │            ├─┘    │              │          │             │
│   ┌───────────────┐    │              │    └────────────┘      │              │          ▼             │
│   └───────────────┘    │              │                        │              │        ┌───┐           │
│                        │              │                        │              │        └───┘           │
│                        │              │                        │              │                        │
└────────────────────────┘              └────────────────────────┘              └────────────────────────┘
             ▲                                       ▲                                  ▲
             │                                       │                                  └────┐
             │                                    ┌──┘                                       │
             │                                    │                                          │
   changes on your local                          │                                once commits are
   file system                          area where you can                         stored, they are
                                        logically group                            immutable forever
                                        changes into packages
                                        called "commits"
```

---
## Navigation
```

                                                             ╔══════════╗
                                                             ║   HEAD   ║
                                                             ╚══════════╝
                                                                   │
                                                                   │
                                                                   │
                                                                   ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘


────────────────────────────────timeline────────────────────────────────▶

```

---
## Detached Head State

```

                                                             ╔══════════╗
                                                             ║   HEAD   ║
                                                             ╚══════════╝
                                                                   │
                          ┌────────────────────────────────────────┘
                          │
                          ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘


────────────────────────────────timeline────────────────────────────────▶
```
---
## Ref(erences)

- HEAD
- Branch
- Tag
- Remote

---
## Branch

```
    main
      │
      │
      │
      ▼
┌───────────┐
│   root    │
└───────────┘
```

---

## Branch

```
                        main
                          │
                          │
                          │
                          ▼
┌───────────┐       ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │
└───────────┘       └───────────┘
```

---

## Branch

```
                                            main
                                              │
                                              │
                                              │
                                              ▼
┌───────────┐       ┌───────────┐       ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │
└───────────┘       └───────────┘       └───────────┘
```

---
## Branch

```
                                                                  main
                                                                    │
                                                                    │
                                                                    │
                                                                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘
```

---

## Branching Off

```
                                                                  main
                                                                    │
                                                                    │
                                                                    │
                                                                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘
                          ▲
                          │
                          │
                          │   ╔══════════╗
                          └───║   HEAD   ║
                              ╚══════════╝
```
---
## Branching Off

```
                                                                  main
                                                                    │
                                                                    │
                                                                    │
                                                                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘
                          ▲
                          │
                          │
                          │  ┌───────────┐         ╔══════════╗
                          └──│  432999f  │◀────────║   HEAD   ║
                             └───────────┘         ╚══════════╝
```

---
## Branching Off

```
                                                                  main
                                                                    │
                                                                    │
                                                                    │
                                                                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘
                          ▲
                          │
                          │
                          │  ┌───────────┐
                          └──│  432999f  │◀──────── feat/1
                             └───────────┘
```
---
## Tags

```
    main
      │
      │
      │
      ▼
┌───────────┐
│   root    │
└───────────┘
```
---
## Tags

```
                        main
                          │
                          │
                          │
                          ▼
┌───────────┐       ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │
└───────────┘       └───────────┘
```
---
## Tags

```
                        main
                          │
                          │
                          │
                          ▼
┌───────────┐       ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │
└───────────┘       └───────────┘
                          ▲
                          │
                          │
                  ┌ ─ ─ ─ ─ ─ ─ ─
                    release-v1.3 │
                  └ ─ ─ ─ ─ ─ ─ ─
```
---
## Tags

```
                                            main
                                              │
                                              │
                                              │
                                              ▼
┌───────────┐       ┌───────────┐       ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │
└───────────┘       └───────────┘       └───────────┘
                          ▲
                          │
                          │
                  ┌ ─ ─ ─ ─ ─ ─ ─
                    release-v1.3 │
                  └ ─ ─ ─ ─ ─ ─ ─
```
---
## Tags

```
                                                                  main
                                                                    │
                                                                    │
                                                                    │
                                                                    ▼
┌───────────┐       ┌───────────┐       ┌───────────┐        ┌───────────┐
│   root    │ ◀─────│  5ebbfdd  │◀──────│  c39294e  │ ◀──────│  fb49033  │
└───────────┘       └───────────┘       └───────────┘        └───────────┘
                          ▲
                          │
                          │
                  ┌ ─ ─ ─ ─ ─ ─ ─
                    release-v1.3 │
                  └ ─ ─ ─ ─ ─ ─ ─
```
---
## Combining Diverged Branches

- Merge
- ~~Rebase~~
- ~~Squash~~
---
## Merge

```
                                        ┌───────────┐            ┌───────────┐
                         ┌──────────────│  5ebbfdd  │◀───────────│  9f53cd9  │◀─────────────────┐
                         │              └───────────┘            └───────────┘                  │
                         │                                                                      │
                         ▼                                                                      │
┌───────────┐      ┌───────────┐      ┌───────────┐                  ┌───────────┐        ┌───────────┐       ┌───────────┐
│   root    │ ◀────│  5ebbfdd  │ ◀────│  c39294e  │◀─────────────────│  fb49033  │◀───────│  3fa6a03  │ ◀─────│  1c729e2  │
└───────────┘      └───────────┘      └───────────┘                  └───────────┘        └───────────┘       └───────────┘
                                            ▲                              │
                                            │                              │
                                            │          ┌───────────┐       │
                                            └──────────│  5ebbfdd  │◀──────┘
                                                       └───────────┘
```

---
## Merge Conflict

Run through a merge conflict resolution.

```
<<<<<<< HEAD
    print("Hello")
=======
    print("World")
>>>>>>> incoming_branch
```
---
## Remote

How do we share work with our peers?

---
## Distributed Git

```
   ┌─────────────────────┐
   │                     │
   │                     │
┌──│         Me          │◀─┐
│  │                     │  │
│  │                     │  │
│  └─────────────────────┘  │
│                           │
│                           │
│                           │
│                           │
│                           │
│  ┌─────────────────────┐  │
│  │                     │  │
│  │                     │  │
└─▶│         You         │──┘
   │                     │
   │                     │
   └─────────────────────┘
```
---
## Distributed Git

```
                                  ┌────────────────────┐
   ┌─────────────────────┐        │                    │
   │                     │        │                    ▼
   │                     │        │         ┌─────────────────────┐
┌──│         Me          │────────┘         │                     │
│  │                     │                  │                     │
│  │                     │                  │       And You       │──┐
│  └─────────────────────┘                  │                     │  │
│             ▲                             │                     │  │
│             │                             └─────────────────────┘  │
│             │                                                      │
│             │                                                      │
│             └───────────────────────────────────┐                  │
│  ┌─────────────────────┐                        │                  │
│  │                     │                        │                  │
│  │                     │                        │                  │
└─▶│         You         │                        │                  │
   │                     │             ┌─────────────────────┐       │
   │                     │             │                     │       │
   └─────────────────────┘             │                     │       │
              │                        │       And You       │◀──────┘
              │                        │                     │
              │                        │                     │
              │                        └─────────────────────┘
              │                                   ▲
              │                                   │
              └───────────────────────────────────┘
```
---
## Centralised Server

```
                      ┌────────────────────────────┐
                      │                            │
                      │       remote server        │
           ┌─────────▶│                            │◀───────────┐
           │          │          (origin)          │            │
           │          │                            │            │
           │          └────────────────────────────┘            │
           │                          ▲                         │
           │                          │                         │
           │                          │                         │
           │                          │                         │
           │                          │                         │
           ▼                          ▼                         ▼
┌────────────────────┐     ┌────────────────────┐    ┌────────────────────┐
│                    │     │                    │    │                    │
│         Me         │     │        You         │    │      And you       │
│                    │     │                    │    │                    │
└────────────────────┘     └────────────────────┘    └────────────────────┘
```

> Remember: git is fully distributed, each participant has a FULL copy of the repo.
---
## Push & Pull

```
                      ┌────────────────────────────┐
                      │                            │
                      │       remote server        │
           ┌─────────▶│                            │────────────┐
           │          │          (origin)          │            │
           │          │                            │            │
           │          └────────────────────────────┘            │
           │                          │                         │
          PUSH                        │                        PULL
           │                          │                         │
           │                          │                         │
           │                          │                         │
           │                          ▼                         ▼
┌────────────────────┐     ┌────────────────────┐    ┌────────────────────┐
│                    │     │                    │    │                    │
│         Me         │     │        You         │    │      And you       │
│                    │     │                    │    │                    │
└────────────────────┘     └────────────────────┘    └────────────────────┘
```

> When speaking from the perspective of a local repo,
> we call the remote ranches by the remote alias first
---
## Clone

How to get a repo locally.

---
## Remote Tracking

```

┌─────────────────────────────────┐                       ┌─────────────────────────────────┐
│                                 │                       │                                 │
│                                 │                       │                                 │
│                       ┌─────────┤                       ├─────────┐                       │
│                       │  main   ├─────────────────────▶ │  main   │                       │
│                       └─────────┤                       ├─────────┘                       │
│                                 │                       │                                 │
│                                 │                       │                                 │
│                                 │                       │                                 │
│                                 │                       │           Remote Repo           │
│             My Repo             │                       │            (origin)             │
│                                 │                       │                                 │
│                                 │                       │                                 │
│                                 │                       │                                 │
│                                 │                       │                                 │
│                       ┌─────────┤                       ├─────────┐                       │
│                       │ feat/1  │─────────────────────▶ │ feat/1  │                       │
│                       └─────────┤                       ├─────────┘                       │
│                                 │                       │                                 │
│                                 │                       │                                 │
└─────────────────────────────────┘                       └─────────────────────────────────┘
```

> When speaking from the perspective of a local repo,
> we call the remote branches by the remote alias first,
> eg. main is tracking origin main

---
## Workflows

- [Gitflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow)
- [Github Flow](https://docs.github.com/en/get-started/using-github/github-flow)
- [Trunk Based Development (TBD)](https://trunkbaseddevelopment.com/)
---
## Github Flow

```
                                                                     Remote Repo
┌─────────   My Repo   ───────────┐                       ┌───────     (origin)     ────────┐
│                                 │                       │                                 │
│                                 │                       │                                 │
│                       ┌─────────┤                       ├─────────┐                       │
│                       │  main   │                       │  main   │◀─┐                    │
│                       └─────────┤                       ├─────────┘  │                    │
│                                 │                       │            │                    │         ┌────────────────────────────────────────────┐
│                                 │                       │            │                    │         │                                            │░
│                                 │                       │                                 │         │  Step 2 is called a Pull Request OR Merge  │░
│                                 │                       │    3. Maintainer merges         │         │ Request. This is NOT a git feature. It is, │░
│                                 │                       │          branch.                │         │   however, a common git service provider   │░
│                                 │                       │                                 │         │                  feature.                  │░
│                                 │                       │            │                    │         │                                            │░
│                                 │                       │            │                    │         │                                            │░
│                                 │                       │            │                    │         └────────────────────────────────────────────┘░
│                       ┌─────────┤                       ├─────────┐  │                    │          ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
│                       │ feat/1  │───1. Push Changes───▶ │ feat/1  │──┘                    │
│                       └─────────┤                       ├─────────┘                       │
│                                 │                       │                                 │
│                                 │                       │                                 │
└─────────────────────────────────┘                       └─────────────────────────────────┘
                 │                                                         ▲
                 │                                                         │
                 └───────2. "Hey, I've added some changes to feat/1 ───────┘
                        branch. Could you please review them and then
                                merge into the main branch?"
```

---
## Resources

- [Docs](https://git-scm.com)
- [OhShitGit](https://ohshitgit.com/)
- [Git by example](https://antonz.org/git-by-example/)
- [House Keeping](https://railsware.com/blog/git-clean-up-in-local-and-remote-branches/)
- Just use the tool.
