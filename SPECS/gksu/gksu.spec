Summary:	gksu is a library and application used to ask the user for passwords to run programs as root. 
Name:		gksu 
Version:	2.0.2
Release:	1
License:	GPLv2+
URL:		http://www.nongnu.org/gksu/
Group:		System Environment/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	http://people.debian.org/~kov/gksu/gksu-2.0.2.tar.gz
%define sha1 gksu=dae634e3ed2aa8c3f2bebac17d875bcb49d825cc
BuildRequires:	intltool gtk2-devel libgksu-devel startup-notification-devel GConf-devel
Requires:	gtk2 libgksu startup-notification GConf
%description
gksu is a library and application used to ask the user for passwords to run programs as root. 
#%package	devel
#Summary:	Header and development files
#Requires:	%{name} = %{version}
#Requires:	mesa-devel
#%description	devel
#It contains the libraries and header files to create applications 
%prep
%setup -q 
%build
%configure --disable-static \
		--enable-nautilus-extension=no
make %{?_smp_mflags}
%install
make DESTDIR=%{buildroot} install
%files
%defattr(-,root,root)
%{_libdir}/*
%{_bindir}/*
%{_datadir}/*
%changelog
*	Wed Feb 24 2016 Harish Udaiya Kumar <hudaiyakumar@vmware.com> 2.0.2-1
-	initial version
