# utc-503- Imporved File Rename
School Python Project.

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

### Exemple :

    $ /bin/python3 /home/inge/utc-503/utc-503/rename.py -p /home/inge/test/ -o -r -v
*Output :*

    rename : tableur.xls --> document_1.xls
    rename : monfichiertext.txt --> document_2.txt
    rename : gif.gif --> image_1.gif
    rename : film.mp4 --> video_1.mp4
    rename : truc.jpp --> file_1.jpp
    rename : phodze.jpeg --> image_2.jpeg
    rename : word.docx --> document_3.docx
    rename : text avec espace.odt --> document_4.odt
    rename : film nul.mov --> video_2.mov
    rename : mon deuxieme fichier --> file_2
    rename : photo1.png --> image_3.png
    rename : musique.mp3 --> music_1.mp3
    rename : musiquenul.wav --> music_2.wav


    create : /home/inge/test/Images
    create : /home/inge/test/Videos
    create : /home/inge/test/Documents
    create : /home/inge/test/Musics
    create : /home/inge/test/Files
    /home/inge/test/music_1.mp3 move to --> /home/inge/test/Musics/music_1.mp3
    /home/inge/test/music_2.wav move to --> /home/inge/test/Musics/music_2.wav
    /home/inge/test/file_1.jpp move to --> /home/inge/test/Files/file_1.jpp
    /home/inge/test/image_1.gif move to --> /home/inge/test/Images/image_1.gif
    /home/inge/test/video_2.mov move to --> /home/inge/test/Videos/video_2.mov
    /home/inge/test/image_2.jpeg move to --> /home/inge/test/Images/image_2.jpeg
    /home/inge/test/document_2.txt move to --> /home/inge/test/Documents/document_2.txt
    /home/inge/test/image_3.png move to --> /home/inge/test/Images/image_3.png
    /home/inge/test/document_3.docx move to --> /home/inge/test/Documents/document_3.docx
    /home/inge/test/video_1.mp4 move to --> /home/inge/test/Videos/video_1.mp4
    /home/inge/test/file_2 move to --> /home/inge/test/Files/file_2
    /home/inge/test/document_1.xls move to --> /home/inge/test/Documents/document_1.xls
    /home/inge/test/document_4.odt move to --> /home/inge/test/Documents/document_4.odt
    Done !
