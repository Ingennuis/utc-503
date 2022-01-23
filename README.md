# utc-503- Imporved File Rename
School Python Project.

## Test.py
It's a simple script, that ask you mutiple questions to do some rename and storage functions.

## rename.py
It's script that works in full cli.

### The fuctions are :
- Choose a working space
- Replace extension file
- Replace spaces in file names
- Change file names by incremanted names (file_1, file_2 ... file_n, image_n, document_n, music_n, ...)
- Sort files according to their extension, and put it in the right directory (ex : .png in /Image)

## Usage :
*Help Output:*

    usage: rename.py [-h] -p PATH [-d DESTINATION] [-s [SPACE_CHARACTER]] [-o] [-ext EXT EXT] [-r] [-v]

    optional arguments:
      -h, --help            show this help message and exit
      -p PATH, --path PATH  path to your directory
      -d DESTINATION, --destination-path DESTINATION
                            choose a destination folder
      -s [SPACE_CHARACTER], --space-replace [SPACE_CHARACTER]
                            replace space by underscore or your choice
      -o, --order-files     organize files in folder acording to their type
      -ext EXT EXT, --ext-replace EXT EXT
                            replace a choosen extension file by an other Usage : -ext [ext-to-replace] [replace-ext]
      -r, --rename          rename all files, file_1, file_2, ..., file_n | image_1...
      -v, --verbose         show you what was done


*The space-replace and ext-raplace are useless when the option rename (-r) is used*
