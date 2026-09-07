# Git Basics: Get Around Without Getting Lost

Git is a tool that helps you track changes in files, especially when working on code or projects with others.

If you are new to programming, Git can feel confusing at first. The good news is that you do not need to memorize everything at once. You only need to understand a few core ideas:

- Git stores versions of your project
- Git helps you work with others
- Git lets you go back when something breaks
- Git keeps a clean history of what changed and when

This note explains the basics in a way that is easy for beginners to understand.

---

## 1. What is Git?

Git is a version control system.

That means it keeps track of changes in your files over time.

Imagine you are writing a report. You save it many times. Sometimes you want to:

- look back to an earlier version,
- compare versions,
- fix a mistake without destroying the good version,
- share your work with others.

Git does that for you.

You can use Git for:

- coding projects
- writing documents
- data analysis scripts
- team collaboration

---

## 2. Why do we need Git?

Without Git, a project may look like this:

- `report_final.docx`
- `report_final_v2.docx`
- `report_final_2024_09_07.docx`
- `report_final_last_final.docx`

This gets messy quickly.

Git gives you a cleaner way:

- each save is a version
- you can name versions clearly
- you can go back to any version
- you can see who changed what

This is extremely useful when:

- you work in a team,
- you want to try something new without losing your old work,
- you need to debug a mistake,
- you want a clear project history.

---

## 3. The Most Important Idea: Repository

A Git repository is simply a project folder that Git is tracking.

When you run Git in a folder, that folder becomes a repository.

Inside the repository, Git tracks files and records changes.

You can think of a repository as a project with a memory.

Example:

```bash
git init
```

This command creates a Git repository in the current folder.

---

## 4. Commit: Save a Snapshot

A commit is a saved version of your project.

It is like taking a snapshot of your files at one moment.

When you make a commit, Git records:

- what changed,
- when it changed,
- who changed it,
- a message describing the change.

Example:

```bash
git add README.md
git commit -m "Add project introduction"
```

This says:

- stage the file,
- create a commit with a message.

A good commit message is short and clear.

Examples:

- "Fix bug in data processing"
- "Add user login page"
- "Update README with setup steps"

---

## 5. Stage: Prepare Changes

Before a commit, changes are not automatically saved.

Git has a staging area.

This is like putting files in a box before finalizing the commit.

Example:

```bash
git add file1.py file2.py
```

This tells Git:

- these files are ready to be recorded in the next commit.

You can stage all files with:

```bash
git add .
```

Then commit them:

```bash
git commit -m "Add code for analysis"
```

Why staging matters:

- you can choose what to include in a commit,
- you do not have to commit every change at once,
- it gives you control over your project history.

---

## 6. Working Directory, Staging Area, and Repository

This is one of the hardest concepts for beginners, but it is important.

Git can be thought of as three main states:

1. Working directory
   - the files you are currently editing

2. Staging area
   - files ready to be saved in the next commit

3. Repository history
   - all committed versions

The flow is:

```text
Edit files -> git add -> git commit
```

So a file moves through stages:

- edited in the working folder,
- staged for the next commit,
- committed into the repository history.

---

## 7. Branches: Separate Lines of Work

A branch is a separate version of your project.

You can think of it as a parallel timeline.

For example:

- `main` branch = official version
- `feature-login` branch = work on a new login feature

This allows you to make changes without disturbing the main project.

Example:

```bash
git checkout -b feature-login
```

or in newer Git:

```bash
git switch -c feature-login
```

Then you can work on new ideas safely.

When the feature is ready, you merge it back into the main branch.

---

## 8. Merge: Combine Work

Merging means combining changes from one branch into another.

Example:

```bash
git switch main
git merge feature-login
```

This brings the feature branch into the main branch.

Sometimes there are conflicts.

A conflict happens when both branches changed the same line in a file.

Git stops and asks you to decide which version should remain.

This is normal and part of teamwork.

---

## 9. Remote Repository: GitHub and Others

Git can work on your own computer, but teams usually store projects on a remote server such as GitHub.

A remote repository is a copy of your project hosted somewhere else.

Typical workflow:

```bash
git remote add origin https://github.com/yourname/project.git
git push -u origin main
```

This sends your local commits to GitHub.

You can also download others' work:

```bash
git pull
```

Or bring a copy from GitHub:

```bash
git clone https://github.com/yourname/project.git
```

This is one reason Git is so useful: it makes teamwork and backup easier.

---

## 10. Push and Pull

### Push

```bash
git push
```

This uploads your local commits to the remote repository.

### Pull

```bash
git pull
```

This downloads updates from the remote repository and merges them into your local project.

These commands are essential when working with others.

---

## 11. Status: See What Changed

This is a very useful command:

```bash
git status
```

It tells you:

- which files are modified,
- which files are staged,
- which branch you are on,
- whether your project is ahead or behind the remote.

This is often the first command you use when you want to understand the current state of the project.

---

## 12. Log: See the Project History

```bash
git log
```

This shows the recent commit history.

You can see:

- commit messages,
- commit dates,
- commit IDs,
- who made the change.

This helps you understand how the project has evolved.

---

## 13. Undoing Mistakes

A big reason beginners learn Git is because it helps recover from mistakes.

### Undo a modification before staging

```bash
git checkout -- filename
```

or newer:

```bash
git restore filename
```

This restores the file to the last committed version.

### Unstage a file

```bash
git restore --staged filename
```

### Go back to an older commit

```bash
git checkout <commit_id>
```

or:

```bash
git switch <branch_or_commit>
```

This is powerful, but beginners should use it carefully.

---

## 14. A Typical Day with Git

A normal workflow might look like this:

```bash
git status
git add .
git commit -m "Fix data cleaning bug"
git push
```

Or when starting a new feature:

```bash
git switch -c new-feature
git status
git add .
git commit -m "Start new feature"
git push -u origin new-feature
```

This pattern is used all the time in real projects.

---

## 15. Important Concepts in One Sentence

Here is a simple summary:

- repository = project folder tracked by Git
- commit = saved snapshot
- branch = separate line of development
- merge = combine changes from one branch to another
- remote = GitHub or another online copy
- push = send local changes to remote
- pull = download remote changes

---

## 16. Why Students Should Learn Git

Git is not only for software engineers.

Students in many fields can benefit from it:

- computer science
- data science
- engineering
- physics
- mathematics
- research projects

It helps you:

- keep backups,
- organize your work,
- collaborate with teammates,
- track project changes,
- learn good programming habits.

This is a skill that matters far beyond the classroom.

---

## 17. A Beginner-Friendly Mental Model

Imagine your project is a book.

Git is the notebook that keeps every version of the book.

Each time you finish a chapter, you create a commit.

If you want to try a different direction, you create a branch.

If the new direction works, you merge it back.

If your teammate edits the book, you can pull in their changes.

This keeps everything organized and safe.

---

## 18. Very Basic Commands You Will Use Most Often

```bash
git init
git status
git add .
git commit -m "message"
git log
git branch
git switch -c new-branch
git merge branch-name
git clone URL
git pull
git push
```

You do not need to memorize all of these immediately. Start with the ones you use most often.

---

## 19. Final Takeaway

Git is a tool for tracking and managing project changes.

At the beginner level, the important idea is this:

Git helps you save your work safely, try new ideas without breaking everything, and work with others in a structured way.

You do not need to understand every advanced feature right away. Start with these basics:

- create a repository
- add files
- commit changes
- check status
- use branches
- push to GitHub

Once these concepts become familiar, the rest of Git becomes much easier.

---

## 20. Quick Practice Example

Try this in a new folder:

```bash
mkdir demo-project
cd demo-project
git init

printf "Hello world\n" > hello.txt
git add hello.txt
git commit -m "Add hello file"

git status
```

This gives you a first real experience with Git, and it is the best way to start understanding how it works.
