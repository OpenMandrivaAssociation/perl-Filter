%define upstream_name    Filter
%define upstream_version 1.39

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Source filter modules for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://search.cpan.org/CPAN/authors/id/P/PM/PMQS/%{upstream_name}-%{upstream_version}.tar.gz
Patch0:		%{name}-1.31.shellbang.patch

BuildRequires:	perl-devel


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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.390.0-3mdv2012.0
+ Revision: 765277
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.390.0-2
+ Revision: 763770
- rebuilt for perl-5.14.x

* Sun May 01 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.390.0-1
+ Revision: 661240
- new version 1.39
- remove Buildroot define

* Thu Apr 28 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.380.0-1
+ Revision: 659934
- update to new version 1.38

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.370.0-3mdv2011.0
+ Revision: 564438
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 1.370.0-2mdv2011.0
+ Revision: 555849
- rebuild for perl 5.12

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.370.0-1mdv2010.1
+ Revision: 403182
- rebuild using %%perl_convert_version

* Wed Jun 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.37-1mdv2010.0
+ Revision: 384797
- update to new version 1.37

* Sun Mar 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.36-1mdv2009.1
+ Revision: 346268
- update to new version 1.36

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.35-1mdv2009.1
+ Revision: 345089
- update to new version 1.35

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.34-3mdv2009.0
+ Revision: 223764
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 1.34-2mdv2008.1
+ Revision: 152083
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Jul 09 2007 Funda Wang <fwang@mandriva.org> 1.34-1mdv2008.0
+ Revision: 50427
- New version

* Tue May 01 2007 Olivier Thauvin <nanardon@mandriva.org> 1.33-1mdv2008.0
+ Revision: 20094
- 1.33


* Fri Jan 20 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.32-1mdk
- New release 1.32

* Fri Sep 23 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.31-1mdk
- new version
- rpmbuilupdate aware
- fix directory ownership
- spec cleanup
- make test in %%check
- fix example scripts shellbangs

* Wed Jun 29 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.30-4mdk
- Rebuild, spec cleanup

* Tue Nov 16 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.30-3mdk
- Rebuild for new perl

* Tue Apr 06 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.30-2mdk
- Rebuild. Change description.

* Thu Aug 21 2003 Fran�ois Pons <fpons@mandrakesoft.com> 1.30-1mdk
- 1.30.

* Wed Aug 13 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 1.29-3mdk
- rebuild for new perl
- don't use PREFIX
- use %%make macro
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.29-2mdk
- rebuild for new auto{prov,req}

