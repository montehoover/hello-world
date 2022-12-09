1. Ensure cmake is installed. It comes with VS build tools on Windows and can be installed with `apt install cmake`.
    ```
    $ cmake --version
    cmake version 3.16.3
    ```

2. We will call cmake to create the infrastructure required for your system's build engine (`make` for Linux or `msbuild` for Windows). The build engine will ultimately call the compiler. So the workflow looks like `cmake` -> `make` -> `g++`.  
Make the build directory, cd into it, and call cmake from there so build artifacts will be stored there. Cmake automatically looks for a file titled `CMakeLists.txt` in the directory you specify.
    Linux:
    ```
    $ mkdir build && cd build
    $ cmake ..
    -- The C compiler identification is GNU 9.4.0
    ...
    Running on Linux...
    -- Configuring done
    -- Generating done
    -- Build files have been written to: /home/monte/code/hello-world/hello-cpp/hello-cmake/build

    ```
    Windows:
    ```
    > mkdir build; cd build
    > cmake ..
    -- Building for: Visual Studio 17 2022
    -- Selecting Windows SDK version 10.0.19041.0 to target Windows 10.0.22000.
    -- The C compiler identification is MSVC 19.32.31332.0
    ...
    Running on Windows...
    -- Configuring done
    -- Generating done
    -- Build files have been written to: C:/Users/monte/code/hello-world/hello-cpp/hello-cmake/build
    ```

3. Call the build engine.
    Linux:
    ```
    $ make
    Scanning dependencies of target hello-cmake
    [ 50%] Building CXX object CMakeFiles/hello-cmake.dir/hello-cmake.cpp.o
    [100%] Linking CXX executable hello-cmake
    [100%] Built target hello-cmake
    ```
    
    Windows:
    ```
    > msbuild hello-cmake.sln
    Microsoft (R) Build Engine version 17.2.1+52cd2da31 for .NET Framework
    Copyright (C) Microsoft Corporation. All rights reserved.
    Building the projects in this solution one at a time. To enable parallel build, please add the "-m" switch.
    Build started 7/9/2022 5:02:07 PM.
    Project "C:\Users\monte\code\hello-world\hello-cpp\hello-cmake\build\hello-cmake.sln" on node 1 (default targets).
    ValidateSolutionConfiguration:
      Building solution configuration "Debug|x64".
    ...
    Done Building Project "C:\Users\monte\code\hello-world\hello-cpp\hello-cmake\build\hello-cmake.sln" (default targets).
    Build succeeded.
        0 Warning(s)
        0 Error(s)
    ```

4. Run the executable:
    Linux:
    ```
    $ ./hello-cmake
    hello, cmake
    ```

    Windows:
    ```
    > Debug\hello-cmake.exe
    hello, cmake
    ```
