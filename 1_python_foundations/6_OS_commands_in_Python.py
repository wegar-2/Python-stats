import os
import sys
import logging # note that messages are displayed using the logging package
import glob

# 0. configuration of the logging
logging.basicConfig(level=logging.INFO)

# 1. getting the current directory
logging.info(msg="Current directory" + os.getcwd())

# 2. getting a list of files in the current directory
logging.info(msg="Files in the current directory: ")
for my_iter, value in enumerate(os.listdir(path=os.getcwd())):
    logging.info(msg=str(my_iter)+": "+value)

# 3. matching a directory in the filesystem using regular expressions


