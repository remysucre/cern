# https://info.cern.ch/hypertext/WWW/Daemon/User/Installation.html

Installation -- /User

# Installing te basic httop daemon

The usual way to install a daemon is to either run it from the bootstrap
command file (for example /etc/rc) so that it runs continuously, or
to set up the internet daemon (inetd) to run it when a call comes
in.

Remember to make a [rule file](https://cern.la/hypertext/WWW/Daemon/User/RuleFile.md) unless you explicitly supress it with
the -R option.

## Using the Internet daemon

There is a csh script to do this for a BSD unix system. You might
want to edit it to run on other systems.

Otherwise, just follow the [instructions for installing a server under
the internet daemon](https://cern.la/hypertext/WWW/Daemon/User/Inetd.md).

## Log file

If a log file is required, make sure that the user name under which
the daemon is run has the right to write the file
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)