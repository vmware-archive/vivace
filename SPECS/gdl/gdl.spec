Summary:	GDL is the Gnome Development/Docking Library.
Name:		gdl
Version:	3.16.0
Release:	1
License:	LGPLv2.1+
URL:		http://gnudatalanguage.sourceforge.net/
Group:		System/Libraries
Source0:	http://ftp.acc.umu.se/pub/gnome/sources/%{name}/3.16/%{name}-%{version}.tar.xz
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	gtk2-devel gtk3-devel intltool glib-devel cracklib-python libxml2-devel pango-devel cairo-devel gdk-pixbuf-devel atk-devel pixman-devel libpng-devel libXrender-devel libXext-devel libX11-devel harfbuzz-devel
Requires:	dbus glib libxml2 pango cairo pixman libpng libXrender libXext libX11 harfbuzz
%description
GDL is the Gnome Development/Docking Library.
%package	devel
Summary:	Header and development files
Group:		Development/Libraries/GNOME
Requires:	%{name} = %{version}
%description	devel
Gnome Devtool Libraries contains components and libraries that are
intended to be shared between GNOME development tools, including
gnome-debug, gnome-build, and anjuta2.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}                 \

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_libdir}/*.so.*

%files devel
%defattr(-, root, root)
%{_includedir}/libgdl*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/girepository-1.0
%{_libdir}/*.so
%{_datadir}

%changelog
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.16.0-1
-	Initial build. First version
