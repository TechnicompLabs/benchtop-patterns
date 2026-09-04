#
# spec file for package patterns-tc-benchtop
#
# Copyright (c) 2026 TechniComp Labs
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
# TC Benchtop Linux, 2026-08-15). Original preserved at
# upstream/patterns-tc-lab-linux.spec.orig; every content change is marked
# "## TCBL:" and catalogued in merge-review.md.


%bcond_with betatest

Name:           patterns-tc-benchtop
Version:        5.0
Release:        0
Summary:        Patterns for TechniComp Benchtop Linux
License:        MIT
Group:          Metapackages
URL:            http://en.opensuse.org/Patterns
Source0:        %name.rpmlintrc
ExclusiveArch:  x86_64 aarch64

%description
This is an internal package that is used to create the patterns as part
of the installation source setup. Installation of this package does
not make sense.

%package base
Summary:        TechniComp Benchtop Linux
Group:          Metapackages
Provides:       pattern() = tc-benchtop_base
Provides:       pattern-category() = Benchtop
Provides:       pattern-icon() = pattern-kubic
Provides:       pattern-order() = 9200
%if %{with betatest}
# need to require it as recommends are off
Requires:       pattern() = update_test
%endif

### Packages formerly provided by minimal_base
Requires:       branding
Requires:       build-key
## TCBL: distribution-release is satisfied by openSUSE/MicroOS release packages
## for now; M2 branding gate replaces this with our own tc-benchtop-release
## (os-release identity — see docs/build-plan.md §2 and merge-review.md).
Requires:       distribution-release
Requires:       filesystem

### Packages formerly provided by bootloader
Requires:       systemd-boot
Requires:       dracut-pcr-signature
Requires:       efibootmgr
Requires:       sdbootutil-rpm-scriptlets
Requires:       sdbootutil-snapper
Requires:       shim
Requires:       uefi_mbr

### Packages formerly provided by base/basesystem
Requires:       /usr/bin/hostname
Requires:       aaa_base
Requires:       bash
## TCBL: zsh re-enabled — notes (Terminal and CLI.md) make zsh the default
## login shell; a login shell must be a system RPM (/etc/shells), not brew.
Requires:       zsh
Requires:       branding-openSUSE
Requires:       btrfsprogs
Requires:       ca-certificates
Requires:       ca-certificates-mozilla
Requires:       coreutils
Requires:       coreutils-systemd
Requires:       glibc
Requires:       NetworkManager
Requires:       NetworkManager-bluetooth
Requires:       NetworkManager-wifi
# boo1230006
Requires:       libmbim
Requires:       iproute2
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
####
Requires:       btrfsmaintenance
Requires:       busybox
Requires:       chrony
# curl indirectly needed by ignition via dracut's url-lib
Requires:       curl
# probably needed for fsck.fat on efi partitions
## TCBL: deduplicated — gzip and hostname each appeared three times in the
## original (Requires + Suggests + Requires); one Requires each is kept
## (gzip below under desktop-common, hostname via /usr/bin/hostname above).
Requires:       dosfstools
Requires:       glibc-locale-base
Requires:       health-checker
Requires:       health-checker-plugins-MicroOS
Requires:       iputils
%ifnarch %{arm}
Requires:       kdump
%endif
Requires:       less
Requires:       microos-tools
Requires:       snapper
Requires:       vim
#Requires:       neovim # Modern terminal environment — TCBL: stays commented; neovim rides the Homebrew channel (installer/README.md Brewfile)
# modern terminal environment
Requires:       tmux
Requires:       wtmpdb
# people are addicted to sudo
Requires:       sudo
## Requires:       systemd-presets-branding-Aeon
## TCBL: our preset package (service enable-list) lands in M1 as
## tc-benchtop-presets — see packages/tc-benchtop-settings/README.md.
Requires:       terminfo-base
Requires:       timezone
Conflicts:      gettext-runtime-mini
Conflicts:      krb5-mini
Obsoletes:      suse-build-key < 12.1
Requires:       yast2-logs
# exfat is an important filesystem too boo#1222955
Requires:       exfatprogs

### Packages formerly provided by base_zypper
Requires:       transactional-update
Requires:       transactional-update-zypp-config
Requires:       zypper
# zypper ps is useless in transactional mode. It also checks for
# /run/reboot-needed though which is created by transactional-update
Requires:       zypper-needs-restarting

### Packages formerly provided by defaults
Requires:       audit
Requires:       systemd-coredump

### Packages formerly provided by hardware
Requires:       ethtool
%ifnarch s390x
Requires:       irqbalance
%endif
%ifarch %ix86 x86_64
Requires:       ucode-amd
Requires:       ucode-intel
%endif
Requires:       fcoe-utils
Requires:       hwinfo

### Packages formerly provided by selinux
Requires:       container-selinux
Requires:       policycoreutils
Requires:       policycoreutils-python-utils
Requires:       selinux-policy-targeted
Requires:       selinux-tools

## Remove X Packages
### Packages formerly provided by x11
## Requires:       xf86-input-libinput
## Requires:       xorg-x11-fonts-core
## Requires:       xorg-x11-server

### Packages formerly provided by desktop-common
# PipeWire is the default sound server
Requires:       gstreamer-plugin-pipewire
Requires:       pipewire-alsa
Requires:       pipewire-pulseaudio
# Add JACK audio support
Requires:       pipewire-jack
# Support UCM Profiles boo#1218510
Requires:       alsa-ucm-conf
## TCBL: printing rebuilt per Printing.md ("IPP driverless only") — the
## inherited Aeon vendor-driver stack contradicted the notes' explicit
## exclusion list. Dropped: OpenPrintingPPDs, epson-inkjet-printer-escpr,
## hplip-hpijs, printer-driver-brlaser. Added: ipp-usb (IPP-over-USB) and
## sane-airscan (eSCL/WSD driverless scanning). ghostscript retained as a
## cups-filters dependency. Full rationale in merge-review.md.
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
# Add thunderbolt device management (boo#1208150)
Requires:       bolt
Requires:       bolt-tools
# Common tools
Requires:       bash-completion
Requires:       bluez-firmware
Requires:       glibc-locale
Requires:       hicolor-icon-theme-branding-openSUSE
Requires:       polkit-default-privs
Requires:       systemd-icon-branding-openSUSE
Requires:       udisks2
Requires:       unzip
Requires:       upower
Requires:       wget
Requires:       xdg-utils
# Support ntfs drives
Requires:       ntfs-3g
Requires:       ntfsprogs
# More "comfortable" base package versions
Requires:       gzip
Requires:       hostname
## TCBL: avahi unconditional (was %if is_opensuse) — mDNS/driverless
## printing/scanning discovery is a hard requirement (Network Services.md,
## Printing.md); avahi-utils added for debugging.
Requires:       avahi
Requires:       avahi-utils
# Desktop notifications about transactional update succeeding/failing
# for the masses
Requires:       transactional-update-notifier
# Needed by both GNOME and KDE for theming of GTK-based flatpak apps properly
Requires:       xdg-desktop-portal-gtk
# Needed to ensure MicroOS Desktop systems are be able to handle varied hardware out
# of the box, and not only during the system installation.
Requires:       kernel-firmware-all
Requires:       sof-firmware
## TCBL addition: firmware updates (fwupd) — Drivers and Firmware.md; GUI
## rides GNOME Software.
Requires:       fwupd

### Packages formerly provided by desktop-gnome
Requires:       gsettings-backend-dconf
## Requires:       distribution-logos-openSUSE-Aeon
## Requires:       gdm-branding-Aeon
# gnome-initial-setup requirements
Requires:       gnome-initial-setup
Requires:       desktop-file-utils
Requires:       gjs
#Requires:       gnome-menus-branding-openSUSE
Requires:       system-group-wheel

### Accessibility packages (boo#1229268)
Requires:       desktop-translations
Requires:       orca
Requires:       brltty
Requires:       brltty-driver-speech-dispatcher
Requires:       brltty-driver-at-spi2
Requires:       brltty-driver-brlapi
Requires:       speech-dispatcher
Requires:       speech-dispatcher-module-espeak

#
# Now the real packages
#
# #332596
Requires:       gnome-keyring
Requires:       gnome-keyring-pam
Requires:       gnome-disk-utility
# boo#1215343
Requires:       gnome-backgrounds
# implied by gdm
#Requires: gnome-shell
#Requires: gnome-settings-daemon
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
# for desktop remote access
Requires:       gnome-remote-desktop
# for shell remote access
Requires:       openssh
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
# Some fonts
Requires:       adobe-sourcecodepro-fonts
Requires:       adobe-sourcesanspro-fonts
Requires:       adobe-sourceserifpro-fonts
# Default fonts for Gnome 48
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
## TCBL additions — Fonts.md required set, high-confidence subset (rest of
## the list stays in package-inventory.md pending TW name verification ⚠):
Requires:       google-caladea-fonts
Requires:       liberation-fonts
Requires:       texlive-tex-gyre-fonts
# So that GNOME keyring works
Requires:       gcr-ssh-agent
Requires:       gcr-ssh-askpass
Requires:       gcr3-ssh-askpass
# So that GNOME prompt for ssh password works
Requires:       openssh-askpass-gnome
# So that GNOME pinentry works
Requires:       pinentry-gnome3
Requires:       gvfs-backend-samba
Requires:       samba
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
# ensure laptop power support is there
## Requires:       power-profiles-daemon
## TCBL: tuned + tuned-ppd kept as-is — this resolves the July plan's open
## item #5 (tuned over power-profiles-daemon, with ppd API compat via
## tuned-ppd so the GNOME power panel keeps working).
Requires:       tuned
Requires:       tuned-ppd


## Gaming Support
# add steam-devices
Requires:       steam-devices
Requires:       selinux-policy-targeted-gaming
Requires:       system-user-games
## TCBL addition: gamemode — Gaming Mode.md (THP toggle scripts hook into it;
## see tc-benchtop-settings). mangohud/gamescope stay in the inventory for the
## gaming sub-pattern decision.
Requires:       gamemode

#
# Low-level parts that we need
#
# bnc#430161
Requires:       NetworkManager-connection-editor
Requires:       NetworkManager-pppoe
Requires:       NetworkManager-strongswan
Requires:       canberra-gtk-play
#
# Branding
#
# #591535
## TCBL: gtk2-branding-openSUSE dropped — Distro Vision.md / Security
## Architecture.md: "Drop all GTK2, Python2". Nothing else in this pattern
## should pull GTK2; CI closure check enforces it (build plan).
## TCBL: remaining openSUSE branding packages are TEMPORARY (fine for private
## M1 testing; the M2 trademark gate replaces them with tc-benchtop-branding-*
## before anything public — openSUSE marks must not ship in a modified public
## derivative).
Requires:       gtk3-branding-openSUSE
Requires:       gtk4-branding-openSUSE

### Packages formerly provided by kiwi file
## TCBL: kernel-default is the M0/M1 placeholder; replaced by kernel-lts
## (verbatim kernel.org 6.18.y, obs/README.md) once that package builds — M2
## images bake kernel-lts as the default boot entry.
Requires:       kernel-default
### systemd-zram stuff
Requires:       systemd-zram-service
### Virtualisation support
Requires:       spice-vdagent
Requires:       qemu-guest-agent
### Container / Distrobox boo#1222909
Requires:       distrobox
Requires:       podman

### Firewall Support
Requires:       firewalld

# bug#1211835 - TPM2.0 support
Requires:       tpm2-0-tss
Requires:       tpm2.0-tools

# Secureboot support
Requires:       mokutil

### x86_64_v3 support is mandatory
## Requires:       x86_64_v3-branding-Aeon
## TCBL: commented out pending verification ⚠ — a bare package name
## `x86_64_v3` almost certainly does not resolve (if it is a pattern, the
## dependency should be `pattern() = <symbol>`; exact symbol unknown).
## A wrong Requires here blocks installation of the whole pattern. Also
## check against the Supported Models list: older Surface units may not be
## x86-64-v3 capable. See merge-review.md.
## Requires:       x86_64_v3 # Note: this is a pattern

### Aeons partitions are defined to use systemd-repart
# systemd-experimental is temproarily required for repart
Requires:       systemd-experimental
## Requires:       systemd-repart-branding-Aeon

### Firstboot Configuration
Requires:       ignition-dracut
Requires:       combustion

### Support screen rotation boo#1222711
Requires:       iio-sensor-proxy

### Support Vulkan boo#1223443
Requires:       libvulkan_radeon
Requires:       libvulkan_intel

### Support fingerprint scanners boo#1212071
Requires:       fprintd
Requires:       fprintd-pam

### Support bluetooth filetransfer boo#1225682
Requires:       bluez-obexd

### Support CIFS mounting via mount boo#1216138
Requires:       cifs-utils

### Support wacom tablets
Requires:       libinput-udev

### Add aeon-check
## Requires:       aeon-check

### gnome-console as default terminal
Requires:       gnome-console

### Add switcheroo-control
Requires:       switcheroo-control

## Video Decoding
Requires:       Mesa-libva
## TCBL: fixed syntax error — original read "Required        libva-utils"
## (invalid tag; would fail the spec parse).
Requires:       libva-utils
## TCBL addition: Intel hardware video decode (Drivers and Firmware.md);
## AMD is covered by Mesa. Legacy i965 driver intentionally omitted.
Requires:       intel-media-driver

## Boot Screens
Requires:       plymouth

## Additional Filesystem Support
Requires:       e2fsprogs
Requires:       f2fs-tools
Requires:       xfsprogs-scrub
## TCBL addition: squashfuse (Filesystems.md FUSE list; live/appimage use).
Requires:       squashfuse

## Hardware and Low-level Tools
Requires:       acpi
Requires:       acpica
Requires:       clinfo
Requires:       cpupower
Requires:       dmidecode
Requires:       flashrom
Requires:       hdparm
Requires:       i2c-tools
#Requires:       inxi
Requires:       lsscsi
Requires:       ltrace
Requires:       Mesa-demo-x
Requires:       mtr
Requires:       numactl
Requires:       nvme-cli
Requires:       pciutils
Requires:       rasdaemon
Requires:       smartmontools
Requires:       strace
Requires:       stress-ng
Requires:       tcpdump
Requires:       usbutils
Requires:       vulkan-tools

## System Monitoring (CLI)
Requires:       htop
Requires:       iotop-c
Requires:       nvtop
Requires:       iftop
Requires:       nethogs
Requires:       powertop
Requires:       atop

### Additional Hardware Support
#Requires:       amdgpu_top
#Requires:       intel-gpu-tools
Requires:       ratbagd
Requires:       OpenRGB-udev-rules
## TCBL addition: Solaar for Logitech devices (Distro Vision.md QoL) —
## package name in TW to verify ⚠ (expected: solaar).
Requires:       solaar

### Developer Support
# Requires:       bpftrace # OpenSUSE packaging requires GCC.  Need to repackage
## TCBL: bpftrace repackaging → OBS backlog ✎ (merge-review.md).
Requires:       binutils
Requires:       checksec
Requires:       elfutils
Requires:       gdb
Requires:       gdbserver
Requires:       git
Requires:       jq
Requires:       patchelf
Requires:       pax-utils
# Requires:       pandoc-cli # OpenSUSE packaging pulls in all of Haskell. Need to repackage.
## TCBL: pandoc moves to the Homebrew channel (already in the default
## Brewfile, installer/README.md) — no repackaging needed.
Requires:       rclone
Requires:       rizin
Requires:       sqlite3
Requires:       tailscale
Requires:       xxd
Requires:       xsv
Requires:       yq

### Database Support
Requires:       libtdsodbc0
Requires:       mariadb-connector-odbc
Requires:       mariadb-client
# Requires:       mongosh # OpenSUSE does not package this.
# Requires:       mssql # OpenSUSE does not package this.
## TCBL: mongosh is available via Homebrew — Brewfile candidate rather than
## OBS repackaging (merge-review.md).
Requires:       postgresql
Requires:       psqlODBC
Requires:       redis
Requires:       sqliteodbc
Requires:       unixODBC

### Container Support
Requires:       buildah
Requires:       helm
Requires:       kubernetes-client
Requires:       kustomize
Requires:       skopeo
Requires:       opentofu

### Filesystem in Userspace Support
Requires:       fuse
Requires:       fuse3

### Archive Support
Requires:       7zip
Requires:       arj
Requires:       lzfse
Requires:       lzip
Requires:       rzip
Requires:       unar
Requires:       zip
Requires:       mkisofs
Requires:       udftools

### AI and Language Models
Requires:       libnuma1
Requires:       librocm-core1
Requires:       rocm-hip
Requires:       rocm-smi
Requires:       rocm-clinfo
Requires:       rocminfo
Requires:       clinfo
## TCBL: llamacpp package name/availability in TW to verify ⚠; NVIDIA-side
## (CUDA) intentionally absent here — arrives with the nvidia KMP against
## kernel-lts (obs/README.md).
## Requires:       llamacpp   # TCBL: provided by our own llama.cpp package (packages repo), not the openSUSE build

### Remote management
Requires:       cockpit
## TCBL: cockpit-firewalld existence as a TW package to verify ⚠ (firewall
## panel may be part of cockpit-networkmanager); patterns do not fail until
## install time, so wrong names here hide — M1 VM resolution check required.
## Requires:       cockpit-firewalld   # TCBL: no such package; Cockpit firewall UI ships in cockpit-networkmanager (already required)
Requires:       cockpit-machines
Requires:       cockpit-networkmanager
Requires:       cockpit-podman
Requires:       cockpit-selinux
Requires:       cockpit-storaged

### User-added Software
Requires:       flatpak-remote-flathub


%description base
This is the TechniComp Benchtop Linux base system.

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
