%define url_ver %(echo %{version}|cut -d. -f1,2)

%define major	0
%define libname	%mklibname gnomesu %major
%define devname	%mklibname -d gnomesu

Summary:	Library for accessing superuser privileges from GNOME
Name:		libgnomesu
Version:	1.0.0
Release:	15
License:	LGPLv2+
Group:		System/Libraries
Url:		http://members.chello.nl/~h.lai/libgnomesu/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/libgnomesu/%{url_ver}/%{name}-%{version}.tar.gz
Patch0:		libgnomesu-0.9.5-pam_stack.patch
Patch1:		libgnomesu-1.0.0-format-strings.patch
Patch2:		libgnomesu-1.0.0-deprecated.patch
BuildRequires:	intltool
BuildRequires:	pam-devel
BuildRequires:	pkgconfig(libgnomeui-2.0)
%rename		gnomesu

%description
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%package -n %{libname}
Summary:	Library for accessing superuser privileges from GNOME
Group:		System/Libraries
Requires:	%{name} >= %{version}-%{release}

%description -n %{libname}
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%package -n %{devname}
Summary:	Library for accessing superuser privileges from GNOME
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d gnomesu 0

%description -n %{devname}
libgnomesu is a library for providing superuser privileges to GNOME 
applications. It supports sudo, consolehelper, PAM and su.

%prep
%setup -q
%apply_patches
intltoolize --force
autoreconf -fi

%build
%configure2_5x \
	--disable-setuid-error

%make

%install
%makeinstall_std
%find_lang %{name}-1.0

#gw fix perms for cpio
chmod 755 %{buildroot}%{_libexecdir}/*

%files -f %{name}-1.0.lang
%doc README ChangeLog NEWS TODO AUTHORS
%config(noreplace) %_sysconfdir/pam.d/gnomesu-pam
%{_bindir}/gnomesu
%{_datadir}/application-registry/gnomesu-nautilus.applications
%{_datadir}/mime-info/gnomesu-nautilus.keys
%attr(4111,root,root) %{_libexecdir}/gnomesu-backend
%attr(4111,root,root) %{_libexecdir}/gnomesu-pam-backend

%files -n %{libname}
%{_libdir}/libgnomesu.so.%{major}*

%files -n %{devname}
%{_includedir}/libgnomesu-1.0/
%{_libdir}/pkgconfig/libgnomesu-1.0.pc
%{_libdir}/lib*.so

