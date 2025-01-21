%global debug_package %{nil}
 
Name:           doublecmd
Version:        1.1.22
Release:        1
Summary:        Cross platform open source file manager with two panels
Group:          File tools
# Full licenses description in licensecheck.txt file
License:        GPL-2.0-or-later AND LGPL-2.0-or-later AND MIT AND MPL-1.1 AND MPL-2.0 AND Apache-2.0 AND BSD-2-Clause AND Zlib
URL:            https://doublecmd.sourceforge.net
Source0:        https://sourceforge.net/projects/%{name}/files/Double%20Commander%20Source/%{name}-%{version}-src.tar.gz
Source1:        %{name}-qt.desktop
Source2:        licensecheck.txt
Source3:        io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
Source4:        io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
 
BuildRequires:  fpc >= 2.6.0
BuildRequires:  fpc-src
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  lazarus >= 1.0.0
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(bzip2)
BuildRequires:  pkgconfig(xproto)
BuildRequires:  pkgconfig(xtrans)
BuildRequires:  util-linux
BuildRequires:  pkgconfig(pango)
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-util
BuildRequires:  which
 
%description
Double Commander GTK2 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.
 
%package        gtk
Summary:        Twin-panel (commander-style) file manager (GTK)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
 
%description    gtk
Double Commander GTK is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.
 
%package        qt
Summary:        Twin-panel (commander-style) file manager (Qt6)
Group:          File tools
Requires:       %{name}-common%{?_isa} = %{version}-%{release}
 
%description    qt
Double Commander QT6 is a cross platform open source file manager with two
panels side by side.
It is inspired by Total Commander and features some new ideas.
 
%package        common
Summary:        Common files for Double Commander
 
Requires:       hicolor-icon-theme
Requires:       polkit%{?_isa}
 
%description    common
Common files for Double Commander GTK2 and Qt.
 
%prep
%autosetup -p0
chmod +x install/linux/install.sh
# Sure to not use libbz2 and libssh2 bundling
rm -rf libraries
 
%build
lcl=qt6 ./build.sh beta
mv ./%name ./%name-qt
mv ./%name.zdli ./%name-qt.zdli
./clean.sh
lcl=gtk2 ./build.sh beta
 
%install
install/linux/install.sh --install-prefix=%{buildroot}
install -pm 0755 ./%{name}-qt %{buildroot}%{_libdir}/%{name}/%{name}-qt
ln -s ../%{_lib}/%{name}/%{name}-qt %{buildroot}%{_bindir}/%{name}-qt
install -pm 0644 ./%{name}-qt.zdli %{buildroot}%{_libdir}/%{name}/%{name}-qt.zdli
desktop-file-install %{SOURCE1}
cp %{SOURCE2} .
install -D -p -m644 %{SOURCE3} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
install -D -p -m644 %{SOURCE4} %{buildroot}%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
 
%files gtk
%{_libdir}/%{name}/%{name}
%{_bindir}/%{name}
%{_libdir}/%{name}/%{name}.zdli
%{_datadir}/applications/%{name}.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdGtk.metainfo.xml
 
 
%files qt
%{_libdir}/%{name}/%{name}-qt
%{_bindir}/%{name}-qt
%{_libdir}/%{name}/%{name}-qt.zdli
%{_datadir}/applications/%{name}-qt.desktop
%{_metainfodir}/io.sourceforge.DoubleCmd.DoubleCmdQt.metainfo.xml
 
%files common
%doc doc/changelog.txt doc/README.txt licensecheck.txt
%license doc/COPYING.LGPL.txt doc/COPYING.modifiedLGPL.txt doc/COPYING.txt
%exclude %{_libdir}/%{name}/%{name}
%exclude %{_libdir}/%{name}/%{name}-qt
%exclude %{_libdir}/%{name}/%{name}.zdli
%exclude %{_libdir}/%{name}/%{name}-qt.zdli
%exclude %{_bindir}/%{name}
%exclude %{_bindir}/%{name}-qt
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/icons/hicolor/scalable/apps/doublecmd.svg
%{_datadir}/polkit-1/actions/org.doublecmd.root.policy
