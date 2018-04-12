Summary:	Utilities for parsing and creating messages using the Multipurpose Internet Mail Extension (MIME)
Name:		gmime
Version:	2.6.20
Release:	1
License:	LGPLv2.1+
URL:		http://spruce.sourceforge.net/gmime/
Group:		Productivity/Networking/Email/Utilities
Source0:	https://download.gnome.org/sources/gmime/2.6/%{name}-%{version}.tar.xz
%define sha1 gmime=d290d628f26ef0a233781bf0793f12b1795d8536
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	glib-devel libgpg-error-devel
Requires:	glib libgpg-error
%description
The GMime package contains a set of utilities for parsing and creating messages using the Multipurpose Internet Mail Extension (MIME) as defined by the applicable RFCs. This is useful as it provides an API which adheres to the MIME specification as closely as possible while also providing programmers with an extremely easy to use interface to the API functions. 
%package	devel
Summary:	Header and development files
Group:		Development/Libraries/GNOME
Requires:	%{name} = %{version}
Requires:	glib-devel libgpg-error-devel
%description	devel
GMime is a C/C++ library which may be used for the creation and parsing of messages using the Multipurpose Internet Mail Extension (MIME), as defined by the following RFCs:
%prep
%setup -q
%build
./configure 	--prefix=%{_prefix} \
		--disable-static

make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_libdir}/*.so.*


%files devel
%defattr(-, root, root)
%doc PORTING
%{_libdir}/*.la
%{_includedir}
%{_libdir}/*.so
%{_libdir}/pkgconfig
%doc %{_datadir}/gtk-doc/html/gmime-2.6/

%changelog
*	Mon Jul 13 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.6.20-1
-	Initial build. First version
