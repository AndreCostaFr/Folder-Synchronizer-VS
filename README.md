
# Folder Synchronizer

The **Folder Synchronizer** is a robust utility designed to mirror the contents of a specified source directory to a target replica directory. It ensures that any modifications—whether additions or deletions—in the source directory are accurately reflected in the replica directory. Users can configure the synchronization interval and specify a text file to record all synchronization activities.

## Features

- **Real-time Synchronization**: Keeps the target directory synchronized with the source directory, reflecting all changes.
- **Configurable Sync Interval**: Allows users to set the time interval (in seconds) for synchronization.
- **Activity Logging**: Logs all synchronization activities in a specified text file.

## Requirements

- Python 3 must be installed on your system.
- Compatible with Linux distributions and Windows systems.

## Usage

To execute the script, enter the following command in your terminal:

```bash
python path/to/synchronizer.py source_directory replica_directory sync_interval log_file

```

Or simply run it in Visual Studio Code (or any other of your choice).
