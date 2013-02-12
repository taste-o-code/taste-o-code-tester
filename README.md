Taste-o-Code Tester
===================

Link to project: [Taste-o-Code](http://taste-o-code.com)  
Project's description and goals: [about page](http://taste-o-code.com/about)

This repo is a part of Taste-o-Code that tests tasks.

It requires python2.7.

Add environment variable to profile (e.g. .bashrc):
```shell
export TOC_TESTER_PATH=%path to this repo%
```

Installing redis:

```shell
wget http://redis.googlecode.com/files/redis-2.4.6.tar.gz
tar xzf redis-2.4.6.tar.gz
cd redis-2.4.6
make
sudo cp src/redis-server src/redis-cli /usr/bin
sudo mkdir /etc/redis
sudo cp redis.conf /etc/redis
```

Setup password in redis.conf

Running redis on boot

```shell
sudo cp TOC_TESTER_PATH/scripts/configs/redis.conf /etc/init
```

To run redis you can reboot or run 'sudo start redis'

Installing pyres:

```shell
sudo apt-get install python-setuptools
sudo apt-get install python-dev
git clone git://github.com/nbeloglazov/pyres.git
cd pyres
python setup.py build
sudo python setup.py install
```


Installing python specific packages

```shell
sudo apt-get install python-yaml
```

Installing additional dependences for tester

```shell
sudo apt-get install timeout
```


Installing prolog

```shell
wget http://www.gprolog.org/gprolog-1.4.0.tar.gz
tar xvf gprolog-1.4.0.tar.gz
cd gprolog-1.4.0/src
./configure
make
sudo make install
```


Installing clojure (run gen_playgrounds.py script before to create playground)

```shell
wget 'http://search.maven.org/remotecontent?filepath=org/clojure/clojure/1.4.0/clojure-1.4.0.jar'  -O %PATH_TO_PlAYGROUND%/files/clojure-1.4.0.jar
```

Installing Unlambda

```shell
wget ftp://quatramaran.ens.fr/pub/madore/unlambda/unlambda-2.0.0.tar.gz
tar xvf unlambda-2.0.0.tar.gz
cd unlambda-2.0.0/c-refcnt/
gcc unlambda.c -o unlambda
cp %PATH_TO_PLAYGROUND%/sandbox-files/unlambda
```
