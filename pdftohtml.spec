Summary:	PDF to HTML converter
Summary(pl):	Konwerter plików PDF do HTML-a
Name:		pdftohtml
Version:	0.36
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/pdftohtml/%{name}-%{version}.tar.gz
# Source0-md5:	75ad095bb51e1f66c9f7691e6af12f44
Patch0:		%{name}-FLAGS.patch
URL:		http://pdftohtml.sourceforge.net/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDF to HTML converter.

%description -l pl
Konwerter PDF do HTML-a.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" CFLAGS="%{rpmcflags}" \
	CXX="%{__cxx}" CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -D pdftohtml $RPM_BUILD_ROOT%{_bindir}/pdftohtml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/pdftohtml
