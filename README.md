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

To see the changes that you have already moved to the staging area (ready to be committed):
```{bash}
git diff --staged
# or
git diff --cached
```

*******


If you are working in the **VSCode**, click the Git icon on the side bar and then click the name of the modified file
you would like to review:

- The left side is the file as it exists in the last commit (or the Staging Area for unstaged changes).
- The right side is your current modified working file.

If you use **vim** as your code editor, you can set your difftool to use vim:

```{bash}
git config --global diff.tool vimdiff
git config --global difftool.prompt false
```
*******


### Updating the last commit message or adding forgotten files

```{bash}
git commit --amend -m "Your new, corrected commit message here"
```

If you need to add some files to your last commit:
```{bash}
# Stage the specific file(s) you forgot
git add <file1> <file2>

# OR, to stage all tracked, modified files:
# git add .

#
git commit --amend --no-edit
```


Since amending a commit changes the commit's history (it gets a brand new `SHA-1` hash), you should **NEVER** amend a commit that has already been pushed to a shared remote repository and possibly pulled by other developers.

If you must amend a commit that has already been pushed, you will need to force-push the change, which is generally discouraged:
```{bash}
git push --force-with-lease origin <your-branch-name>
```

The `--force-with-lease` option adds a crucial safety check before overwriting the remote branch. This effectively means: "I want to force push, but only if no one else has pushed any new commits to the remote branch since I last fetched."

The `--force` option is a command of pure power that unconditionally overwrites the remote branch. It overwrites the remote branch with your local branch's history, regardless of what has happened on the remote since your last fetch. If another developer has pushed new commits to that same branch (commits you don't have locally), `--force` will wipe out their commits completely and permanently from the remote repository without warning.

### Squashing small commits

To squash the **last 3 commits**:
```{bash}
git rebase -i HEAD~3
```

To squash all commits on your current feature branch back to where it split from main
```{bash}
git rebase -i main
```

After running the command, an editor (like Vim) will open with a list of the commits you selected. This list is in reverse chronological order (oldest commit at the top).

```
pick a4b5c6d First working feature commit
pick 1e2f3g4 Minor fix: change variable name
pick 5h6i7j8 Add documentation for feature
#
# Commands:
# p, pick = use commit
# r, reword = use commit, but edit the commit message
# e, edit = use commit, but stop for amending
# s, squash = use commit, but meld into previous commit
# f, fixup = like "squash", but discard this commit's log message
# ...
```

To squash the commits:

- Leave the first (oldest) commit as pick. This commit will become the base, or the final, single commit.
- Change pick to squash (or s) for all subsequent commits you want to combine into the first one.

```
pick a4b5c6d First working feature commit  <-- This one REMAINS 'pick'
squash 1e2f3g4 Minor fix: change variable name
squash 5h6i7j8 Add documentation for feature
```


1. Save and close the editor file.
2. *Git* will then combine the changes and immediately open the editor a second time. This time, it contains the combined messages of all the commits you marked as pick and squash.
3. Delete the individual messages and write a single, clean, and descriptive commit message that summarizes all the changes being combined.
4. Save and close this final editor file.