Summary:	Simple tunneling for applications that don't speak IPv6
Summary(pl.UTF-8):	Proste narzędzie do tunelowania
Name:		6tunnel
Version:	0.13
Release:	1
License:	GPL v2
Group:		Networking/Utilities
#Source0Download: https://github.com/wojtekka/6tunnel/releases
Source0:	https://github.com/wojtekka/6tunnel/releases/download/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b13ba5ad8efc5d74b2dd71c2df85ef35
URL:		https://github.com/wojtekka/6tunnel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you want to access some services that are avaiable only for IPv6
hosts and the application doesn't support it or you have no time to
play with patches, use this tool. Simple `6tunnel 6668 irc6.net 6667'
will do :)

%description -l pl.UTF-8
Teog narzędzia można użyć, aby uzyskać dostęp do niektórych usług,
dostępnych wyłącznie poprzez IPv6, z aplikacji, która nie obsługuje
IPv6 - np. `6tunnel 6668 irc6.net 6667'.

%prep
%setup -q

%build
%configure \
	ac_cv_lib_inet6_main=no \
	ac_cv_lib_nsl_t_accept=no \
	ac_cv_lib_socket_socket=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/6tunnel
%{_mandir}/man1/6tunnel.1*
