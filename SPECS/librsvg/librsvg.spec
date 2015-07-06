Summary:	library and tools used to manipulate SVG images.
Name:		librsvg
Version:	2.40.9
Release:	1
License:	LGPLv2+
URL:		http://www.gnome.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/2.40/%{name}-%{version}.tar.xz
BuildRequires:	gdk-pixbuf-devel pango-devel libcroco-devel gobject-introspection-devel gobject-introspection-python
Requires:	gdk-pixbuf pango libcroco gobject-introspection
%description
The librsvg package contains a library and tools used to manipulate, convert and view Scalable Vector Graphic (SVG) images.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
Requires:	gdk-pixbuf-devel pango-devel libcroco-devel gobject-introspection-devel gobject-introspection-python
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
# --enable-vala
./configure --prefix=%{_prefix} \
            --disable-static
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%check
make -k check |& tee %{_specdir}/%{name}-check-log || %{nocheck}
%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/*
%exclude %{_libdir}/debug/
%files devel
%defattr(-,root,root)
%{_datadir}/*
%{_includedir}/*
%changelog
*	Wed May 27 2015 Alexey Makhalov <amakhalov@vmware.com> 2.40.9-1
-	initial version
