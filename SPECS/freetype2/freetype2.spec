Summary:	contains functions for rendering various font types, such as TrueType and Type1.
Name:		freetype2
Version:	2.5.5
Release:	1
License:	(FTL or GPLv2+) and BSD and MIT and Public Domain and zlib with acknowledgement
URL:		http://www.freetype.org/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/freetype/freetype-%{version}.tar.bz2
%define sha1 freetype=7b7460ef51a8fdb17baae53c6658fc1ad000a1c2
BuildRequires:	zlib-devel freetype2-initial harfbuzz-devel
Requires:	zlib icu harfbuzz
%description
The FreeType2 package contains a library which allows applications to properly render TrueType fonts.
%package	devel
Summary:	Header and development files for freetype2
Requires:	%{name} = %{version}
Requires:	zlib-devel harfbuzz-devel
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q -n freetype-%{version}
%build
sed -i  -e "/AUX.*.gxvalid/s@^# @@" \
        -e "/AUX.*.otvalid/s@^# @@" \
	        modules.cfg                        &&
sed -ri -e 's:.*(#.*SUBPIXEL.*) .*:\1:' \
	        include/config/ftoption.h          &&
./configure --prefix=%{_prefix} --disable-static --with-zlib=yes
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
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
*	Mon May 18 2015 Alexey Makhalov <amakhalov@vmware.com> 2.5.5-1
-	initial version
