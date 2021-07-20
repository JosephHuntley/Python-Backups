# Backup any file with the .py extension.
import zipfile
import os
import shutil
#Create the zipfile.
zip_file = zipfile.ZipFile('Programs.zip', 'w')
# Walk the entire folder tree and compress the files in each folder.
os.chdir('C:\\Users\\Jchun\\Documents\\Programs')
for foldername, subfolders, filenames in os.walk('.'):
    print('Adding files in %s...' % (foldername))

# Add the current folder to the ZIP file.
    zip_file.write(foldername)
    # Add all the files in this folder to the ZIP file.
    for filename in filenames:
        if filename.endswith('.py'):
            zip_file.write(os.path.join(foldername, filename))
        else:
            continue
zip_file.close()
print('Done.')

#Move zipfile to onedrive
shutil.move('Programs.zip', 'C:\\Users\\Jchun\\Onedrive\\Programs.zip')
print('Files moved to C:\\Users\\Jchun\\Onedrive\\Programs.zip')
