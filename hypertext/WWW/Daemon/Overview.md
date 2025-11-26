# https://info.cern.ch/hypertext/WWW/Daemon/Overview.html

Overview -- /Daemon

# W3 Server Software

A [W3](https://cern.la/hypertext/WWW/TheProject.md) server, like the ftp [daemon](https://cern.la/hypertext/WWW/Terms.md#daemon) , is a program which responds to
an incoming tcp connection and provides a service to the caller.There
are many varieties of W3 server software to serve different forms
of data.

## The basic daemon

The basic W3 daemon program serves files already in hypertext or
plain text. This daemon then is used as a basis for many other types
of server and gateway. Documentation includes:

* [User guide](https://cern.la/hypertext/WWW/Daemon/User/Guide.md) .* [Internals](https://cern.la/hypertext/WWW/Daemon/Basic.md) -- a description of the code.

Much of the above may also apply in whole or part to other servers
mentioned below. Whatever server you are running, you will probably
be interested in:

* [Tools for information providers](https://cern.la/hypertext/WWW/Tools/Overview.md)

## Making a new server

This daemon is often used as a basis for a more specific server for
a given application. A server which allows a world of data to be
seen as part of the W3 universe is known as a gateway. (Most servers
could therefore be regarded as gateways, but the term implies some
conversion or mapping between dissimilar worlds) . For short tutorials
with examples, see:

* [Writing a server in C](https://cern.la/hypertext/WWW/Daemon/JanetAndJohn.md)* [Writing a server as a script](https://cern.la/hypertext/WWW/Provider/ShellScript.md)

It is a good idea to pick the basic daemon or one of the servers below
as a starting point when making a new server.

## Other servers and Gateways

These are servers which provide data extracted from other systems.
they are built using code from the basic daemon, or scripts.

[FIND gateway](https://cern.la/hypertext/WWW/FIND/Overview.md): for CERN/VM XFIND which calls a REXX exec to get the information from the XFIND system running on the CERNVM mainframe. [VMS Help gateway](https://cern.la/hypertext/WWW/VMSHelp/Overview.md): This allows any VMS help files to be made available to WWW clients. Runs on VAX/VMS. [WAISGate](https://cern.la/hypertext/WWW/Daemon/WAISGate.md): A gateway to information available using the W.A.I.S. protocol. [DCLServer](https://cern.la/hypertext/WWW/Daemon/DCLServer.md): A server for VMS systems which allows you to write a gateway to your own favorite information system using DCL. [System33](https://cern.la/hypertext/WWW/Daemon/System33/Gateway.md): A (big) csh script server providing data including Xerox System33 documents, man pages in plain text, phone numbers, etc. etc...! [Oracle](https://cern.la/hypertext/WWW/Daemon/Oracle/Overview.md): A generic server to oracle. Could be used as a basis for gateways to specific Oracle databases. [Geography](https://cern.la/hypertext/WWW/Daemon/Geography/Overview.md): Gateway to the

Geography server at U Michigan[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)