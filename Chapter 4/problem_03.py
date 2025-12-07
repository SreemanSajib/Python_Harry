# Check that a tuple type cannot be changed in python.

a = (34, 234, "Sajib")

a[2] = "Chandra" # This will raise an error since tuples are immutable in python.