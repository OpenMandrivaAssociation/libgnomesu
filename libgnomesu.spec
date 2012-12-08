%define name libgnomesu
%define version 1.0.0
%define release %mkrel 9
%define major 0
%define libname %mklibname gnomesu %major
%define libnamedev %mklibname -d gnomesu

Summary: Library for accessing superuser privileges from GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.gz
Patch0: libgnomesu-0.9.5-pam_stack.patch
Patch1:	libgnomesu-1.0.0-format-strings.patch
Patch2: libgnomesu-1.0.0-deprecated.patch
License: LGPLv2+
Group: System/Libraries
Url: http://members.chello.nl/~h.lai/libgnomesu/
BuildRequires: libgnomeui2-devel
BuildRequires: pam-devel
BuildRequires: intltool
Provides: gnomesu
Obsoletes: gnomesu

%description
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%package -n %libname
Summary: Library for accessing superuser privileges from GNOME
Group: System/Libraries
Requires: %name >= %version-%release

%description -n %libname
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%package -n %libnamedev
Summary: Library for accessing superuser privileges from GNOME
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release
Obsoletes: %mklibname -d gnomesu 0

%description -n %libnamedev
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%prep
%setup -q
%apply_patches
intltoolize --force
autoreconf -fi

%build
%configure2_5x --disable-setuid-error
%make

%install
rm -rf %{buildroot} %name-1.0.lang
%makeinstall_std
%find_lang %name-1.0
#gw fix perms for cpio
chmod 755 %{buildroot}%_libexecdir/*

%files -f %name-1.0.lang
%defattr(-,root,root)
%doc README ChangeLog NEWS TODO AUTHORS
%config(noreplace) %_sysconfdir/pam.d/gnomesu-pam
%_bindir/gnomesu
%_datadir/application-registry/gnomesu-nautilus.applications
%_datadir/mime-info/gnomesu-nautilus.keys
%attr(4111,root,root) %_libexecdir/gnomesu-backend
%attr(4111,root,root) %_libexecdir/gnomesu-pam-backend

%files -n %libname
%defattr(-,root,root)
%_libdir/libgnomesu.so.%{major}*

%files -n %libnamedev
%defattr(-,root,root)
%_includedir/libgnomesu-1.0/
%_libdir/pkgconfig/libgnomesu-1.0.pc
%_libdir/lib*.so


%changelog
* Tue Feb 21 2012 Jon Dill <dillj@mandriva.org> 1.0.0-9mdv2012.0
+ Revision: 778799
- rebuild against new version of libffi4

* Wed Nov 16 2011 Götz Waschk <waschk@mandriva.org> 1.0.0-8
+ Revision: 731092
- rebuild
- rebuild
- fix build

* Wed Nov 11 2009 Götz Waschk <waschk@mandriva.org> 1.0.0-5mdv2010.1
+ Revision: 464603
- fix format strings
- update license

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.0.0-3mdv2009.0
+ Revision: 248721
- rebuild
- kill re-definition of %{buildroot} on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Oct 08 2007 Götz Waschk <waschk@mandriva.org> 1.0.0-1mdv2008.1
+ Revision: 95685
- new version
- fix URL

* Thu Aug 02 2007 Götz Waschk <waschk@mandriva.org> 0.9.5-5mdv2008.0
+ Revision: 57988
- unpack patch
- new devel name
- Import libgnomesu



* Tue Aug 01 2006 Frederic Crozat <fcrozat@mandriva.com> 0.9.5-5mdv2007.0
- Rebuild with latest dbus

* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 0.9.5-1mdv2007.0
- Rebuild

* Mon Jan 30 2006 Olivier Blin <oblin@mandriva.com> 0.9.5-3mdk
- use "include" directive instead of deprecated pam_stack (Patch0)

* Mon Mar 14 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.9.5-2mdk
- provide and obsolete gnomesu

* Wed Jan 12 2005 G�tz Waschk <waschk@linux-mandrake.com> 0.9.5-1mdk
- initial package
