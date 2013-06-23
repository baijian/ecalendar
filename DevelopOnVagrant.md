
## Develop 

Before develop, you need a [Python](http://python.org/) environment, and please install [Vagrant](http://www.vagrantup.com/).

Please follow [Google Python Style Guide](http://google-styleguid.googlecode.com/svn/trunk/pyguide.html).

### Get codes

First [Fork](https://github.com/liangsun/ecalendar/fork_select) codes to your own github account, then clone the codes.

```
$ git clone git@github.com:${github_name}/ecalendar.git
```

```
$ git remote add upstream git@github.com:liangsun/ecalendar.git
```

### Prepare develop environment

```
$ cd ecalendar
$ script/bootstrap
$ .bootstrap/ve fab vagrant develop
```

script/bootstrap will download vagrant precise64.box, then deploy develop environment in vm, it will cost some download time.

if you haven't add box precise64.box to your computer, vagrant will automatically download from http://files.vagrantup.com/precise64.box

```
$ vagrant box add precise64.box http://files.vagrantup.com/precise64.box
```

if network is not very good, you can set a http proxy

```
$ export http_proxy=http://proxy.xxx.com:1111
$ script/bootstrap
```

### Run the project

Enter the vm
```
$ .bootstrap/ve vagrant ssh
```

#### Init the database
```
vagrant@precise64:/vagrant$ mysql -u<root> -p<password>
vagrant@precise64:/vagrant$ create database huodongrili
vagrant@precise64:/vagrant$ source db.sql 
```

#### Start Web Service
```
vagrant@precise64:/vagrant$ python manager.py runserver 0.0.0.0:8000

open chrome of your system [http://192.168.222.6:8000/admin/](http://192.168.222.6:8000)

#### SSH

#### MySQL

#### Commands

* start vm
>`$ .bootstrap/ve vagrant up`

* shoutdown vm 
>`$ .bootstrap/ve vagrant halt`

* reload conf of vm
>`$ .bootstrap/ve vagrant reload`

* provision develop environment
>`$ .bootstrap/ve fab vagrant develop`

* enter vm
>`$ vagrant ssh`

