# nb2py
application for quick conversion of jupyter-notebooks to .py files

```
usage: python nb2py.py [-h] [-o OUT_PATH] [-w WORD_COUNT] [-i IGNORE] [-c] in_path

application for quick conversion of jupyter-notebooks to .py files

positional arguments:
  in_path               path of input notebook file to be converted

optional arguments:
  -h, --help            show this help message and exit
  -o OUT_PATH, --out_path OUT_PATH
                        path of ouput py file (default: None)
  -w WORD_COUNT, --word_count WORD_COUNT
                        number of words per line of markdown cells (default: 15)
  -i IGNORE, --ignore IGNORE
                        string pattern which cells containing it will be ignored/skipped (default: None)
  -c, --code_only       writes only code cells (exluceds markdown cells) (default: False)

author: itamar.g
```
## Optional Argument

- ```-w``` (word count : int) - when proccessing markdown cells (into commented lines), limits the number of words per line. This makes the code much more readable. the default nubmer of words per line in the output file is 15. 
- ```-o``` (output path : str) - if not defined, the output file will be written to the current working directory (from where the nb2py.py is executed), with the same name as the input notebook file, only differentiated by a .py suffix
- ```-i``` (ignore : str) - a string pattern that when encountered at the top of a code cell (first line) will cause the same cell to be excluded from the the ouptut .py file. The implementation of the method is done using regex, so regular expression patterns are excepeted.
- ```-c``` (code only) - only process code cells, and excludes markdown cells from output .py file.
