# ft

`ft` is a plugin that find for a string in a file 😎 It a little bit like [`ripgrep`](https://github.com/BurntSushi/ripgrep)

## How to use

### Installation
1. Enter `git clone https://github.com/developerHaneum/ft.git` at Terminal

2. Add `.zshrc` to `alias ft="usr/bin/python3 (Cloned directory path)/exec.py"`

### Basics to use

### USAGE

#### `ft [FLAGS] '(text)' (path)`
This basics form is **find** a string in a file 🙂

#### `ft [FLAGS] '(text)' (directory)` (It is demo)
This form is **find** a stirng in among the files in the directory 🙃

**If you don't want to write qutoes, You don't use to write  qutoes ! 🙃**

### FLAGS

#### `ft -h` or `ft --help`
Prints **help** information 😝

### Return value of ft

#### `1`
Text be at file or Text be at directory (Directory mode return path, too 😝)

#### `0`
File don't be or Directory don't be 😢

#### `-1`
Text don't be at file or Text don't be at Directory 😕

## Version
Now version: v5.0 (21/6/4)

## License
Use MIT License so everyone can use it 😉
