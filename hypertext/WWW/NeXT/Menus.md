WorldWideWeb Menus

# Menus

The menu items of the [WWW](https://cern.la/hypertext/WWW/NeXT/WorldWideWeb.md) application operate in the usual NeXTStep
way in most cases. Where the menu item has a character at the right
hand end of the menu item, typing that character while holding down
the Command key will have the same effect as the menu item: see [the
list of such keys](https://cern.la/hypertext/WWW/NeXT/CommandKeys.md) . There follows a list of the menu items in the
application, under the top level items: [Info](https://cern.la/hypertext/WWW/NeXT/Menus.md#info) , [Links](https://cern.la/hypertext/WWW/NeXT/Menus.md#links) , [Navigate](https://cern.la/hypertext/WWW/NeXT/Menus.md#navigate) ,[File](https://cern.la/hypertext/WWW/NeXT/Menus.md#window) , [Edit](https://cern.la/hypertext/WWW/NeXT/Menus.md#edit) , [Print](https://cern.la/hypertext/WWW/NeXT/Menus.md#27) , [Page Layout](https://cern.la/hypertext/WWW/NeXT/Menus.md#29) , [Style](https://cern.la/hypertext/WWW/NeXT/Menus.md#styles) , [Keyword search](https://cern.la/hypertext/WWW/NeXT/Menus.md#search) , [Help](https://cern.la/hypertext/WWW/NeXT/Menus.md#39)
, [Hide](https://cern.la/hypertext/WWW/NeXT/Menus.md#hide) , [Quit](https://cern.la/hypertext/WWW/NeXT/Menus.md#quit) .

## Info

This displays a little information about the particular version of
WWW which you have. The submenu has two items:

### Panel

This displays a single panel with information such as the version
number of your software - you can check this against the [history](https://cern.la/hypertext/WWW/NeXT/Implementation/Features.md) to
find out whether you're missing any serious improvments in the latest
copy.

### Help

This takes you to a small document shipped with the application, which
has pointers to the user manual (part of which you're reading now).
The help page is local to your machine -- you can edit it. The user
manual is, by default, on a central server machine, unless you have
changed the links in your help page. (Taking a private copy of the
user manual means it might become out of date, but it will be quicker
to access).

## Links

Items in this menu are used to manipulate the connections, or [links](https://cern.la/hypertext/WWW/Terms.md#link)
, between different hypertext documents.

Creating a link is done in two stages. Firstly, the destination of
the link (the bit which will be jumped to ) is "marked". Secondly,
the source of the link is selected, and "Link to mark" used. The source
and destination regions are known as [anchors](https://cern.la/hypertext/WWW/Terms.md#anchor) .

If you want to make a link to a document whose address you know, but
which you can't access through other links, then first [open it using
its address](https://cern.la/hypertext/WWW/NeXT/Menus.md#openfromreference), then mark it and link to it.

### Mark All

This marks the whole document as the destination of a link. Use this
to refer to a whole document rather than any part of it, or when the
server does not allow you to make an anchor within it.

### Mark Selection

This marks just the area you have selected as the destination of the
next link(s) you might create.

### Link To Marked

This creates a link from the selection to the marked text. First,
select the piece of text you wish to be sensitive, and then use this
item. From then on, clicking on that piece of text will take you to
the previously marked document or anchor.

### Link to File

This allows you to link the selected text to any file. You are prompted
for the name with an "Open" panel. The file need not be a hypertext
file. If is not a file type which WorldWideWeb recognizes and handles
itself, then following the link will cause the file to be opened from
the workspace. You cannot link to a directory (yet).

### Link to New

This creates a link from the current selection to a new node to be
stored as a file. A panel opens to allow you to select the name of
the file.

### Unlink

This remove link information from the selection. ALL link information
(coming or going) is removed from the selected text, which then becomes
ordinary text.. This may be used to trim an anchor whose sensitive
area is too big, or to remove an anchor entirely.

## Navigate

These options allow you to move through lists of items, for example,
with ease, and should prevent you geting lost.

### Back

The applicatioin keeps a record of every link you jump through. This
item allows you to retrace your steps. Each time you use it, you go
back one link, until you get to the first link you used.

### Next

This has the same effect as using "BackUp", and then selecting the
next link from that last document. For example, if you had just selected
the first of a list of references, then using "NeXT" would allow you
to move through successive one by one. It you select a news conference
and then a news article in it, NeXT allows you to move to the next
article directly, without going back to the conference.

### Previous

This is like " [Next](https://cern.la/hypertext/WWW/NeXT/Menus.md#Next) ", but goes to the link before the one you last
selected rather than the one after.

### Home

This goes back to the document which is first loaded when you run
the application.

### Panel

This brings up a navigation panel. The buttons in the panel are mostly
the same as the functions in the menu.

## File

The items in this menu allow hypertext documents ("nodes") to be loaded
explicitly and saved.

### Open file

This allows a file to be opened explicitly by file name. An HTML file
(.html filetype) will be read as hypertext. A Rich Text Format (.rtf)
file will be read as rich (ie formatted text). Files without extension
or with .txt extensions are read as plain text. All other files are
opened as the workspace manager considers fit.

### Open using full hypertext reference

This option allows not only files, but also news groups, news articles,
and information on remote hypertext servers to be loaded. You need
the complete hypertext reference for the information. See [Address
Formats](https://cern.la/hypertext/WWW/Addressing/Addressing.md) for a description of the various formats.

### New file...

This creates a new hypertext file. A panel appears to prompt you for
a filename.

When you have created a new file, you should make links from existing
files to it so that you can later reach it by browsing. See also the["Link to New"](https://cern.la/hypertext/WWW/NeXT/Menus.md#16) menu item which makes a link at the same time.

The file is generated from a master blank file. If you have a "blank.html"
in the WWW subdirectory of your home directory, that will be used:
otherwise, a copy will be taken of the file "/usr/local/lib/WWW/blank.html".
Therefore, you can customise the blank file.

### Diagnostics

You don't have to use these: they are for debugging the software.
They will (typically) dump a load of information onto the standard
output device, which will be the system console. These functions are
not guarranteed.

### Save

When a file is editable, this allows it to be saved back. Until this
is used, your changes are not safe. This condidtion is indicated by
the close button (X) in the top right of the document window becoming
a broken cross.

### Save a copy in

This option allows documents to be saved as a file, whether or not
they were originally loaded from a file. Note that the window will
continue to be associated with the original (network) document (This
is different from some other NeXT applications' "sav as".). If you
want to open the new file for editing, you must use the [Open](https://cern.la/hypertext/WWW/NeXT/Menus.md#10) command.
Before you get a save panel, a submenu is presented which allows
you to select the format:

HyperText Markup Language: This is the normal storage format for WWW files. It includes the style and anchor information. The file extension is mandatory and is ".html". You can use the copy as the basis for a new document by later [open](https://cern.la/hypertext/WWW/NeXT/Menus.md#10) ing it. Rich Text Format: This is a transfer format allowing you to export WWW files to other word processors such as Microsoft Word, WriteNow, etc. Beware that the copy saved in rtf, although it is formatted, has no style name or anchor information left. The file extension is mandatory and is ".rtf". Plain Text: This is plain ASCII text, without formatting except for line breaks to mark paragraph ends. Normally, your style sheet specifies some white space between paragraphs so the plain text version has more than one line feed character. This format may be suitable for mailing, for example - though you may want to chop the long lines. The file extension is mandatory and is ".txt".

### Save all edited windows

This perfoms a [Save](https://cern.la/hypertext/WWW/NeXT/Menus.md#8) operation on all windows which have been edited
since they were last saved. This is a wise thing to do from time
to time, and certainly before you quit.

### Miniaturize

This will shrink the current window down to a miniature window. The
text in the window will still be loaded. Clicking on the miniature
window, or following a link which leads to that document, will bring
it back up immediately.

### Open Master template

This allows you to edit the template file which is used as a basis
whenever you use " [New](https://cern.la/hypertext/WWW/NeXT/Menus.md#22) " or " [Link to new](https://cern.la/hypertext/WWW/NeXT/Menus.md#16) " commands.

### [Close other windows](https://cern.la/hypertext/WWW/NeXT/Menus.md#22)

The number of windows can rapidly become very large when one follows
links through the web. This command (also key Cmd/W) allows all windows
to be closed except for the main window and any windows which have
been modified but not yet saved.

### [Close](https://cern.la/hypertext/WWW/NeXT/Menus.md#22)

This closes the current window. The contents are removed from memory.
WorldWideWeb remebers that you had been there, so (unless you have
already backtracked over it) you will be able to find it by backtracking
with [BackUp](https://cern.la/hypertext/WWW/NeXT/Menus.md#backup) . When you reaccess the document, it is reloaded from
the server or file. This is therefore a way of picking up changed
information. If you don't want to have to wait for this (if it a slow
server for example), you could always [Miniturize](https://cern.la/hypertext/WWW/NeXT/Menus.md#miniturize) the window instead.

## Edit

This menu is the standard NeXTStep edit menu, allowing you to cut,
copy and paste text to and from hypertext documents. You can also
select the whole document. (Not all hypertext documents are writeable,
so paste won't always work).

## Print...

This brings up the print panel, which allows you to print the current
window. You can also preview what it will look like printed, and you
can save an image of the document in the window in postscript format.

See also the [Page Layout](https://cern.la/hypertext/WWW/NeXT/Menus.md#29) panel. You may also want to [load](https://cern.la/hypertext/WWW/NeXT/Menus.md#49) a different
style sheet for printing.

## Page Layout...

This brings up a panel for choosing the size and orientation of the
paper you may want to [print](https://cern.la/hypertext/WWW/NeXT/Menus.md#27) on.

The paper type you select is remebered between invokations of WorldWideWeb.
The other parameters revert to their default values when you start
WorldWideWeb. They are not stored in documents.

The margins which you can specify in this panel are the regions of
white paper around the edge of each page on which nothing is printed.
What you see on the screen window is the area between the margins.

Note that when a window is created, it is generally made wide enough
to contain a document. This means that the paper type and left and
right margins you select will affect the size of new windows.

## Style

This item brings up the Style submenu for changing the formatting
of characters in the text. [(More on Styles)](https://cern.la/hypertext/WWW/NeXT/Styles.md)

### Copy style

The style of the currently selected text is picked up for later use
in "Apply style"

### Apply style

The style previously picked up with "copy style" is applied to the
paragraph or paragraphs which include the selected text.

### Panel

This brings up the style editor panel. [(More on styles.)](https://cern.la/hypertext/WWW/NeXT/Styles.md) The style
editor allows you to format your document using styles, edit the format
represented by each style, and load and save style sheets. Clicking
on the >> buttons allows you to scroll through the available styles.

The buttons "Load " and "Save" allow you to load and save the entire
set of styles (" [stylesheet](https://cern.la/hypertext/WWW/NeXT/Styles.md#sheet) ") you are using. When loading a style
sheet, any styles which were originally present but do not exist in
the new style sheet remain defined, while those which do exist in
the new sheet are redefined.

### Style of selection

This button sets the style editor to the style of the text which has
been selected in the main window (if any).

### Apply style to selection

This applies the style in the style editor to the currently selected
text. If the style is a paragraph style, it will be applied to all
paragraphs which contain any selected text

(or the caret is the selection is of zero length).

Two buttons are provided to help in converting existing unstyles documents
into HTML:-

### Find unstyled text

This will highlight the first peice of text inthe document which has
not been given a style.

### Apply style to all similar text

This will apply the selected style to not only the selected text,
but also all that text which has the same paragraph layout (indents,
etc) and font. If you have a document which is formatted in rtf, but
not styled, you maybe able to pick up all the headings, for example,
in this way.

Editing of styles is not currently supported (Nov 1990).

## Keyword search

This brings up the keyword search panel. You can only use the keyword
search panel when the main window (the one with the dark title bar)
is an index document. (Index documents normally say that they are
indexes and very little else).

To search an index, enter one or more keywords on the keyword field
of the panel, and press return. The result will be a page of (virtual)
hypertext which gives you a list of references satisfying your search.
You can click on one of these to select the one which you are interested
in. Alternatively, you can change your keywords, and try again.

## Help

This jumps to the WorldWideWeb documentation. If it doesn't work,
then see your system manager to ensure that the application is properly
installed with its documentation.

## Hide

This hides the application as is usual on the NeXT. The state of it
is unchanged. Double-click on the application's icon to bring it back.

## Quit

This quits the application as is usual on the NeXT, except that currently
(Nov90) it DOES NOT CHECK FOR UNSAVED WINDOWS. It is wise to " [save
all edited](https://cern.la/hypertext/WWW/NeXT/Menus.md#12) " before using "quit".