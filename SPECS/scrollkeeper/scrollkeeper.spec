Summary:	A cataloging system for documentation on open systems
Name:           scrollkeeper
Version:        0.3.14
Release:        1
License:        LGPL
Url:		http://scrollkeeper.sourceforge.net/index.shtml
Group:		System Environment/Base
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:        http://sourceforge.net/projects/%{name}/files/%{name}/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  libxslt docbook-xml docbook-xsl intltool
Requires:	libxslt docbook-xml docbook-xsl

%description
ScrollKeeper is a cataloging system for documentation on open systems. It manages documentation metadata (as specified by the Open Source Metadata Framework(OMF)) and provides a simple API to allow help browsers to find, sort, and search the document catalog. It will also be able to communicate with catalog servers on the Net to search for documents which are not on the local system. 
%prep
%setup -q
%build
./configure --prefix=%{_prefix}
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install 
%files
%defattr(-,root,root)
%doc COPYING AUTHORS README ChangeLog NEWS INSTALL 
#%{_datadir}/omf/scrollkeeper
#%{_sysconfdir}/
%{_bindir}/*
%{_libdir}/*
/usr/man
#%{_mandir}
%{_datadir}/
/usr/etc
/usr/var

%changelog
*	Mon Jun 29 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 0.3.14-1
-	Initial version. 

