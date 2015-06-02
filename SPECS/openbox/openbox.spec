Summary:	highly configurable desktop window manager.
Name:		openbox
Version:	3.5.2
Release:	1
License:	GPLv2+
URL:		http://openbox.org
Group:		User Interface/Desktops
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://openbox.org/dist/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	intltool gtk2-devel glib-devel libX11-devel cairo-devel pango-devel gdk-pixbuf-devel atk-devel pixman-devel libXrender-devel libXext-devel libpng-devel harfbuzz-devel libxml2-devel fontconfig-devel freetype2-devel harfbuzz-devel libSM-devel libXcursor-devel libXft-devel libXau-devel libICE-devel libXinerama-devel
Requires:	gtk2 libxml2 fontconfig freetype2 harfbuzz libSM libXcursor libXft libXau libICE libXinerama
%description
Openbox is a highly configurable desktop window manager with extensive standards support. It allows you to control almost every aspect of how you interact with your desktop.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix} \
	    --sysconfdir=%{_sysconfdir} \
	    --disable-static \
	    --docdir=/usr/share/doc/%{name}-%{version}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_sysconfdir}/*
%{_bindir}/*
%{_libexecdir}/*
%{_libdir}/*
%exclude %{_libdir}/*.la
%{_datadir}/*
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_libdir}/*.la
%changelog
*	Tue May 26 2015 Alexey Makhalov <amakhalov@vmware.com> 3.5.2-1
-	initial version
