Summary:	Copy and paste with any OS
Summary(pl.UTF-8):	Kopiuj/Wklej niezależnie od systemu
Name:		perl-Clipboard
Version:	0.13
Release:	0.1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/authors/id/K/KI/KING/Clipboard-%{version}.tar.gz
# Source0-md5:	691e17df1d4c074284c85abac6c0c973
URL:		http://search.cpan.org/dist/Clipboard/
BuildRequires:	perl(Spiffy)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	xclip
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Who doesn't remember the first time they learned to copy and paste,
and generated an exponentially growing text document? Yes, that's
right, clipboards are magical.

%description -l pl.UTF-8
Kto z was nie pamięta kiedy po raz pierwszy użył funkcji kopiuj i
wklej tylko po to by stworzyć wykładniczo rozrastający się plik
tekstowy? Tak, to wszystko dzięki magicznemu schowkowi.

%prep
%setup -q -n Clipboard-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

# remove .packlist
rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/auto/Clipboard/.packlist

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/clipaccumulate
%attr(755,root,root) %{_bindir}/clipbrowse
%attr(755,root,root) %{_bindir}/clipedit
%attr(755,root,root) %{_bindir}/clipfilter
%attr(755,root,root) %{_bindir}/clipjoin
%dir %{perl_vendorlib}/Clipboard
%{perl_vendorlib}/Clipboard.pm
%{perl_vendorlib}/Clipboard/MacPasteboard.pm
%{perl_vendorlib}/Clipboard/Win32.pm
%{perl_vendorlib}/Clipboard/Xclip.pm
%{_mandir}/man1/clipaccumulate.1p.*
%{_mandir}/man1/clipbrowse.1p.*
%{_mandir}/man1/clipedit.1p.*
%{_mandir}/man1/clipfilter.1p.*
%{_mandir}/man1/clipjoin.1p.*
%{_mandir}/man3/Clipboard.3pm.*
