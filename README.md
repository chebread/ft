# ft
`ft` is a plugin that find for a string in a file 😎 It a little bit like [`ripgrep`](https://github.com/BurntSushi/ripgrep), [`fd`](https://github.com/sharkdp/fd) 🗂
## How to use

### Installation ⚙️
1. **Enter** `git clone https://github.com/developerHaneum/ft.git` at Terminal

2. **Add** `.zshrc` to `alias ft="usr/bin/python3 (Cloned or Downloaded directory path)/exec.py"`

### How to use `man ft` 📚
**Enter** `cp (Cloned or Downloaded directory path of 'ft')/doc/ft.1 /usr/local/share/man/man1/ft.1` at Terminal

## Basics to use

### USAGE 🏠

#### `ft [FLAGS/<text>] [OPTIONS/<path>]`
This basics form is **find** a string in a file and a string in among the files in the directory. 🤩

### Tips of USAGE
- **If you don't want to write qutoes, You don't use to write  qutoes ! (Most of case)😉**

- **As of v7.2.0, you can find a string regardless of uppercase and lowercase letters**

### FLAGS

#### `ft -h` or `ft --help`
Prints **help** information 😝

#### `ft -V` or `ft --version`
Prints the information **version** of `ft` 😗

### OPTIONS

#### `ft <text> !` or `ft <text> '*'` or `ft <text or not blank> (blank)`
Entering `!`, `*` in `(path)` allows you to find for a string in files in the directory you **currently** belong to 😌

### Return value of `ft`

#### `1` or `(Numbers)`
Text be at file or Text be at directory (Directory mode return path, too 😝)

#### `0`
File or Directory don't be 😢

#### `-1`
Text don't be at file or Text don't be at Directory 😕

### Return color of `ft`

#### Blue 🧢
It mean is **directories** 

#### Green 🚛
It mean is directories in **files**

#### Yellow 🥎
It mean is **files**

#### White 🐮
It mean is a **number**

<!-- ## Help

### ~~5.2 version shouldn't~~ -> **v6.0 was resolved in version** 🤩
1. ~~If a directory exists inside a directories~~

    ~~I will add this function ASAP 😭~~

### ~~v7.8.5 이하 버전들은  등의 파일들을 읽기 때문에, 되도록이면 .png, .jpg, .env, node_modules (dir) 등과 같은 파일이나 디렉토리가 있는 곳에서 버그가 고쳐질때 까지 ft 를 사용하지 마세요 😢~~ -> This issue has been **resolved in version v7.9.0** 🥳

### v8.0.0 에서 v7.8.5에 관한 버그를 완벽히 수정하였습니다. 자세한 설명은 versions.md 파일을 읽어보세요! 😃

### How to use of `ft '' !` or `ft (blank) (blank)`
It **find** for a string in **all files** in the directory you currently belong to 🥳

## Goal

### I will want to upload to Homebrew package 👻
But It isn't **enough** level of completion 🥲 -->

## Version
✋Now version: **v8.0.3** (25/04/21) 🎇

## License
MIT LICENSE &copy; 2021-2025 Cha Haneum
