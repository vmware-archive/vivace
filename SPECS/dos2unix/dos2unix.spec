Summary:	Text file format converters.
Name:		dos2unix
Version:	7.2.2
Release:	1
License:	BSD
URL:		http://waterlan.home.xs4all.nl/dos2unix.html
Group:		Applications/Text
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://waterlan.home.xs4all.nl/dos2unix/%{name}-%{version}.tar.gz
%define sha1 dos2unix=c16183dfb99526f9bc7c10806ef7ab6bd34db61e
BuildRequires:	intltool gettext
Requires:	gettext
%description
Convert text files with DOS or Mac line endings to Unix line endings and 
vice versa.
and for creating libraries which extend those applications.
%prep
%setup -q
%build
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%changelog
*	Mon Jun 8 2015 Alexey Makhalov <amakhalov@vmware.com> 7.2.2-1
-	initial version
