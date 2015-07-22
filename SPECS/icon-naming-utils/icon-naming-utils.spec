Summary:	A Perl script used for maintaining backwards compatibility with current desktop icon themes
Name:		icon-naming-utils
Version:	0.8.90 
Release:	1
License:	GPLv2
URL:		http://tango.freedesktop.org/Standard_Icon_Naming_Specification
Group:		Development/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://tango.freedesktop.org/releases/%{name}-%{version}.tar.bz2
%define sha1 icon-naming-utils=4e8025f129f9e536eafff847f65e44ede3e5e7ef
BuildRequires:	perl-XML-LibXML-Simple 
Requires:	pkg-config
BuildArch:	noarch
%description
The icon-naming-utils package contains a Perl script used for maintaining backwards compatibility with current desktop icon themes, while migrating to the names specified in the Icon Naming Specification.  
%prep
%setup -q
%build
autoreconf
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING AUTHORS README
%{_bindir}/
%{_datadir}/
%{_datadir}/pkgconfig
%changelog
*	Fri Jul 10 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 3.12.0-1
-	initial version
