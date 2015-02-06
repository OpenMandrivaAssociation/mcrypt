Summary:	Data encryption/decryption program
Name:		mcrypt
Version:	2.6.8
Release:	6
License:	GPLv2+
Group:		File tools
URL:		http://mcrypt.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/mcrypt/%{name}-%{version}.tar.gz
Patch0:		mcrypt-2.6.8-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	libmhash-devel >= 0.8.15
BuildRequires:	libmcrypt-devel >= 2.5.0

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the following
encryption (block) algorithms: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH, RC6, IDEA and GOST. The
unix crypt algorithm is also included, to allow compatibility with the crypt(1)
command. CBC, ECB, OFB and CFB modes of encryption are supported.

%prep

%setup -q
%patch0 -p0 -b .format_not_a_string_literal_and_no_format_arguments

%build

%configure2_5x

# ugly hack
export MKINSTALLDIRS="`pwd`/mkinstalldirs"
find -name "Makefile" | xargs perl -pi -e "s|^MKINSTALLDIRS.*|MKINSTALLDIRS=\"$MKINSTALLDIRS\"|g"

%make

%install
rm -rf %{buildroot}

%makeinstall

%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO doc/FORMAT doc/magic doc/sample*
%{_bindir}/*
%{_mandir}/man1/*


%changelog
* Sat Dec 03 2011 Oden Eriksson <oeriksson@mandriva.com> 2.6.8-4
+ Revision: 737491
- various fixes

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 2.6.8-3mdv2011.0
+ Revision: 620309
- the mass rebuild of 2010.0 packages

* Tue Feb 03 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.6.8-2mdv2009.1
+ Revision: 337140
- keep bash completion in its own package

* Sun Feb 01 2009 Oden Eriksson <oeriksson@mandriva.com> 2.6.8-1mdv2009.1
+ Revision: 336165
- 2.6.8
- fix build with -Werror=format-security (P0)

* Mon Aug 25 2008 Emmanuel Andry <eandry@mandriva.org> 2.6.7-1mdv2009.0
+ Revision: 275924
- New version
- fix license

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 2.6.5-3mdv2009.0
+ Revision: 252174
- rebuild
- fix no-buildroot-tag

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 2.6.5-1mdv2008.1
+ Revision: 129811
- kill re-definition of %%buildroot on Pixel's request


* Tue Feb 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.5-1mdv2007.0
+ Revision: 122966
- Import mcrypt

* Tue Feb 20 2007 Oden Eriksson <oeriksson@mandriva.com> 2.6.5-1mdv2007.1
- 2.6.5

* Thu May 12 2005 Lenny Cartier <lenny@mandriva.com> 2.6.4-4mdk
- rebuild

