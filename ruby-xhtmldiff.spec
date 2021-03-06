%define pkgname xhtmldiff
Summary:	Ruby XHTML difference finder
Summary(pl.UTF-8):	Narzędzie do znajdywania różnic w XHTML-u napisane w Rubym
Name:		ruby-%{pkgname}
Version:	1.2.2
Release:	3
License:	Ruby
Source0:	http://theinternetco.net/projects/ruby/%{pkgname}-%{version}.tar.gz
# Source0-md5:	b1536c3a2f378a4e918dcc5fae2038b3
Group:		Development/Libraries
URL:		http://theinternetco.net/projects/ruby/xhtmldiff
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
Requires:	ruby-diff-lcs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XHTMLDiff finds the difference between any two XHTML documents and
returns the result as valid XHTML with <ins> and <del> tags.

%description -l pl.UTF-8
XHTMLDiff znajduje różnice między dwoma dokumentami XHTML i zwraca
wynik jako poprawny XHTML ze znacznikami <ins> i <del>.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%package -n xhtmldiff
Summary:	Find differences in XHTML documents
Summary(pl.UTF-8):	Znajdywanie różnic w dokumentach XHTML
Group:		Applications/Text

%description -n xhtmldiff
Find differences in XHTML documents.

%description -n xhtmldiff -l pl.UTF-8
Znajdywanie różnic w dokumentach XHTML.

%prep
%setup -q -n %{pkgname}-%{version}

%build
rdoc --ri --op ri lib
rdoc --op rdoc lib
rm -r ri/{Math,REXML}
rm ri/created.rid
rm ri/cache.ri

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_ridir},%{ruby_rdocdir},%{_bindir}}

install -d $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -a bin/* $RPM_BUILD_ROOT%{_bindir}

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/xhtmldiff.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/XHTMLDiff

%files -n xhtmldiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xhtmldiff
