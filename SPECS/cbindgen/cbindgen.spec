Summary:	Cbindgen can be used to generate C bindings for Rust code.
Name:		cbindgen
Version:	0.20.0
Release:	1%{?dist}
License:	LGPLv2+
URL:		https://github.com/eqrion
Group:          Development/Tools
Vendor:		VMware, Inc.
Distribution:	Photon
Source0:	https://github.com/eqrion/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
%define sha1 cbindgen=51d822f4a6fe18427f778b43ceae3f51638fe3d8
BuildRequires:	rust curl
%description
Cbindgen can be used to generate C bindings for Rust code.
%prep
%setup -q
%build
cargo build --release
%install
install -Dm755 target/release/cbindgen %{buildroot}%{_bindir}/cbindgen
%files
%defattr(-,root,root)
%{_bindir}/*
%changelog
* Fri Aug 06 2021 Alexey Makhalov <amakhalov@vmware.com> 0.20.0-1
- initial version
