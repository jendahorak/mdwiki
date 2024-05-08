# ✏ [[prime git lecture]]

# Man
Everything about git is in the manual pages on every linux based system. 
`man man`, `man git`

![[Pasted image 20240321210642.png]]

**Bold** - type exactly as shown 

# Terminology

Distributed version control system. Before it was centralized, one person had a file and if he was on vacation it was "locked". 
In git you have your version. 

In gits there are two types of commands:
1. Porcelain commands
2. Plumbing commands

**repo** - something that has a .git folder in it, therefore is actively tracked by git
**commit** - a point in time representing the project in its entirety - sha for commit is 40 a-f 0-9 chars. calculated from contents of change, author, time and more
**index** / *staging area* - git index is critical data structure it is a staging area between the files localy and your commit history `git add .` files from working directory are hashed and stroed as objects in the index. 
**squash** - taking n commits and squashing them to n-1
**worktree** - your git repo - setup by `git init` or `git clone`
## Flow of git

Files in git repo are in one of these baskets:
Untracked -> Staging -> Tracked


## Facts

- git is acyclic graph 
- each commit is a node in a graph, each pointer  is the child to parent rel, there can be no cycle
- deleting untracked files means that they are gone forever (*commit often and early*), lot of commits doesn't mean messy history - history can be managed by **squashing** commits.
- `man git-<op>` - is good
- most of git is: git pull, add, commit, push, status, this is good but sometimes you fu** up and then you have to google git rebase or worse and you cry
- *why git* - most of the difficulty about computer engineering is not the code itself but the code from the past and collaboration with other people who wrote it (including your past self)

# config

Something done when setting up computer, and forgotten. 

Type of configs: **global** x **local** (there are more)

![[Pasted image 20240321223017.png]]


- all git config keys are in shape `<section>.<key>`
- `--global` setting is for all projects
-  `user.name` and `user.email` these keys are used to create a commit tied to these keys (past you)
- to add a key you: `git config --add --global <key> "<value>"`

@todo - if  `git config --get user.name` returns empty just add `user.name`, `user.email`

```bash
git config --agg -global user.name "YourName"
git config --agg -global user.email "YourEmail"
```

# create a repo

`git init` - adds a .git folder into current directory every git repo has a `.git` folder, all the data structures live here

# the basics

`git add <path-to-file | pattern>` - will add zero or more file to the index (*staging area*)
`git commit -m "<message>"` - will commit changes presented in in the index
`git status` - will describe the state of your git repository which will include tracked, staged and untracked files 

Lets look at the journey of the file thru git stages.

1. create a file `whatever.md`
2. check the status
3. add the file into a index
4. check the status
5. commit with a message ("batman" - its a first commit) 
6. check the status

Now you have a commit. 

## check what changes have been made

`git-log`

lets read something about git log `man git log` especially about `--graph` and `--decorate`

- what  is a ref name? - well everything is a commit everything has a sha and we can reference those commits with some named item (branches, tags, head etc.) 

# how git works

- sha
- to reference via sha first 7 chars are needed, rest is automatic
- `git log` - is the way how to get sha `--graph` `--decorate` (make it look better)
- commits live in .git/objects directory with their shas first two letters as a name of directory and the rest as a file

This is very fine wrist rest and i love it however it needs to be little more slanted


