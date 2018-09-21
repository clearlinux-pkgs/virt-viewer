#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xBE86EBB415104FDF (dan@berrange.com)
#
Name     : virt-viewer
Version  : 7.0
Release  : 13
URL      : https://virt-manager.org/download/sources/virt-viewer/virt-viewer-7.0.tar.gz
Source0  : https://virt-manager.org/download/sources/virt-viewer/virt-viewer-7.0.tar.gz
Source99 : https://virt-manager.org/download/sources/virt-viewer/virt-viewer-7.0.tar.gz.asc
Summary  : Virtual Machine Viewer
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: virt-viewer-bin
Requires: virt-viewer-data
Requires: virt-viewer-license
Requires: virt-viewer-locales
Requires: virt-viewer-man
BuildRequires : gettext
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-export-2.0)
BuildRequires : pkgconfig(gthread-2.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libvirt)
BuildRequires : pkgconfig(libvirt-glib-1.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(spice-client-glib-2.0)
BuildRequires : pkgconfig(spice-client-gtk-3.0)
BuildRequires : pkgconfig(spice-protocol)
BuildRequires : shared-mime-info
BuildRequires : spice-gtk
BuildRequires : spice-gtk-dev

%description
Virtual Machine Viewer provides a graphical console client for connecting
to virtual machines. It uses the GTK-VNC or SPICE-GTK widgets to provide
the display, and libvirt for looking up VNC/SPICE server details.

%package bin
Summary: bin components for the virt-viewer package.
Group: Binaries
Requires: virt-viewer-data
Requires: virt-viewer-license
Requires: virt-viewer-man

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
%setup -q -n virt-viewer-7.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1536454554
%configure --disable-static --with-gtk=3.0 --disable-update-mimedb --with-spice-gtk
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1536454554
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/virt-viewer
cp COPYING %{buildroot}/usr/share/doc/virt-viewer/COPYING
%make_install
%find_lang virt-viewer

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/remote-viewer
/usr/bin/virt-viewer

%files data
%defattr(-,root,root,-)
/usr/share/appdata/remote-viewer.appdata.xml
/usr/share/applications/remote-viewer.desktop
/usr/share/icons/hicolor/16x16/apps/virt-viewer.png
/usr/share/icons/hicolor/22x22/apps/virt-viewer.png
/usr/share/icons/hicolor/24x24/apps/virt-viewer.png
/usr/share/icons/hicolor/24x24/devices/virt-viewer-usb.png
/usr/share/icons/hicolor/24x24/devices/virt-viewer-usb.svg
/usr/share/icons/hicolor/256x256/apps/virt-viewer.png
/usr/share/icons/hicolor/32x32/apps/virt-viewer.png
/usr/share/icons/hicolor/48x48/apps/virt-viewer.png
/usr/share/mime/packages/virt-viewer-mime.xml

%files license
%defattr(-,root,root,-)
/usr/share/doc/virt-viewer/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/remote-viewer.1
/usr/share/man/man1/virt-viewer.1

%files locales -f virt-viewer.lang
%defattr(-,root,root,-)

