Folder Synchronizer

The Folder Synchronizer was created to copy the source folder/directory of your choice to a replica (also of your choice) folder. Anything you add or delete from the source folder should also be added or deleted from the replica folder. You can set the time between the syncs and it also logs all actions into a text file of your choice.


The script should work only in Linux distros and in Windows.
To run this script you must have Python 3 installed.

You can run it using command lines by typing "python" + the path to this file.
Use the source file's path and the replica file's path as arguments to dictate which are the files you want to copy.
As the third argument, use the ammount of time (in seconds) you want the synchronizer to update the replica file, and as the fourth argument, the path to the logs text file.

This script only works while it is running on terminal, if you kill the terminal it will stop synchronizing. Also, make sure the folders/directory paths you are running the script doesn't have any spaces between words since it might break the script and it will not work.


Terminal command line example:

python synchronizer.py .\documents\source .\documents\replica 10 .\documents\test.txt
