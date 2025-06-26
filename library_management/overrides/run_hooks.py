# file: run_hooks.py

from file_hooks import write_file, delete_file

write_file("demo.txt", "Hello from hook!")
delete_file("demo.txt")
