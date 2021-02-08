import os.path
import shutil
import re

# Returns the content of the file as a string
def content_as_str(filename):
    with open(filename, 'r') as file:
        data = file.read()

    return data


# Returns the content of the file as a string, and removes new lines.
def content_as_str_noreturn(filename):
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '')

    return data


# checks if file exists
def file_exists(filename):
    return os.path.isfile(filename)


# checks if directory exists
def dir_exists(filename):
    return os.path.isdir(filename)


# copy file/directory
def file_copy(filename, dest):
    if file_exists(filename):
        shutil.copyfile(filename, dest)
    elif dir_exists(filename):
        shutil.copytree(filename, dest)
    else:
        raise FileNotFoundError('The file/directory: {0} does not exist.'.format(filename))


# make a directory
def make_dir(dir_path):
    os.makedirs(dir_path)


# remove a directory
def rm_dir(dir_path):
    if dir_exists(dir_path):
        shutil.rmtree(dir_path)


# get the filename without the extension
def get_filename_no_ext(filename):
    return os.path.basename(os.path.splitext(filename)[0])


# check if a string exists in a file
def str_in_file(filename, str):
    if(file_exists(filename)):
        with open(filename) as f:
            return str in f.read()
    return False


# note that regardless of the flag 'ignore_empty_lines' value, the last line is always ignored
def nr_of_lines(filename, ignore_empty_lines=False):
    with open(filename) as f:
        if ignore_empty_lines:
            return len([i for i in f if i[:-1]])
        else:
            return len([i for i in f])


# replace a string using regex in a file
def replace_in_file(filename, regex, string):
    return re.sub(regex, string, content_as_str(filename))
