# ft

`ft` is a plugin that find for a string in a file 😎 It a little bit like [`ripgrep`](https://github.com/BurntSushi/ripgrep)

## How to use

### Installation
1. Enter `git clone https://github.com/developerHaneum/ft.git` at Terminal

2. Add `.zshrc` to `alias ft="usr/bin/python3 (Cloned directory path)/exec.py"`

### Basics to use

### USAGE

#### `ft [FLAGS] '[<text>]' [<path/OPPTIONS>]`
This basics form is **find** a string in a file and a string in among the files in the directory. 🙂

### Tips of USAGE
- **If you don't want to write qutoes, You don't use to write  qutoes ! (Most of case)😉**

- **As of v7.2.0, you can find a string regardless of uppercase and lowercase letters**

### FLAGS

#### `ft -h` or `ft --help`
Prints **help** information 😝

#### `ft -V` or `ft --version`
Prints the information **version** of `ft` 😗

### OPPTIONS

#### `ft <text> !`
Entering `!` in `(path)` allows you to find for a string in files in the directory you **currently** belong to 😌

### Return value of ft

#### `1`
Text be at file or Text be at directory (Directory mode return path, too 😝)

#### `0`
File or Directory don't be 😢

#### `-1`
Text don't be at file or Text don't be at Directory 😕

## Help
### ~~5.2 version shouldn't~~ -> **v6.0 was resolved in version** 🤩
1. ~~If a directory exists inside a directories~~

    ~~I will add this function ASAP 😭~~

## Version
Now version: **v7.4.0** (21/6/7)

## License
Use **MIT License** so everyone can use it 😉
