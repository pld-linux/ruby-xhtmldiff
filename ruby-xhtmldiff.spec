%define ruby_archdir    %(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby XHTML difference finder
Name:		ruby-xhtmldiff
Version:	1.0.0
Release:	1
License:	GPL
Source0:		http://theinternetco.net/projects/ruby/xhtmldiff-%{version}.tar.gz
# Source0-md5:	ed14f163a4e755714f455b6e4bac16fb
Group:		Development/Libraries
URL:	http://theinternetco.net/projects/ruby/xhtmldiff
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	ruby

%description
XHTMLDiff finds the difference between any two XHTML documents and returns the
result as valid XHTML with <ins> and <del> tags.

%package -n xhtmldiff
Summary:	Find differences in XHTML documents
Group:	Applications/Text

%description -n xhtmldiff
Find differences in XHTML documents

%prep
%setup -q -n xhtmldiff-%{version}

%build
ruby setup.rb config --site-ruby=%{ruby_rubylibdir} --so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{ruby_rubylibdir}
ruby setup.rb install --prefix=$RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%{ruby_rubylibdir}/xhtmldiff*

%files -n xhtmldiff
%attr(755,root,root) %{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT
