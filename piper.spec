Name:           piper
Version:        0.8
Release:        4
Summary:        GTK application to configure gaming devices
Group:          System/Configuration
License:        GPLv2+
URL:            https://github.com/libratbag/piper
Source0:        https://github.com/libratbag/piper/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  meson
BuildRequires:  gettext
BuildRequires:  ratbagd
BuildRequires:  gtk-update-icon-cache
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python%{pyver}dist(evdev)
BuildRequires:  python%{pyver}dist(lxml)
BuildRequires:  python%{pyver}dist(pycairo)
BuildRequires:  python%{pyver}dist(pygobject)
BuildRequires:  python%{pyver}dist(flake8)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       ratbagd
Requires:       python%{pyver}dist(evdev)
Requires:       python%{pyver}dist(lxml)
Requires:       python%{pyver}dist(pycairo)
Requires:       python%{pyver}dist(pygobject)
Requires:       python-gobject3
Requires:       python-gi
Requires:       %{_lib}gdkx11-gir3.0

BuildArch:      noarch

%description

Piper is a GTK+ application to configure gaming mice. It is a graphical
front-end to the ratbagd DBus daemon.

Ratbagd currently supports devices from:
  - Logitech,
  - Etekcity,
  - GSkill,
  - Roccat,
  - Steelseries.

See the device files or the wiki page for a complete list of supported devices:
https://github.com/libratbag/libratbag/wiki/Devices

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%{_bindir}/%{name}
%{_datadir}/applications/org.freedesktop.Piper.desktop
%{_datadir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/org.freedesktop.Piper.svg
%{_iconsdir}/hicolor/symbolic/apps/org.freedesktop.Piper-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.Piper.appdata.xml
%{_mandir}/man1/*
%{python_sitelib}/%{name}
