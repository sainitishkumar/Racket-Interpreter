#!/usr/bin/env python3

import os
inp = int(input('repl or from file? : 1/2 :'))
if inp == 2:
    os.system('python3 repl.py')
else:
    os.system('python3 run_file.py') 
