# TODO: decide to use libinet6 or not
Summary:	Simple tunneling for applications that don't speak IPv6
Summary(pl.UTF-8):   Proste narzędzie do tunelowania
Name:		6tunnel
Version:	0.11
%define		_rc	rc1
Release:	0.%{_rc}.1
License:	GPL
Group:		Networking/Utilities
Source0:	http://toxygen.net/6tunnel/%{name}-%{version}%{_rc}.tar.gz
# Source0-md5:	b325fa9d238e32195fbb3fc3646b0d28
URL:		http://toxygen.net/6tunnel/
# probably not needed, but used if found, so BR or BC is needed
# to force stable build environment
# (should be disabled in configure if not needed)
BuildRequires:	autoconf
BuildRequires:	libinet6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
If you want to access some services that are avaiable only for IPv6
hosts and the application doesn't support it or you have no time to
play with patches, use this tool. Simple `6tunnel 6668 irc6.net 6667'
will do :)

%description -l pl.UTF-8
Jeśli chcesz uzyskać dostęp do niektórych usług, dostępnych wyłącznie
poprzez IPv6 z aplikacji, która nie wspiera IPv6 możesz użyć tego
narzędzia. Np. `6tunnel 6668 irc6.net 6667'.

%prep
%setup -q -n %{name}-0.11

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install 6tunnel		$RPM_BUILD_ROOT%{_bindir}
install 6tunnel.1	$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog contrib/cron.sh
%attr(755,root,root) %{_bindir}/6tunnel
%{_mandir}/man?/*
