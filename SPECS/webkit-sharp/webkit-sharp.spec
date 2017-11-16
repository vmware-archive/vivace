Summary:	A fast, high-quality web browser engine.
Name:		webkit-sharp
Version:	0.3
Release:	1
License:	MIT
URL:		http://www.mono-project.com/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://download.mono-project.com/sources/webkit-sharp/webkit-sharp-0.3.tar.gz
%define sha1 webkit-sharp=cbf77978fc16df95bdfdd926d219929fd519125f
BuildRequires:	automake gtk-sharp2 mono-devel mono-addins libwebkit-devel
Requires:	libwebkit
%description
webkit-sharp provides access to WebKit, a fast, high-quality web browser engine suited for embedding in GTK+ applications. It features bleeding-edge HTML5, AJAX, SVG and JavaScript capabilities with seamless UI integration.

%prep
%setup -q 

%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc AUTHORS COPYING README
%{_prefix}/lib/mono/gac/webkit-sharp
%{_prefix}/lib/mono/webkit-sharp
%{_libdir}/pkgconfig/webkit-sharp-1.0.pc

%changelog
*	Thu Sep 17 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.3-1
-	initial version
