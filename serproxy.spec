Summary:	Proxy for redirecting TCP connections to/from serial links
Summary(pl.UTF-8):	Proxy przekierowujące połączenia TCP do/z połączeń szeregowych
Name:		serproxy
Version:	0.1.2
Release:	2
License:	GPL
Group:		Networking/Daemons
Source0:	http://www.lspace.nildram.co.uk/files/%{name}-%{version}.tar.gz
# Source0-md5:	3cdac9c05fb3a272e4cc4d7ae433fb17
URL:		http://www.lspace.nildram.co.uk/freeware.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Serproxy is a GPL multi-threaded proxy program for redirecting network
socket connections to/from serial links, in cases where the remote end
of the serial link doesn't have a TCP/IP stack (eg an embedded or
microcontroller system). The proxy allows other hosts on the network
to communicate with the system on the remote end of the serial link.
When run, it listens for incoming connections on a number of tcp
ports. Whenever a connection is made data is proxied to and from that
connection to a serial port.

%description -l pl.UTF-8
Serproxy jest wielowątkowym proxy do przekierowywania połączeń
sieciowych na/z łączy szeregowych w przypadkach kiedy końcówka nie ma
stosu TCP/IP (np. w systemach wbudowanych lub mikrokontrolerach). Ten
proxy pozwala innym komputerom w sieci na komunikację z końcówką na
połączeniu szeregowym. Po uruchomieniu słucha na portach TCP. Po
połączeniu dane są przekierowywane do i z tego połączenia na port
szeregowy.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -D__UNIX__ %{?debug:-DDEBUG}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_sysconfdir}}

install serproxy $RPM_BUILD_ROOT%{_sbindir}
install serproxy.cfg $RPM_BUILD_ROOT%{_sysconfdir}


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_sbindir}/*
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/serproxy.cfg
