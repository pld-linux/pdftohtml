Summary:	PDF to HTML converter
Summary(pl):	Konwerter plików PDF do HTML-a
Name:		pdftohtml
Version:	0.32b
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://prdownloads.sourceforge.net/pdftohtml/pdftohtml_0_32b.tar.gz
Patch0:		%{name}.patch
URL:		http://pdftohtml.sourceforge.net/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	gcc-c++
BuildRequires:	libstdc++-devel
Requires:	pdftops

%description
PDF to HTML converter.

%description -l pl
Konwerter PDF do HTML.

%package pdftops
Summary:	PDF to PS converter
Group:		Applications/Publishing
Obsoletes:	pdftops
Provides:	pdftops

%description pdftops
PDF to PS converter

%prep
%setup -q -n pdftohtml
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/%{_bindir}

install pdftohtml.bin $RPM_BUILD_ROOT/%{_bindir}/pdftohtml
install pdftops.bin $RPM_BUILD_ROOT/%{_bindir}/pdftops
install pdftohtml $RPM_BUILD_ROOT/%{_bindir}/pdftohtml.sh

gzip -9nf CHANGES COPYING README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,COPYING,README}.gz
%attr(755,root,root) %{_bindir}/pdftohtml.sh
%attr(755,root,root) %{_bindir}/pdftohtml

%files pdftops
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/pdftops
