Summary:	PDF to HTML converter
Summary(pl.UTF-8):   Konwerter plików PDF do HTML-a
Name:		pdftohtml
Version:	0.38
Release:	1
License:	GPL
Group:		Applications/Publishing
Source0:	http://dl.sourceforge.net/pdftohtml/%{name}-%{version}.tar.gz
# Source0-md5:	4f69f650a5cb2012b2ca63f15c31f6a9
Patch0:		%{name}-FLAGS.patch
Patch1:		%{name}-CAN-2004-1125.patch
Patch2:		%{name}-nobodycolors_opt.patch
Patch3:		%{name}-c++.patch
URL:		http://pdftohtml.sourceforge.net/
BuildRequires:	libstdc++-devel
# for X11 headers used in xpdf/XPDFCore.cc
BuildRequires:	xorg-lib-libX11-devel
Obsoletes:	pdftohtml-pdftops
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PDF to HTML converter.

%description -l pl.UTF-8
Konwerter PDF do HTML-a.

%prep
%setup -q
%patch0 -p1
cd xpdf
%patch1 -p0
cd ..
%patch2 -p1
%patch3 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D src/pdftohtml $RPM_BUILD_ROOT%{_bindir}/pdftohtml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS CHANGES README
%attr(755,root,root) %{_bindir}/pdftohtml
