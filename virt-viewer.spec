#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : virt-viewer
Version  : 3.1
Release  : 3
URL      : https://virt-manager.org/download/sources/virt-viewer/virt-viewer-3.1.tar.gz
Source0  : https://virt-manager.org/download/sources/virt-viewer/virt-viewer-3.1.tar.gz
Summary  : MinGW Windows virt-viewer console application
Group    : Development/Tools
License  : GPL-2.0 GPL-2.0+
Requires: virt-viewer-bin
Requires: virt-viewer-data
Requires: virt-viewer-locales
Requires: virt-viewer-doc
BuildRequires : gettext
BuildRequires : gtk+-dev
BuildRequires : intltool
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libvirt)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : shared-mime-info
BuildRequires : spice-gtk
BuildRequires : spice-gtk-dev

%description
MinGW Windows virt-viewer console application

%package bin
Summary: bin components for the virt-viewer package.
Group: Binaries
Requires: virt-viewer-data

%description bin
bin components for the virt-viewer package.


%package data
Summary: data components for the virt-viewer package.
Group: Data

%description data
data components for the virt-viewer package.


%package doc
Summary: doc components for the virt-viewer package.
Group: Documentation

%description doc
doc components for the virt-viewer package.


%package locales
Summary: locales components for the virt-viewer package.
Group: Default

%description locales
locales components for the virt-viewer package.


%prep
%setup -q -n virt-viewer-3.1

%build
%configure --disable-static --with-gtk=2.0
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
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
%exclude /usr/share/mime/XMLnamespaces
%exclude /usr/share/mime/aliases
%exclude /usr/share/mime/generic-icons
%exclude /usr/share/mime/globs
%exclude /usr/share/mime/globs2
%exclude /usr/share/mime/magic
%exclude /usr/share/mime/mime.cache
%exclude /usr/share/mime/subclasses
%exclude /usr/share/mime/treemagic
%exclude /usr/share/mime/types
/usr/share/applications/remote-viewer.desktop
/usr/share/icons/hicolor/16x16/apps/virt-viewer.png
/usr/share/icons/hicolor/22x22/apps/virt-viewer.png
/usr/share/icons/hicolor/24x24/apps/virt-viewer.png
/usr/share/icons/hicolor/24x24/devices/virt-viewer-usb.png
/usr/share/icons/hicolor/24x24/devices/virt-viewer-usb.svg
/usr/share/icons/hicolor/256x256/apps/virt-viewer.png
/usr/share/icons/hicolor/32x32/apps/virt-viewer.png
/usr/share/icons/hicolor/48x48/apps/virt-viewer.png
/usr/share/mime/application/x-virt-viewer.xml
/usr/share/mime/icons
/usr/share/mime/packages/virt-viewer-mime.xml
/usr/share/mime/version
/usr/share/virt-viewer/ui/remote-viewer-connect.xml
/usr/share/virt-viewer/ui/virt-viewer-about.xml
/usr/share/virt-viewer/ui/virt-viewer-auth.xml
/usr/share/virt-viewer/ui/virt-viewer-guest-details.xml
/usr/share/virt-viewer/ui/virt-viewer-preferences.xml
/usr/share/virt-viewer/ui/virt-viewer-vm-connection.xml
/usr/share/virt-viewer/ui/virt-viewer.xml

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*

%files locales -f virt-viewer.lang 
%defattr(-,root,root,-)

