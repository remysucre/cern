# https://info.cern.ch/hypertext/WWW/MarkUp/Connolly/complete.html

# A Complete Set of Constructs

The [recommended usage](https://cern.la/hypertext/WWW/MarkUp/Connolly/recommended.md) is
incomplete; it only includes those constructs that are easy to
implement and explain. This section discusses a few more constructs
that allow you to do anything that can legally be done. There are [constructs beyond these](https://cern.la/hypertext/WWW/MarkUp/Connolly/supported.md), but they
can all be reduced to constructs shown here.

## Document Structure

An HTML document is a header part followed by a BODY element.

The header part consists of the TITLE, ISINDEX, and NEXTID elements
which each appear zero or one time in any order. (see [ISINDEX test](https://cern.la/hypertext/WWW/MarkUp/Connolly/structure1.md), [no title test](https://cern.la/hypertext/WWW/MarkUp/Connolly/structure2.md))

The BODY start and end tags may be omitted. They will be inferred by
SGML parsers. ["Recommended
Usage"](https://cern.la/hypertext/WWW/MarkUp/Connolly/recommended.md) is an example of this. This entity is an example of
explicitly including the BODY tags.

The PLAINTEXT tag signals the end of the HTML text entity, and
the beginning of a non-SGML data entity. (The format of the data
is governed by the MIME text/plain content type.)

See Also:

* [plaintext at the beginning of a
  document](https://cern.la/hypertext/WWW/MarkUp/Connolly/structure3.md)* [plaintext at the beginning of
    the body](https://cern.la/hypertext/WWW/MarkUp/Connolly/structure4.md)* [plaintext after the body](https://cern.la/hypertext/WWW/MarkUp/Connolly/structure5.md)* [tolerated errors in
        structure](https://cern.la/hypertext/WWW/MarkUp/Connolly/tolerated.md#id1).* [severe errors in
          structure](https://cern.la/hypertext/WWW/MarkUp/Connolly/errors.md#structure).

## Header Elements

### TITLE

The title can have an '<' character, as long as it's not followed
by a '/' and a letter. See [the
section on SGML delimiters in CDATA](https://cern.la/hypertext/WWW/MarkUp/Connolly/Text.md#CDATA).

## Body Elements

The normal text content of body elements may include several kinds of
markup.

A comment that you shouldn't see:  For copyrights, RCS keywords, etc.

processing instruction: bold lkjsdf  If you've \_got\_ to
stick TeX macros or something in there, use this. The sample
implementation won't even tell you it's there, though.

### Entity References

Entity references are recognized in normal body elements (anyplace
#PCDATA appears in the DTD) and attribute value literals.
See [the Entities section of
"Text and Markup"](https://cern.la/hypertext/WWW/MarkUp/Connolly/Text.md#Entities) for more details.
The HTML DTD defines the following entities for characters that might
otherwise be parsed as markup:

#### HTML Entities

Name: Definition lt: < gt: > amp: & quot": " apos: '

#### ISO Latin-1 Characters

The HTML DTD references the public text
"ISO 8879:1986//ENTITIES Added Latin 1//EN"
to define entities for latin-1 characters, for example Gödel was a
famous mathemetician.

## Anchors

### Order and Apperance of Attributes

[name implied](https://cern.la/hypertext/WWW/MarkUp/Connolly/complete.md#top)

HREF implied

[HREF before name](https://cern.la/hypertext/WWW/MarkUp/Connolly/complete.md#top)

### Quotes In Attribute Values

In order to include quotes in the value of the content-type attribute,
use "&quot;" and "&apos;" entity references:
link
to SGMLS software distribution with fancy content-type attribute

#### Note: Interpretation of Literals

Section 7.9.3 of the SGML standard states

* An attribute value literal is interpreted as an attribute value by
  replacing references within it, ignoring Ee and RS, and replacing RE
  or SEPCHAR with SPACE.

For the SGML-impared, Ee is Entity End (like EOF); RS is '\n'; RE is
'\r'; SEPCHAR is '\t' and SPACE is ' '.

Since to date there are no HTML attributes containing newlines or
spaces, that is not much of an issue.

@@But replacement of literals is. For one thing, this creates an
interaction between the syntax of URLs and SGML syntax. We could
resolve this issue by removing '&' from [the
URL syntax](https://cern.la/hypertext/WWW/Addressing/BNF.md#xalpha)
.

### Headings

Six levels of headings are defined:

#### Level four heading

#### Another level four heading. It's long. It's only conventional and suggested that lines be less than 72 characters long. It's certainly not specified, defined, or required.

##### Level five heading

###### Level six heading

### Paragraphs

Normal paragraphs consist of text consisting of words, sentences, and
other stuff.
Line breaks are not significant.
This is still the first
paragraph of this section.

Here's the second paragraph. It's long. It's only conventional and suggested that lines be less than 72 characters long. It's certainly not specified, defined, or required.

A P tag isn't needed between a paragraph and some other element, like
a heading.

### Ordered lists

These are for things like lists of steps, where the order is
significant.

1. This is the first item of an unordered list.- This is the second item. It's kinda long, and should wrap around
     on most screens.- This is the third item.- This is the fourth and final item.

### Case of names is not significant: different cases

### Case of names is not significant: both lower case

### TYPEWRITER

Anything you could put on a typewriter (or an ASCII display
device, more precicesly) can be represented in a TYPEWRITER
element:
Tags: <start> </end>
Entity references: &lt; &amp;
Tables made from tabs:
col 1 col 2 col 3 col 4
1 3 4
2 3 4
1 2 3 4
Plus, you can use [hypertext links.](https://cern.la/hypertext/WWW/MarkUp/Connolly/recommended.md)
Linebreaks \_are\_ significant. There should be three blank lines from here
to here.
The ASCII Horizontal Tab (HT) character should be interpreted as the
smallest positive nonzero number of spaces which will leave the number
of characters so far on the line as a multiple of 8. Its use is not
recommended however.

## Literal Text Elements

Comment declaration as data follows:
Markup declaration as data follows:
Start tag follows:
 tags are fine!
& as long as it's not followed by a letter or '#', it's fine!
&# is even ok, unless it's followed by a letter or a number.
</XMP>
Tabs in XMP content:
<XMP>
This is literal text with tabs. THESE words
should line up under THESE words.
</XMP>
</BODY>