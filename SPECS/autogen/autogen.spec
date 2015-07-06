Summary:	Automated Text File Generator
Name:		autogen
Version:	5.16.2
Release:	1
License:	GPL-3.0+
URL:		http://autogen.sourceforge.net/
Group:		Development/Tools/Building
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://downloads.sourceforge.net/project/%{name}/AutoGen/AutoGen-%{version}/%{name}-%{version}.tar.gz
BuildRequires:	libtool pkg-config libxml2-devel guile-devel libltdl-devel which 

%description
AutoGen is a tool designed to simplify the creation and maintenance of programs that contain large amounts of repetitious text. It is especially valuable in programs that have several blocks of text that must be kept synchronized.

%prep
%setup -q 
%build
./configure 	--prefix=%{_prefix} \
		--disable-static 

make %{?_smp_mflags}
%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_libdir}/pkgconfig
mv %{buildroot}%{_datadir}/pkgconfig/*.pc  %{buildroot}%{_libdir}/pkgconfig/
%post
/sbin/ldconfig
install-info --info-dir=%{_infodir} %{_infodir}/autogen.info.gz

%postun
/sbin/ldconfig
install-info --delete --info-dir=%{_infodir} %{_infodir}/autogen.info.gz

%files 
%defattr(-, root, root)
%doc NEWS ChangeLog
%exclude %{_infodir}/dir
%{_bindir}/*
%{_includedir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man?/*.gz
%{_datadir}/aclocal/*
%{_datadir}/autogen
%{_infodir}/*.gz


%changelog
*	Wed Jul 1 2015 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 5.16.2-1
-	initial version
