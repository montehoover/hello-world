import argparse

# 1. If you don't want the user to use a name (e.g. --output-file), you must specify a "dest" for that arg.
# 2. Unnamed args ("positional args") are required by default. If you want it to be optional you must specify "nargs='?'".
# 3. Named args are created simply by adding a name as the first parameter. You can add as many names as you want as long as they start with dashes.
# 4. Named args are optional by default. If you want it to be required add "required=True".
# 5. Boolean flags are created by specifying "action='store_true'". This will show up as True if the user enters the flag.
# 6. Notice that our named args have hyphens (--output-file) but get stored with underscores (args.output_file). Also notice that if two names are 
# given, it uses the second (args.verbose instead of args.v).
# 7. Does type checking for you if you specify "type="
# Test run with: python parse_args.py "hi" -n 10


parser = argparse.ArgumentParser(description="Example of parsing command line args.")
parser.add_argument(dest="greeting", help="The first argument on the command line. Not optional")
parser.add_argument(dest="in_file", nargs='?', default='some_file.txt', help="The second argument. Optional")
parser.add_argument("-o", "--output-file", default="out_file.txt", help="An optional argument specified by a name.")
parser.add_argument("-n", "--num-lines", required=True, help="An argument that must be entered by name. Not optional")
parser.add_argument("-v", "--verbose", action="store_true", help="Boolean flag for making verbose. Optional, and True only if entered")
parser.add_argument("--number", type=int, help="Does int type checking for us.")
parser.add_argument("--file", type=argparse.FileType('r'), help="Ensures file exists")
args = parser.parse_args()

print(args.greeting)
print(args.in_file)
print(args.output_file)
print(args.num_lines)
print(args.verbose)
print(args.number)
print(args.file)
