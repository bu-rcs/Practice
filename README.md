# Practice
RCS Repository to practice Git tools

### Setup terminal and OnDemand Environment
```{bash}
module load python3
```

### Uncommitted changes

to review the changes that have been done to the files (and has not been committed yet) with the last commit:
```{bash}
git diff
```

If you are working in the **VSCode(()), click the Git icon on the side bar and then click the name of the modified file
you would like to review:

- The left side is the file as it exists in the last commit (or the Staging Area for unstaged changes).
- The right side is your current modified working file.

If you use **vim** as your code editor, you can set your difftool to use vim:

```{bash}
git config --global diff.tool vimdiff
git config --global difftool.prompt false
```