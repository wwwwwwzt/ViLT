# Import the make_arrow function from the vilt.utils.write_vqa module
from vilt.utils.write_vqa import make_arrow

# Define the variables root and arrows_root
root = "./perpareDataViLT"
arrows_root = "./arrows"

# Call the make_arrow function
make_arrow(root, arrows_root)