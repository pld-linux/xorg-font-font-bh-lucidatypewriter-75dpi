Summary:	bh-lucidatypewriter-75dpi font
Summary(pl):	Font bh-lucidatypewriter-75dpi
Name:		xorg-font-font-bh-lucidatypewriter-75dpi
Version:	0.99.0
Release:	0.01
License:	MIT
Group:		Fonts
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/font/font-bh-lucidatypewriter-75dpi-%{version}.tar.bz2
# Source0-md5:	4e6132f4fa8e692dc9f6b12754babee5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-app-bdftopcf
BuildRequires:	xorg-app-mkfontdir
BuildRequires:	xorg-app-mkfontscale
BuildRequires:	xorg-font-font-util
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
bh-lucidatypewriter-75dpi font.

%description -l pl
Font bh-lucidatypewriter-75dpi.

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
