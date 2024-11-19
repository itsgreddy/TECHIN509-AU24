# TECHIN509-AU24-Week6

## Introduction to GIT

### Creating a new Git Repo

```
git init
```

### To know the state of working directory and the staging area

```
git status
```

### Adding 'ALL' the changes that has been made to the file.

The '.' represents all files in the current directory

```
git add .
```

### Creating a commit

The '-m' is used to tag an message along with the commit. This helps to keep tracks of the commits and makes it easier for us to debug in future

```
git commit -m "<the message here>"
```

### To remotely add the repo link

```
git remote add <name> <url>
```

### To know which branch you are in right now

```
git branch
```

### Pushing the branch or commit to github

```
git push <name> <branch>
```

### If working with others and you want other's work to reflect on your local computer

Git pull fetches the changes as well as merges them afterwards

```
git pull <name> <branch>
```

### To have more control we can use fetch instead of git pull

This command gives you the ability to initially review before merging. It stores them in local repo

```
git fetch <remote> <branch>
```

### Later now we can then make the merge to our required branch

```
git merge <branch_name>
```

### To view all the commits and all changes to the git repo

```
git log
```
