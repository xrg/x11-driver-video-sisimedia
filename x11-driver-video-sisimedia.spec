
%define date 20091203
%define rel  10
%define git_repo x11-driver-video-sisimedia
%define git_head HEAD

Name: x11-driver-video-sisimedia
Version: %git_get_ver
Release: %mkrel %git_get_rel
Summary: Video driver for SiS 670 / 671 cards
Group: System/X11
URL: http://www.linuxconsulting.ro/xorg-drivers/
Source: %git_bs_source %{name}-%{version}.tar.gz
# SiS patch from 20102701
License: MIT
BuildRequires: libdrm-devel >= 2.0
BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-server-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires: GL-devel
Requires: x11-server-common %(xserver-sdk-abi-requires videodrv)
Conflicts: xorg-x11-server < 7.0
Obsoletes: x11-driver-video-sis-imedia < %{version}-%{release}

%description
x11-driver-video-sisimedia is the video driver for SiS 670 / 671
cards. These are not supported by the X.org 'sis' driver. This code
is very different, so the two cannot be easily merged.

%prep
%git_get_source
%setup -q

%build
autoreconf -ifs

%configure2_5x --disable-static
%make

%install
%makeinstall_std
# it's just a copy of the x.org driver manpage and so not really any
# use - AdamW 2008/08
rm -f %{buildroot}%{_mandir}/man4/sis.*

%files
%defattr(-,root,root)
%doc readme
%{_libdir}/xorg/modules/drivers/sisimedia_drv.la
%{_libdir}/xorg/modules/drivers/sisimedia_drv.so
