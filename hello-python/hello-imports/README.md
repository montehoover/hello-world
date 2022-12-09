# Importing local python files

## Simple case - files in the same folder

1. If you have another file in the same directory, simply say `import <the file>`:
    main.py:
    ```python
    import helpers

    helpers.hello()
    ```
    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ python3 main.py 
    hello from helpers.py
    ```
2. If the file is in a directory, simply do the same thing but add the directory name followed by a dot. Python simply treats all directories as "modules".
    File structure:
    ```
    hello_imports/
        main.py
        utils/
            my_util.py
    ```
    main.py:
    ```python
    import utils.my_util

    utils.my_util.do_something()
    ```

    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ python3 main.py 
    my_util.py doing something
    ```

## More complicated - files in sibling folders, absolute imports

It's surprisingly hard if you simply have two folders on the same level in a parent folder like this:
```
hello_imports/
utils/
    my_util.py
scripts/
    my_script.py
```    
There is a notion of relative imports in python but you can not simply use a path string with dots like `import "../utils/my_util.py`. Instead you use Python's module notation where you essentially replace slashes with dots and drop the file extensions: `import ..utils.my_util`. However the official PEP8 recommendation is to use absolute imports instead of these relative imports, and the relative imports don't work the way you would expect anyway. (More on [relative imports](#Relative-imports) below.)

How to import my_util.py from my_script.py:
1. As before, treat the directory structure as a python module:
    my_script.py
    ```python
    import utils.my_util

    def run():
        utils.my_util.do_something()

    run()
    ```

    Notice the error when you run this normally:
    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ python3 scripts/my_script.py 
    Traceback (most recent call last):
    File "scripts/my_script.py", line 2, in <module>
        import utils.my_util
    ModuleNotFoundError: No module named 'utils'
    ```

2. Confusingly, we have no problem running the same file but calling it from main.py instead of calling it directly:
    main.py:
    ```python
    import scripts.my_script

    scripts.my_script.run()
    ```

    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ python3 main.py 
    my_util.py doing something
    ```

    You can see that `main.py` calls `my_script.py` which imports `my_util.py`, and it has no problem this time. This is because the module import path changes depending on how a file is executed. We fix this by either calling the script as a module (`python -m`) or appending to `PYTHONPATH`.

2. Call the script as a module:
    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ python3 -m scripts.my_script
    my_util.py doing something
    ```

3. --or-- Append the project folder to `PYTHONPATH`:
    ```bash
    ~/code/hello-world/hello-python/hello-imports
    $ export PYTHONPATH=${PYTHONPATH}:$(pwd)
    ~/code/hello-world/hello-python/hello-imports
    $ python3 scripts/my_script.py 
    my_util.py doing something
    ```

## Python import locations

I don't like either of these. I don't like the module option because I'm used to being able to execute a python script in the simple explicit way, and on top of that I lose path completion when using the dot notation instead of slashes. I don't like the `PYTHONPATH` thing because I simply don't want to have to do that. But at least with that method it is more explicit what is happening and becomes a bit of a learning point. In the import process python searches for modules in four places in the following order:

1. Built in modules. These come with python like `math`, `random`, and `sys` and are found in the default installation location like `/usr/lib/python3.8/`. They can be viewed with `sys.modules` and `sys.builtin_module_names`.
2. Directory of the file. This (and the next two) can be seen listed in `sys.path`. The script directory is indicated by an empty string (`''`).
3. All the directories (if any) listed in `PYTHONPATH`. (Same syntax and the normal `PATH` variable.)
4. Things installed by pip/conda. (Pip: `<your venv>/lib/python3.8/site-packages`, Conda: `~/miniconda/envs/<your env>/lib/python3.8/site-packages`)

So you can see that by default python is looking for modules only in the exact folder where the script is located, and not searching the parent or sibling directories. Adding the parent to `PYTHONPATH` gives us what we want. This is also why running the script as a module works. If you add `import sys; print(sys.path)` to the end of my_script.py you can see that the current directory as the first entry to `sys.path`.

## Relative imports

Now it is possible to import based on relative path location, but this is officially discouraged, and even if you use it, it only works when the file is executed as a module. This is because the relative import mechanism looks in the path from a variable called `__package__` and that variable only gets created when a file is executed as a module. So the real use case here is for having a utility import another utility from the same project and you want to use a relative path to shorten the path name. You can see the way this works in `relative_import_script.py`:

relative_import_script.py
```python
from ..utils.my_util import do_something

do_something()
```

```bash
~/code/hello-world/hello-python/hello-imports
$ cd ..
~/code/hello-world/hello-python
$ python3 -m hello-imports.scripts.relative_import_script
my_util.py doing something
```

Notice that I had to cd up one level and call it naming the project directory as a module. This is because it constructs that `__package__` variable based on the modules specified on the command line (or when called from a file like `main.py`), and it treats the current working directory as the first parent directory about the script module. In our case this is `scripts`. So when it reads `..utils` it is looking for the parent of the current directory (`scripts`). If we didn't include `hello-imports` in our command, it wouldn't know what the parent of `scripts` is. 

That explanation was very confusing, and it probabl won't make sense until you play around with it. But basically the problem is that python is not actually using a notion of directory structure here for the relative import, rather it is using its own variable it constructs to represent the module's folder hierarchy, and only then looking in the actual filesystem.