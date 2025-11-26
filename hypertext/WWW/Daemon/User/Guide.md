# https://info.cern.ch/hypertext/WWW/Daemon/User/Guide.html

Guide -- /User

# WWW Daemon user guide

The http daemon, [httpd](https://cern.la/hypertext/WWW/Daemon/User/Installation.md) , is a general server program which runs a
w3 protocol, " [HTTP](https://cern.la/hypertext/WWW/Protocols/HTTP/AsImplemented.md) ".

## More Information

[Distribution](https://cern.la/hypertext/README.md): How to get the code. [Compilation](https://cern.la/hypertext/WWW/Daemon/User/Compilation.md): How to compile the daemon for your system. [Installation](https://cern.la/hypertext/WWW/Daemon/User/Installation.md): How to install a server under unix internet daemon [Options](https://cern.la/hypertext/WWW/Daemon/User/CommandLine.md): Command line options at run time [Rule File](https://cern.la/hypertext/WWW/Daemon/User/RuleFile.md): The format of a rule file. By default, /etc/httpd.conf [Debugging](https://cern.la/hypertext/WWW/Daemon/User/Debugging.md): If it doesn't seem to work [Known bugs](https://cern.la/hypertext/WWW/Daemon/Bugs.md): and improvements desired [History](https://cern.la/hypertext/WWW/Daemon/Features.md): change list of improvements made and bug fixes.

## Note

During the test phase of the WWW project, the port number to which
the daemon listens was 2784. W3 has officially allocated port number
80. Servers should use port 80 and advertise their address with the
explicit port number (i.e. http://host:80/etc...). Details of the
final changeover plan will be advertised on the www-announce [mailing
list](https://cern.la/hypertext/WWW/Administration/Mailing/Overview.md) .

Background: [The W3 project](https://cern.la/hypertext/WWW/TheProject.md) , [Other servers](https://cern.la/hypertext/WWW/Daemon/Overview.md) .

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)