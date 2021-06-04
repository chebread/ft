# ft

`ft` is a plugin that find for a string in a file 😎 It a little bit like [`ripgrep`](https://github.com/BurntSushi/ripgrep)

## How to use

### Installation
1. Enter `git clone https://github.com/developerHaneum/ft.git` at Terminal

2. Add `.zshrc` to `alias ft="usr/bin/python3 (Cloned directory path)/exec.py"`

### Basics to use

#### USAGE

##### `ft [FLAGS] '(text)' (path)`
This basics form is **find** a string in a file 🙂

##### `ft [FLAGS] '(text)' (directory)` (It is demo)
This form is **find** a stirng in among the files in the directory 🙃

**If you don't want to write qutoes, You don't use to write  qutoes ! 🙃**

#### FLAGS

##### `ft -h` or `ft --help`
Prints **help** information 😝

#### Return value of ft

##### `1`
Text be at file or Text be at directory (Directory mode return path, too 😝)

##### `0`
File don't be or Directory don't be 😢

##### `-1`
Text don't be at file or Text don't be at Directory 😕

#### Return error of ft

##### `Error: No 'help.md' file`
1. You should restore 'help.md' file  in ft/doc

    1.2. How to resotre 'help.md' file

        1. Move to the 'ft/doc' directory

        2. Enter `touch help.md`

        3. Enter 'vim help.md'

        4. **Paste** [Held.md](###Help.md) into 'help.md'

        5. Enter `:wq` at vim

        6. Finish !
2. You should **install** the `ft` again


## Help

### Help.md
This is 'help.md' file
```
ft 4.0

USAGE:
    ft [FLAGS] [<text>] [<path>]

FLAGS:
    -h, --help          Prints help information

ARGS:
    <text>              Enter text to find in files in a directory
    <path>              Enter the name of the file or the directory
```

## Version
Now version: v4.0 (21/6/4)

## License
Use MIT License so everyone can use it 😉
