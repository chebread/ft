# ft
`ft` is a program to find for text in files. It a little bit like [`ripgrep`](https://github.com/BurntSushi/ripgrep), [`fd`](https://github.com/sharkdp/fd).

## How to use

### Installation
1. **Enter** `git clone https://github.com/developerHaneum/ft.git`

2. **Enter** `pip install colorama`

3. **Add** `alias ft="python3 (Cloned directory path)/main.py"`

## Basics to use

### USAGE

#### `ft [OPTIONS] [text] [path]`
This basics form is **find** a string in a file and a string in among the files in the directory.

### OPTIONS

#### `ft -h` or `ft --help`
It prints **help** information.

#### `ft -V` or `ft --version`
It prints the information **version** of `ft`.

### ARGS

#### `[text]`
The `[text]` argument is the text you want to find. If your `[text]` argument contains spaces, be sure to include the `'` or `"`  quotes.

#### `[path]`
The `[path]` argument is the file or directory you want to find. If the `[path]` argument contains spaces, be sure to include the `'` or `"` quotes.

If you enter `.` or leave it empty for the `[path]` argument, it will search for the string in files in the current directory.

If you want to leave the `[text]` argument blank and enter only the `[path]` argument, you must enter a space character, such as '', in the `[text]` argument.

If you omit the `[text]` argument and enter only the `[path]` argument, `ft` considers it to be a positional argument, and treats the argument you entered as the [path] argument as the [text] argument.

### Return value of `ft`
#### blank
The file you are looking for is not found.

#### not blank
The file you are looking for is found.

### Return color of `ft`
#### Blue 🧢
It mean is **directories** 

#### White
It mean is **files**

## Version
Now version: **9.0** (25/06/21)

## License
MIT LICENSE &copy; 2021-2025 Cha Haneum