%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           pygtk
Version:        2.24.0
Release:	1
Summary:        Python Bindings for GTK
Group:          Development/Languages
License:        LGPLv2+
Vendor:		VMware, Inc.
Distribution:	Photon
URL:            ftp://ftp.gnome.org
Source0:        ftp://ftp.gnome.org/pub/gnome/sources/%{name}/2.24/%{name}-%{version}.tar.bz2
%define sha1 pygtk=344e6a32a5e8c7e0aaeb807e0636a163095231c2
BuildRequires:	pygobject2 gtk2-devel py2cairo
Requires:	gtk2 
Requires:	pygobject2

%description
Python bindings for GTK.

%prep
%setup -q

%build
%configure
make

%install
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/python*/*
%{_libdir}/pygtk/*
%{_datadir}/*
%{_includedir}/*

%changelog
*	Fri May 22 2015 Alexey Makhalov <amakhalov@vmware.com> 2.24.0-1
-	Initial build.	First version
