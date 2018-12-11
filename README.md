# Project Title

filemover

## Getting Started

Moves Moments/Classifieds exports into folders based on publication days, via the rundate tags from corresponding xml file.
Usage: run from parent folder, and name subfolder. Orignal files are deleted


### Running as executable

The executable file "datemover" should be placed in a directory next to subfolders named "Oyeblikk" and "Torg", containing the raw export files from the ftp server.

Run the script from the terminal, (it will not work if run from Finder) by entering the directory datemover is located and type
```
./datemover
```

### Running as python3 script

Alternatively to running the executable, "filemover.py" the script also from windows environments. Make sure python 3 is installed.

The script "datemover.py" should be placed in a directory next to subfolders named "Oyeblikk" and "Torg", containing the raw export files from the ftp server.

Run the script from the terminal, by entering the directory datemover.py is located and type
```
python3 datemover.py
```


## File structure

├── Oyeblikk                    # Raw Moments export files
│   ├── 88_32054_1542356134.pdf            # Exported pdf card(s)
│   ├── 88_32054_1542356134.xml            # Corresponding XML file(s)
│   └── ...                                
├── Torg                        # Raw Classifieds export files
│   ├── 88_32054_1542356134.pdf            # Exported pdf card(s)
│   ├── 88_32054_1542356134.xml            # Corresponding XML file(s)
│   └── ...                                
└── filemover / filemover.py    # Executable or python script


## Authors

* **Johan Ludvig Holst** - *Initial work* - [johanludvigholst](https://github.com/johanludvigholst)



## License

This project is licensed under the GNU General Public License v3.0 - see the their website file for details
