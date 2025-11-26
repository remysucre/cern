# https://info.cern.ch/hypertext/WWW/LineMode/Defaults/Distribution.html

Distribution -- /LineMode

# Getting the WWW files

Read this if you have not yet got the WWW files you need, and you
cannot NFS mount a directory on which they reside.

The source and binary of WWW project files are currently available
(see [copyright](https://cern.la/hypertext/Copyright.md) ) by anonymous FTP from node info.cern.ch. This node
is currently 128.141.201.74 but THIS MAY CHANGE. The files are compressed
tape archive files (.tar.Z). To get a file using anonymous FTP,
use user name "anonymous", and your email address as a password:-
 > ftp info.cern.ch
Enter user name: anonymous
Password: me@myhost.edu
ftp> cd /pub/www/src
ftp> binary
ftp> get WWWLineMode\_vvv.tar.Z
ftp> quit
>
The file name will depend on the product you want. Here vvv is the
version number of the software.

Once you have the compressed tar file, you must uncompress it and
unwrap it.
 uncompress WWWLineMode\_vvv.tar.Z
This will make a rather larger file with the name without the ".Z".
To unwrap it,
 tar xvf WWWLineMode\_vvv.tar
Now you should [install the line mode browser](https://cern.la/hypertext/WWW/LineMode/Defaults/Installation.md) , [install the server](https://cern.la/hypertext/WWW/Daemon/User/Guide.md)
, [install Viola](https://cern.la/hypertext/Viola/Installation.md) , etc.
[Tim BL](https://cern.la/hypertext/TBL_Disclaimer.md)