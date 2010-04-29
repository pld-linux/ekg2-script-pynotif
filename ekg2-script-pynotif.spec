
Summary:	Notification script for ekg2
Summary(pl.UTF-8):	Skrypt programu ekg2 wysyłający powiadomienia
Name:		ekg2-script-pynotif
Version:	1.0
Release:	1
License:	GPL v3
Group:		Applications/Communications
Source0:	http://github.com/grodzik/pynotif/tarball/v%{version}
# Source0-md5:	5f90a561dc68997827d8b996fdcc07b2
URL:		http://github.com/grodzik/pynotif/tree/master
BuildRequires:	rpm-pythonprov
Requires:	dbus(org.freedesktop.Notifications)
Requires:	ekg2-plugin-scripting-python >= 0.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pynotif is an extension for ekg2. It sends dbus notifications about
status changes and incoming messages.

%description -l pl.UTF-8
pynotify jest rozszerzeniem programu ekg2, które wysyła dbusowe
powiadomienia o zmianach statusów i przychodzących wiadomościach.

%prep
%setup -qc
mv grodzik-pynotif-*/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/ekg2/scripts/

install pynotif.py $RPM_BUILD_ROOT%{_datadir}/ekg2/scripts/pynotif.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO-pl
%{_datadir}/ekg2/scripts/pynotif.py
