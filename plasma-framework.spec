#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : plasma-framework
Version  : 5.57.0
Release  : 15
URL      : https://download.kde.org/stable/frameworks/5.57/plasma-framework-5.57.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.57/plasma-framework-5.57.0.tar.xz
Source99 : https://download.kde.org/stable/frameworks/5.57/plasma-framework-5.57.0.tar.xz.sig
Summary  : Plasma library and runtime components based upon KF5 and Qt5
Group    : Development/Tools
License  : GPL-2.0 LGPL-2.1
Requires: plasma-framework-bin = %{version}-%{release}
Requires: plasma-framework-data = %{version}-%{release}
Requires: plasma-framework-lib = %{version}-%{release}
Requires: plasma-framework-license = %{version}-%{release}
Requires: plasma-framework-locales = %{version}-%{release}
Requires: plasma-framework-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules pkgconfig(egl)
BuildRequires : extra-cmake-modules pkgconfig(xcb) xcb-util-cursor-dev xcb-util-image-dev xcb-util-keysyms-dev xcb-util-renderutil-dev xcb-util-wm-dev xcb-util-dev
BuildRequires : kactivities-dev
BuildRequires : kglobalaccel-dev
BuildRequires : kirigami2-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : mesa-dev
BuildRequires : qtbase-dev mesa-dev
BuildRequires : qtdeclarative-dev
BuildRequires : qtmultimedia-dev
BuildRequires : qtquickcontrols2-dev
BuildRequires : qtsvg-dev
BuildRequires : qtxmlpatterns-dev

%description
libplasma
This directory contains the classes making up libplasma, which provides the
core framework used by Plasma applications, such as the Plasma desktop shell
and its components. This includes applet and extension definitions and loading,
common GUI elements, data and service interaction, search system, etc.

%package bin
Summary: bin components for the plasma-framework package.
Group: Binaries
Requires: plasma-framework-data = %{version}-%{release}
Requires: plasma-framework-license = %{version}-%{release}

%description bin
bin components for the plasma-framework package.


%package data
Summary: data components for the plasma-framework package.
Group: Data

%description data
data components for the plasma-framework package.


%package dev
Summary: dev components for the plasma-framework package.
Group: Development
Requires: plasma-framework-lib = %{version}-%{release}
Requires: plasma-framework-bin = %{version}-%{release}
Requires: plasma-framework-data = %{version}-%{release}
Provides: plasma-framework-devel = %{version}-%{release}
Requires: plasma-framework = %{version}-%{release}

%description dev
dev components for the plasma-framework package.


%package lib
Summary: lib components for the plasma-framework package.
Group: Libraries
Requires: plasma-framework-data = %{version}-%{release}
Requires: plasma-framework-license = %{version}-%{release}

%description lib
lib components for the plasma-framework package.


%package license
Summary: license components for the plasma-framework package.
Group: Default

%description license
license components for the plasma-framework package.


%package locales
Summary: locales components for the plasma-framework package.
Group: Default

%description locales
locales components for the plasma-framework package.


%package man
Summary: man components for the plasma-framework package.
Group: Default

%description man
man components for the plasma-framework package.


%prep
%setup -q -n plasma-framework-5.57.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1555205077
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1555205077
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/plasma-framework
cp COPYING %{buildroot}/usr/share/package-licenses/plasma-framework/COPYING
cp COPYING.LIB %{buildroot}/usr/share/package-licenses/plasma-framework/COPYING.LIB
pushd clr-build
%make_install
popd
%find_lang libplasma5

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/plasmapkg2

%files data
%defattr(-,root,root,-)
/usr/share/kdevappwizard/templates/cpp-plasmoid.tar.bz2
/usr/share/kdevappwizard/templates/plasma-wallpaper-with-qml-extension.tar.bz2
/usr/share/kdevappwizard/templates/plasma-wallpaper.tar.bz2
/usr/share/kdevappwizard/templates/qml-plasmoid-with-qml-extension.tar.bz2
/usr/share/kdevappwizard/templates/qml-plasmoid.tar.bz2
/usr/share/kservices5/plasma-dataengine-testengine.desktop
/usr/share/kservices5/plasma-scriptengine-applet-declarative.desktop
/usr/share/kservicetypes5/plasma-applet.desktop
/usr/share/kservicetypes5/plasma-containment.desktop
/usr/share/kservicetypes5/plasma-containmentactions.desktop
/usr/share/kservicetypes5/plasma-dataengine.desktop
/usr/share/kservicetypes5/plasma-generic.desktop
/usr/share/kservicetypes5/plasma-lookandfeel.desktop
/usr/share/kservicetypes5/plasma-packagestructure.desktop
/usr/share/kservicetypes5/plasma-scriptengine.desktop
/usr/share/kservicetypes5/plasma-service.desktop
/usr/share/kservicetypes5/plasma-shell.desktop
/usr/share/kservicetypes5/plasma-wallpaper.desktop
/usr/share/locale/lt/LC_SCRIPTS/libplasma5/libplasma5.js
/usr/share/locale/lt/LC_SCRIPTS/libplasma5/plasmoids.js
/usr/share/plasma/desktoptheme/air/colors
/usr/share/plasma/desktoptheme/air/dialogs/background.svgz
/usr/share/plasma/desktoptheme/air/dialogs/kickoff.svgz
/usr/share/plasma/desktoptheme/air/dialogs/krunner.svgz
/usr/share/plasma/desktoptheme/air/icons/akonadi.svgz
/usr/share/plasma/desktoptheme/air/icons/akregator.svgz
/usr/share/plasma/desktoptheme/air/icons/amarok.svgz
/usr/share/plasma/desktoptheme/air/icons/applications.svgz
/usr/share/plasma/desktoptheme/air/icons/apport.svgz
/usr/share/plasma/desktoptheme/air/icons/audio.svgz
/usr/share/plasma/desktoptheme/air/icons/battery.svgz
/usr/share/plasma/desktoptheme/air/icons/bookmarks.svgz
/usr/share/plasma/desktoptheme/air/icons/computer.svgz
/usr/share/plasma/desktoptheme/air/icons/configure.svgz
/usr/share/plasma/desktoptheme/air/icons/device.svgz
/usr/share/plasma/desktoptheme/air/icons/edit.svgz
/usr/share/plasma/desktoptheme/air/icons/kdeconnect.svgz
/usr/share/plasma/desktoptheme/air/icons/keyboard.svgz
/usr/share/plasma/desktoptheme/air/icons/kget.svgz
/usr/share/plasma/desktoptheme/air/icons/klipper.svgz
/usr/share/plasma/desktoptheme/air/icons/konv_message.svgz
/usr/share/plasma/desktoptheme/air/icons/konversation.svgz
/usr/share/plasma/desktoptheme/air/icons/kopete.svgz
/usr/share/plasma/desktoptheme/air/icons/korgac.svgz
/usr/share/plasma/desktoptheme/air/icons/kpackagekit.svgz
/usr/share/plasma/desktoptheme/air/icons/ktorrent.svgz
/usr/share/plasma/desktoptheme/air/icons/nepomuk.svgz
/usr/share/plasma/desktoptheme/air/icons/network.svgz
/usr/share/plasma/desktoptheme/air/icons/notification.svgz
/usr/share/plasma/desktoptheme/air/icons/preferences.svgz
/usr/share/plasma/desktoptheme/air/icons/printer.svgz
/usr/share/plasma/desktoptheme/air/icons/quassel.svgz
/usr/share/plasma/desktoptheme/air/icons/slc.svgz
/usr/share/plasma/desktoptheme/air/icons/start.svgz
/usr/share/plasma/desktoptheme/air/icons/system.svgz
/usr/share/plasma/desktoptheme/air/icons/view.svgz
/usr/share/plasma/desktoptheme/air/icons/wallet.svgz
/usr/share/plasma/desktoptheme/air/metadata.desktop
/usr/share/plasma/desktoptheme/air/opaque/dialogs/background.svgz
/usr/share/plasma/desktoptheme/air/opaque/dialogs/krunner.svgz
/usr/share/plasma/desktoptheme/air/opaque/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/air/opaque/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/air/opaque/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/air/translucent/dialogs/background.svgz
/usr/share/plasma/desktoptheme/air/translucent/dialogs/krunner.svgz
/usr/share/plasma/desktoptheme/air/translucent/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/air/translucent/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/air/translucent/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/air/widgets/action-overlays.svgz
/usr/share/plasma/desktoptheme/air/widgets/actionbutton.svgz
/usr/share/plasma/desktoptheme/air/widgets/analog_meter.svgz
/usr/share/plasma/desktoptheme/air/widgets/arrows.svgz
/usr/share/plasma/desktoptheme/air/widgets/background.svgz
/usr/share/plasma/desktoptheme/air/widgets/bar_meter_horizontal.svgz
/usr/share/plasma/desktoptheme/air/widgets/bar_meter_vertical.svgz
/usr/share/plasma/desktoptheme/air/widgets/branding.svgz
/usr/share/plasma/desktoptheme/air/widgets/busywidget.svgz
/usr/share/plasma/desktoptheme/air/widgets/button.svgz
/usr/share/plasma/desktoptheme/air/widgets/checkmarks.svgz
/usr/share/plasma/desktoptheme/air/widgets/clock.svgz
/usr/share/plasma/desktoptheme/air/widgets/containment-controls.svgz
/usr/share/plasma/desktoptheme/air/widgets/dragger.svgz
/usr/share/plasma/desktoptheme/air/widgets/frame.svgz
/usr/share/plasma/desktoptheme/air/widgets/glowbar.svgz
/usr/share/plasma/desktoptheme/air/widgets/identiconshapes.svgz
/usr/share/plasma/desktoptheme/air/widgets/identicontheme.svgz
/usr/share/plasma/desktoptheme/air/widgets/labeltexture.svgz
/usr/share/plasma/desktoptheme/air/widgets/line.svgz
/usr/share/plasma/desktoptheme/air/widgets/lineedit.svgz
/usr/share/plasma/desktoptheme/air/widgets/listitem.svgz
/usr/share/plasma/desktoptheme/air/widgets/media-delegate.svgz
/usr/share/plasma/desktoptheme/air/widgets/monitor.svgz
/usr/share/plasma/desktoptheme/air/widgets/pager.svgz
/usr/share/plasma/desktoptheme/air/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/air/widgets/picker.svgz
/usr/share/plasma/desktoptheme/air/widgets/plot-background.svgz
/usr/share/plasma/desktoptheme/air/widgets/scrollbar.svgz
/usr/share/plasma/desktoptheme/air/widgets/scrollwidget.svgz
/usr/share/plasma/desktoptheme/air/widgets/slider.svgz
/usr/share/plasma/desktoptheme/air/widgets/systemtray.svgz
/usr/share/plasma/desktoptheme/air/widgets/tabbar.svgz
/usr/share/plasma/desktoptheme/air/widgets/tasks.svgz
/usr/share/plasma/desktoptheme/air/widgets/toolbar.svgz
/usr/share/plasma/desktoptheme/air/widgets/toolbox.svgz
/usr/share/plasma/desktoptheme/air/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/air/widgets/translucentbackground.svgz
/usr/share/plasma/desktoptheme/air/widgets/viewitem.svgz
/usr/share/plasma/desktoptheme/breeze-dark/colors
/usr/share/plasma/desktoptheme/breeze-dark/metadata.desktop
/usr/share/plasma/desktoptheme/breeze-light/colors
/usr/share/plasma/desktoptheme/breeze-light/metadata.desktop
/usr/share/plasma/desktoptheme/default/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/icons/akonadi.svgz
/usr/share/plasma/desktoptheme/default/icons/akregator.svgz
/usr/share/plasma/desktoptheme/default/icons/amarok.svgz
/usr/share/plasma/desktoptheme/default/icons/applications.svgz
/usr/share/plasma/desktoptheme/default/icons/apport.svgz
/usr/share/plasma/desktoptheme/default/icons/audio.svgz
/usr/share/plasma/desktoptheme/default/icons/battery.svgz
/usr/share/plasma/desktoptheme/default/icons/bookmarks.svgz
/usr/share/plasma/desktoptheme/default/icons/cantata.svgz
/usr/share/plasma/desktoptheme/default/icons/computer.svgz
/usr/share/plasma/desktoptheme/default/icons/configure.svgz
/usr/share/plasma/desktoptheme/default/icons/device.svgz
/usr/share/plasma/desktoptheme/default/icons/distribute.svgz
/usr/share/plasma/desktoptheme/default/icons/document.svgz
/usr/share/plasma/desktoptheme/default/icons/drive.svgz
/usr/share/plasma/desktoptheme/default/icons/edit.svgz
/usr/share/plasma/desktoptheme/default/icons/fcitx.svgz
/usr/share/plasma/desktoptheme/default/icons/go.svgz
/usr/share/plasma/desktoptheme/default/icons/ime.svgz
/usr/share/plasma/desktoptheme/default/icons/input.svgz
/usr/share/plasma/desktoptheme/default/icons/kalarm.svgz
/usr/share/plasma/desktoptheme/default/icons/kdeconnect.svgz
/usr/share/plasma/desktoptheme/default/icons/keyboard.svgz
/usr/share/plasma/desktoptheme/default/icons/kget.svgz
/usr/share/plasma/desktoptheme/default/icons/kgpg.svgz
/usr/share/plasma/desktoptheme/default/icons/kleopatra.svgz
/usr/share/plasma/desktoptheme/default/icons/klipper.svgz
/usr/share/plasma/desktoptheme/default/icons/kmail.svgz
/usr/share/plasma/desktoptheme/default/icons/konv_message.svgz
/usr/share/plasma/desktoptheme/default/icons/konversation.svgz
/usr/share/plasma/desktoptheme/default/icons/kopete.svgz
/usr/share/plasma/desktoptheme/default/icons/korgac.svgz
/usr/share/plasma/desktoptheme/default/icons/kpackagekit.svgz
/usr/share/plasma/desktoptheme/default/icons/kruler.svgz
/usr/share/plasma/desktoptheme/default/icons/kteatime.svgz
/usr/share/plasma/desktoptheme/default/icons/ktorrent.svgz
/usr/share/plasma/desktoptheme/default/icons/list.svgz
/usr/share/plasma/desktoptheme/default/icons/mail.svgz
/usr/share/plasma/desktoptheme/default/icons/media.svgz
/usr/share/plasma/desktoptheme/default/icons/nepomuk.svgz
/usr/share/plasma/desktoptheme/default/icons/network.svgz
/usr/share/plasma/desktoptheme/default/icons/notification.svgz
/usr/share/plasma/desktoptheme/default/icons/osd.svgz
/usr/share/plasma/desktoptheme/default/icons/phone.svgz
/usr/share/plasma/desktoptheme/default/icons/plasmavault.svgz
/usr/share/plasma/desktoptheme/default/icons/plasmavault_error.svgz
/usr/share/plasma/desktoptheme/default/icons/preferences.svgz
/usr/share/plasma/desktoptheme/default/icons/printer.svgz
/usr/share/plasma/desktoptheme/default/icons/quassel.svgz
/usr/share/plasma/desktoptheme/default/icons/slc.svgz
/usr/share/plasma/desktoptheme/default/icons/software.svgz
/usr/share/plasma/desktoptheme/default/icons/start.svgz
/usr/share/plasma/desktoptheme/default/icons/system.svgz
/usr/share/plasma/desktoptheme/default/icons/touchpad.svgz
/usr/share/plasma/desktoptheme/default/icons/user.svgz
/usr/share/plasma/desktoptheme/default/icons/video-card.svgz
/usr/share/plasma/desktoptheme/default/icons/video.svgz
/usr/share/plasma/desktoptheme/default/icons/view.svgz
/usr/share/plasma/desktoptheme/default/icons/vlc.svgz
/usr/share/plasma/desktoptheme/default/icons/wallet.svgz
/usr/share/plasma/desktoptheme/default/icons/window.svgz
/usr/share/plasma/desktoptheme/default/icons/zoom.svgz
/usr/share/plasma/desktoptheme/default/metadata.desktop
/usr/share/plasma/desktoptheme/default/opaque/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/opaque/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/opaque/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/translucent/dialogs/background.svgz
/usr/share/plasma/desktoptheme/default/translucent/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/translucent/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/widgets/action-overlays.svgz
/usr/share/plasma/desktoptheme/default/widgets/actionbutton.svgz
/usr/share/plasma/desktoptheme/default/widgets/analog_meter.svgz
/usr/share/plasma/desktoptheme/default/widgets/arrows.svgz
/usr/share/plasma/desktoptheme/default/widgets/background.svgz
/usr/share/plasma/desktoptheme/default/widgets/bar_meter_horizontal.svgz
/usr/share/plasma/desktoptheme/default/widgets/bar_meter_vertical.svgz
/usr/share/plasma/desktoptheme/default/widgets/branding.svgz
/usr/share/plasma/desktoptheme/default/widgets/busywidget.svgz
/usr/share/plasma/desktoptheme/default/widgets/button.svgz
/usr/share/plasma/desktoptheme/default/widgets/calendar.svgz
/usr/share/plasma/desktoptheme/default/widgets/checkmarks.svgz
/usr/share/plasma/desktoptheme/default/widgets/clock.svgz
/usr/share/plasma/desktoptheme/default/widgets/configuration-icons.svgz
/usr/share/plasma/desktoptheme/default/widgets/containment-controls.svgz
/usr/share/plasma/desktoptheme/default/widgets/dragger.svgz
/usr/share/plasma/desktoptheme/default/widgets/frame.svgz
/usr/share/plasma/desktoptheme/default/widgets/glowbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/line.svgz
/usr/share/plasma/desktoptheme/default/widgets/lineedit.svgz
/usr/share/plasma/desktoptheme/default/widgets/listitem.svgz
/usr/share/plasma/desktoptheme/default/widgets/media-delegate.svgz
/usr/share/plasma/desktoptheme/default/widgets/monitor.svgz
/usr/share/plasma/desktoptheme/default/widgets/notes.svgz
/usr/share/plasma/desktoptheme/default/widgets/pager.svgz
/usr/share/plasma/desktoptheme/default/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/default/widgets/picker.svgz
/usr/share/plasma/desktoptheme/default/widgets/plot-background.svgz
/usr/share/plasma/desktoptheme/default/widgets/scrollbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/scrollwidget.svgz
/usr/share/plasma/desktoptheme/default/widgets/slider.svgz
/usr/share/plasma/desktoptheme/default/widgets/tabbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/tasks.svgz
/usr/share/plasma/desktoptheme/default/widgets/toolbar.svgz
/usr/share/plasma/desktoptheme/default/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/default/widgets/translucentbackground.svgz
/usr/share/plasma/desktoptheme/default/widgets/viewitem.svgz
/usr/share/plasma/desktoptheme/oxygen/colors
/usr/share/plasma/desktoptheme/oxygen/dialogs/background.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/akonadi.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/akregator.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/amarok.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/applications.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/apport.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/audio.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/battery.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/bookmarks.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/computer.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/configure.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/device.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/edit.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/kdeconnect.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/keyboard.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/kget.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/klipper.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/konv_message.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/konversation.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/kopete.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/korgac.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/kpackagekit.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/ktorrent.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/nepomuk.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/network.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/notification.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/preferences.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/printer.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/quassel.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/slc.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/start.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/system.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/view.svgz
/usr/share/plasma/desktoptheme/oxygen/icons/wallet.svgz
/usr/share/plasma/desktoptheme/oxygen/metadata.desktop
/usr/share/plasma/desktoptheme/oxygen/opaque/dialogs/background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/dialogs/krunner.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/oxygen/opaque/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/action-overlays.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/actionbutton.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/analog_meter.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/arrows.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/bar_meter_horizontal.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/bar_meter_vertical.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/branding.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/busywidget.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/button.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/clock.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/containment-controls.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/dragger.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/extender-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/extender-dragger.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/frame.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/glowbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/line.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/lineedit.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/media-delegate.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/monitor.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/pager.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/panel-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/plot-background.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/scrollbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/scrollwidget.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/slider.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tabbar.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tasks.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/timer.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/tooltip.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/translucentbackground.svgz
/usr/share/plasma/desktoptheme/oxygen/widgets/viewitem.svgz
/usr/share/plasma/services/dataengineservice.operations
/usr/share/plasma/services/plasmoidservice.operations
/usr/share/plasma/services/storage.operations

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Plasma/Applet
/usr/include/KF5/Plasma/Containment
/usr/include/KF5/Plasma/ContainmentActions
/usr/include/KF5/Plasma/Corona
/usr/include/KF5/Plasma/DataContainer
/usr/include/KF5/Plasma/DataEngine
/usr/include/KF5/Plasma/DataEngineConsumer
/usr/include/KF5/Plasma/FrameSvg
/usr/include/KF5/Plasma/Package
/usr/include/KF5/Plasma/PackageStructure
/usr/include/KF5/Plasma/Plasma
/usr/include/KF5/Plasma/PluginLoader
/usr/include/KF5/Plasma/Service
/usr/include/KF5/Plasma/ServiceJob
/usr/include/KF5/Plasma/Svg
/usr/include/KF5/Plasma/Theme
/usr/include/KF5/PlasmaQuick/AppletQuickItem
/usr/include/KF5/PlasmaQuick/ConfigModel
/usr/include/KF5/PlasmaQuick/ConfigView
/usr/include/KF5/PlasmaQuick/ContainmentView
/usr/include/KF5/PlasmaQuick/Dialog
/usr/include/KF5/plasma/applet.h
/usr/include/KF5/plasma/containment.h
/usr/include/KF5/plasma/containmentactions.h
/usr/include/KF5/plasma/corona.h
/usr/include/KF5/plasma/datacontainer.h
/usr/include/KF5/plasma/dataengine.h
/usr/include/KF5/plasma/dataengineconsumer.h
/usr/include/KF5/plasma/framesvg.h
/usr/include/KF5/plasma/package.h
/usr/include/KF5/plasma/packagestructure.h
/usr/include/KF5/plasma/plasma.h
/usr/include/KF5/plasma/plasma_export.h
/usr/include/KF5/plasma/pluginloader.h
/usr/include/KF5/plasma/scripting/appletscript.h
/usr/include/KF5/plasma/scripting/dataenginescript.h
/usr/include/KF5/plasma/scripting/scriptengine.h
/usr/include/KF5/plasma/service.h
/usr/include/KF5/plasma/servicejob.h
/usr/include/KF5/plasma/svg.h
/usr/include/KF5/plasma/theme.h
/usr/include/KF5/plasma/version.h
/usr/include/KF5/plasma_version.h
/usr/include/KF5/plasmaquick/appletquickitem.h
/usr/include/KF5/plasmaquick/configmodel.h
/usr/include/KF5/plasmaquick/configview.h
/usr/include/KF5/plasmaquick/containmentview.h
/usr/include/KF5/plasmaquick/dialog.h
/usr/include/KF5/plasmaquick/packageurlinterceptor.h
/usr/include/KF5/plasmaquick/plasmaquick_export.h
/usr/lib64/cmake/KF5Plasma/KF5PlasmaConfig.cmake
/usr/lib64/cmake/KF5Plasma/KF5PlasmaConfigVersion.cmake
/usr/lib64/cmake/KF5Plasma/KF5PlasmaMacros.cmake
/usr/lib64/cmake/KF5Plasma/KF5PlasmaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Plasma/KF5PlasmaTargets.cmake
/usr/lib64/cmake/KF5PlasmaQuick/KF5PlasmaQuickConfig.cmake
/usr/lib64/cmake/KF5PlasmaQuick/KF5PlasmaQuickConfigVersion.cmake
/usr/lib64/cmake/KF5PlasmaQuick/KF5PlasmaQuickTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5PlasmaQuick/KF5PlasmaQuickTargets.cmake
/usr/lib64/libKF5Plasma.so
/usr/lib64/libKF5PlasmaQuick.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Plasma.so.5
/usr/lib64/libKF5Plasma.so.5.57.0
/usr/lib64/libKF5PlasmaQuick.so.5
/usr/lib64/libKF5PlasmaQuick.so.5.57.0
/usr/lib64/qt5/plugins/kpackage/packagestructure/containmentactions_packagestructure.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/dataengine_packagestructure.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/plasmageneric_packagestructure.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/plasmatheme_packagestructure.so
/usr/lib64/qt5/plugins/kpackage/packagestructure/plasmoid_packagestructure.so
/usr/lib64/qt5/plugins/plasma/scriptengines/plasma_appletscript_declarative.so
/usr/lib64/qt5/plugins/plasma_engine_testengine.so
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/BusyIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Button.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/CheckBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/CheckDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/CheckIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ComboBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Container.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Control.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Dial.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Dialog.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/DialogButtonBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Drawer.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Frame.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/GroupBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ItemDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Label.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Menu.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/MenuItem.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/PageIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Popup.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ProgressBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/RadioButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/RadioDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/RadioIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/RangeSlider.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/RoundButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ScrollBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ScrollView.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Slider.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/SpinBox.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/Switch.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/SwitchDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/SwitchIndicator.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/TabBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/TabButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/TextArea.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/TextField.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ToolButton.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/ToolTip.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/ButtonShadow.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/MobileCursor.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/MobileTextActionsToolBar.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/RoundShadow.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/TextFieldFocus.qml
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/private/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls.2/Plasma/qmldir
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ApplicationWindowStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/BusyIndicatorStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/CalendarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/CheckBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ComboBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/CursorDelegate.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/CursorHandleStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/EditMenuTouch.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/FocusFrameStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/GroupBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/MenuBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/MenuStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ProgressBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/RadioButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ScrollViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/SelectionHandleStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/SliderStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/SpinBoxStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/StatusBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/SwitchStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/TabViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/TableViewStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/TextAreaStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/TextFieldStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ToolBarStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/ToolButtonStyle.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/private/ButtonShadow.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/private/RoundShadow.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/private/TextFieldFocus.qml
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/private/Util.js
/usr/lib64/qt5/qml/QtQuick/Controls/Styles/Plasma/qmldir
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Plasma/Icon.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Plasma/Theme.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/Plasma/Units.qml
/usr/lib64/qt5/qml/org/kde/kirigami.2/styles/org.kde.desktop.plasma/Units.qml
/usr/lib64/qt5/qml/org/kde/plasma/accessdenied/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/calendar/CalendarToolbar.qml
/usr/lib64/qt5/qml/org/kde/plasma/calendar/DayDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/calendar/DaysCalendar.qml
/usr/lib64/qt5/qml/org/kde/plasma/calendar/MonthMenu.qml
/usr/lib64/qt5/qml/org/kde/plasma/calendar/MonthView.qml
/usr/lib64/qt5/qml/org/kde/plasma/calendar/libcalendarplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/calendar/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/plasma/calendar/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/components.3/BusyIndicator.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Button.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/CheckBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/CheckDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/CheckIndicator.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ComboBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Container.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Control.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Dial.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Frame.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/GroupBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ItemDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Label.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ProgressBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/RadioButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/RadioDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/RadioIndicator.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/RangeSlider.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ScrollBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Slider.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/SpinBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/Switch.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/SwitchDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/SwitchIndicator.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/TabBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/TabButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/TextArea.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/TextField.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ToolBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/ToolButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/ButtonShadow.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/DefaultListItemBackground.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/MobileCursor.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/MobileTextActionsToolBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/RoundShadow.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/TextFieldFocus.qml
/usr/lib64/qt5/qml/org/kde/plasma/components.3/private/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/components.3/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/components/BusyIndicator.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Button.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ButtonColumn.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ButtonGroup.js
/usr/lib64/qt5/qml/org/kde/plasma/components/ButtonRow.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/CheckBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ComboBox.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/CommonDialog.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ContextMenu.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Dialog.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Highlight.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Label.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ListItem.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ModelContextMenu.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Page.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/PageStack.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ProgressBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/QueryDialog.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/RadioButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ScrollBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/SectionScroller.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/SelectionDialog.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Sheet.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Slider.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/Switch.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/TabBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/TabButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/TabGroup.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/TextArea.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/TextField.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ToolBar.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ToolBarLayout.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/ToolButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/libplasmacomponentsplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/components/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/plasma/components/private/AppManager.js
/usr/lib64/qt5/qml/org/kde/plasma/components/private/DualStateButton.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/private/InlineDialog.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/private/PageStack.js
/usr/lib64/qt5/qml/org/kde/plasma/components/private/ScrollBarDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/private/ScrollDecoratorDelegate.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/private/SectionScroller.js
/usr/lib64/qt5/qml/org/kde/plasma/components/private/TabBarLayout.qml
/usr/lib64/qt5/qml/org/kde/plasma/components/private/TabGroup.js
/usr/lib64/qt5/qml/org/kde/plasma/components/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/core/libcorebindingsplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/core/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/plasma/core/private/DefaultToolTip.qml
/usr/lib64/qt5/qml/org/kde/plasma/core/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/extras/App.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/ConditionalLoader.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/DescriptiveLabel.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/Heading.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/PageRow.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/Paragraph.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/ScrollArea.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/Title.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/animations/ActivateAnimation.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/animations/AppearAnimation.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/animations/DisappearAnimation.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/animations/PressedAnimation.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/animations/ReleasedAnimation.qml
/usr/lib64/qt5/qml/org/kde/plasma/extras/libplasmaextracomponentsplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/extras/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/plasma/extras/qmldir
/usr/lib64/qt5/qml/org/kde/plasma/platformcomponents/libplatformcomponentsplugin.so
/usr/lib64/qt5/qml/org/kde/plasma/platformcomponents/plugins.qmltypes
/usr/lib64/qt5/qml/org/kde/plasma/platformcomponents/qmldir

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/plasma-framework/COPYING
/usr/share/package-licenses/plasma-framework/COPYING.LIB

%files man
%defattr(0644,root,root,0755)
/usr/share/man/ca/man1/plasmapkg2.1
/usr/share/man/de/man1/plasmapkg2.1
/usr/share/man/es/man1/plasmapkg2.1
/usr/share/man/it/man1/plasmapkg2.1
/usr/share/man/man1/plasmapkg2.1
/usr/share/man/nl/man1/plasmapkg2.1
/usr/share/man/pt/man1/plasmapkg2.1
/usr/share/man/pt_BR/man1/plasmapkg2.1
/usr/share/man/sv/man1/plasmapkg2.1
/usr/share/man/uk/man1/plasmapkg2.1

%files locales -f libplasma5.lang
%defattr(-,root,root,-)

