# Installing WWW

This section describes how to install
the World-Wide Web [line-mode browser](https://cern.la/hypertext/WWW/LineMode/Defaults/QuickGuide.md)
called "www". First of all,

* If you have a VAX/VMS machine, then
  see the [special instuctions for VMS](https://cern.la/hypertext/WWW/LineMode/Defaults/Installation_VMS.md)* If you have not already got hold
    of the files, see the section on[getting them](https://cern.la/hypertext/WWW/LineMode/Defaults/Distribution.md) .* If you have a VM mainframe, see [special
      instructions](https://cern.la/hypertext/WWW/LineMode/vm-cms/Overview.md).

The browser has already been ported
to many machines. Check the list
of [machine types](https://cern.la/hypertext/WWW/LineMode/Defaults/MachineTypes.md) for your machine.
If your machine is not one of those,
see the section on [porting](https://cern.la/hypertext/WWW/LineMode/Defaults/Porting.md) .

## If the binary is available

If you found your machine type, check
in the anonymous FTP archive for
the subdirectory of /pub/www/bin
for your machine. If that directory
exists and contains a file named
www with some version number appended,
then select binary mode and take
the file, calling your copy www.
Otherwise, go to >a href=#Compiling>"compiling
from source" .

* Copy www into an apropriate directory
  which appears in your path. If you
  can be superuser, this can be /usr/local/bin/www
  (typically) so that everyone can
  use www. If you cannot be superuser,
  see [how to use ww without being superuser](https://cern.la/hypertext/WWW/LineMode/Defaults/InstallNotSU.md)
  ).* If you type "rehash", you will be
    able to use www. It will start at
    a default home page which is at CERN.* To make your own home page, take
      the tar file WWWLineModeDefaults.tar.Z.
      Unwrap it and put the files into
      a directory /usr/local/lib/WWW. Now
      skip to [make yourself at home](https://cern.la/hypertext/WWW/LineMode/Defaults/Installation.md#Home) below.

## Compiling from source

If a binary is not available, get
the sources.

* You must get, uncompress and untar
  BOTH the WWWLineMode\* product AND
  the WWWLibrary\* product source tar
  files.* Find the subdirectory of WWW/LineMode
    named after your machine type. cd
    to it.* Check the directory definitions in
      the Makefile, and change them if
      necessary. See the definition of
      the macros in the file [Implementation/CommonMakefile](https://cern.la/hypertext/WWW/LineMode/Implementation/CommonMakefile)
      .* Type "make lib". You should get a
        file WWW/Library/libwww.a* Type "make". You should get a binary
          of WWW/LineMode/www.

## Installing * Become superuser (su root). If you can't do this, see [how to do it without being superuser](https://cern.la/hypertext/WWW/LineMode/Defaults/InstallNotSU.md) ).* Type "make install". A reference copy of the executable is made and copied into the system. The "make install" step creates a copy in your system directories of the www executable and the basic documenattion. If you wish to just soft link them to the files on the WWW tree, say "make link" instead. After either of these, "make clean" will remove intermediate files.Make yourself at homeYou must now check that the default "Home" page works, and [customize it](https://cern.la/hypertext/WWW/LineMode/Defaults/Customisation.md) if it is not what you want. The default home page just a place to start. The cern.html file (distributed at the same time) is an example of a customized home page. You may wish to chose one of these as a basis.Setting up newsTo read Internet news, you must have first defined the [news server's address](https://cern.la/hypertext/WWW/LineMode/Defaults/NewsServer.md) . [Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)