import zipfile
import os
import sys


def backupToZip(folder):
    folder = os.path.abspath(folder)
    # make sure folder is absolute
    # Figure out the filename this code should use based on what files already exist.
    number = 1
    while True:
        zipFilename = '{}_{} .zip'.format(os.path.basename(folder),str(number))
        if not os.path.exists(zipFilename):
            break
        number = number + 1

    # Create the ZIP file.
    print('Creating %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    # Walk the entire folder tree and compress the files in each folder.
    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))

        # Add the current folder to the ZIP file.
        backupZip.write(foldername)

        # Add all the files in this folder to the ZIP file.
        for filename in filenames:
            newBase = '{}_'.format(os.path.basename(folder))
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
    print('done.')
folder = sys.argv[1]
if __name__ == "__main__":
    backupToZip(folder)



