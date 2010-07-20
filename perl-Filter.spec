%define upstream_name    Filter
%define upstream_version 1.37

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:	Source filter modules for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{upstream_name}-%{upstream_version}.tar.bz2
Patch0:		%{name}-1.31.shellbang.patch

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
Source filter modules for Perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
%patch0

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
# clean up AFTER compilation
find examples -type f -name \*.bak | xargs rm -f
find examples -type f | xargs perl -pi -e 's|^#!/usr/local/bin/perl|#!/usr/bin/perl|' 

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}%{perl_vendorarch}/Filter/Util/Call.pm
rm -rf %{buildroot}%{perl_vendorarch}/auto/Filter/Util/Call
rm -rf %{buildroot}%{_mandir}/*/Filter::Util::Call.*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes examples README
%{_mandir}/*/*
%{perl_vendorarch}/auto/Filter
%{perl_vendorarch}/Filter
%{perl_vendorarch}/filter-util.pl
%{perl_vendorarch}/perlfilter.pod
