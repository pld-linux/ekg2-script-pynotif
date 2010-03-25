
Summary:	Notification script for ekg2
Summary(pl.UTF-8):	Skrypt programu ekg2 wysyłający powiadomienia
Name:		ekg2-script-pynotif
Version:	0
Release:	0.20100325.1
License:	GPL v3
Group:		Applications/Communications
# git clone git://github.com/pawelz/pynotif.git
Source0:	pynotif.py
URL:		http://github.com/pawelz/pynotif/tree/master
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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/ekg2/scripts/

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/ekg2/scripts/pynotif.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/ekg2/scripts/pynotif.py
