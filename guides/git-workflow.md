# Typical git workflow

This document describes the typical `git` workflow of creating/cloning a repository,
adding/modifying files, and committing changes.

## 1. Create or clone a git repository

-  Create a *new* git repository in the folder `TECH2-H25`:
    ```bash
    mkdir TECH2-H25
    cd TECH2-H25
    git init -b main
    ```

-   *Alternatively,* clone an *existing* repository:
    ```bash
    git clone https://github.com/richardfoltyn/TECH2-H25.git
    ```

-   *Alternatively,* update an *existing* repository:
    ```bash
    git pull
    ```

## 2. Add or modify files

For example, let's create a "Hello world!" Python script
stored in the file `hello.py`:

```bash
echo 'print("Hello world!")' > hello.py
```

## 3. Inspect changes to repository

-   Use `git status` to display new/modified/deleted files:
    ```bash
    git status
    ```
    This produces the output
    ```bash
    Untracked files:
    (use "git add <file>..." to include in what will be committed)
            hello.py

    nothing added to commit but untracked files present (use "git add" to track)
    ```

-   Use `git diff` to show line-by-line changes compared to the last commit:
    ```bash
    git diff
    ```
    In this case nothing will be shown since `hello.py` is a newly added file.

## 4. Add modifications to repository (staging)

-   Use `git add` to stage any added or modified files:
    ```bash
    git add hello.py
    ```

-   Verify with `git status` that the changes have been staged. The output is
    ```bash
    Changes to be committed:
    (use "git rm --cached <file>..." to unstage)
        new file:   hello.py
    ```

## 5. Commit changes

-   Staged changes are not yet part of the repository. You need to commit
    them using `git commit`:
    ```bash
    git commit -m "Commit message"
    ```
    The `-m` option allows you to specify a commit message directly 
    on the command line.

    The command produces output similar to the following, indicating
    that a new commit has been created:
    ```bash
    [main (root-commit) 0cdfff2] Commit message
     1 file changed, 1 insertion(+)
     create mode 100644 hello.py
    ```

-   You can verify that everything has been committed with `git status`
    which produces the following output:
    ```bash
    On branch main
    nothing to commit, working tree clean
    ```
    

## 6. Push changes to remote repository (optional)

-   If you have a remote repository, you can now push the changes to the cloud:
    ```bash
    git push
    ```

-   If you don't yet have a remote repository, create a new one on GitHub
    and follow the instructions stated there to configure a new remote
    repository.