# This is a bash script for Ubuntu based distros for setting up all the 
# programming languages I want to use
echo 'this will require su privileges to run properly'
echo
echo 'installing package managers and PPAs'
echo 'This will require some input from user'
echo
sleep 1.5s

# installs sdkman jdk/jvm language manager, rustup rust manager, choosenim nim
# manager, deadsnakes python ppa, pypy python ppa, openjdk java manager,
curl -s "https://get.sdkman.io" | bash
curl https://sh.rustup.rs -sSf | sh
curl https://nim-lang.org/choosenim/init.sh -sSf | sh
sudo add-apt-repository ppa:deadsnakes/ppa -y
sudo add-apt-repository ppa:pypy/ppa -y
sudo add-apt-repository ppa:openjdk-r/ppa -y

sudo apt update -y

echo
echo 'installing compilers'
echo
sleep 0.5s

# this allows lts ubuntu versions to get unstable stuff
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y

# installs gcc 9, clang c family compiler, tcc c compiler, typescript, 
# D reference
sudo apt install gcc-9 g++-9 -y
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-9

curl -SL http://releases.llvm.org/8.0.1/clang+llvm-8.0.1-x86_64-linux-gnu-ubuntu-18.04.tar.xz | tar -xJC .
mv clang+llvm-8.0.1-x86_64-linux-gnu-ubuntu-18.04 clang_8.0.1
sudo mv clang_8.0.1 /usr/local/

sudo apt install tcc
npm install -g typescript
curl -fsS https://dlang.org/install.sh | bash -s dmd

echo
echo 'installing programming languages'
echo 'note that some languages have been installed with the first step'
echo
sleep 0.5s

# installs python3.8, gcc go, lua5.3, ruby, nodejs, c#, haskell, java 8 and 11,
# gcc D, kotlin, groovy, kotlin kscript, pypy, pypy3
sudo apt install python3.8 gccgo lua5.3 ruby-full nodejs haskell-platform openjdk-8-jdk openjdk-11-jdk gdc pypy pypy3
sdk install kotlin groovy kscript

wget -q https://packages.microsoft.com/config/ubuntu/16.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb
sudo dpkg -i packages-microsoft-prod.deb
sudo apt-get install apt-transport-https
sudo apt-get update
sudo apt-get install dotnet-sdk-2.2
./dotnet-install.sh -c Current

echo
echo 'appending bashrc'
echo
sleep 1s

echo 'export PATH=.:~/.cargo/bin:$PATH' >> ~/.bashrc
echo 'export PATH=/usr/local/clang_7.0.1/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/clang_7.0.1/lib:$LD_LIBRARY_PATH' >> ~/.bashrc

