Summary:	PNIAM - revolutionary authentication and authorization library 
Name:		pniam
Version:	0.04
Release:	2
License:	GPL
URL:		http://www.pld.org.pl/
Source0:	http://www.nc.orc.ru/pub/Linux/pniam/%{name}-%{version}.tgz
Patch0:		pniam.patch
Group:		Base/Authentication and Autorization
Group(pl):	Podstawowe/Autentykacja i Autoryzacja
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
blah blah blach

%prep
%setup -q 
%patch -p 1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir} \
$RPM_BUILD_ROOT%{_sysconfdir}/pniam.d \
	$RPM_BUILD_ROOT/etc/security \
	$RPM_BUILD_ROOT/lib \
	$RPM_BUILD_ROOT/lib/pniam \
	$RPM_BUILD_ROOT%{_includedir}/pniam
	
install lib/libpniam.so  $RPM_BUILD_ROOT/lib/libpniam.so
install include/pniam.h	 $RPM_BUILD_ROOT%{_includedir}/pniam/pniam.h
install include/pniam_mod.h	 $RPM_BUILD_ROOT%{_includedir}/pniam/pniam_mod.h
install modules/pniam_pwd/pwdlib/libpwnew.so  $RPM_BUILD_ROOT/lib/libpwnew.so
install modules/pniam_anything/pniam_anything.so  $RPM_BUILD_ROOT/lib/pniam/pniam_anything.so
install modules/pniam_ask/pniam_ask.so  $RPM_BUILD_ROOT/lib/pniam/pniam_ask.so
install modules/pniam_pwd/pniam_pwd.so  $RPM_BUILD_ROOT/lib/pniam/pniam_pwd.so
install modules/pniam_rootok/pniam_rootok.so  $RPM_BUILD_ROOT/lib/pniam/pniam_rootok.so
install modules/pniam_anything/pniam_anything.conf  $RPM_BUILD_ROOT/etc/security/pniam_anything.conf

gzip -9nf README TODO docs/pniam.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO,docs/pniam.txt}.gz docs/pniam*.html
%dir %{_sysconfdir}/pniam.d
%dir /etc/security
%dir %{_includedir}/pniam
/lib/* 
/etc/security/*
%{_includedir}/pniam/*
