# nb2py
application for quick conversion of jupyter-notebooks to .py files

```
usage: nb2py.py [-h] [-o OUT_PATH] [-w WORD_COUNT] [-i IGNORE] [-c] in_path

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
