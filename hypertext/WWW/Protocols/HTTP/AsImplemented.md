# HTTP as implemented in WWW

This document defines the Hypertext
Transfer protocol (HTTP) as currently
implemented by the [WorldWideWeb](https://cern.la/hypertext/WWW/TheProject.md) initaitive
software. This is a subset of the
[proposed](https://cern.la/hypertext/WWW/Protocols/HTTP.md) full HTTP protocol. No
client profile information is transferred
with the query. Future HTTP protocols
will be back-compatible with this
protocol.

The definition of this protocol is
in the public domain (see [policy](https://cern.la/hypertext/WWW/Policy.md)
).

The protocol uses the normal internet-style
telnet protocol style on a TCP-IP
link. The following describes how
a client acquires a (hypertext) document
from an HTTP server, given an HTTP
document [address](https://cern.la/hypertext/WWW/Addressing/HTTPAddressing.md) .

## Connection

The client makes a TCP-IP connection
to the host using the [domain name](https://cern.la/hypertext/WWW/Addressing/BNF.md#5)
or [IP number](https://cern.la/hypertext/WWW/Addressing/BNF.md#45) , and the [port number](https://cern.la/hypertext/WWW/Addressing/BNF.md#7)
given in the address.

If the port number is not specified,
80 is always assumed for HTTP.

The server accepts the connection.

Note: HTTP currently runs over TCP,
but could run over any connection-oriented
service. The interpretation of
the protocol below in the case of
a sequenced packet service (such
as DECnet(TM) or ISO TP4) is that
that the request should be one TPDU,
but the response may be many.

## Request

The client sends a document request
consisting of a line of ASCII characters
terminated by a CR LF (carriage return,
line feed) pair. A well-behaved server
will not require the carriage return
character.

This request consists of the word
"GET", a space, the [document address](https://cern.la/hypertext/WWW/Addressing/BNF.md#1)
, omitting the "http:, host and port
parts when they are the coordinates
just used to make the connection.
(If a gateway is being used, then
a full document address may be given
specifying a different naming scheme).

The search functionality of the protocol
lies in the ability of the addressing
syntax to describe a [search on a
named index](https://cern.la/hypertext/WWW/Addressing/Search.md) .

A search should only be requested
by a client when the index document
itself has been descibed as an index
using the [ISINDEX tag](https://cern.la/hypertext/WWW/MarkUp/Tags.md#18) .

## Response

The response to a simple GET request
is a message in hypertext mark-up
language ( [HTML](https://cern.la/hypertext/WWW/MarkUp/MarkUp.md) ). This is a byte
stream of ASCII characters.

Lines shall be delimited by an optional
carriage return followed by a mandatory
line feed chararcter. The client
should not assume that the carriage
return will be present. Lines may
be of any length. Well-behaved servers
should retrict line length to 80
characters excluding the CR LF pair.

The format of the message is HTML
- that is, a trimmed SGML document.
Note that this format allows for
menus and hit lists to be returned
as hypertext. It also allows for
plain ASCII text to be returned following
the [PLAINTEXT tag](https://cern.la/hypertext/WWW/MarkUp/Tags.md#7) .

The message is terminated by the
closing of the connection by the
server.

Well-behaved clients will read the
entire document as fast as possible.
The client shall not wait for user
action (output paging for example)
before reading the whole of the document.
The server may impose a timeout
of the order of 15 seconds on inactivity.

Error responses are supplied in human
readable text in HTML syntax. There
is no way to distinguish an error
response from a satisfactory response
except for the content of the text.

## Disconnection

The TCP-IP connection is broken by
the server when the whole document
has been transferred.

The client may abort the transfer
by breaking the connection before
this, in which case the server shall
not record any error condition.

Requests are [idempotent](https://cern.la/hypertext/WWW/Protocols/HTTP.md#13) . The server
need not store any information about
the request after disconnection.

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)