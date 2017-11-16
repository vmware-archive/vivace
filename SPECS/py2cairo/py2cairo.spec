Name:           py2cairo
Version:        1.10.0
Release:	1
Summary:        Python Bindings for Cairo
Group:          Development/Languages
License:        LGPLv2+
Vendor:		VMware, Inc.
Distribution:	Photon
URL:            http://cairographics.org
Source0:        http://cairographics.org/releases/%{name}-%{version}.tar.bz2
%define sha1 py2cairo=2efa8dfafbd6b8e492adaab07231556fec52d6eb
BuildRequires: 	python2-devel
BuildRequires: 	python2-libs
BuildRequires:	xcairo-devel
Requires:	python2 xcairo

%description
Python bindings for Cairo.

%prep
%setup -q

%build
./waf configure --prefix=%{_prefix}
./waf build

%install
./waf install --destdir=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_libdir}/*
%{_includedir}/*
%exclude /usr/lib/debug

%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 1.10.0-1
-	Initial build.	First version
