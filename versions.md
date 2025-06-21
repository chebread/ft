# Versions

### v1.0
Mode: Find file

### v2.0
Mode: Find Directory in file

### v3.0
mode: Add -h flag

### v4.0
Edit -h flag error

### v5.0
Edit -h flag error, Add -V flag

### v5.1
1. Add  -h and --help flag function
2. Edit NameError error

### v5.2
1. Edit return value or ft. Add -1 of value of no directory
2. Added ability to find for string in any-type directories 😎

### v5.3
Entering `'*'` in `(path)` allows you to find for a string in files in the directory you currently belong to 😌

### v6.0
1. Now you can find files in a directory or file were included to a directories 😎

2. Now you can find the string in any file, All the result of finding all files are printed

### v6.1
Edit return value of FindDir function.

### v6.2
Edit bug of FindDir

### v6.3
Edit the FindDir function to not read the `.git` directory

### v6.4
Edit the FindDir function design to print

### v6.4.2
Add the FindDir function to not read the `.DS_Store` file

### v6.4.3
Add the FindDir function to not read the `.github` file

### v7.0
Now You can find for a string in any files or directories, files created with the pickle module cannot be finded

### v7.0.1
Edit `doc/help.md` file

### v7.1.0 (important upgrade)
Edit the FindDir function bugs, errors 😎

### v7.1.1
Clean code

### v7.1.2
Edit the FindDir function to return value of -1 (No find to files and directories)

### v7.1.3
Edit the FindDir function to return value of -1 of function

### v7.2.0 (A little important upgrade)
you can find a string regardless of uppercase and lowercase letters

### v7.2.1
Edit the value of result (directory)

### v7.3.0 (A little important upgrade)
Edit value of result (all)

### v7.3.1
Change `'*' to `!``

### v7.3.2
Add expert sentense of 0x80 bytes..

### v7.4.0
Add functions to v7.2.0 have been corrected

### v7.4.1
Add '*' or '!', too

### v7.4.2
Edit global varibale at file of value

### v7.4.3
Edit code clean

### v7.4.4
Edit code clean and fix bugs

### v7.4.5
Add value of 1 at the PrintValue function

### v7.5.0
1. If try `ft (blank) (blank)`, Now you get list of files
2. Print files is sorted 🤩

### v7.5.1
If try `ft <text or not blank> (blank)`, you get same print as `ft <text> (! or '*')`

### v7.5.2
Edit bug of 'v7.5.1'

### v7.5.3
Edit bug of 'v7.5.2'

### v7.5.4
Edit bug of 'v7.5.3'

### v7.5.5 (Important upgrade)
1. Edit bug of 'v7.5.4'
2. Edit bug of FindDir, IndexError

### v7.5.6
Edit `help.md` file

### v7.5.7
Add text of 'versions.md'

### v7.6.0 (A little important upgrade)
Edit the indFile in find() function. The find() function has been changed to the KMP algorithm, The KMP algorithm is definded as the Find() fucntion 😎

### v7.6.1 (Important upgrade)
Edit bug of v7.6.0

### v7.6.2 (Important upgrade)
1. Edit bug of v7.6.1
2. Edit the 'readme.md' file

### v7.6.3 (Important upgrade)
1. Edit bug of v7.6.2
2. Edit bug of `ft`

### v7.6.4
Edit the fucntion Find of the bug

### v7.6.5
Edit bugs of `ft`

### v7.6.6
Add the function of man

### v7.6.7
Add the function of all file to find 😎

### v7.6.8
Edit print of file-list. It don't view of all file-list, Now view short file-list 🤩

### v7.7.0 (Important upgrade)
Add the function of color, It look better when you look at the print 🥳

### v7.7.1 (Important upgrade)
Edit the PrintValue function of bugs

### v7.7.2
Edit the help page of Version place, It is changed the `pyfiglet` of `ogre` font. May It be change !

### v7.7.3
Edit interface of print `ft -h`. Become v7.7.1 of print `ft -h`

### v7.7.4
Clean code of `ft`

### v7.7.5
Edit the Print function of bugs

### v7.7.6
1. Edit bugs of `ft`.
2. Add the fucntion of blank file read to print

### v7.7.7
Edit the bug of `ft`.

### v7.7.8
Edit code, Clean code of `ft`

### v7.8.0 (Important upgrade)
Add the FindDir function to not read the `.png` file! 🙂

### v7.8.1 (Important upgrade)
Edit bug of `v7.8.0`, Fix the export sentense in function of `Print`

### v7.8.2
Clean code of `ft`

### v7.8.3
Edit sentense of `ft.1` man file

### v7.8.4
Edit Flags function, because yet Argv is global variable, but now argv is argv variable

### v7.8.5
Edit v7.8.4 bugs, v7.8.4에서 고친 버그들이 더욱더 잘못되게 다시 고쳤습니다.

### v7.9.0
.png, .mov, .jpg, env, ... 등 문자열 검색이 불가능 한 파일들이나 보안이 요구되는 파일을 읽지 않도록 수정햐였습니다.

### v7.9.1
Add don't read file '.swp'.

### v8.0.0
This time update be about user securities 🔒
1. Now, You can find files only Markdown file, Python file, text file, LICENSE file, Ruby file, Unix command man file. but You can add readable file list. That's add readable file list at number 69 of exec.py file 😃
2. 또한, 사용자가 텍스트로 읽을 수 없거나 보안이 요구되는 디렉토리를 ft가 못 읽도록 설정하였습니다. ft가 못 읽는 디렉토리는 .git, .github, node_modules, .vscode, build 가 있습니다. 또한, ft가 아예 읽을 수 없도록 하는 파일은 .env, .localized, .gitignore 가 있습니다.

### v8.0.1
Remove test.txt, Etc bugs fixed.

### v8.0.2
Changed the clint module used to use color when printing output to the rich module.

### v8.0.3
Change doc internal file format from md to txt
Fix minor things
