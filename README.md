
Folder Synchronizer

The Folder Synchronizer is a robust utility designed to mirror the contents of a specified source directory to a target replica directory. It ensures that any modifications—whether additions or deletions—in the source directory are accurately reflected in the replica directory. Users can configure the synchronization interval and specify a text file to record all synchronization activities.

This script is compatible with Linux distributions and Windows systems. To use it, Python 3 must be installed on your system.

To execute the script, enter the following command in your terminal:
python path/to/synchronizer.py source_directory replica_directory sync_interval log_file

Here, source_directory is the path to the folder you want to synchronize, and replica_directory is the path to the target folder. The sync_interval parameter defines how frequently (in seconds) the synchronization should occur. The log_file parameter specifies the path to the text file where synchronization logs will be saved. If no log file is provided, the script will create a default log file named synchronizer.log in the same directory as the script.

It is important to note that the script must be run in a terminal session, as it will stop synchronizing if the terminal is closed. Additionally, ensure that the paths used for directories and files do not contain spaces, as this may cause the script to malfunction.

For example, to synchronize contents from source to replica every 10 seconds and log actions to test.txt, use the following command:
python synchronizer.py ./documents/source ./documents/replica 10 ./documents/test.txt
