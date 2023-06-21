import os
import time

source='C:\\Users\harsh\Desktop\Certificate_190130111060'
targeted_directory = 'C:\\Users\harsh\OneDrive'

# Create target directory if it is not present
if not os.path.exists(targeted_directory):
    os.mkdir(targeted_directory)  # make directory

# 3. The files are backed up into a zip file.
# 4. The current day is the name of the subdirectory
# in the main directory.

today = targeted_directory + os.sep + time.strftime('%Y-%m-%d')   
#The os.sep indicates the character used by the operating system to separate pathname components.

now = time.strftime('%H%M%S')

comment = input('Enter a comment --->')

# Ceck if comment is entered
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + '_' + comment.replace(' ','_',today)   

#Create a subdirectory if does not exist
if not os.path.exists(today):
    os.mkdir(today)
    print("Successfully created directory",today)
    
# 5. We use the zip command to put files in zip archive
zip_command =  "zip -r {0} {1}".format(target, ' '.join(source))

# Run the backup command
print("Zip command is")
print(zip_command)
print("Running...")
if os.system(zip_command) == 0:
    print(f"Successfull backup target is {target}")
else:
    print("Failed to backup target")    

         
