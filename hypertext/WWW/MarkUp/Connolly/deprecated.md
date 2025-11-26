# https://info.cern.ch/hypertext/WWW/MarkUp/Connolly/deprecated.html

HTML Guide: Obscure Usage

# Deprecated Usage

These SGML constructs are too messy to support even
in the sample implementation. But they are implemented
by, for example, the SGMLs parser by James Clark.
It is in direct conflict with the SGML standard not to
support these, but tough cookies.

newline foo.
marked sections ignore:  ]]>

marked sections cdata:  hideous stuff: </HTML id=#foo>

untermiated end tag:   The start tag for this DL element is not terminated. By virtue of
    SHORTTAG YES in the SGML declaration, this is legal.