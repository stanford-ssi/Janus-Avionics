# Using Github
This document outlines how you to pull and push code from and to the official AV repository

## Installing Git / Github CLI
1. Visit https://git-scm.com/install,  select your operating system, and follow the instruction to install Git
2. Visit https://cli.github.com/, select your operating system, and follow the instuctions to install GitHub CLI.

## Logging in using git
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
### Gaining Access to the Repository
Once you have completed all prior steps, then, send a message to the current avionics lead in the [#satellite-avionics](https://ssi-teams.slack.com/archives/C2L29KW8J) channel on the official SSI Slack, requesting access using your github username.

## Properly cloning the repository for usage
To download the repository to your computer, run the following command:

```bash
 git clone https://github.com/stanford-ssi/Janus-Avionics.git
 ```

## Creating Pull Requests
When working on research, design, documentation, or any other change to be made to the remote repository. You must use the standard git pull request process commonly used in software development.

**Checking out a new branch**
To add a new feature, fix, design, etc. You must checkout a new branch using the local copy clone you just created.

To do this, create a new copy of the repository, or use your old one and navigate to the cloned folder

```bash
# Clone the reposity (from before)
 git clone https://github.com/stanford-ssi/Janus-Avionics.git

 # Navigate into the repository folder
 cd Janus-Avionics

 # Checkout a new Branch with the purpose of your change
 git checkout -b FMU/LM2302 # (this chip might not exist its just an example, just name your branch something reasonable)

 # Another example
 git checkout -b DESIGN/TTC
 ```

 **After adding changes**
 You shoud add and commit your changes to the newly created remote branch

In your cloned repository folder, run the following:
 ```bash
 # Adds all changed files to commit
 git add .

 # Commits changes to history
 git commit -m "Describe your change here"

 # Push to Remote (Whatever you)
 git push origin "Branch name here"
 # ex: "git push origin FMU/LM2302"

```
