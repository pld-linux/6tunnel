Name:		6tunnel
Version:	0.04
Release:	1
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
License:	GPL
BuildRoot:	/tmp/%{name}-%{version}-root
Source0:	ftp://bzium.eu.org/pub/%{name}-%{version}.tar.gz
Summary:	Simple tunneling for applications that don't speak IPv6.
Summary(pl):	Proste narzêdzie do tunelowania.

%description
If you want to access some services that are avaiable only for IPv6 hosts
and the application doesn't support it or you have no time to play with
patches, use this tool. Simple `6tunnel 6668 irc6.net 6667' will do :)

%description -l pl
Je¶li chcesz uzyskaæ dostêp do niektórych us³ug, dostêpnych wy³±cznie
poprzez IPv6 z aplikacji, która nie wspiera IPv6 mo¿esz u¿yæ tego
narzêdzia. Np. `6tunnel 6668 irc6.net 6667'.

%prep
%setup -q -n %{name}

%build
make CC="gcc $RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install -s 6tunnel $RPM_BUILD_ROOT%{_bindir}
install 6tunnel.1  $RPM_BUILD_ROOT%{_mandir}/man1
gzip -9nf	   $RPM_BUILD_ROOT%{_mandir}/man*/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/6tunnel
%{_mandir}/man1/6tunnel.*
