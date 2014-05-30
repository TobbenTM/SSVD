#Drobo Config

You need:

* SSH Access
* Apache (or some other web server)
* Python 2.7.5

##Setup ssvd

* Copy ssvd directory to DroboApps directory.
* Config conf.json
* Run setup

    python setup.py
		
* Run initial index

    python tree.py
		
You should now be able to access your library at http://drofo-fs.local !

##Setup cron:

Follow [this](http://blog.troyastle.com/2010/06/activate-cron-daemon-on-drobofs.html) guide.

Setup rule:

    crontab -e
		00 02 * * * python /mnt/DroboFS/Shares/DroboApps/ssvd/bin/tree.py