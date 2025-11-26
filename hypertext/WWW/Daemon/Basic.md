# https://info.cern.ch/hypertext/WWW/Daemon/Basic.html

Overview -- /Daemon

# The basic W3 server: Internals

This describes the generic hypertext [daemon](https://cern.la/hypertext/WWW/Terms.md#daemon) (server) program. The
daemon is part of the [WWW](https://cern.la/hypertext/WWW/TheProject.md) project. See also:

* [User guide](https://cern.la/hypertext/WWW/Daemon/User/Guide.md) .* [Bugs](https://cern.la/hypertext/WWW/Daemon/Bugs.md) and [Features](https://cern.la/hypertext/WWW/Daemon/Features.md)* [Other servers](https://cern.la/hypertext/WWW/Daemon/Overview.md)

The hypertext daemon, like the ftp daemon, is a program which responds
to an incomming tcp connection and provides a service to the caller.

## Sources

A compilation option (SELECT) controls whether more than one connection
can be handled at a time. This is a function of whether the TCP/IP
implementation beneath the application has a working "select()" routine.
If it is not true, this implementation services one connection, then
drops it before accepting another one. In neither case does the daemon
concurrently serve two clients, nor does it fork off a process to
do that.

The basic server loop is in the file [HTDaemon.c](https://cern.la/hypertext/WWW/Daemon/Implementation/HTDaemon.c) . A separate module
(for example [HTRetrieve.c](https://cern.la/hypertext/WWW/Daemon/Implementation/HTRetrieve.c) ) contains the code to handle one request.
Various specific versions of this may be written for different flavours
of server. Also used are various modules of WWW common code.
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)