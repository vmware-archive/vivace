Summary:        XML::SAX module
Name:           perl-XML-SAX
Version:        0.99
Release:        1
License:        GPL+ or Artistic
Group:          Development/Libraries
URL:            http://search.cpan.org/dist/XML-SAX
Source0:        http://search.cpan.org/CPAN/authors/id/G/GR/GRANTM/XML-SAX-%{version}.tar.gz
%define sha1 XML-SAX=9685c417627d75ae18ab0be3b1562608ee093d5c
Vendor:		VMware, Inc.
Distribution:	Photon
BuildArch:      noarch
BuildRequires:	perl libxml2-devel zlib-devel perl-XML-SAX-Base
Requires:	perl libxml2 zlib perl-XML-SAX-Base perl-XML-NamespaceSupport

# Remove bogus XML::SAX::PurePerl* dependencies and unversioned provides
%global __requires_exclude ^perl\\(XML::SAX::PurePerl
%global __provides_exclude ^perl\\(XML::SAX::PurePerl\\)$

%description
SAX parser access API for Perl.

%prep
%setup -q -n XML-SAX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor 
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
#rm %{buildroot}%{perl_vendorlib}/x86_64-linux/auto/XML/SAX/.packlist
find %{buildroot} -name 'perllocal.pod' -delete

%check
make test

%files
%{perl_vendorlib}
%{_mandir}

%changelog
*	Thu Jun 4 2015 Alexey Makhalov <amakhalov@vmware.com> 0.99-1
-	Initial version.



