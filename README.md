# git_github_demo

git init
git clone <URL from GitHUB https://.... >

$ git status -s
?? demo_Scripts/

```
$ git add demo_Scripts
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

	new file:   demo_Scripts/classPython.py
	new file:   demo_Scripts/countAlphabet.py
	new file:   demo_Scripts/formatOutput.py
	new file:   demo_Scripts/functionPython.py
	new file:   demo_Scripts/helloWorld.py
	new file:   demo_Scripts/ifElseStmt.py
	new file:   demo_Scripts/namespaceScope.py
	new file:   demo_Scripts/userInput.py
	new file:   demo_Scripts/variableTest.py
	new file:   demo_Scripts/whileForLoop.py
```
```
$ git commit -m "Pushing demo_Scripts"
[master fd2793a] Pushing demo_Scripts
 10 files changed, 303 insertions(+)
 create mode 100644 demo_Scripts/classPython.py
 create mode 100644 demo_Scripts/countAlphabet.py
 create mode 100644 demo_Scripts/formatOutput.py
 create mode 100644 demo_Scripts/functionPython.py
 create mode 100755 demo_Scripts/helloWorld.py
 create mode 100644 demo_Scripts/ifElseStmt.py
 create mode 100644 demo_Scripts/namespaceScope.py
 create mode 100644 demo_Scripts/userInput.py
 create mode 100644 demo_Scripts/variableTest.py
 create mode 100644 demo_Scripts/whileForLoop.py
```
```
$ git status
On branch master
Your branch is ahead of 'origin/master' by 1 commit.
  (use "git push" to publish your local commits)
nothing to commit, working directory clean
```
```
$ git pull origin master
remote: Counting objects: 2, done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 2 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (2/2), done.
From https://github.com/bibhuWork/git_github_demo
 * branch            master     -> FETCH_HEAD
   874e99b..09d92c3  master     -> origin/master
Updating 874e99b..09d92c3
Fast-forward
 formatOutput.py | 30 ------------------------------
 1 file changed, 30 deletions(-)
 delete mode 100644 formatOutput.py
```
```
$ git push origin master
Username for 'https://github.com': bibhuWork
Password for 'https://bibhuWork@github.com': 
Counting objects: 13, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (13/13), done.
Writing objects: 100% (13/13), 3.36 KiB | 0 bytes/s, done.
Total 13 (delta 0), reused 0 (delta 0)
To https://github.com/bibhuWork/git_github_demo.git
   09d92c3..fd2793a  master -> master
```
```
$ git log
commit fd2793a651d3f3a76cf0d776bdcd808be6f4d086
Author: Bibhudatta Sarangi <simply.bibhu@gmail.com>
Date:   Mon Jun 4 22:27:34 2018 -0400

    Pushing demo_Scripts

commit 09d92c3614592d9cc128a257a86936054cd572af
Author: Bibhudatta Sarangi <38837035+bibhuWork@users.noreply.github.com>
Date:   Thu May 31 21:20:23 2018 -0400

    Delete the script

commit 874e99b0f1f84706d6567b34b1bf12696078601b
Author: Bibhudatta Sarangi <simply.bibhu@gmail.com>
Date:   Thu May 31 21:17:36 2018 -0400

    Pushing files from server to GitHUB

```
```
git rm --cached FileName ,
git log --oneline ,
git log FileName ,
git log since_commit_id..until_commit_id , 
git log -n 3 : last 3 commits 
```
