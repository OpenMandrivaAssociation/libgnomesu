%define name libgnomesu
%define version 0.9.5
%define release %mkrel 5
%define major 0
%define libname %mklibname gnomesu %major

Summary: Library for accessing superuser privileges from GNOME
Name: %{name}
Version: %{version}
Release: %{release}
Source0: ftp://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
Patch0: libgnomesu-0.9.5-pam_stack.patch.bz2
License: LGPL
Group: System/Libraries
Url: http://www.gnome.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libgnomeui2-devel
BuildRequires: pam-devel
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

%package -n %libname-devel
Summary: Library for accessing superuser privileges from GNOME
Group: Development/C
Requires: %libname = %version-%release
Provides: %name-devel = %version-%release

%description -n %libname-devel
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%prep
%setup -q
%patch0 -p1 -b .pam_stack

%build
%configure2_5x --disable-setuid-error
%make

%install
rm -rf $RPM_BUILD_ROOT %name-1.0.lang
%makeinstall_std
%find_lang %name-1.0
#fix libtool mess
perl -pi -e "s°-L$RPM_BUILD_DIR/%name-%version/src°°" %buildroot/%_libdir/lib*.la
#gw fix perms for cpio
chmod 755 %buildroot%_libexecdir/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -n %libname -p /sbin/ldconfig
%postun -n %libname -p /sbin/ldconfig

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
%_libdir/lib*.so.*

%files -n %libname-devel
%defattr(-,root,root)
%_includedir/libgnomesu-1.0/
%_libdir/pkgconfig/libgnomesu-1.0.pc
%_libdir/lib*.so
%_libdir/lib*.la
