# Github Notes

## Resources

- [Branching Standards and conventions](https://gist.github.com/digitaljhelms/4287848)
- [Forking](https://gist.github.com/Chaser324/ce0505fbed06b947d962)
- [Style Guide](https://github.com/agis/git-style-guide)
- [Up for Grab - Open Source Project List](https://up-for-grabs.net/#/)
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
