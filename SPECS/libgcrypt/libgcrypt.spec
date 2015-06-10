Summary:	Password daemon 
Name:		libgcrypt
Version:	1.6.3
Release:	1
License:	LGPLv2+
URL:		http://gnupg.org
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	ftp://ftp.gnupg.org/gcrypt/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	intltool libgpg-error
Requires:	libgpg-error
%description
The GNOME Keyring package contains a daemon that keeps passwords and other secrets for users.
%package	devel
Summary:	Header and development files
Requires:	%{name} = %{version}
%description	devel
It contains the libraries and header files to create applications 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
rm %{buildroot}/usr/share/info/dir
%files
%defattr(-,root,root)
%{_bindir}
%{_libdir}
%exclude %{_libdir}/debug/
%{_datadir}
%exclude %{_datadir}/info
%files devel
%defattr(-,root,root)
%{_includedir}/*
%{_datadir}/info
%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 1.6.3-1
-	initial version
