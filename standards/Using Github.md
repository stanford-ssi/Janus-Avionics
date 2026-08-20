# Using Github
This document outlines how you to pull and push code from and to the official AV repository

### Installing Git / Github CLI
1. Visit https://git-scm.com/install,  select your operating system, and follow the instruction to install Git
2. Visit https://cli.github.com/, select your operating system, and follow the instuctions to install GitHub CLI.

### Logging in using git
To login to github and gain access to the repository, please make sure you have an account first. You can sign up for a github account at https://github.com/.

Once you have an account, and have installed Git, run the following in a terminal (command prompt/powershell on windows), replacing your credentials where necessary:

```bash
git config --global user.name "Your Github Username Here"
git config --global user.email "your.email@here.com"
```

After configuring your name and email signature on github, run the following to securely authenticate git using github, following the instructions after running the command:

```bash
gh auth login
```