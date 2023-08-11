import os

def copy_file(file_copy_from, file_copy_to):

	file_copy_from = os.path.abspath(file_copy_from)
	file_copy_to = os.path.abspath(file_copy_to)

	print("Source file path:", file_copy_from)
	print("Destination file path:", file_copy_to)

	if os.path.exists(file_copy_from) and os.path.exists(file_copy_to):
		with open(file_copy_from) as file_to_read :
			with open(file_copy_to, "w") as file_to_write :
				for line in file_to_read :
					file_to_write.write(line)
		print(f"the size of the copied to file is : {os.path.getsize(file_copy_to)} Bytes")

	else :
		print("there is an error")






def inside_dir(dir):
	for name in os.listdir(dir):
		fullname = os.path.join(dir, name)
		if os.path.isdir(fullname):
			print(f"{fullname} is a directory")
		else:
			print(f"{fullname} is a file")



def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, 'w') as file:
    file.write(comments)
  filesize = os.path.getsize(filename)
  return(filesize)

# test : print(create_python_script("program.py"))


def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    os.mkdir(directory)

  # Create the new file inside of the new directory
  os.chdir(directory)
  with open (filename, 'w') as file:
    pass

  # Return the list of files in the new directory
  return os.listdir()

# test : print(new_directory("PythonPrograms", "script.py"))




import datetime

def file_date(filename):
  # Create the file in the current directory
  temp_dir = '/tmp/'
  file_path = os.path.join(temp_dir, filename)
  with open(file_path, 'w') as file :
    pass
  timestamp = os.path.getmtime(file_path)
  # Convert the timestamp into a readable format, then into a string
  file_date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

  # Return just the date portion 
  # Hint: how many characters are in “yyyy-mm-dd”? 
  return file_date

# test : print(file_date("newfile.txt")) 
# Should be today's date in the format of yyyy-mm-dd


def parent_directory():
   # Create a relative path to the parent
    # of the current working directory
  current_dir = os.getcwd()
  relative_parent = os.path.join(current_dir, os.pardir)

    # Return the absolute path of the parent directory
  return os.path.abspath(relative_parent)

# test : print(parent_directory()) this one i got it wrong need to revise