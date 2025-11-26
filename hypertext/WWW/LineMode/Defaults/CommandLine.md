# https://info.cern.ch/hypertext/WWW/LineMode/Defaults/CommandLine.html#5

CommandLine -- /LineMode

# Command line syntax

The syntax is:
www [options] [docaddress [keywords]]
With no arguments, the [www](https://cern.la/hypertext/WWW/LineMode/Defaults/QuickGuide.md) shell command allows you to browse from
the system default page, /usr/local/lib/WWW/default.html.

Options should be specified before other arguments. Currently available
options are:-

-n: Non-interactive mode. Outputs the formatted document to the standard output, then exits. Pages are delimited with form feed (FF) characters. -: A minus sign with no trailing characters indicates that the program will accept [HTML format](https://cern.la/hypertext/WWW/LineMode/../MarkUp/MarkUp.md) input from the standard input. This allows www to be used as a filter from html to plain text for example. Relative links in the input are parsed as though the address of the document was that of the home page (or docaddress if specified). Implies non-interactive mode. -listrefs: Implies non-interactive. Adds a list of the addresses of all documents references to the end. -pn: where n is a number, specifies the page length. Without a number, makes the page length infinite. Default is 24. -source: Display the original source of a document instead of parsing it. Has effect for HTML from w3 servers, and news articles. (v1.2a or later) -v: Verbose mode: Gives a running commentary on the program's attempts to read data in various ways. -wn: where n is a number, specifies the page width in columns. The default is 78, 79 or 80 depending on the system. (v1.0 or later) -na: Hides anchor positions in the text. Useful, when printing out the document. -a format: Specifies the printf-style format string to be used when printing references. Must contain the two characters "%d" where the numbers should occur. Be sure to escape or quote any special characters you use. For example under unix:

www -a \<%d\>
www -a " (Type %d)"
If present, the next argument (docaddress) is the [hypertext address](https://cern.la/hypertext/WWW/Addressing/Addressing.md)
, of the document at which you want to start browsing. You may want
to define an alias for www followed by name of your favourite index.

Any further command line arguments are taken as keywords. The first
argument must refer to an index in this case. The index is searched
for entries matching the keywords, and a list of matching entries
is displayed.
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)