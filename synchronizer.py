import os
import sys
import time
import platform

def copy_file(source, replica):
    """Copy file from source to replica."""
    print("[+] Copying file:")
    print(f"[+] Source: {source}")
    print(f"[+] Replica: {replica}")

    try:
        with open(source, 'rb') as source_file, open(replica, 'wb') as replica_file:
            while True:
                chunk = source_file.read(4096)

                if not chunk:
                    break
                replica_file.write(chunk)
        print("[+] File copied successfully!")

    except Exception as e:
        print(f"[-] An error occurred while copying file: {e}")

def synchronize_folders(source, replica, log_file):
    """Synchronize files and folders from source to replica folder."""
    if not os.path.exists(source):
        return

    if not os.path.exists(replica):
        os.makedirs(replica)

    with open(log_file, 'a') as log:
        log.write(f"--- Synchronization started at {time.ctime()} ---\n")

    source_files = set()
    source_dirs = set()

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            source_dirs.add(os.path.relpath(os.path.join(root, directory), source))

        for file in files:
            source_files.add(os.path.relpath(os.path.join(root, file), source))

    replica_dirs = set()
    for root, dirs, files in os.walk(replica):
        for directory in dirs:
            replica_dirs.add(os.path.relpath(os.path.join(root, directory), replica))

        for file in files:
            replica_file = os.path.relpath(os.path.join(root, file), replica)
            if replica_file not in source_files:
                replica_path = os.path.join(replica, replica_file)
                os.remove(replica_path)
                print(f"[-] Removed file: {replica_path}")
                with open(log_file, 'a') as log:
                    log.write(f"Removing file {replica_path}\n")

    for root, dirs, files in os.walk(source):
        for directory in dirs:
            source_dir = os.path.join(root, directory)
            replica_dir = os.path.join(replica, os.path.relpath(source_dir, source))

            if not os.path.exists(replica_dir):
                os.makedirs(replica_dir)
                print(f"[+] Created directory: {replica_dir}")
            replica_dirs.add(os.path.relpath(replica_dir, replica))

        for file in files:
            source_file = os.path.join(root, file)
            replica_file = os.path.join(replica, os.path.relpath(source_file, source))

            if not os.path.exists(replica_file) or os.path.getmtime(source_file) > os.path.getmtime(replica_file):
                with open(log_file, 'a') as log:
                    log.write(f"Copying {source_file} to {replica_file}\n")
                copy_file(source_file, replica_file)

    for dir_path in replica_dirs - source_dirs:
        replica_dir = os.path.join(replica, dir_path)

        with open(log_file, 'a') as log:
            log.write(f"Removing directory {replica_dir}\n")
        os.rmdir(replica_dir)
        print(f"[-] Removed directory: {replica_dir}")

    with open(log_file, 'a') as log:
        log.write(f"--- Synchronization completed at {time.ctime()} ---\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("[-] You should give the correct arguments: Path to Source Folder, Path to Replica Folder, Number of Seconds and Log File, in this exact order.")
        sys.exit(1)

    source_folder = sys.argv[1]
    replica_folder = sys.argv[2]
    interval_seconds = int(sys.argv[3])
    log_file = sys.argv[4]

    if interval_seconds == None:
        interval_seconds = 10

    system_platform = platform.system()
    if system_platform == 'Windows':
        print("[+] Running on Windows...")
    elif system_platform == 'Linux':
        print("[+] Running on Linux...")
    else:
        print("[-] Unsupported operating system. This script is intended to run on Windows or Linux only.")
        sys.exit(1)

    print(f"[+] Synchronizing {source_folder} to {replica_folder} every {interval_seconds} seconds. Logging to {log_file}.")

    while True:
        synchronize_folders(source_folder, replica_folder, log_file)
        time.sleep(interval_seconds)
