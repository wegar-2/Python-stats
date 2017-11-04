import os
# import sys
import logging # note that messages are displayed using the logging package
# import glob

# 0. configuration of the logging
logging.basicConfig(level=logging.INFO) # all the output with importants equal to or greater than INFO is printed

# 1. getting the current directory
logging.info(msg="Current directory: " + os.getcwd())

# 2. getting a list of files in the current directory
logging.info(msg="Files in the current directory: ")
for my_iter, value in enumerate(os.listdir(path=os.getcwd())):
    logging.info(msg=str(my_iter)+": "+value)

# 3. getting the directory of the current script
logging.info(msg="__file__: " + __file__)
logging.info(msg="os.path.dirname(os.path.abspath(__file__)): " + os.path.dirname(os.path.abspath(__file__)))

# 4. getting the directory in which the cwd is located
logging.info(msg="os.path.dirname(os.getcwd()): " + os.path.dirname(os.getcwd()))

# 5. concatenating into a path
cntnd_path = os.path.join(os.getcwd(), "0_elementary_numpy.py")
logging.info(msg="cntnd_path: " + cntnd_path)

# 6. checking whether a file exists in the current directory
if os.path.isfile(path=cntnd_path):
    logging.info(msg="The file pointed at by cntnd_path exists. ")
else:
    logging.info(msg="The file pointed at by cntnd_path does not exist. ")

