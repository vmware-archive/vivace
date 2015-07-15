Summary:	MIME database
Name:		shared-mime-info
Version:	1.4
Release:	1
License:	GPLv2+
URL:		http://freedesktop.org
Group:		Applications/Internet
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://freedesktop.org/~hadess/%{name}-%{version}.tar.xz
%define sha1 shared-mime-info=f7a3881acca3df1d9757d670e99d2d56ac9f7bca
BuildRequires:	intltool glib-devel libxml2-devel
Requires:	gettext glib libxml2
%description
The Shared Mime Info package contains a MIME database. This allows central updates of MIME information for all supporting applications.
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_bindir}
%{_datadir}
%changelog
*	Wed Jun 3 2015 Alexey Makhalov <amakhalov@vmware.com> 1.4-1
-	initial version
