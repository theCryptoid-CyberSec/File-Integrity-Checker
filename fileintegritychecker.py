import hashlib
import os
import json
import time

# Function to calculate the SHA-256 hash of a file
def calculate_file_hash(file_path, algorithm="sha256"):
    hash_algorithm = hashlib.new(algorithm)
    
    try:
        with open(file_path, 'rb') as file:
            while chunk := file.read(4096):
                hash_algorithm.update(chunk)
        return hash_algorithm.hexdigest()
    except Exception as e:
        print(f"Error calculating hash for {file_path}: {e}")
        return None

# Function to load stored hashes from a file
def load_stored_hashes(hash_file="file_hashes.json"):
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as file:
            return json.load(file)
    else:
        return {}

# Function to store hashes in a file
def store_hashes(hashes, hash_file="file_hashes.json"):
    with open(hash_file, 'w') as file:
        json.dump(hashes, file, indent=4)

# Function to monitor files and check integrity
def monitor_files(file_paths, hash_file="file_hashes.json", algorithm="sha256"):
    stored_hashes = load_stored_hashes(hash_file)
    
    for file_path in file_paths:
        if os.path.exists(file_path):
            current_hash = calculate_file_hash(file_path, algorithm)
            if current_hash:
                # Check if the file's hash is stored or not
                if file_path in stored_hashes:
                    if stored_hashes[file_path] != current_hash:
                        print(f"Warning: File '{file_path}' has been modified!")
                else:
                    print(f"New file detected: '{file_path}' - Storing its hash.")
                    stored_hashes[file_path] = current_hash
        else:
            print(f"File '{file_path}' not found!")

    # Store updated hashes
    store_hashes(stored_hashes)

# Example usage
if __name__ == "__main__":
    # List of files to monitor (add files as needed)
    files_to_monitor = [
        "important_file1.txt",
        "important_file2.txt",
        "config.json"
    ]

    # Monitor files every 10 seconds (for demonstration purposes)
    try:
        while True:
            monitor_files(files_to_monitor)
            print("Integrity check completed. Sleeping for 10 seconds...\n")
            time.sleep(10)
    except KeyboardInterrupt:
        print("File integrity checker stopped.")
