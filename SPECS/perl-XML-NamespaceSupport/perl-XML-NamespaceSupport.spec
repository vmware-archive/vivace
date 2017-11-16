%global debug_package %{nil}
Summary:        XML::NamespaceSupport module
Name:           perl-XML-NamespaceSupport
Version:        1.11
Release:        1
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-NamespaceSupport
Source0:        http://search.cpan.org/CPAN/authors/id/P/PE/PERIGRIN/XML-NamespaceSupport-%{version}.tar.gz
%define sha1 XML-NamespaceSupport=a948c02de081542f4d30e0efabc2929754b62a3b
Vendor:		VMware, Inc.
Distribution:	Photon
BuildRequires:	perl libxml2-devel zlib-devel
Requires:	perl libxml2 zlib

%description
Perl interface to the GNOME libxml2 library.

%prep
%setup -q -n XML-NamespaceSupport-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name 'perllocal.pod' -delete

%check
make test

%files
%{perl_vendorlib}
%{_mandir}

%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 1.11-1
-	Initial version.



