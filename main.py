import runpy
import sys
""" This script will run a specified file in the scr directory.  
    The only reason for this is to allow running one of the scr files with the "Run" button.
"""

# Add the src directory to the path 
sys.path.append("./src")

# Update this line to be the name of the file you want to run from src
scr_file = "sample.py"

# Run the file
runpy.run_path("src/%s" % scr_file)