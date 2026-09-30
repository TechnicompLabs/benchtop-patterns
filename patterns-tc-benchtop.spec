#
# spec file for package patterns-tc-benchtop
#
# Copyright (c) 2026 Technicomp Labs
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.technicomp.org/
#
# TCBL: renamed from patterns-tc-lab-linux (TC LabOS / Lab Linux / Workbench →
# TC Benchtop Linux, 2026-08-15).


%bcond_with betatest

Name:           patterns-tc-benchtop
Version:        5.0
Release:        0
Summary:        Patterns for Technicomp Benchtop Linux
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name.rpmlintrc

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package base
Summary:        Technicomp Benchtop Linux
Group:          Metapackages
Provides:       pattern() = tc-benchtop_base
Provides:       pattern-category() = Benchtop
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9200
%if %{with betatest}
# need to require it as recommends are off
Requires:       pattern() = update_test
%endif

### Base system
Requires:       branding
Requires:       build-key
## TCBL: distribution-release is satisfied by openSUSE/MicroOS release packages
## for now; M2 branding gate replaces this with our own tc-benchtop-release
## (os-release identity).
Requires:       distribution-release
Requires:       filesystem
Requires:       tc-benchtop-settings
Requires:       /usr/bin/hostname
Requires:       aaa_base
Requires:       bash
## TCBL: zsh re-enabled — notes (Terminal and CLI.md) make zsh the default
## login shell; a login shell must be a system RPM (/etc/shells), not brew.
Requires:       zsh
Requires:       branding-openSUSE
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       coreutils-systemd
# Command-line tools Benchtop guarantees. The base system's own packages
# already require gawk, grep, sed, findutils, diffutils and file; patch is
# under Build tools.
Requires:       bc
Requires:       tar
Requires:       time
Requires:       which
# pipe progress (pv) and parallel jobs (GNU parallel)
Requires:       pv
Requires:       gnu_parallel
Requires:       glibc
Requires:       lastlog2
Requires:       libnss_usrfiles2
Requires:       openSUSE-build-key
Requires:       pam
Requires:       pam-config
Requires:       procps
Requires:       rpm
Requires:       shadow
Requires:       systemd
Requires:       util-linux
Requires:       group(nobody)
Requires:       user(nobody)
Requires:       busybox
Requires:       chrony
# curl indirectly needed by ignition via dracut's url-lib
Requires:       curl
Requires:       glibc-locale-base
Requires:       glibc-locale
Requires:       less
# manual pages: the man program, and the pages for the Linux kernel and C
# library interfaces
Requires:       man
Requires:       man-pages
Requires:       vim
#Requires:       neovim # Modern terminal environment — TCBL: stays commented; neovim rides the Homebrew channel
# modern terminal environment
Requires:       tmux
Requires:       wtmpdb
# people are addicted to sudo
Requires:       sudo
# wheel members authenticate with their own password for sudo and polkit
# (openSUSE's default asks for root's password: sudo targetpw, polkit root admin)
Requires:       sudo-policy-wheel-auth-self
## Requires:       systemd-presets-branding-Aeon
## TCBL: tc-benchtop-settings carries TCBL's presets (85-tcbl.preset) instead.
Requires:       terminfo-base
Requires:       timezone
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
# openSUSE:Factory prefers this build-only variant when building packages;
# sleuthkit's libewf would otherwise bring it into the image
Conflicts:      libuna1-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs
Requires:       bash-completion
Requires:       wget
Requires:       systemd-coredump
Requires:       systemd-zram-service
# More "comfortable" base package versions
## TCBL: deduplicated — gzip and hostname each appeared three times in the
## original (Requires + Suggests + Requires); one Requires each is kept
## (hostname via /usr/bin/hostname above).
Requires:       gzip
Requires:       hostname

### Boot and first boot
Requires:       systemd-boot
Requires:       dracut-pcr-signature
Requires:       efibootmgr
Requires:       sdbootutil-rpm-scriptlets
Requires:       sdbootutil-snapper
Requires:       shim
Requires:       uefi_mbr
# Plymouth in the initrd (splash and graphical disk-password prompt); openSUSE
# installs it through Supplements, which the image build does not pull in
Requires:       plymouth-dracut
# Boot Screens
Requires:       plymouth
## TCBL: kernel-default is the M0/M1 placeholder; replaced by kernel-lts
## (verbatim kernel.org 6.18.y) once that package builds — M2
## images bake kernel-lts as the default boot entry.
Requires:       kernel-default
Requires:       ignition-dracut
Requires:       combustion
# systemd components that Tumbleweed packages separately: the TPM2 measurement
# and pcrlock services, sysupdate, oomd and others (systemd-repart itself comes
# with udev)
Requires:       systemd-experimental
## Requires:       systemd-repart-branding-Aeon

### Updates and snapshots
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       zypper
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting
Requires:       snapper
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       microos-tools
# Desktop notifications about transactional update succeeding/failing
# for the masses
Requires:       transactional-update-notifier
# Add aeon-check
## Requires:       aeon-check

### Security
Requires:       audit
Requires:       container-selinux
Requires:       policycoreutils
Requires:       policycoreutils-python-utils
Requires:       selinux-policy-targeted
Requires:       selinux-tools
Requires:       polkit-default-privs
Requires:       firewalld
# bug#1211835 - TPM2.0 support
Requires:       tpm2-0-tss
Requires:       tpm2.0-tools
# Secureboot support
Requires:       mokutil

### Hardware support and firmware
%ifnarch s390x
Requires:       irqbalance
%endif
%ifarch %ix86 x86_64
Requires:       ucode-amd
Requires:       ucode-intel
%endif
# Needed to ensure MicroOS Desktop systems are be able to handle varied hardware out
# of the box, and not only during the system installation.
Requires:       kernel-firmware-all
Requires:       sof-firmware
## TCBL addition: firmware updates (fwupd) — Drivers and Firmware.md; GUI
## rides GNOME Software.
Requires:       fwupd
Requires:       bluez-firmware
# Add thunderbolt device management (boo#1208150)
Requires:       bolt
Requires:       bolt-tools
Requires:       upower
# ensure laptop power support is there
## Requires:       power-profiles-daemon
## TCBL: tuned + tuned-ppd kept as-is — this resolves the July plan's open
## item #5 (tuned over power-profiles-daemon, with ppd API compat via
## tuned-ppd so the GNOME power panel keeps working).
Requires:       tuned
Requires:       tuned-ppd
Requires:       switcheroo-control
# x86_64_v3 support is mandatory
# tc-benchtop-settings' tcbl-x86-64-v3.service installs the x86-64-v3
# optimized libraries after automatic updates, on CPUs that support them
# Support screen rotation boo#1222711
Requires:       iio-sensor-proxy
# Support Vulkan boo#1223443
Requires:       libvulkan_radeon
Requires:       libvulkan_intel
# Video Decoding
Requires:       Mesa-libva
## TCBL: fixed syntax error — original read "Required        libva-utils"
## (invalid tag; would fail the spec parse).
Requires:       libva-utils
## TCBL addition: Intel hardware video decode (Drivers and Firmware.md);
## AMD is covered by Mesa. Legacy i965 driver intentionally omitted.
Requires:       intel-media-driver
# Support fingerprint scanners boo#1212071
Requires:       fprintd
Requires:       fprintd-pam
# Support bluetooth filetransfer boo#1225682
Requires:       bluez-obexd
# Support wacom tablets
Requires:       libinput-udev
Requires:       ratbagd
# rules only: until openSUSE takes the change, home:technicomp:benchtop carries a
# branch of OpenRGB whose udev-rules subpackage does not require the app
Requires:       OpenRGB-udev-rules
# udev rules only, for the Solaar Flatpak (Logitech receivers); openSUSE ships
# them without Solaar itself
Requires:       solaar-udev
# Hybrid graphics and ASUS laptops, held back: supergfxctl is in Tumbleweed,
# but openSUSE's preset starts supergfxd on every machine, and its udev rule
# turns on runtime power management for every NVIDIA GPU. asusctl is not in
# Tumbleweed and is to be packaged in home:technicomp:benchtop.
#Requires:       supergfxctl
#Requires:       asusctl

### Desktop
# #591535
## TCBL: gtk2-branding-openSUSE dropped — Distro Vision.md / Security
## Architecture.md: "Drop all GTK2, Python2". Nothing else in this pattern
## should pull GTK2.
## TCBL: remaining openSUSE branding packages are TEMPORARY (fine for private
## M1 testing; the M2 trademark gate replaces them with tc-benchtop-branding-*
## before anything public — openSUSE marks must not ship in a modified public
## derivative).
Requires:       gtk3-branding-openSUSE
Requires:       gtk4-branding-openSUSE
# Technicomp wallpaper and logos. Its distribution-logos-tc-benchtop takes the
# place of openSUSE's logos, so openSUSE's boot splash, GDM login screen,
# icons and Cockpit show the Technicomp logo.
Requires:       tc-benchtop-branding
Requires:       hicolor-icon-theme-branding-openSUSE
Requires:       systemd-icon-branding-openSUSE
Requires:       gsettings-backend-dconf
## Requires:       distribution-logos-openSUSE-Aeon
## Requires:       gdm-branding-Aeon
## TCBL: gdm-branding-Aeon pulled gdm in; dropping it with the Aeon
## branding left the image with no display manager -> text-console boot.
## Require gdm and pin its openSUSE branding (resolves the gdm-branding
## choice, matching the other -openSUSE branding kept above for M1).
Requires:       gdm
Requires:       gdm-branding-openSUSE
# native gdm.service (enabled by openSUSE's default preset) instead of the
# xdm wrapper, which brings xdm and its X11 tools
Requires:       gdm-systemd
# gnome-initial-setup requirements
Requires:       gnome-initial-setup
Requires:       desktop-file-utils
Requires:       gjs
#Requires:       gnome-menus-branding-openSUSE
Requires:       system-group-wheel
## Remove X Packages
## Requires:       xf86-input-libinput
## Requires:       xorg-x11-fonts-core
## Requires:       xorg-x11-server
# #332596
Requires:       gnome-keyring
Requires:       gnome-keyring-pam
Requires:       gnome-disk-utility
# boo#1215343
Requires:       gnome-backgrounds
# implied by gdm
Requires:       gnome-shell
Requires:       gnome-settings-daemon
# implied by gnome-shell
#Requires:       gnome-control-center
#
# Default sessions:
# - We also explicitly put the packages required by those sessions, in case
#   gnome-session-*-session is not installable, to make sure the livecd is
#   somehow a bit usable
#
Requires:       gnome-session-default-session
# ensure we have wayland session available (and used by default)
Requires:       gnome-session-wayland
# boo#1090117
Requires:       flatpak
# Flathub is added to each user's own installation (tcbl-flathub.service in
# tc-benchtop-settings), not system-wide; config.kiwi keeps openSUSE's
# flatpak-remote-flathub out
## Requires:       gnome-branding-Aeon
Requires:       gnome-color-manager
#Requires:       gnome-packagekit
Requires:       gnome-software
## Requires:       gnome-system-monitor
Requires:       gnome-user-docs
# bnc#879466
Requires:       gpgme
# for online accounts and calendar integration
Requires:       gnome-bluetooth
# for display color profile support boo#1210492
Requires:       gnome-control-center-color
# needed to ensure bluetooth is enabled at startup (glgo#GNOME/gnome-bluetooth#110)
Requires:       bluez-auto-enable-devices
Requires:       gnome-control-center-goa
Requires:       gnome-online-accounts
Requires:       gnome-shell-calendar
# For seeing thumbnails in Nautilus
Requires:       ffmpegthumbnailer
Requires:       gdk-pixbuf-loader-jxl
Requires:       gdk-pixbuf-loader-libheif
Requires:       glycin-loaders
Requires:       gnome-directory-thumbnailer
Requires:       gnome-directory-thumbnailer-lang
Requires:       gsf-office-thumbnailer
Requires:       jxl-thumbnailer
Requires:       raw-thumbnailer
Requires:       rsvg-thumbnailer
# sushi currently pulls in evince
Requires:       sushi
Requires:       totem-video-thumbnailer
# So that GNOME shell extensions can be installed
## Requires:       chrome-gnome-shell
# So users can be configured and have pretty face thumbnails
Requires:       gnome-control-center-users
Requires:       gnome-control-center-user-faces
# So users can configure Parental controls
Requires:       malcontent-control
# we need something for xdg-su
Requires:       gnome-shell-search-provider-nautilus
Requires:       libgnomesu
Requires:       nautilus
# Some extensions add context menus to nautilus using python scripts (example GSConnect)
# For this to work we need nautilus-python bindings
Requires:       python3-nautilus
Requires:       nautilus-share
Requires:       nautilus-extension-terminal
# For encrypting and decrypting files to work in Nautilus
Requires:       nautilus-extension-seahorse
Requires:       seahorse-daemon
# So Trash and mounting USB sticks work in Nautilus
Requires:       gvfs-backends
Requires:       gvfs-backend-afc
Requires:       gvfs-backend-goa
Requires:       gvfs-fuse
# We need the icons to work
Requires:       adwaita-icon-theme
# We need this for accessability and the lack of it causes big performance issues (boo#1204564)
Requires:       at-spi2-core
# So that GNOME keyring works
Requires:       gcr-ssh-agent
Requires:       gcr-ssh-askpass
Requires:       gcr3-ssh-askpass
# So that GNOME prompt for ssh password works
Requires:       openssh-askpass-gnome
# So that GNOME pinentry works
Requires:       pinentry-gnome3
Requires:       gvfs-backend-samba
# So that GNOME builtin screen recorder works
Requires:       gstreamer-plugins-bad
Requires:       gstreamer-plugins-good
# #509829
Requires:       xdg-user-dirs-gtk
Requires:       yelp
# Polkit integration with GNOME
Requires:       polkit-gnome
# https://build.opensuse.org/request/show/921373
Requires:       xdg-desktop-portal-gnome
# Needed by both GNOME and KDE for theming of GTK-based flatpak apps properly
Requires:       xdg-desktop-portal-gtk
Requires:       xdg-utils
# gnome-console as default terminal
Requires:       gnome-console
# Accessibility packages (boo#1229268)
Requires:       desktop-translations
Requires:       orca
Requires:       brltty
Requires:       brltty-driver-speech-dispatcher
Requires:       brltty-driver-at-spi2
Requires:       brltty-driver-brlapi
Requires:       speech-dispatcher
Requires:       speech-dispatcher-module-espeak
# PipeWire is the default sound server
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
# Add JACK audio support
Requires:       pipewire-jack
# Support UCM Profiles boo#1218510
Requires:       alsa-ucm-conf
Requires:       canberra-gtk-play

### Fonts
# Some fonts
Requires:       adobe-sourcecodepro-fonts
Requires:       adobe-sourcesanspro-fonts
Requires:       adobe-sourceserifpro-fonts
# Fonts required by the supported GNOME release
Requires:       adwaita-fonts
Requires:       dejavu-fonts
Requires:       ghostscript-fonts-other
Requires:       ghostscript-fonts-std
Requires:       google-carlito-fonts
Requires:       google-droid-fonts
Requires:       google-opensans-fonts
Requires:       google-roboto-fonts
Requires:       noto-coloremoji-fonts
Requires:       noto-emoji-fonts
Requires:       noto-sans-fonts
## TCBL additions — the curated font stack in Fonts.md, and the fonts that
## fontconfig's own metric-compatible aliases (30-metric-aliases.conf) use in
## place of common Microsoft and PostScript fonts (Caladea, Gelasio,
## Liberation, TeX Gyre). Names checked against Tumbleweed.
Requires:       fira-code-fonts
Requires:       gnu-unifont-otf-fonts
Requires:       google-caladea-fonts
Requires:       google-noto-sans-cjk-fonts
Requires:       hack-fonts
Requires:       ibm-plex-fonts
Requires:       intel-one-mono-fonts
Requires:       inter-fonts
Requires:       jetbrains-mono-fonts
Requires:       liberation-fonts
Requires:       saja-cascadia-code-fonts
# Atkinson Hyperlegible Next and Mono, and Gelasio (Georgia's metrics): only
# TeX Live packages them, but their OpenType files are in the system font path,
# so every application can use them
Requires:       texlive-atkinson-fonts
Requires:       texlive-gelasio-fonts
Requires:       texlive-tex-gyre-fonts
Requires:       ubuntu-fonts
# Noto for every script: google-noto-fonts requires all of openSUSE's Noto
# fonts except the CJK and emoji ones. CJK: Hong Kong Chinese Sans (the other
# four regions come with google-noto-sans-cjk-fonts above), and Serif for all
# five regions.
Requires:       google-noto-fonts
Requires:       google-noto-sans-hk-fonts
Requires:       google-noto-serif-hk-fonts
Requires:       google-noto-serif-jp-fonts
Requires:       google-noto-serif-kr-fonts
Requires:       google-noto-serif-sc-fonts
Requires:       google-noto-serif-tc-fonts

### Printing and scanning
## TCBL: printing rebuilt per Printing.md ("IPP driverless only") — the
## inherited Aeon vendor-driver stack contradicted the notes' explicit
## exclusion list. Dropped: OpenPrintingPPDs, epson-inkjet-printer-escpr,
## hplip-hpijs, printer-driver-brlaser. Added: ipp-usb (IPP-over-USB) and
## sane-airscan (eSCL/WSD driverless scanning). ghostscript retained as a
## cups-filters dependency.
Requires:       bluez-cups
Requires:       cups
Requires:       cups-filters2
Requires:       cups-pk-helper
Requires:       ghostscript
Requires:       ipp-usb
Requires:       system-config-printer-common
Requires:       system-config-printer-dbus-service
Requires:       udev-configure-printer
# Support scanners boo#1214614
Requires:       sane-backends
Requires:       sane-airscan

### Networking
Requires:       NetworkManager
Requires:       NetworkManager-bluetooth
Requires:       NetworkManager-wifi
# boo1230006
Requires:       libmbim
# bnc#430161
Requires:       NetworkManager-connection-editor
Requires:       NetworkManager-pppoe
Requires:       NetworkManager-strongswan
# strongSwan's editor plugins for GNOME Settings and the connection editor, and
# its password prompt; openSUSE pulls this in only through Supplements, which
# the image build does not follow
Requires:       NetworkManager-applet-strongswan
Requires:       NetworkManager-openvpn
Requires:       NetworkManager-applet-openvpn
Requires:       NetworkManager-openconnect
Requires:       NetworkManager-applet-openconnect
# WireGuard's tools; NetworkManager handles WireGuard connections itself
Requires:       wireguard-tools
Requires:       tailscale
## TCBL: avahi unconditional (was %if is_opensuse) — mDNS/driverless
## printing/scanning discovery is a hard requirement (Network Services.md,
## Printing.md); avahi-utils added for debugging.
Requires:       avahi
Requires:       avahi-utils
Requires:       iproute2
Requires:       iputils
# pings many hosts at once; like ping, it runs without root
Requires:       fping
Requires:       ethtool
Requires:       mtr
Requires:       tcpdump
# packet capture and analysis without the GUI: tshark, dumpcap, editcap,
# capinfos and others (the Qt interface is wireshark-ui-qt); administrators
# capture without root through tc-benchtop-settings
Requires:       wireshark
# throughput (iperf3) and route diagnostics
Requires:       iperf
Requires:       traceroute
# DNS: dig, host, nslookup
Requires:       bind-utils
Requires:       netcat-openbsd
Requires:       socat
Requires:       whois
# Nmap (Nmap Public Source License): openSUSE builds it in
# openSUSE:Factory:NonFree, and home:technicomp:benchtop links that package
Requires:       nmap

### Remote access and management
# for desktop remote access
Requires:       gnome-remote-desktop
# for shell remote access
Requires:       openssh
# mobile shell: sessions survive roaming, sleep and changing networks
Requires:       mosh
Requires:       cockpit
# opens the firewall for Cockpit's web console (port 9090), so Cockpit is
# reachable from other machines; the firewall panel itself is in
# cockpit-networkmanager
Requires:       cockpit-firewalld
Requires:       cockpit-machines
Requires:       cockpit-networkmanager
Requires:       cockpit-podman
Requires:       cockpit-selinux
Requires:       cockpit-storaged

### File sharing, remote file systems and synchronization
# Windows file sharing: the Samba server (off until configured) and its client
# tools (smbclient)
Requires:       samba
Requires:       samba-client
# Support CIFS mounting via mount boo#1216138
Requires:       cifs-utils
# NFS client and server (the server is off until configured), and NFSv4 ACLs
Requires:       nfs-client
Requires:       nfs-kernel-server
Requires:       nfs4-acl-tools
# SSH file system, and synchronization
Requires:       sshfs
Requires:       rsync
Requires:       rclone

### Storage and file systems
Requires:       btrfsprogs
Requires:       btrfsmaintenance
# probably needed for fsck.fat on efi partitions
Requires:       dosfstools
# exfat is an important filesystem too boo#1222955
Requires:       exfatprogs
# Support ntfs drives
Requires:       ntfs-3g
Requires:       ntfsprogs
Requires:       e2fsprogs
Requires:       f2fs-tools
Requires:       xfsprogs
Requires:       xfsprogs-scrub
## TCBL addition: squashfuse (Filesystems.md FUSE list; live/appimage use).
Requires:       squashfuse
Requires:       fuse
Requires:       fuse3
Requires:       udisks2
Requires:       fcoe-utils
# partitioning, software RAID, LVM and disk encryption
Requires:       parted
Requires:       gptfdisk
Requires:       mdadm
Requires:       lvm2
Requires:       cryptsetup
# disk imaging: partclone (what Clonezilla uses), and fsarchiver, whose
# archives restore to partitions of a different size
Requires:       partclone
Requires:       fsarchiver
# data recovery and file system forensics
Requires:       gnu_ddrescue
Requires:       testdisk
Requires:       photorec
Requires:       sleuthkit

### Backup
# deduplicating, encrypted backups (Snapper keeps the system snapshots)
Requires:       restic
Requires:       borgbackup

### Archives
Requires:       7zip
Requires:       arj
Requires:       lzfse
Requires:       lzip
Requires:       rzip
Requires:       unar
Requires:       unzip
Requires:       zip
Requires:       mkisofs
Requires:       udftools

### Virtualization, containers and infrastructure
Requires:       spice-vdagent
Requires:       qemu-guest-agent
# Container / Distrobox boo#1222909
Requires:       distrobox
Requires:       podman
Requires:       buildah
Requires:       helm
Requires:       kubernetes-client
Requires:       kustomize
Requires:       skopeo
Requires:       opentofu
# configuration management; collections come from ansible-galaxy
Requires:       ansible-core

### System monitoring
Requires:       htop
Requires:       iotop-c
Requires:       nvtop
Requires:       iftop
Requires:       nethogs
Requires:       powertop
Requires:       atop
# sar, iostat, mpstat and pidstat (its data collection is off until enabled)
Requires:       sysstat
# open files, and process tools (killall, fuser, pstree)
Requires:       lsof
Requires:       psmisc

### Performance analysis and tracing
# Keep this aligned with Benchtop's kernel-lts when that replaces
# kernel-default.
Requires:       perf
# eBPF
Requires:       bpftool
Requires:       bpftrace
Requires:       bpftrace-tools
Requires:       bpftop
# storage and I/O testing
Requires:       fio

### Hardware diagnostics
Requires:       acpi
Requires:       acpica
Requires:       clinfo
Requires:       cpupower
Requires:       dmidecode
Requires:       edid-decode
# counterfeit (fake-capacity) flash drives and memory cards
Requires:       f3
Requires:       flashrom
Requires:       hdparm
Requires:       hwinfo
Requires:       i2c-tools
#Requires:       inxi
Requires:       lsscsi
Requires:       Mesa-demo-x
Requires:       numactl
Requires:       nvme-cli
Requires:       pciutils
Requires:       rasdaemon
Requires:       sdparm
Requires:       sensors
Requires:       sg3_utils
Requires:       smartmontools
Requires:       stress-ng
Requires:       usbutils
Requires:       vulkan-tools
# Intel GPU tools (intel_gpu_top and others)
%ifarch %ix86 x86_64
Requires:       intel-gpu-tools
%endif
# AMD GPU usage and sensors (tc-benchtop-settings-rpm leaves out its terminal
# launcher)
Requires:       amdgpu_top
# Secure erase and sanitize come with the tools above: hdparm (ATA), nvme-cli
# (NVMe) and sg3_utils (SCSI and SAS), plus blkdiscard (util-linux) and shred
# (coreutils). config.kiwi installs MemTest86+ with its boot entry.

### Programming languages
# C and C++ toolchain: pip, npm, cargo and go build native code with the
# system compiler
Requires:       gcc
Requires:       gcc-c++
Requires:       clang
Requires:       llvm
Requires:       lld

# x86 assembler (GNU as comes with binutils)
Requires:       nasm

# Other GCC languages
Requires:       gcc-ada
Requires:       gcc-algol68
Requires:       gcc-cobol
Requires:       gcc-d
Requires:       gcc-fortran
Requires:       gcc-m2
Requires:       gcc-obj-c++
Requires:       gcc-objc

# D package manager
Requires:       dub

# Python
# Interpreter and venv are already installed
Requires:       python3-pip
Requires:       python3-devel
Requires:       python3-curses
Requires:       python3-dbm
Requires:       python3-tk

# Ruby (RubyGems and Bundler are part of Ruby)
Requires:       ruby
Requires:       ruby-devel

# Perl: cpan, and the headers and xsubpp that XS modules compile with, are
# part of perl (Tumbleweed has no perl-devel)
Requires:       perl

# Java
Requires:       java-devel
Requires:       maven

# Scala
# TODO: package Scala 3 and a build tool for Benchtop/OBS. Tumbleweed has
# scala 2.13.12, which predates support for JDK 25, the JDK java-devel
# installs (Scala's compatibility table starts at 2.13.17), and no sbt, the
# usual Scala build tool.
#Requires:       scala

# Kotlin
# TODO: package Kotlin for Benchtop/OBS.
# No satisfactory official Tumbleweed compiler package is currently available.

# Go
Requires:       go

# Rust
Requires:       rust
Requires:       cargo

# JavaScript, with the Node headers: openSUSE's node-gyp compiles native
# addons against them instead of downloading headers
Requires:       nodejs-default
Requires:       npm-default
Requires:       nodejs-devel-default

# PHP, with the extensions a default PHP build enables, which Tumbleweed
# packages separately
Requires:       php8-cli
Requires:       php8-devel
Requires:       php-composer2
Requires:       php8-ctype
Requires:       php8-dom
Requires:       php8-fileinfo
Requires:       php8-iconv
Requires:       php8-pdo
Requires:       php8-posix
Requires:       php8-sqlite
Requires:       php8-tokenizer
Requires:       php8-xmlreader
Requires:       php8-xmlwriter

# Lua
Requires:       lua
Requires:       lua-devel
Requires:       lua54-luarocks

# Tcl/Tk, with the headers for C extensions
Requires:       tcl
Requires:       tcl-devel
Requires:       tk
Requires:       tk-devel

# R, with the headers and build setup that CRAN packages with C, C++ or
# Fortran code compile against
Requires:       R-base
Requires:       R-base-devel

# GNU Octave: the interpreter without the Qt interface, which comes from
# Flathub, and mkoctfile, which pkg install uses to compile extensions
Requires:       octave-cli
Requires:       octave-devel

# Julia
# TODO: package the Julia runtime directly for Benchtop/OBS.
# Do not use juliaup; Benchtop should ship the rolling runtime itself.

# Erlang and Elixir
Requires:       erlang
Requires:       erlang-rebar3
Requires:       elixir
Requires:       elixir-hex

# Haskell
Requires:       ghc
Requires:       cabal-install

# OCaml, with the compiler libraries a standard OCaml installation includes;
# ppx packages (ppxlib) build against them
Requires:       ocaml
Requires:       ocaml-compiler-libs-devel
Requires:       opam

# Common Lisp
Requires:       sbcl

# Scheme (Guile), with the headers for C extensions
Requires:       guile
Requires:       guile-devel

# Racket
Requires:       racket

# Clojure, with Leiningen for projects and dependencies
Requires:       clojure
Requires:       leiningen

# Nim
Requires:       nim

# Zig
# benchtop-zig: a Benchtop-owned selector package that requires the Zig series
# Benchtop designates; update it when Tumbleweed's desired Zig generation
# changes. Not yet packaged.
#Requires:       benchtop-zig

# .NET / C# / F#
# TODO: package the current .NET SDK/runtime for Benchtop/OBS.
# Tumbleweed does not currently provide an official modern dotnet-sdk package.
# Do not substitute Mono; it is not equivalent to the current .NET SDK.

# Dart
# TODO: evaluate/package Dart SDK for Benchtop/OBS.
# No official Tumbleweed package currently suitable for the base image.

# Swift
# TODO: evaluate/package the upstream Swift toolchain for Benchtop/OBS
# if native Linux Swift is considered part of the supported language set.

### Build tools
Requires:       autoconf
Requires:       automake
Requires:       bison
# compiler cache
Requires:       ccache
Requires:       cmake-full
# builds Flatpaks from manifests; runtimes and SDKs download per user
Requires:       flatpak-builder
Requires:       flex
Requires:       libtool
Requires:       make
Requires:       meson
Requires:       ninja
Requires:       patch
Requires:       pkgconf-pkg-config

### Version control
Requires:       git
# large files (media, datasets, model weights) kept outside the repository;
# some Flatpak manifest sources use it too
Requires:       git-lfs
# GitHub's command-line tool
Requires:       gh
# Jujutsu (jj), a Git-compatible version control system
Requires:       jujutsu
# other version control systems, current and historical
Requires:       mercurial
Requires:       subversion
Requires:       fossil
Requires:       cvs
Requires:       rcs
# Breezy (Bazaar's maintained successor) is not in Tumbleweed; to be packaged
#Requires:       breezy

### Debugging and binary analysis
Requires:       binutils
Requires:       checksec
Requires:       elfutils
Requires:       gdb
Requires:       gdbserver
Requires:       hexedit
Requires:       ltrace
Requires:       patchelf
Requires:       pax-utils
Requires:       rizin
# Ghidra's decompiler for rizin
Requires:       rz-ghidra
Requires:       strace
Requires:       valgrind
Requires:       xxd

### Security analysis
# malware signatures (YARA), firmware images (binwalk) and file metadata
Requires:       yara
Requires:       binwalk
Requires:       exiftool

### Data processing and documents
Requires:       jq
# CSV, TSV and JSON processing (mlr), in place of xsv, which is unmaintained
# upstream
Requires:       miller
Requires:       yq
# document conversion
Requires:       pandoc-cli

### Electronics and embedded development
# microcontroller programming and debugging, serial consoles and logic
# analyzers
Requires:       avrdude
Requires:       dfu-util
Requires:       openocd
Requires:       picocom
Requires:       sigrok-cli

### Databases
Requires:       sqlite3
Requires:       libtdsodbc0
Requires:       mariadb-connector-odbc
Requires:       mariadb-client
# Requires:       mongosh # OpenSUSE does not package this.
# Requires:       mssql # OpenSUSE does not package this.
## TCBL: mongosh is available via Homebrew — Brewfile candidate rather than
## OBS repackaging.
Requires:       postgresql
Requires:       psqlODBC
Requires:       sqliteodbc
Requires:       unixODBC

### AI and language models
Requires:       libnuma1
Requires:       librocm-core1
Requires:       rocm-hip
Requires:       rocm-smi
Requires:       rocm-clinfo
Requires:       rocminfo
# Tumbleweed's llamacpp (ggml) has CPU, Vulkan, OpenCL and OpenVINO backends,
# but no CUDA or ROCm.
## NVIDIA-side (CUDA) intentionally absent here — arrives with the nvidia
## KMP against kernel-lts.
Requires:       llamacpp
# the Vulkan backend (AMD, Intel and NVIDIA GPUs): libggml only recommends it,
# and the image is built without recommended packages
Requires:       libggml-vulkan

### Gaming
# add steam-devices
Requires:       steam-devices
Requires:       selinux-policy-targeted-gaming
Requires:       system-user-games
## TCBL addition: gamemode — Gaming Mode.md. mangohud and gamescope come from
## Flathub, as the Flatpak Vulkan layers
## org.freedesktop.Platform.VulkanLayer.MangoHud and
## org.freedesktop.Platform.VulkanLayer.gamescope.
Requires:       gamemode

%description base
This is the Technicomp Benchtop Linux base system.

%prep
# empty on purpose

%build
# empty on purpose

%install
mkdir -p %{buildroot}%{_docdir}/patterns-tc-benchtop/
PATTERNS='
    base
'
for i in $PATTERNS; do
    echo "This file marks the pattern $i to be installed." \
        > %{buildroot}%{_docdir}/patterns-tc-benchtop/${i}.txt
done

%files base
%dir %{_docdir}/patterns-tc-benchtop
%{_docdir}/patterns-tc-benchtop/base.txt

%changelog
