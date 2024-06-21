Name:           piper
Version:        0.5.1
Release:        3
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
BuildRequires:  pkgconfig(python)
BuildRequires:  python3dist(evdev)
BuildRequires:  python3dist(lxml)
BuildRequires:  python3dist(pycairo)
BuildRequires:  python3dist(pygobject)
BuildRequires:  python3dist(flake8)
BuildRequires:  pkgconfig(gtk+-3.0)

Requires:       ratbagd
Requires:       python3dist(evdev)
Requires:       python3dist(lxml)
Requires:       python3dist(pycairo)
Requires:       python3dist(pygobject)

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
%{_datadir}/metainfo/org.freedesktop.Piper.appdata.xml
%{_mandir}/man1/*
%{python_sitelib}/%{name}
