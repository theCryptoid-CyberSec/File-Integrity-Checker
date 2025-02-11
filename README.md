# File Integrity Checker
## Explanation:
1. `calculate_file_hash(file_path, algorithm)`: This function computes the cryptographic hash of a file. It supports any hash algorithm like SHA-256 or MD5 by specifying the algorithm parameter. It reads the file in chunks to handle large files efficiently.
2. `load_stored_hashes(hash_file)`: This function loads previously stored hashes from a JSON file (or any storage file you prefer). The hashes are stored as a dictionary with file paths as keys and their corresponding hash values as values.
3. `store_hashes(hashes, hash_file)`: This function saves the current hashes to a JSON file so that they can be compared later.
4. `monitor_files(file_paths, hash_file)`: This function monitors the given list of files. It checks the current hash of each file and compares it with the stored hash. If the hash has changed, it will alert the user about the modification. If it's a new file, its hash will be stored.
5. Main section: The script runs an infinite loop to monitor the integrity of the files in files_to_monitor. The script checks the integrity every 10 seconds (for demonstration purposes). You can adjust the interval or trigger the check manually based on your use case.
## How to Use:
1. Add the paths of the files you want to monitor into the files_to_monitor list.
2. When the script is run for the first time, it will compute and store the hashes of the files in file_hashes.json.
3. The tool will then periodically check the hashes of the files and alert you if there are any changes.
## Notes:
- You can adjust the hash algorithm used (MD5, SHA-256, etc.) by changing the algorithm parameter.
- You may want to enhance this by adding logging functionality or more advanced notifications.
- For large-scale monitoring, consider using file system watchers like watchdog for event-driven checks instead of periodic checks.