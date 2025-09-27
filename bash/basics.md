
# Linux Commands Introduction


This guide provides an introduction to basic Linux commands that can be run in **Git Bash**.  
Each command is shown with a **description** and **example usage**.

---

## **1. Navigation and File System**

### `pwd` – Print Working Directory
Shows the full path of the current directory you are in.
```bash
pwd
```
**Example output:**
```
/c/Users/JohnDoe
```

---

### `ls` – List Files and Directories
Lists files and directories in the current folder.
```bash
ls
```

**Common options:**
- `-l` – long listing format (permissions, size, dates)
- `-a` – show hidden files
- `-lh` – long listing + human-readable sizes

```bash
ls -la
```

---

### `cd` – Change Directory
Used to navigate between folders.

```bash
cd folder_name        # Go into a folder
cd ..                 # Go one level up
cd /c/Users/Matous    # Go to an absolute path
cd ~                  # Go to home directory
```

---

### `clear` – Clear Terminal
Clears the terminal window for a clean view.
```bash
clear
```

---

## **2. Creating and Managing Files**

### `touch` – Create Empty File
Creates a new empty file or updates the timestamp of an existing file.
```bash
touch myfile.txt
```

---

### `mkdir` – Create Directory
Creates a new folder (directory).
```bash
mkdir my_folder
```

**Create nested directories:**
```bash
mkdir -p parent/child/grandchild
```

---

### `rm` – Remove Files or Directories
Deletes files or folders **permanently** (no recycle bin).

```bash
rm myfile.txt           # Remove a file
rm -r my_folder         # Remove a folder and its contents
```

⚠️ **Be careful!**  
Using `rm` cannot be undone.

---

### `cp` – Copy Files or Directories
Copies files or folders.

```bash
cp file.txt backup.txt            # Copy file
cp -r my_folder backup_folder     # Copy folder recursively
```

---

### `mv` – Move or Rename
Moves or renames files and folders.

```bash
mv oldname.txt newname.txt         # Rename a file
mv file.txt /c/Users/Matous/Desktop # Move file to another location
```

---

## **3. Viewing Files**

### `cat` – View File Contents
Displays the content of a file in the terminal.

```bash
cat myfile.txt
```

---

### `less` – View Large Files
Opens a file in a scrollable viewer.  
Navigate using:
- **Space** – next page
- **q** – quit

```bash
less bigfile.txt
```

---

### `head` – View First Lines
Shows the first **10 lines** of a file by default.
```bash
head myfile.txt
```

Show a specific number of lines:
```bash
head -n 5 myfile.txt
```

---

### `tail` – View Last Lines
Shows the last **10 lines** of a file by default.
```bash
tail myfile.txt
```

Follow changes live (like a log file):
```bash
tail -f mylog.txt
```

---

## **4. Editing Files**

### `nano` – Simple Terminal Text Editor
Edit files directly from the terminal.
```bash
nano myfile.txt
```
Controls:
- **CTRL + O** – Save changes
- **CTRL + X** – Exit editor

> *Note: `nano` may not be available in Git Bash by default.*

---

## **5. Searching and Filtering**

### `grep` – Search Text in Files
Search for specific text inside files.

```bash
grep "hello" myfile.txt
```

**Recursive search through folders:**
```bash
grep -r "error" logs/
```

---

### `wc` – Word, Line, and Character Count
Counts lines, words, and characters in a file.

```bash
wc myfile.txt
```

---

### `sort` – Sort File Lines
Sorts the lines of a file alphabetically.

```bash
sort myfile.txt
```

---

### `uniq` – Remove Duplicate Lines
Filters out duplicate lines from a sorted file.

```bash
sort myfile.txt | uniq
```

---

## **6. Redirection and Pipes**

### Redirect Output to a File
Use `>` to **overwrite** a file or `>>` to **append**.

```bash
echo "Hello World" > hello.txt      # Overwrite
echo "Another line" >> hello.txt    # Append
```

---

### Pipe `|`
Pass the output of one command as input to another.

```bash
ls -l | grep "txt"
```
*Lists only files containing `txt` in their names.*

---

## **7. System Information**

### `whoami` – Current User
Displays the current username.
```bash
whoami
```

---

### `uname` – System Information
Shows basic information about the system.
```bash
uname        # Kernel name
uname -a     # Detailed system info
```

---

### `date` – Show Date and Time
Displays the current date and time.
```bash
date
```

---

### `uptime` – System Uptime
Shows how long the system has been running.
```bash
uptime
```

---

### `history` – Command History
Lists previously used commands.

```bash
history
```

Run a previous command by number:
```bash
!42
```

---

## **8. Shortcuts**

| Shortcut | Description |
|-----------|-------------|
| `CTRL + C` | Stop running command |
| `CTRL + L` | Clear screen (same as `clear`) |
| `TAB` | Auto-complete filenames or commands |
| `↑` / `↓` | Navigate command history |

---

## **9. Example: Creating and Managing a Project**

```bash
mkdir my_project           # Create project folder
cd my_project              # Enter folder
touch main.py README.md    # Create Python file and README
echo "print('Hello')" > main.py  # Add code to Python file
ls -la                      # Check files
cat main.py                  # View file content
```

---

## **10. Exiting Git Bash**

### `exit` – Close Terminal
```bash
exit
```

---

## **Summary**

| Command | Description |
|----------|-------------|
| `pwd` | Show current directory |
| `ls` | List files |
| `cd` | Change directory |
| `touch` | Create empty file |
| `mkdir` | Create folder |
| `rm` | Delete files/folders |
| `cp` | Copy files/folders |
| `mv` | Move/rename files |
| `cat` | View file contents |
| `grep` | Search inside files |
| `history` | View command history |

---
