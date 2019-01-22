# M.A.C. :robot:
## Manjaro Automatic Configurator 

#### This is a tool to install every basic needed app and make some other configurations to a Manjaro KDE fresh install

## Features :sparkles:

### 1. Multiple config files :page_facing_up:

You can add multiple .json files in the config folder, there is one default config which installs everytime regardless of the selected option for very common apps (like Chrome or VSCode) and then you can choose your flavor to install specific apps.

This files should have the following structure:

```javascript
{
  name: string,
  apps: array
}
```
**Example**

```javascript
{
  "name": "Web",
  "apps": [nodejs, npm, yarn]
}
```
### 2. Custom commands :memo:

You can add, in adition to the apps array in a config file, custom commands.

**Example**

Lets pretend you want to create a folder and clone inside a repo, you can add a "command" key to the config json:
```javascript
{
  "name": "Web",
  "apps": [node, npm, yarn],
  "commands": ["mkdir Workspace", "cd Workspace", "git clone repo-url"]
}
```
Then every command will execute one by one.

### 3. Always updated :arrow_up:

Since pacman and yay are used to install the packages, latests versions are always installed.

### 4. Archusable :alien:

This is aimed to Arch's distro Manjaro, but it can be used in every Arch distro, since it uses Arch core package manager to perform instalations

## How to use :question: 

Just execute the .py file from the latest release and follow the instructions!
