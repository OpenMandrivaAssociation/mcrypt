Summary:	Data encryption/decryption program
Name:		mcrypt
Version:	2.6.8
Release:	%mkrel 1
License:	GPLv2+
Group:		File tools
URL:		http://mcrypt.sourceforge.net/
Source0:	http://belnet.dl.sourceforge.net/sourceforge/mcrypt/%{name}-%{version}.tar.gz
Source1:	%{name}.bash-completion
Patch0:		mcrypt-2.6.8-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	libmhash-devel >= 0.8.15
BuildRequires:	libmcrypt-devel >= 2.5.0
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A replacement for the old unix crypt(1) command. Mcrypt uses the following
encryption (block) algorithms: BLOWFISH, DES, TripleDES, 3-WAY, SAFER-SK64,
SAFER-SK128, CAST-128, RC2 TEA (extended), TWOFISH, RC6, IDEA and GOST. The
unix crypt algorithm is also included, to allow compatibility with the crypt(1)
command. CBC, ECB, OFB and CFB modes of encryption are supported.

%prep

%setup -q
%patch0 -p0 -b .format_not_a_string_literal_and_no_format_arguments

cp %{SOURCE1} %{name}.bash-completion

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

install -d %{buildroot}%{_sysconfdir}/bash_completion.d
install -m0644 %{name}.bash-completion %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}

%clean
rm -rf %{buildroot}

%files -f %name.lang
%defattr(-,root,root)
%doc ABOUT-NLS AUTHORS ChangeLog COPYING INSTALL NEWS README THANKS TODO doc/FORMAT doc/magic doc/sample*
%config(noreplace) %{_sysconfdir}/bash_completion.d/%{name}
%{_bindir}/*
%{_mandir}/man1/*


