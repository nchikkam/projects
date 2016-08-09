C:\n\mv\projects\fp\hs>cabal update
Downloading the latest package list from hackage.haskell.org

C:\n\mv\projects\fp\hs>cabal install parallel
Resolving dependencies...
Downloading parallel-3.2.1.0...
Configuring parallel-3.2.1.0...
Building parallel-3.2.1.0...
Installed parallel-3.2.1.0

C:\n\mv\projects\fp\hs>ghc -O2 --make parallel.hs -threaded -rtsopts
[1 of 1] Compiling Main             ( parallel.hs, parallel.o )

parallel.hs:4:1: warning: [-Wtabs]
    Tab character found here, and in six further locations.
    Please use spaces instead.
Linking parallel.exe ...

C:\n\mv\projects\fp\hs>ghc parellel.hs

C:\n\mv\projects\fp\hs>parallel.exe
1405006117752879898543142606244511569936384000014954
