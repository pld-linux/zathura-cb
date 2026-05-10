%define		_zathura_api_ver	%(pkg-config --variable=apiversion zathura 2> /dev/null || echo -1)
%define		_zathura_abi_ver	%(pkg-config --variable=abiversion zathura 2> /dev/null || echo -1)

Summary:	Comic book support for zathura
Summary(pl.UTF-8):	Obsługa komiksów dla zathury
Name:		zathura-cb
Version:	2026.05.10
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-cb/download/%{name}-%{version}.tar.xz
# Source0-md5:	b6fc49cfebc9535263f2741a462fd218
URL:		https://pwmt.org/projects/zathura-cb/
BuildRequires:	cairo-devel
# C23
BuildRequires:	gcc >= 6:14
BuildRequires:	girara-devel >= 2026.02.03
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	libarchive-devel >= 3
BuildRequires:	meson >= 0.61
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 2026.01.30
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 2026.02.03
Requires:	libarchive >= 3
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
