Summary:	Nemiver graphical debugger
Name:		nemiver
Version:	0.9.5
Release:	1
License:	GPL
URL:		https://wiki.gnome.org/Apps/Nemiver/
Group:		Development/Debuggers
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://download.gnome.org/sources/%{name}/0.9/%{name}-%{version}.tar.xz
BuildRequires:	sqlite-autoconf gnome-vfs-devel pkg-config perl desktop-file-utils libgnomeui-devel gdb libgnome-devel gettext dbus libgnome glib-devel gtk3-devel systemd libgtop-devel alsa-lib-devel libgnome-keyring-devel boost python2-libs python2-devel harfbuzz-devel itstool pixman-devel GConf-devel vte290-devel popt-devel libbonobo-devel libart_lgpl-devel libbonoboui-devel scrollkeeper libglade-devel perl pcre-devel binutils-devel gdl-devel libgda-devel gtksourceview gtksourceviewmm-devel 
Requires:	libgnome glib  alsa-lib libgda vte290 pixman openssl gtk3 libgnomeui python2 harfbuzz libgnomecanvas libgnome-keyring GConf popt libbonobo libart_lgpl binutils gdl gtksourceviewmm gdb 

%description
Nemiver is an on going effort to write an easy to use standalone C/C++ debugger that integrates well in the GNOME environment.

%package devel
Summary: Development files for Nemiver
Group:   Development/Libraries
Requires: %{name} = %{version}
Requires: libgnomeui-devel, libglade-devel, pkg-config boost gnome-vfs libxml2 glibmm

%description devel
Nemiver is an on going effort to write an easy to use standalone C/C++ debugger that integrates well in the GNOME environment.

%prep
%setup -q 

%build
./configure 	--prefix=%{_prefix} \
		--disable-static \
		--disable-schemas-install

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

desktop-file-install 	--dir %{buildroot}%{_datadir}/applications	\
			--remove-category=Application	\
			--delete-original	\
			%{buildroot}/%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/pixmaps
ln -s ../icons/hicolor/48x48/apps/nemiver.png %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf %{buildroot}

%post
update-mime-database %{_datadir}/mime &> /dev/null 
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null 
/sbin/ldconfig

%postun
/sbin/ldconfig
update-mime-database %{_datadir}/mime &> /dev/null 
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null 

%files 
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_bindir}/*
%{_libdir}/nemiver/
%{_prefix}%{_sysconfdir}/gconf
%{_datadir}/nemiver/
%{_datadir}/applications/*
%{_datadir}/icons/*/*/apps/nemiver.*
%{_mandir}/man1/nemiver.1.gz
%{_datadir}/help
%{_datadir}/locale
%{_datadir}/pixmaps

%files devel
%defattr(-,root,root)
%doc AUTHORS README NEWS TODO
%{_includedir}/nemiver/

%changelog
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.9.5-1
-	initial version
