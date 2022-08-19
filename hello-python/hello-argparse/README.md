# Hello Argparse

Basic usage is:
```
parser = argparse.ArgumentParser()
parser.add_argument("--my-arg")
args = parser.parse_args()
print(args.my-arg)
```

Notes:
1. If you don't want the user to use a name (e.g. --output-file), you must specify a "dest" for that arg.
2. Unnamed args ("positional args") are required by default. If you want it to be optional you must specify "nargs='?'".
3. Named args are created simply by adding a name as the first parameter. You can add as many names as you want as long as they start with dashes.
4. Named args are optional by default. If you want it to be required add "required=True".
5. Boolean flags are created by specifying "action='store_true'". This will show up as True if the user enters the flag.
6. Notice that our named args have hyphens (--output-file) but get stored with underscores (args.output_file). Also notice that if two names are given, it uses the second (args.verbose instead of args.v).
7. Does type checking for you if you specify "type=".

Test run with: python parse_args.py "hi" -n 10