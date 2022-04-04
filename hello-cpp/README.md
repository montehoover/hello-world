# Linux

1. Install gcc compiler: `$ sudo apt install gcc`
2. Compile hello.cpp to create an executable program: `$ gcc hello.cpp`
(There should be no output)
3. Check to see if it created the executable program named `a.out`:
```
$ ls
a.out  hello.cpp
```
4. Execute `a.out`:
```
$ ./a.out
hello, world
```

# Windows

1. Install Visual Studio Build Tools to get C++ compiler: https://visualstudio.microsoft.com/downloads/#other
2. Launch Developer Command Prompt
3. Check to make sure compiler `cl.exe` is available:
```
> cl.exe
Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30133 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

usage: cl [ option... ] filename... [ /link linkoption... ]
```
4. Compile hello.cpp to create an executable program: `$ cl hello.cpp`
```
> cl hello.cpp
Microsoft (R) C/C++ Optimizing Compiler Version 19.29.30133 for x86
Copyright (C) Microsoft Corporation.  All rights reserved.

hello.cpp
C:\Program Files (x86)\Microsoft Visual Studio\2019\BuildTools\VC\Tools\MSVC\14.29.30133\include\ostream(746): warning C4530: C++ exception handler used, but unwind semantics are not enabled. Specify /EHsc
hello.cpp(5): note: see reference to function template instantiation 'std::basic_ostream<char,std::char_traits<char>> &std::operator <<<std::char_traits<char>>(std::basic_ostream<char,std::char_traits<char>> &,const char *)' being compiled
Microsoft (R) Incremental Linker Version 14.29.30133.0
Copyright (C) Microsoft Corporation.  All rights reserved.

/out:hello.exe
hello.obj
```
5. Note that it created two files: `hello.obj` and `hello.exe`. `hello.obj` contains binary code that calls other libraries, and these are combined by the linker into `hello.exe`.
6. Execute the program:
```
> hello.exe
hello, world
```