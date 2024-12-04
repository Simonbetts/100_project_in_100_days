<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="Cheat_Sheet-top"></a>

<!--
*** Thanks for checking out the Python-CheatSheet. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->



# Github Cheat Sheet

<p align="center">
<img src="assets/images/github_logo.png" alt="Guithub Logo" width="300" height="300">
</p>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#python-basics">Python Basic</a></li>
 
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
<!--
Here's a blank template to get started: To avoid retyping too much info. Do a search and replace with your text editor for the following: `github_username`, `repo_name`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `project_title`, `project_description`
-->
Source: [Here][source]
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## Adding SSH Key
You can access and write data in repositories on GitHub using SSH (Secure Shell Protocol). When you connect via SSH, you authenticate using a private key file on your local machine. For more information, see "[About SSH.][About_SSH]"

When you generate an SSH key, you can add a passphrase to further secure the key. Whenever you use the key, you must enter the passphrase. If your key has a passphrase and you don't want to enter the passphrase every time you use the key, you can add your key to the SSH agent. The SSH agent manages your SSH keys and remembers your passphrase.

If you don't already have an SSH key, you must generate a new SSH key to use for authentication. If you're unsure whether you already have an SSH key, you can check for existing keys. For more information, see "[Checking for existing SSH keys.][Checking_SSH]"

If you want to use a hardware security key to authenticate to GitHub, you must generate a new SSH key for your hardware security key. You must connect your hardware security key to your computer when you authenticate with the key pair. For more information, see the [OpenSSH 8.2 release notes][releasenotes_8_2].

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

### Generating a new SSH key
You can generate a new SSH key on your local machine. After you generate the key, you can add the public key to your account on GitHub.com to enable authentication for Git operations over SSH.

>**Note:**
>
>GitHub improved security by dropping older, insecure key types on March 15, 2022.
>As of that date, DSA keys (ssh-dss) are no longer supported. You cannot add new DSA keys to your personal account on GitHub.
>RSA keys (ssh-rsa) with a valid_after before November 2, 2021 may continue to use any signature algorithm. RSA keys generated after that date must use a SHA-2 signature algorithm. Some older clients may need to be upgraded in order to use SHA-2 signatures.

1. Open Terminal
2. Paste the text below, replacing the email used in the example with your GitHub email address.

```sh
    ssh-keygen -t ed25519 -C "your_email@example.com"
```
>**Note:**
>
>If you are using a legacy system that doesn't support the Ed25519 algorithm, use:
>
>```sh
>   ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
>```

This creates a new SSH key, using the provided email as a label.

```sh
    > Generating public/private ALGORITHM key pair.
```
When you're prompted to "Enter a file in which to save the key", you can press Enter to accept the default file location. Please note that if you created SSH keys previously, ssh-keygen may ask you to rewrite another key, in which case we recommend creating a custom-named SSH key. To do so, type the default file location and replace id_ALGORITHM with your custom key name.

```sh
    > Enter file in which to save the key (/c/Users/YOU/.ssh/id_ALGORITHM):[Press enter]
```
3. At the prompt, type a secure passphrase. For more information, see "[Working with SSH key passphrases.][passphrases]"

```sh
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

### Adding your SSH key to the ssh-agent

Before adding a new SSH key to the ssh-agent to manage your keys, you should have checked for existing SSH keys and generated a new SSH key.

If you have [GitHub Desktop][github_desktop] installed, you can use it to clone repositories and not deal with SSH keys.

1. In a new admin elevated PowerShell window, ensure the ssh-agent is running. You can use the "Auto-launching the ssh-agent" instructions in "[Working with SSH key passphrases][passphrases]", or start it manually:
```sh
    # start the ssh-agent in the background
    Get-Service -Name ssh-agent | Set-Service -StartupType Manual
    Start-Service ssh-agent
```

2. In a terminal window without elevated permissions, add your SSH private key to the ssh-agent. If you created your key with a different name, or if you are adding an existing key that has a different name, replace id_ed25519 in the command with the name of your private key file.

```sh
    ssh-add c:/Users/YOU/.ssh/id_ed25519
```
3. Add the SSH public key to your account on GitHub. For more information, see "[Adding a new SSH key to your GitHub account.][adding_ssh]"

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

### Generating a new SSH key for a hardware security key

If you are using macOS or Linux, you may need to update your SSH client or install a new SSH client prior to generating a new SSH key. For more information, see "[Error: Unknown key type][error_keytype]".

1. Insert your hardware security key into your computer.
2. Open Git Bash.
3. Paste the text below, replacing the email address in the example with the email address associated with your account on GitHub.

```sh
ssh-keygen -t ed25519-sk -C "your_email@example.com"
```
> **Note**
>
>If the command fails and you receive the error <mark style="color: black; background-color: lightgrey"> invalid format </mark> or <mark style="color: black; background-color: lightgrey"> feature not supported </mark>, you may be using a hardware security key that does not support the Ed25519 algorithm. Enter the following command instead.
>
>   ```sh
>   ssh-keygen -t ecdsa-sk -C "your_email@example.com"
>   ```

4. When you are prompted, touch the button on your hardware security key.

5. When you are prompted to "Enter a file in which to save the key," press Enter to accept the default file location.
   
```sh
    > Enter a file in which to save the key (c:\Users\YOU\.ssh\id_ed25519_sk):[Press enter]
```

6. When you are prompted to type a passphrase, press Enter.

```sh
    > Enter passphrase (empty for no passphrase): [Type a passphrase]
    > Enter same passphrase again: [Type passphrase again]
```

8. Add the SSH public key to your account on GitHub. For more information, see "[Adding a new SSH key to your GitHub account.][adding_ssh]"

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

---

## Setup Github

Configuring user information used across all local repositories.

* Set a name that is identifiable for credit when review version history:

```sh
    git config --global user.name “[firstname lastname]”
```

* Email will be associated with each history marker:
  
```sh
    git config --global user.email “[valid-email]” set an email address that 
```

* Set automatic command line coloring for Git for easy reviewing:

```sh
    git config --global color.ui auto 
```
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>


## SETUP & INIT 

Configuring user information, initializing and cloning repositories.

* Initialize an existing directory as a Git repository:
```sh
    git init 
```
* Retrieve an entire repository from a hosted location via URL:

```sh
    git clone [url]
```
## STAGE & SNAPSHOT 

Working with snapshots and the Git staging area. 

* Show modified files in working directory, staged for the next commit:
```sh
    git status 
```

* Add a file as it is now to the next commit (stage):
```sh
    git add [file]
```
* Unstage a file while retaining the changes in working directory:
```sh
    git reset [file] 
```
* Differance between what has changed but is not staged:
```sh
    git diff 
```
* Differance between what is staged but not yet committed:
```sh
    git diff --staged 
```
* Commit staged content as a new commit snapshot with message:
```sh
    git commit -m “[descriptive message]”
```
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## BRANCH & MERGE
Isolating work in branches, changing context, and integrating changes.

* List all branches. (*) will appear next to the currently active branch:
```sh
git branch
```

* Create a new branch at the current commit:
```sh
git branch [branch-name] 
```

* Switch to another branch and make it the current working directory:
```sh
git checkout 
```

* Merg the specified branch history into the current one:
```sh
git merge [branch] 
```

* Show all commits in the current branch history:
```sh
git log 
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

## INSPECT & COMPARE 
Examining logs, diffs and object information.

* Show the commit history for the currently active branch:
```sh
git log 
```

* Show the commits on branchA that are not on branchB:
```sh
git log branchB..branchA 
```
<!--Clarify this comment -->
* Show the commits that changed file, even across renames:
```sh
git log --follow [file] 
```

* Show the differance between what is in branchA and not in branchB:
```sh
git diff branchB...branchA 
```

* Show any object in Git in a human-readable format:
```sh
git show [SHA] 
```
<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>

TRACKING PATH CHANGES Versioning file removes and path changes git rm [file] delete the file from project and stage the removal for commit git mv [existing-path] [new-path] change an existing file path and stage the move git log --stat -M show all commit logs with indication of any paths that moved

IGNORING PATTERNS Preventing unintentional staging or commiting of files

logs/ *.notes pattern*/ Save a file with desired patterns as .gitignore with either direct string matches or wildcard globs.

git config --global core.excludesfile [file] system wide ignore pattern for all local repositories

SHARE & UPDATE Retrieving updates from another repository and updating local repos git remote add [alias] [url] add a git URL as an alias git fetch [alias] fetch down all the branches from that Git remote git merge [alias]/[branch] merge a remote branch into your current branch to bring it up to date git push [alias] [branch] Transmit local branch commits to the remote repository branch git pull fetch and merge any commits from the tracking remote branch


REWRITE HISTORY Rewriting branches, updating commits and clearing history git rebase [branch] apply any commits of current branch ahead of specified one git reset --hard [commit] clear staging area, rewrite working tree from specified commit

TEMPORARY COMMITS Temporarily store modified, tracked files  in order to change branches git stash Save modified and staged changes git stash list list stack-order of stashed file changes git stash pop write working from top of stash stack git stash drop discard  the changes from top of stash stack

>?
>
>?
>
>?
>
>?
>
>?

* Print Statment :
  
```py
    print(f'Hello World')
```   
* Variables:

```py
    x = 5
    y = "S"
    z:char= 'D' #Type set variable
```

* Data Types:

```py
    int_var = 10
    float_var = 10.5
    str_var = "Hello"
    char_var = 'R'
    list_var = [1,2,3]
    tuple_var = (4,5,6)
    dict_var = {"Key1":"Value1","Key2":"Value2"}
```

<p align="right">(<a href="#Cheat_Sheet-top">back to top</a>)</p>



---

<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
###### by Simon A. Betts 03/12/2024
<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->


<!-- Links for External -->
[Source]:https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent
[About_SSH]:https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh
[Checking_SSH]:https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys
[releasenotes_8_2]:https://www.openssh.com/txt/release-8.2
[passphrases]:https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases
[github_desktop]:https://desktop.github.com/
[adding_ssh]:https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account
[error_keytype]:https://docs.github.com/en/authentication/troubleshooting-ssh/error-unknown-key-type

<!-- Links for Images -->
[Python_Logo]:assets/images/python_logo.png
[Linux_mascot_tux]: assets/images/Linux_mascot_tux.png