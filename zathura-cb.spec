Summary:	Comic book support for zathura
Summary(pl.UTF-8):	Obsługa komiksów dla zathury
Name:		zathura-cb
Version:	0.1.11
Release:	1
License:	BSD-like
Group:		Applications/Publishing
Source0:	https://pwmt.org/projects/zathura-cb/download/%{name}-%{version}.tar.xz
# Source0-md5:	7bb8589ca179484ee0ab1923d4b02415
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
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zathura-devel >= 0.3.8
Requires(post,postun):	desktop-file-utils
Requires:	girara >= 0.1.8
Requires:	zathura >= 0.3.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The zathura-cb plugin adds comic book support to zathura.

%description -l pl.UTF-8
Wtyczka zathura-ps dodaje do zathury obsługę komiksów.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
