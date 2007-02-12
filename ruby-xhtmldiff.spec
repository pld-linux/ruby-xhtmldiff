Summary:	Ruby XHTML difference finder
Summary(pl.UTF-8):   Narzędzie do znajdywania różnic w XHTML-u napisane w Rubym
Name:		ruby-xhtmldiff
Version:	1.2.0
Release:	2
License:	Ruby
Source0:	http://theinternetco.net/projects/ruby/xhtmldiff-%{version}.tar.gz
# Source0-md5:	bfe68b63d44759247f8271ae60475d32
Group:		Development/Libraries
URL:		http://theinternetco.net/projects/ruby/xhtmldiff
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-modules
Requires:	ruby-Diff-LCS
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XHTMLDiff finds the difference between any two XHTML documents and
returns the result as valid XHTML with <ins> and <del> tags.

%description -l pl.UTF-8
XHTMLDiff znajduje różnice między dwoma dokumentami XHTML i zwraca
wynik jako poprawny XHTML ze znacznikami <ins> i <del>.

%package -n xhtmldiff
Summary:	Find differences in XHTML documents
Summary(pl.UTF-8):   Znajdywanie różnic w dokumentach XHTML
Group:		Applications/Text

%description -n xhtmldiff
Find differences in XHTML documents.

%description -n xhtmldiff -l pl.UTF-8
Znajdywanie różnic w dokumentach XHTML.

%prep
%setup -q -n xhtmldiff-%{version}

%build
ruby setup.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/xhtmldiff*

%files -n xhtmldiff
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
