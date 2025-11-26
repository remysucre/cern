# https://info.cern.ch/hypertext/WWW/Daemon/WAISGate.html

WAISGate -- /Daemon

# The W.A.I.S. - WWW gateway

This is an example of a WWW [server](https://cern.la/hypertext/WWW/Daemon/Overview.md) and a [WAIS](https://cern.la/hypertext/Products/WAIS/Overview.md) client. It uses the
common WWW daemon [sources](https://cern.la/hypertext/WWW/Daemon/Overview.md#13) and also has one extra file, [WAISGate.c](https://cern.la/hypertext/WWW/Daemon/Implementation/WAISGate.c)
The [command line syntax](https://cern.la/hypertext/WWW/Daemon/User/Guide.md) is the same as for the normal W3 daemon, except
that a rule file is not used. (No -r or -R options).

See a summary of [some data available through the gateway](https://cern.la/hypertext/Products/WAIS/Sources/Overview.md) .

## WSRC files

The gateway keeps a cache of WAIS "source" files. These are files

describing WAIS servers. They are normally picked up automatically
by searching a "directory of servers" index. Once the gateway has
picked up a desciption of a server, it uses the description to describe
the server to those who follow links to it.

These source files are converted into hypertext, and are kept in the
directory /usr/local/lib/WAIS under the server name, port, and database
name.

To add an extra source file to this cache by hand, feed it as standard
input to the ParseWSRC program.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)