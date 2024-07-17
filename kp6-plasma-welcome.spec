#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	6.1.3
%define		qtver		5.15.2
%define		kpname		plasma-welcome
%define		kf6ver		5.102.0

Summary:	Plasma Welcome App
Name:		kp6-%{kpname}
Version:	6.1.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	294bf123004fc33f1b373f3423cb530d
URL:		https://kde.org/
BuildRequires:	Qt6Core-devel >= 5.15.2
BuildRequires:	Qt6Gui-devel >= 5.15.2
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6Qml-devel
BuildRequires:	Qt6Quick-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Widgets-devel >= 5.15.0
BuildRequires:	cmake >= 3.16.0
BuildRequires:	fontconfig-devel
BuildRequires:	freetype-devel
BuildRequires:	gettext
BuildRequires:	gettext-devel
BuildRequires:	ka6-kaccounts-integration-devel
BuildRequires:	kf6-attica-devel >= 5.103.0
BuildRequires:	kf6-extra-cmake-modules >= 5.82
BuildRequires:	kf6-kauth-devel >= 5.103.0
BuildRequires:	kf6-kcodecs-devel >= 5.103.0
BuildRequires:	kf6-kcompletion-devel >= 5.103.0
BuildRequires:	kf6-kconfigwidgets-devel >= 5.103.0
BuildRequires:	kf6-kcoreaddons-devel >= 5.97.0
BuildRequires:	kf6-kdbusaddons-devel >= 5.98
BuildRequires:	kf6-kdeclarative-devel >= 5.98
BuildRequires:	kf6-ki18n-devel >= 5.98
BuildRequires:	kf6-kio-devel >= 5.98
BuildRequires:	kf6-kirigami-devel >= 5.98
BuildRequires:	kf6-kitemviews-devel >= 5.103.0
BuildRequires:	kf6-kjobwidgets-devel >= 5.103.0
BuildRequires:	kf6-knewstuff-devel >= 5.98
BuildRequires:	kf6-knotifications-devel >= 5.98
BuildRequires:	kf6-kpackage-devel >= 5.103.0
BuildRequires:	kf6-kservice-devel >= 5.98
BuildRequires:	kf6-kwidgetsaddons-devel >= 5.103.0
BuildRequires:	kf6-kwindowsystem-devel >= 5.98
BuildRequires:	kf6-kxmlgui-devel >= 5.103.0
BuildRequires:	kf6-solid-devel >= 5.103.0
BuildRequires:	kirigami-addons-devel >= 0.11.90
BuildRequires:	kuserfeedback-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-%{kpname} < %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt6dir		%{_libdir}/qt6

%description
A Friendly onboarding wizard for Plasma

Welcome Center is the perfect introduction to KDE Plasma! It can help
you learn how to connect to the internet, install apps, customize the
system, and more!

There are two usage modes:
- Run the app normally and it will show a welcome/onboarding wizard.
- Run the app with the `--after-upgrade-to` argument to show a
  post-upgrade message. For example: `plasma-welcome --after-upgrade-to
  5.25`.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DKDE_INSTALL_DOCBUNDLEDIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-welcome
%attr(755,root,root) %{_libdir}/qt6/plugins/kf6/kded/kded_plasma-welcome.so
%{_desktopdir}/org.kde.plasma-welcome.desktop
%{_datadir}/metainfo/org.kde.plasma-welcome.appdata.xml
