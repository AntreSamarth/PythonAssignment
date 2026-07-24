# Duplicate File Removal Automation

## Description

This automation script scans the specified directory recursively, finds duplicate files using MD5 checksum, deletes duplicate copies, creates a log file, and sends the log file through email.

## Features

- Scan directory recursively
- Detect duplicate files using MD5 checksum
- Delete duplicate files
- Generate log file
- Send log file through email
- Automatic execution using schedule

## Requirements

- Python 3.x
- schedule

Install schedule using:

```bash
pip install schedule
```

## Project Files

```
DuplicateFileRemoval.py
MarvellousChecksum.py
MarvellousLog.py
MarvellousMail.py
README.md
```

## Run

```bash
python DuplicateFileRemoval.py DirectoryName
```

Example

```bash
python DuplicateFileRemoval.py D:\Demo
```

## Output

- Duplicate files removed
- Log file created
- Log file emailed