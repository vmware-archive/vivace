Summary:	Open source implementation of Microsoft's .NET Framework.
Name:		mono
Version:	4.0.1.44
Release:	1
License:	MIT
URL:		http://www.mono-project.com
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool gettext glib-devel tzdata
#gtk2-devel which python2-devel python2-libs unzip zip nspr nss-devel icu-devel libjpeg-turbo-devel libpng-devel zlib-devel yasm-devel alsa-lib-devel fontconfig-devel freetype2-devel harfbuzz-devel cairo-devel libXt-devel libXext-devel libXrender-devel libX11-devel libffi pixman-devel glib-devel pango-devel gdk-pixbuf-devel atk-devel libSM-devel libICE-devel libXcomposite-devel libXfixes-devel libXdamage-devel
Requires:	gettext glib
%description
Mono is an open source implementation of Microsoft's .NET Framework based on the ECMA standards for C# and the Common Language Runtime.
%prep
%setup -q -n %{name}-4.0.1
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%{_datadir}
%{_prefix}/etc
%{_includedir}
%changelog
*	Tue Jun 2 2015 Alexey Makhalov <amakhalov@vmware.com> 4.0.1.44-1
-	initial version
