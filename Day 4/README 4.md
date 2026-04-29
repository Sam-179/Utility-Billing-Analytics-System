Day 4: Safety Checks & Clean Code

Modular Folders: Cleaned up the project by moving helper code into a separate file called utility.py.

Crash Protection: Added "Error Handling" (try-except) so the program doesn't break if the CSV file has a typo, a blank line, or a letter instead of a number.

File Safety: Added a check to make sure the CSV file actually exists before the program tries to open it, preventing "File Not Found" errors.