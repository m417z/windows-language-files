# Windows language files

This repo holds some common Windows language files. They can be useful
sometimes, e.g. for automation or modding. Some of these files can't be found
anywhere and the easiest way to get them is to download the relevant Windows
updates or ISOs, that's why this repo was created.

## Creation details

[Windows 11, version 24H2 (26100.1457)
amd64](https://uupdump.net/selectlang.php?id=92ec64ac-7c04-4309-b3cc-50e40cbcb609)
was used for creating this repo. All
`Microsoft-Windows-Client-LanguagePack-Package` files were downloaded and
extracted, and then `organize.py` was used to sort the contents.

Winbindex
([winbindex-data-insider](https://github.com/m417z/winbindex-data-insider)) was
used to help with the downloading and extracting process. See
[winbindex-data-insider.patch](winbindex-data-insider.patch) for the adjustment
that was used.
