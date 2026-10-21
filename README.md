# patterns-tc-benchtop

The package sets (patterns) for **Technicomp Benchtop Linux**, an immutable
Tumbleweed-based openSUSE derivative. Built on OBS directly from this repo via
scmsync. The spec is the package inventory: Benchtop installs what
`patterns-tc-benchtop-base` requires. Packages that Tumbleweed does not provide
yet are listed there commented out, with a note.

Two optional sets can be chosen in the installer, or installed later with
`sudo transactional-update pkg install <package>` and a reboot:
`patterns-tc-benchtop-admin`, remote administration and servers (Cockpit, the
Samba and NFS servers, container image and infrastructure tools, database
clients), and `patterns-tc-benchtop-languages`, programming languages.
