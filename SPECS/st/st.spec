Summary:	st is a simple terminal implementation for X.
Name:		st
Version:	0.8.2
Release:	1%{?dist}
License:	MIT/X
URL:		https://st.suckless.org/
Group:		Development/Libraries
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://dl.suckless.org/st/st-0.8.2.tar.gz
%define sha1 st=1093714e46adf3f02f9ae9922c49d8ff63b83128
BuildRequires:	libX11-devel libXft-devel xfontconfig-devel
Requires:	libX11 libXft xfontconfig
%description
st is a simple terminal implementation for X.
%prep
%setup -q
%build
sed -i '/setlocale/d' x.c
make %{?_smp_mflags} CC=gcc
%install
make DESTDIR=%{buildroot} PREFIX=%{_prefix}  install
%files
%defattr(-,root,root)
%{_bindir}/*
%{_datadir}/*
%changelog
* Thu Jun 13 2019 Alexey Makhalov <amakhalov@vmware.com> 0.8.2-1
- initial version
