Summary:   PNIAM - revolutionary authentication and authorization library 
Name:      pniam
Version:   0.04
Release:   1
URL:       http://www.pld.org.pl/
Source:    http://www.nc.orc.ru/pub/Linux/pniam/%{name}-%{version}.tgz
Patch:     pniam.patch
Copyright: GPL
Group:     Base/Authentication and Autorization
Group(pl): Podstawowe/Autentykacja i Autoryzacja
Buildroot: /tmp/%{name}-%{version}-root
Packager:  Grzegorz Stanislawski <stangrze@open.net.pl>

%description
blah blah blach

%prep
%setup -q 
%patch -p 1

%build
make

%install
mkdir -p $RPM_BUILD_ROOT/etc
mkdir -p $RPM_BUILD_ROOT/etc/pniam.d
mkdir -p $RPM_BUILD_ROOT/etc/security
mkdir -p $RPM_BUILD_ROOT/lib
mkdir -p $RPM_BUILD_ROOT/lib/pniam
mkdir -p $RPM_BUILD_ROOT/usr/
mkdir -p $RPM_BUILD_ROOT/usr/include/
mkdir -p $RPM_BUILD_ROOT/usr/include/pniam
install lib/libpniam.so  $RPM_BUILD_ROOT/lib/libpniam.so
install include/pniam.h	 $RPM_BUILD_ROOT/usr/include/pniam/pniam.h
install include/pniam_mod.h	 $RPM_BUILD_ROOT/usr/include/pniam/pniam_mod.h
install modules/pniam_pwd/pwdlib/libpwnew.so  $RPM_BUILD_ROOT/lib/libpwnew.so
install modules/pniam_anything/pniam_anything.so  $RPM_BUILD_ROOT/lib/pniam/pniam_anything.so
install modules/pniam_ask/pniam_ask.so  $RPM_BUILD_ROOT/lib/pniam/pniam_ask.so
install modules/pniam_pwd/pniam_pwd.so  $RPM_BUILD_ROOT/lib/pniam/pniam_pwd.so
install modules/pniam_rootok/pniam_rootok.so  $RPM_BUILD_ROOT/lib/pniam/pniam_rootok.so
install modules/pniam_anything/pniam_anything.conf  $RPM_BUILD_ROOT/etc/security/pniam_anything.conf

%post

%postun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(755,root,root)      /lib/* 
%dir			  /etc/pniam.d
%dir			  /etc/security
%attr(644,root,root)      /etc/security/*
%dir			  /usr/include/pniam
%attr(644,root,root)      /usr/include/pniam/*
%doc                      README TODO docs/pniam.txt docs/pniam*.html

%changelog
* Wed Jun  2 1999 Grzegorz Stanislawski <stangrze@open.net.pl>
- First RPM release 
