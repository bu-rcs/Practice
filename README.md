# GitPractice
RCS Repository to practice Git commands and tools

### Setup SCC Environment
```{bash}
module load python3
```

### The Standard Pull Request Workflow
A Pull Request is not a Git feature; it's a feature of *GitHub* (or other hosting services like GitLab/Bitbucket) that asks for a review and merge of one remote branch (your temporary branch) into another remote branch (usually main).

**1. Create and Work on a Local Branch**
Before starting any changes, create a new local branch off your intended target branch (e.g., main).

```
# 1. Ensure you're on the latest code
git checkout main
git pull origin main

# 2. Create your temporary/feature branch
git checkout -b feature/my-new-feature
```

**2. Commit and Push the Branch**
As you make changes, commit them locally. When you're ready to propose them for review, you must push the branch to your GitHub remote. This is what makes the branch visible to GitHub and allows a PR to be created.

```
# Commit your changes
git add .
git commit -m "feat: finished the new feature logic"

# Push the local branch to the remote repository for the first time
git push -u origin feature/my-new-feature
```

**3. Create the Pull Request**

Once the branch is pushed, you have two primary ways to initiate the Pull Request on GitHub:

**Option A**: Using the Terminal Link (Fastest) The output from the git push command will almost always include a direct URL to create the pull request. You can copy this link and paste it into your browser.

```
...
* [new branch] feature/my-new-feature -> feature/my-new-feature
...
```

remote: Create a pull request for 'feature/my-new-feature' on GitHub by visiting:
remote:   https://github.com/YourOrg/YourRepo/pull/new/feature/my-new-feature

**Option B**: Using the GitHub UI Navigate to your repository's page on GitHub. A yellow banner will usually appear automatically, detecting the new branch you just pushed and offering a "Compare & pull request" button.

**4. Continuous Updates**
If you receive feedback and need to make more commits, you just continue to commit and push to the same branch.
The existing Pull Request will automatically update with the new commits and changes.

*******


### Working on GitHub Issue

The typical workflow for fixing a bug or implementing a feature tracked by a GitHub Issue is structured around the principle of isolating changes on a temporary branch before proposing them for review via a Pull Request (PR). This process ensures the main branch (main or master) remains stable and only contains approved, finished code.

**1. Sync Local Repository**: 

Always start by ensuring your local copy of the main branch is up to date with the remote.


```{bash}
git checkout main
git pull origin main
```

**2. Create Temporary Branch**: 

Create a new local branch based on main. A best practice is to include the Issue number and a short description in the branch name.

Example: For Issue #42, fixing a bug.

```{bash}
git checkout -b fix/42-negative-log
```

You can often click a "Create a branch" button directly on the GitHub Issue page. GitHub will suggest a branch name and automatically set it up for linking.


**3. Work on the feature or fix locally**

- Make Changes: Write code to address the problem described in the Issue.
- Commit Changes: Stage your changes and create commits. It's often helpful to mention the Issue number in your commit message, especially the final one.

```{bash}
git add .
git commit -m "fix: fixing a bug (logarithm of a negative value) based on issue #42"
```
Clean Up History (*Optional*): If you have many small, messy commits, consider using interactive rebase (git rebase -i) to squash them into one clean, meaningful commit before pushing.

**4. Pushing and Pull Request (PR) Submission** 


Push the Branch: Upload your local branch and its history to the remote repository. The `-u` flag sets the upstream tracking branch for future pushes.

```{bash}
git push -u origin fix/42-negative-log
```

*Create the Pull Request (PR)*: After pushing, GitHub usually displays a yellow banner with a "Compare & pull request" button—click this to start the PR creation.

*Link to the Issue*: In the PR description, use a closing keyword and the Issue number to automatically close the Issue when the PR is merged.

Example closing keyword: **Closes #42** or **Fixes #42**.

*Submit PR*: Set the base branch (e.g., main) and the head branch (your temporary branch), add a descriptive title, assign reviewers, and click Create pull request (or Create Draft pull request if it's not ready).

*******

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
