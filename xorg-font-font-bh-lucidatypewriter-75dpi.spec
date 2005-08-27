# $Rev: 3198 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	font-bh-lucidatypewriter-75dpi
Summary(pl):	font-bh-lucidatypewriter-75dpi
Name:		xorg-font-font-bh-lucidatypewriter-75dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		X11
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bh-lucidatypewriter-75dpi-%{version}.tar.bz2
# Source0-md5:	4e6132f4fa8e692dc9f6b12754babee5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/font-bh-lucidatypewriter-75dpi-%{version}-root-%(id -u -n)

%description
font-bh-lucidatypewriter-75dpi

%description -l pl
font-bh-lucidatypewriter-75dpi


%prep
%setup -q -n font-bh-lucidatypewriter-75dpi-%{version}


%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_libdir}/X11/fonts/75dpi/*
