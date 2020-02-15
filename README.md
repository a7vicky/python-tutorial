# Python Tutorial 

Install python 3.8 on rhel7/centos7 [guide](https://www.workaround.cz/howto-compile-install-latest-python-37-38-39-centos-7-8/)

Step 1 – prepare Linux box for Python compilation

```
sudo yum -y update
sudo yum -y install wget yum-utils gcc openssl-devel bzip2-devel libffi-devel
```
 

Step 2 – download and unpack Python source code
We download the a source code of latest Python from the official Python page https://www.python.org/ftp/python/ and extract Python-3.8.1.tgz to the  /tmp directory.

```
cd /tmp/
wget https://www.python.org/ftp/python/3.8.1/Python-3.8.1.tgz
tar xzf Python-3.8.1.tgz
cd Python-3.8.1
```
 

Step 3 – compile Python source code into binaries

```
sudo ./configure --enable-optimizations --with-lto --prefix=/opt/python38
sudo make -j <code>$(nproc)</code> sudo make altinstall
sudo rm /tmp/Python-3.8.1.tgz
```
 

Step 4 – Post-install stuff

Make post-install stuff

```
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python3
sudo ln -s /opt/python38/bin/python3.8 /opt/python38/bin/python
sudo ln -s /opt/python38/bin/python3.8 /usr/bin/python38
```

Add some symbolic links for pip
```
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip3
sudo ln -s /opt/python38/bin/pip3.8 /opt/python38/bin/pip
```




