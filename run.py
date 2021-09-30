from dash_webpage.test import my_print 
my_print()

import dash_webpage as test_file 
test_file.test.my_print()

import dash_webpage.test as test_file2
test_file2.my_print()

# folder that does not have __init__.py
import dash_webpage_2.test as test_file3
test_file3.my_print()
