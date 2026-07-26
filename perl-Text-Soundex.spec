%define modname Text-Soundex
Summary:	Perl implementation of the Soundex algorithm
Name:		perl-%{modname}
Version:	3.05
Release:	4
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/release/Text-Soundex
Source0:	https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Text-Soundex-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::Command::MM)
BuildRequires:	perl(Test::Harness)
BuildRequires:	make

%description
A perl implementation of the soundex algorithm.

%prep
%autosetup -p1 -n %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%{perl_vendorarch}/auto/Text/Soundex
%{perl_vendorarch}/Text/Soundex.pm
%{_mandir}/man3/*
