%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	Comic book support for zathura
Summary(pl.UTF-8):	Obsługa komiksów dla zathury
Name:		zathura-cb
Version:	2026.01.30
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-cb/download/%{name}-%{version}.tar.xz
# Source0-md5:	669dae0e0355622e5db9ca1340c2758c
URL:		https://pwmt.org/projects/zathura-cb/
BuildRequires:	cairo-devel
# C17
BuildRequires:	gcc >= 6:8.1.0
BuildRequires:	girara-devel >= 0.1.8
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libarchive-devel
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 2026.01.30
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	zathura >= 2026.01.30
Requires:	zathura(plugin-abi) = %_zathura_abi_ver
Requires:	zathura(plugin-api) = %_zathura_api_ver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-cb plugin adds comic book support to zathura.

%description -l pl.UTF-8
Wtyczka zathura-ps dodaje do zathury obsługę komiksów.

%prep
%setup -q

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.md
%attr(755,root,root) %{_libdir}/zathura/libcb.so
%{_desktopdir}/org.pwmt.zathura-cb.desktop
%{_datadir}/metainfo/org.pwmt.zathura-cb.metainfo.xml
