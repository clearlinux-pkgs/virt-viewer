#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
# Source0 file verified with key 0xBE86EBB415104FDF (dan@berrange.com)
#
Name     : virt-viewer
Version  : 11.0
Release  : 23
URL      : https://releases.pagure.org/virt-viewer/virt-viewer-11.0.tar.xz
Source0  : https://releases.pagure.org/virt-viewer/virt-viewer-11.0.tar.xz
Source1  : https://releases.pagure.org/virt-viewer/virt-viewer-11.0.tar.xz.asc
Summary  : Virtual Machine Viewer
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: virt-viewer-bin = %{version}-%{release}
Requires: virt-viewer-data = %{version}-%{release}
Requires: virt-viewer-license = %{version}-%{release}
Requires: virt-viewer-locales = %{version}-%{release}
Requires: virt-viewer-man = %{version}-%{release}
BuildRequires : bash-completion-dev
BuildRequires : buildreq-meson
BuildRequires : desktop-file-utils
BuildRequires : gtk+-dev
BuildRequires : pkgconfig(bash-completion)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libvirt-glib-1.0)
BuildRequires : pkgconfig(vte-2.91)
BuildRequires : rest-dev
BuildRequires : spice-gtk
BuildRequires : spice-gtk-dev
BuildRequires : vte-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: rest-version-fix.patch

%description
Virtual Machine Viewer provides a graphical console client for connecting
to virtual machines. It uses the GTK-VNC or SPICE-GTK widgets to provide
the display, and libvirt for looking up VNC/SPICE server details.

%package bin
Summary: bin components for the virt-viewer package.
Group: Binaries
Requires: virt-viewer-data = %{version}-%{release}
Requires: virt-viewer-license = %{version}-%{release}

%description bin
bin components for the virt-viewer package.


%package data
Summary: data components for the virt-viewer package.
Group: Data

%description data
data components for the virt-viewer package.


%package license
Summary: license components for the virt-viewer package.
Group: Default

%description license
license components for the virt-viewer package.


%package locales
Summary: locales components for the virt-viewer package.
Group: Default

%description locales
locales components for the virt-viewer package.


%package man
Summary: man components for the virt-viewer package.
Group: Default

%description man
man components for the virt-viewer package.


%prep
%setup -q -n virt-viewer-11.0
cd %{_builddir}/virt-viewer-11.0
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1687483859
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs

%install
mkdir -p %{buildroot}/usr/share/package-licenses/virt-viewer
cp %{_builddir}/virt-viewer-%{version}/COPYING %{buildroot}/usr/share/package-licenses/virt-viewer/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1 || :
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang virt-viewer
## Remove excluded files
rm -f %{buildroot}*/usr/share/mime/XMLnamespaces
rm -f %{buildroot}*/usr/share/mime/aliases
rm -f %{buildroot}*/usr/share/mime/generic-icons
rm -f %{buildroot}*/usr/share/mime/globs
rm -f %{buildroot}*/usr/share/mime/globs2
rm -f %{buildroot}*/usr/share/mime/magic
rm -f %{buildroot}*/usr/share/mime/mime.cache
rm -f %{buildroot}*/usr/share/mime/subclasses
rm -f %{buildroot}*/usr/share/mime/treemagic
rm -f %{buildroot}*/usr/share/mime/types

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/remote-viewer
/usr/bin/virt-viewer

%files data
%defattr(-,root,root,-)
/usr/share/applications/remote-viewer.desktop
/usr/share/bash-completion/completions/virt-viewer
/usr/share/icons/hicolor/16x16/apps/virt-viewer.png
/usr/share/icons/hicolor/22x22/apps/virt-viewer.png
/usr/share/icons/hicolor/24x24/apps/virt-viewer.png
/usr/share/icons/hicolor/256x256/apps/virt-viewer.png
/usr/share/icons/hicolor/32x32/apps/virt-viewer.png
/usr/share/icons/hicolor/48x48/apps/virt-viewer.png
/usr/share/icons/hicolor/scalable/apps/virt-viewer.svg
/usr/share/metainfo/remote-viewer.appdata.xml
/usr/share/mime-packages/virt-viewer-mime.xml

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/virt-viewer/68c94ffc34f8ad2d7bfae3f5a6b996409211c1b1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/remote-viewer.1
/usr/share/man/man1/virt-viewer.1

%files locales -f virt-viewer.lang
%defattr(-,root,root,-)

