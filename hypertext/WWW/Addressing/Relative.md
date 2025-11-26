# https://info.cern.ch/hypertext/WWW/Addressing/Relative.html

/Net/cernvax/userd/tbl/hypertext/WWW/Addressing/Relative.html

# Relative naming

The address of a hypertext document is normally given within the context
of another hypertext document. Where the addresses of the two documents
are the similar, this allows only the difference between the two names
to be given, saving space. An example is the address of the [destination
of a hypertext link](https://cern.la/hypertext/WWW/MarkUp/Tags.md#13) , which is specified relative to the source document
address.

(A futher practical advantage is that a group of documents may be
transmitted without internal changes, or accessed using more than
one address.)

This implies that certain characters ("/", "..") have a significance
reserved for representing a hierarchical space, and must be recognized
as such by both clients and servers.

In the [WWW address format](https://cern.la/hypertext/WWW/Addressing/Addressing.md) , the rules for relative naming are:

* If the " [scheme](https://cern.la/hypertext/WWW/Addressing/Addressing.md#17) " parts are different, the whole absolute address
  must be given. Other wise, the scheme is omitted, and:* If the "host" and/or "port" [parts](https://cern.la/hypertext/WWW/Addressing/BNF.md#3) are different, the host name and
    all the rest of the address must be given. The host name may be given
    using internet hostname conventions, ie domains may be omitted where
    different. This is not very well defined: one tends to assume that
    if any dot is present, then the full domain name is being given, up
    to the root (.) domain, while if there are no dots, the domain is
    the same as that of the hostname part of the the base address.* If the access and host parts are the same, then the path may be given
      with the unix convention, including the use of ".." to mean indicate
      deletion of a path element. Within the path:* If a leading slash is present, the path is absolute. Otherwise:* The last part of the path of the base address (e.g. the filename of
          the current document) is removed, and the given relative address
          appended in its place.* Within the result, all occurences "xxx/.." or "/." are recursively
            removed, where xxx is one path element (directory).

The use of the slash "/" and double dot ".." in this case must be
respected by all servers. If necessary, this may mean converting their
local representations in order that these characters should not appear
within path elements (see ["escaping"](https://cern.la/hypertext/WWW/Addressing/Escaping.md) ).