# Github Notes

## Resources

### Basics
- [Branching Standards and conventions](https://gist.github.com/digitaljhelms/4287848)
- [Forking](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
- [Style Guide](https://github.com/agis/git-style-guide)

### Open Source
- [Up for Grab - Open Source Project List](https://up-for-grabs.net/#/)
- [Licensing a repository](https://help.github.com/en/articles/licensing-a-repository)
- [Explore - Discover Projects on Github](https://github.com/explore)

## Useful Commands

### Branching

#### See branches

```
git branch
```
* Use -a flag to see all local and remote branches.

#### Switch to a branch

To switch and work on the branch.
```
git checkout [branch-name]
```

To switch and test the branch.
```
git checkout [origin/branch-name]
```

#### Create a branch

```
git checkout -b [new_branch_name]
```
To push the new branch to remote repo, enter
```
git push origin [new_branch_name]
```

#### Download branches

Download all branches.
```
git fetch --all
```

#### Delete a branch

Delete local branch.
```
git branch -d [new_branch_name]
```
Delete remote branch.
```
git push origin :[name_of_your_new_branch]
```

#### Merge to master
```
# in the branch directory
git merge master
```

### File Change
#### Revert file changes
```
# for single file
git checkout <filename>

# for all changes
git checkout .
```

#### Undo staged files (uncommited)
```
# for single file
git reset <filename>

# for all staging
git reset .
```

#### Undo commits (WARNING: Be careful when doing this)

```
# simply undo latest commit and leave files staged
git reset --soft HEAD~1

# simply undo latest commit & staging but leave files as they are
git reset HEAD~1

# undo both commits, staging, and file changes
git reset --hard HEAD~1
```

Reference: [Stack Overflow](https://stackoverflow.com/questions/927358/how-do-i-undo-the-most-recent-commits-in-git)

#### Remove remote files but save local files
```
# for single file
git rm --cached <myFile>

# for directory
git rm --cached -r <myFile>
```

Reference: [Stack Overflow](https://stackoverflow.com/questions/1143796/remove-a-file-from-a-git-repository-without-deleting-it-from-the-local-filesyste)

#### Remove local files
```
# check what files will be removed
git clean -n

# remove the files that are listed in the message from entering the command above
git clean -f

# remove untracked directories
git clean -fd

# remove ignored files as well
git clean -fX

# remove both untracked and ignored files
git clean -fx
```


## .gitignore
Git ignore is a way to tell Git to ignore local files.
This is helpful when you have files that you don't want to upload to the cloud (i.e. config files, test files, etc.).

To do this, create a **.gitignore** file in the project root directory and type in the file names you wish to ignore. Github provides a large amount of sample gitignore files which you can find [here](https://github.com/github/gitignore).
