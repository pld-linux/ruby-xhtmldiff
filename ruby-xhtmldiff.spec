%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby XHTML difference finder
Summary(pl):	Narzêdzie do znajdywania ró¿nic w XHTML-u napisane w Rubym
Name:		ruby-xhtmldiff
Version:	1.2.0
Release:	1
License:	Ruby
Source0:	http://theinternetco.net/projects/ruby/xhtmldiff-%{version}.tar.gz
# Source0-md5:	bfe68b63d44759247f8271ae60475d32
Group:		Development/Libraries
URL:		http://theinternetco.net/projects/ruby/xhtmldiff
BuildRequires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XHTMLDiff finds the difference between any two XHTML documents and
returns the result as valid XHTML with <ins> and <del> tags.

%description -l pl
XHTMLDiff znajduje ró¿nice miêdzy dwoma dokumentami XHTML i zwraca
wynik jako poprawny XHTML ze znacznikami <ins> i <del>.

%package -n xhtmldiff
Summary:	Find differences in XHTML documents
Summary(pl):	Znajdywanie ró¿nic w dokumentach XHTML
Group:		Applications/Text

%description -n xhtmldiff
Find differences in XHTML documents.

%description -n xhtmldiff -l pl
Znajdywanie ró¿nic w dokumentach XHTML.

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
