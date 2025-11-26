# https://info.cern.ch/hypertext/WWW/MailRobot/Installation.html

Installing the Mail Robot

# Installation

Here are the steps necessary to install the [Mail Robot](https://cern.la/hypertext/WWW/MailRobot/Overview.md) product on
your unix system.

## Customisation

Set up the variables in [listserv.h](https://cern.la/hypertext/WWW/MailRobot/Implementation/listserv.h) and [CommonMakefile](https://cern.la/hypertext/WWW/MailRobot/Implementation/CommonMakefile) to suit your
site.

POSTMASTER: The address from which messages appear to come. Why not listserv? Perhaps to prevent mail loops. SECUREWWW: The executable W3 line mode browser (v1.3 or later, so as to have the -listrefs option). This is a separate product. For security, www should be writable only by root. SERVERDIR: The directory in which you want to put your mailing lists and help about them.

## Compile the programs

Everything compiled on AEM's MicroVax II running ULTRIX 3.0 then TBL's
NeXT without any problem at all. Your results may vary.

## Create your SERVDIR

wherever you specified in listserv.h. Install a HELP file, perhaps
using the example-files/HELP in this directory as a template.

## Set up an alias "listserv"

Make an alias in your /etc/aliases (or /etc/sendmail/aliases, whatever
you have) that points to this program, for example:
listserv: "|/usr/local/mail/listserv"
robot: "|/usr/local/mail/listserv"

## For each mailing list

Create a name.info file giving a bit of information about that mailing
list. see the \*.info files in the example-files subdirectory.

Create a name file in the same directory, consisting of email addresses
one to a line of subscribers to a group. If it is for a brand-new
group, create an empty file. Remember that this file must be writable
by the mail daemon. The name of the file is just the name of the group.

Depending on how you have your mailing lists set up, you may need
to add an alias to the /etc/aliases file for each of the mailing lists.
For example:
 real-recipes: :include:/usr/local/mail/maillists/recipes
So sending mail to real-recipes actually goes to each of the subscribers
listed in /usr/local/mail/maillists/recipes

## Install listserv

Install in the appropriate directory. Edit the CommonMakefile and
then
 make install

## Run newaliases

This gets sendmail to read the changes in /etc/aliases.
 newaliases

## Try it out

Send mail to listserv with body
HELP
for example.