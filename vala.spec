#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vala
Version  : 0.52.4
Release  : 53
URL      : https://download.gnome.org/sources/vala/0.52/vala-0.52.4.tar.xz
Source0  : https://download.gnome.org/sources/vala/0.52/vala-0.52.4.tar.xz
Summary  : The Vala compiler library
Group    : Development/Tools
License  : LGPL-2.1
Requires: vala-bin = %{version}-%{release}
Requires: vala-data = %{version}-%{release}
Requires: vala-lib = %{version}-%{release}
Requires: vala-license = %{version}-%{release}
Requires: vala-man = %{version}-%{release}
BuildRequires : bison
BuildRequires : buildreq-gnome
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : flex
BuildRequires : help2man
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libgvc)

%description


%package bin
Summary: bin components for the vala package.
Group: Binaries
Requires: vala-data = %{version}-%{release}
Requires: vala-license = %{version}-%{release}

%description bin
bin components for the vala package.


%package data
Summary: data components for the vala package.
Group: Data

%description data
data components for the vala package.


%package dev
Summary: dev components for the vala package.
Group: Development
Requires: vala-lib = %{version}-%{release}
Requires: vala-bin = %{version}-%{release}
Requires: vala-data = %{version}-%{release}
Provides: vala-devel = %{version}-%{release}
Requires: vala = %{version}-%{release}

%description dev
dev components for the vala package.


%package lib
Summary: lib components for the vala package.
Group: Libraries
Requires: vala-data = %{version}-%{release}
Requires: vala-license = %{version}-%{release}

%description lib
lib components for the vala package.


%package license
Summary: license components for the vala package.
Group: Default

%description license
license components for the vala package.


%package man
Summary: man components for the vala package.
Group: Default

%description man
man components for the vala package.


%prep
%setup -q -n vala-0.52.4
cd %{_builddir}/vala-0.52.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1622822469
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1622822469
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vala
cp %{_builddir}/vala-0.52.4/COPYING %{buildroot}/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/vala-0.52/gen-introspect-0.52

%files bin
%defattr(-,root,root,-)
/usr/bin/vala
/usr/bin/vala-0.52
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.52
/usr/bin/valac
/usr/bin/valac-0.52
/usr/bin/valadoc
/usr/bin/valadoc-0.52
/usr/bin/vapigen
/usr/bin/vapigen-0.52

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/vala-0.52/Attributes.html
/usr/share/devhelp/books/vala-0.52/Classes.html
/usr/share/devhelp/books/vala-0.52/Concepts.html
/usr/share/devhelp/books/vala-0.52/Delegates.html
/usr/share/devhelp/books/vala-0.52/Enumerated_types__Enums_.html
/usr/share/devhelp/books/vala-0.52/Errors.html
/usr/share/devhelp/books/vala-0.52/Expressions.html
/usr/share/devhelp/books/vala-0.52/GIDL_metadata_format.html
/usr/share/devhelp/books/vala-0.52/GIR_metadata_format.html
/usr/share/devhelp/books/vala-0.52/Generics.html
/usr/share/devhelp/books/vala-0.52/Interfaces.html
/usr/share/devhelp/books/vala-0.52/Methods.html
/usr/share/devhelp/books/vala-0.52/Namespaces.html
/usr/share/devhelp/books/vala-0.52/Overview.html
/usr/share/devhelp/books/vala-0.52/Preprocessor.html
/usr/share/devhelp/books/vala-0.52/Statements.html
/usr/share/devhelp/books/vala-0.52/Structs.html
/usr/share/devhelp/books/vala-0.52/Types.html
/usr/share/devhelp/books/vala-0.52/default.css
/usr/share/devhelp/books/vala-0.52/index.html
/usr/share/devhelp/books/vala-0.52/vala-0.52.devhelp2
/usr/share/vala-0.52/vapi/SDL2_gfx.deps
/usr/share/vala-0.52/vapi/SDL2_gfx.vapi
/usr/share/vala-0.52/vapi/SDL2_image.deps
/usr/share/vala-0.52/vapi/SDL2_image.vapi
/usr/share/vala-0.52/vapi/SDL2_mixer.deps
/usr/share/vala-0.52/vapi/SDL2_mixer.vapi
/usr/share/vala-0.52/vapi/SDL2_net.deps
/usr/share/vala-0.52/vapi/SDL2_net.vapi
/usr/share/vala-0.52/vapi/SDL2_ttf.deps
/usr/share/vala-0.52/vapi/SDL2_ttf.vapi
/usr/share/vala-0.52/vapi/alsa.deps
/usr/share/vala-0.52/vapi/alsa.vapi
/usr/share/vala-0.52/vapi/atk.deps
/usr/share/vala-0.52/vapi/atk.vapi
/usr/share/vala-0.52/vapi/atspi-2.deps
/usr/share/vala-0.52/vapi/atspi-2.vapi
/usr/share/vala-0.52/vapi/avahi-client.vapi
/usr/share/vala-0.52/vapi/avahi-gobject.deps
/usr/share/vala-0.52/vapi/avahi-gobject.vapi
/usr/share/vala-0.52/vapi/bzlib.vapi
/usr/share/vala-0.52/vapi/cairo-gobject.deps
/usr/share/vala-0.52/vapi/cairo-gobject.vapi
/usr/share/vala-0.52/vapi/cairo-xcb.deps
/usr/share/vala-0.52/vapi/cairo-xcb.vapi
/usr/share/vala-0.52/vapi/cairo.vapi
/usr/share/vala-0.52/vapi/ccss-1.vapi
/usr/share/vala-0.52/vapi/clutter-1.0.deps
/usr/share/vala-0.52/vapi/clutter-1.0.vapi
/usr/share/vala-0.52/vapi/clutter-gdk-1.0.deps
/usr/share/vala-0.52/vapi/clutter-gdk-1.0.vapi
/usr/share/vala-0.52/vapi/clutter-gst-2.0.deps
/usr/share/vala-0.52/vapi/clutter-gst-2.0.vapi
/usr/share/vala-0.52/vapi/clutter-gst-3.0.deps
/usr/share/vala-0.52/vapi/clutter-gst-3.0.vapi
/usr/share/vala-0.52/vapi/clutter-gtk-0.10.deps
/usr/share/vala-0.52/vapi/clutter-gtk-0.10.vapi
/usr/share/vala-0.52/vapi/clutter-gtk-1.0.deps
/usr/share/vala-0.52/vapi/clutter-gtk-1.0.vapi
/usr/share/vala-0.52/vapi/clutter-x11-1.0.deps
/usr/share/vala-0.52/vapi/clutter-x11-1.0.vapi
/usr/share/vala-0.52/vapi/cogl-1.0.deps
/usr/share/vala-0.52/vapi/cogl-1.0.vapi
/usr/share/vala-0.52/vapi/cogl-pango-1.0.deps
/usr/share/vala-0.52/vapi/cogl-pango-1.0.vapi
/usr/share/vala-0.52/vapi/curses.vapi
/usr/share/vala-0.52/vapi/dbus-glib-1.vapi
/usr/share/vala-0.52/vapi/enchant-2.vapi
/usr/share/vala-0.52/vapi/enchant.vapi
/usr/share/vala-0.52/vapi/fuse.deps
/usr/share/vala-0.52/vapi/fuse.vapi
/usr/share/vala-0.52/vapi/gconf-2.0.vapi
/usr/share/vala-0.52/vapi/gdesktopenums-3.0.vapi
/usr/share/vala-0.52/vapi/gdk-2.0.deps
/usr/share/vala-0.52/vapi/gdk-2.0.vapi
/usr/share/vala-0.52/vapi/gdk-3.0.deps
/usr/share/vala-0.52/vapi/gdk-3.0.vapi
/usr/share/vala-0.52/vapi/gdk-pixbuf-2.0.deps
/usr/share/vala-0.52/vapi/gdk-pixbuf-2.0.vapi
/usr/share/vala-0.52/vapi/gdk-x11-2.0.deps
/usr/share/vala-0.52/vapi/gdk-x11-2.0.vapi
/usr/share/vala-0.52/vapi/gdk-x11-3.0.deps
/usr/share/vala-0.52/vapi/gdk-x11-3.0.vapi
/usr/share/vala-0.52/vapi/gdl-1.0.deps
/usr/share/vala-0.52/vapi/gdl-1.0.vapi
/usr/share/vala-0.52/vapi/gdl-3.0.deps
/usr/share/vala-0.52/vapi/gdl-3.0.vapi
/usr/share/vala-0.52/vapi/gedit-2.20.deps
/usr/share/vala-0.52/vapi/gedit-2.20.vapi
/usr/share/vala-0.52/vapi/geocode-glib-1.0.deps
/usr/share/vala-0.52/vapi/geocode-glib-1.0.vapi
/usr/share/vala-0.52/vapi/gio-2.0.deps
/usr/share/vala-0.52/vapi/gio-2.0.vapi
/usr/share/vala-0.52/vapi/gio-unix-2.0.deps
/usr/share/vala-0.52/vapi/gio-unix-2.0.vapi
/usr/share/vala-0.52/vapi/gio-windows-2.0.deps
/usr/share/vala-0.52/vapi/gio-windows-2.0.vapi
/usr/share/vala-0.52/vapi/glib-2.0.vapi
/usr/share/vala-0.52/vapi/gmodule-2.0.deps
/usr/share/vala-0.52/vapi/gmodule-2.0.vapi
/usr/share/vala-0.52/vapi/gnet-2.0.deps
/usr/share/vala-0.52/vapi/gnet-2.0.vapi
/usr/share/vala-0.52/vapi/gnome-desktop-2.0.deps
/usr/share/vala-0.52/vapi/gnome-desktop-2.0.vapi
/usr/share/vala-0.52/vapi/gnome-desktop-3.0.deps
/usr/share/vala-0.52/vapi/gnome-desktop-3.0.vapi
/usr/share/vala-0.52/vapi/gnome-vfs-2.0.vapi
/usr/share/vala-0.52/vapi/gnu.deps
/usr/share/vala-0.52/vapi/gnu.vapi
/usr/share/vala-0.52/vapi/gnutls.vapi
/usr/share/vala-0.52/vapi/gobject-2.0.deps
/usr/share/vala-0.52/vapi/gobject-2.0.vapi
/usr/share/vala-0.52/vapi/gobject-introspection-1.0.deps
/usr/share/vala-0.52/vapi/gobject-introspection-1.0.vapi
/usr/share/vala-0.52/vapi/goocanvas-2.0.deps
/usr/share/vala-0.52/vapi/goocanvas-2.0.vapi
/usr/share/vala-0.52/vapi/goocanvas.deps
/usr/share/vala-0.52/vapi/goocanvas.vapi
/usr/share/vala-0.52/vapi/graphene-1.0.deps
/usr/share/vala-0.52/vapi/graphene-1.0.vapi
/usr/share/vala-0.52/vapi/graphene-gobject-1.0.deps
/usr/share/vala-0.52/vapi/graphene-gobject-1.0.vapi
/usr/share/vala-0.52/vapi/gsl.vapi
/usr/share/vala-0.52/vapi/gst-editing-services-1.0.deps
/usr/share/vala-0.52/vapi/gst-editing-services-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-allocators-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-allocators-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-app-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-app-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-audio-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-audio-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-bad-allocators-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-bad-allocators-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-base-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-base-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-check-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-check-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-controller-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-controller-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-fft-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-fft-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-net-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-net-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-pbutils-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-pbutils-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-play-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-play-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-player-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-player-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-riff-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-riff-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-rtp-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-rtp-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-rtsp-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-rtsp-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-rtsp-server-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-rtsp-server-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-sdp-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-sdp-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-tag-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-tag-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-video-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-video-1.0.vapi
/usr/share/vala-0.52/vapi/gstreamer-webrtc-1.0.deps
/usr/share/vala-0.52/vapi/gstreamer-webrtc-1.0.vapi
/usr/share/vala-0.52/vapi/gtk+-2.0.deps
/usr/share/vala-0.52/vapi/gtk+-2.0.vapi
/usr/share/vala-0.52/vapi/gtk+-3.0.deps
/usr/share/vala-0.52/vapi/gtk+-3.0.vapi
/usr/share/vala-0.52/vapi/gtk+-unix-print-2.0.deps
/usr/share/vala-0.52/vapi/gtk+-unix-print-2.0.vapi
/usr/share/vala-0.52/vapi/gtk+-unix-print-3.0.deps
/usr/share/vala-0.52/vapi/gtk+-unix-print-3.0.vapi
/usr/share/vala-0.52/vapi/gtk4-unix-print.deps
/usr/share/vala-0.52/vapi/gtk4-unix-print.vapi
/usr/share/vala-0.52/vapi/gtk4.deps
/usr/share/vala-0.52/vapi/gtk4.vapi
/usr/share/vala-0.52/vapi/gtkmozembed.deps
/usr/share/vala-0.52/vapi/gtkmozembed.vapi
/usr/share/vala-0.52/vapi/gtksourceview-2.0.deps
/usr/share/vala-0.52/vapi/gtksourceview-2.0.vapi
/usr/share/vala-0.52/vapi/gudev-1.0.deps
/usr/share/vala-0.52/vapi/gudev-1.0.vapi
/usr/share/vala-0.52/vapi/hal.deps
/usr/share/vala-0.52/vapi/hal.vapi
/usr/share/vala-0.52/vapi/harfbuzz-gobject.deps
/usr/share/vala-0.52/vapi/harfbuzz-gobject.vapi
/usr/share/vala-0.52/vapi/hildon-1.deps
/usr/share/vala-0.52/vapi/hildon-1.vapi
/usr/share/vala-0.52/vapi/hildon-fm-2.deps
/usr/share/vala-0.52/vapi/hildon-fm-2.vapi
/usr/share/vala-0.52/vapi/javascriptcoregtk-4.0.vapi
/usr/share/vala-0.52/vapi/json-glib-1.0.deps
/usr/share/vala-0.52/vapi/json-glib-1.0.vapi
/usr/share/vala-0.52/vapi/libarchive.deps
/usr/share/vala-0.52/vapi/libarchive.vapi
/usr/share/vala-0.52/vapi/libbonoboui-2.0.vapi
/usr/share/vala-0.52/vapi/libdaemon.vapi
/usr/share/vala-0.52/vapi/libepc-1.0.vapi
/usr/share/vala-0.52/vapi/libesmtp.vapi
/usr/share/vala-0.52/vapi/libftdi.deps
/usr/share/vala-0.52/vapi/libftdi.vapi
/usr/share/vala-0.52/vapi/libgeoclue-2.0.deps
/usr/share/vala-0.52/vapi/libgeoclue-2.0.vapi
/usr/share/vala-0.52/vapi/libglade-2.0.deps
/usr/share/vala-0.52/vapi/libglade-2.0.vapi
/usr/share/vala-0.52/vapi/libgnome-2.0.vapi
/usr/share/vala-0.52/vapi/libgnome-menu-3.0.deps
/usr/share/vala-0.52/vapi/libgnome-menu-3.0.vapi
/usr/share/vala-0.52/vapi/libgnome-menu.vapi
/usr/share/vala-0.52/vapi/libgnomeui-2.0.deps
/usr/share/vala-0.52/vapi/libgnomeui-2.0.vapi
/usr/share/vala-0.52/vapi/libgrss.deps
/usr/share/vala-0.52/vapi/libgrss.vapi
/usr/share/vala-0.52/vapi/libgsf-1.deps
/usr/share/vala-0.52/vapi/libgsf-1.vapi
/usr/share/vala-0.52/vapi/libgvc.vapi
/usr/share/vala-0.52/vapi/libmagic.vapi
/usr/share/vala-0.52/vapi/libnl-1.vapi
/usr/share/vala-0.52/vapi/libnl-2.0.deps
/usr/share/vala-0.52/vapi/libnl-2.0.vapi
/usr/share/vala-0.52/vapi/libnl-3.0.deps
/usr/share/vala-0.52/vapi/libnl-3.0.vapi
/usr/share/vala-0.52/vapi/libnotify.deps
/usr/share/vala-0.52/vapi/libnotify.vapi
/usr/share/vala-0.52/vapi/liboobs-1.vapi
/usr/share/vala-0.52/vapi/libosso.vapi
/usr/share/vala-0.52/vapi/libpanelapplet-2.0.deps
/usr/share/vala-0.52/vapi/libpanelapplet-2.0.vapi
/usr/share/vala-0.52/vapi/libpeas-1.0.deps
/usr/share/vala-0.52/vapi/libpeas-1.0.vapi
/usr/share/vala-0.52/vapi/libpeas-gtk-1.0.deps
/usr/share/vala-0.52/vapi/libpeas-gtk-1.0.vapi
/usr/share/vala-0.52/vapi/libpq.vapi
/usr/share/vala-0.52/vapi/libsexy.deps
/usr/share/vala-0.52/vapi/libsexy.vapi
/usr/share/vala-0.52/vapi/libsoup-2.4.deps
/usr/share/vala-0.52/vapi/libsoup-2.4.vapi
/usr/share/vala-0.52/vapi/libunwind-generic.vapi
/usr/share/vala-0.52/vapi/libusb-1.0.deps
/usr/share/vala-0.52/vapi/libusb-1.0.vapi
/usr/share/vala-0.52/vapi/libusb.vapi
/usr/share/vala-0.52/vapi/libwnck-1.0.deps
/usr/share/vala-0.52/vapi/libwnck-1.0.vapi
/usr/share/vala-0.52/vapi/libwnck-3.0.deps
/usr/share/vala-0.52/vapi/libwnck-3.0.vapi
/usr/share/vala-0.52/vapi/libxml-2.0.vapi
/usr/share/vala-0.52/vapi/linux.deps
/usr/share/vala-0.52/vapi/linux.vapi
/usr/share/vala-0.52/vapi/loudmouth-1.0.vapi
/usr/share/vala-0.52/vapi/lua.vapi
/usr/share/vala-0.52/vapi/mysql.vapi
/usr/share/vala-0.52/vapi/orc-0.4.vapi
/usr/share/vala-0.52/vapi/packagekit-glib2.deps
/usr/share/vala-0.52/vapi/packagekit-glib2.vapi
/usr/share/vala-0.52/vapi/pango.deps
/usr/share/vala-0.52/vapi/pango.vapi
/usr/share/vala-0.52/vapi/pangocairo.deps
/usr/share/vala-0.52/vapi/pangocairo.vapi
/usr/share/vala-0.52/vapi/pixman-1.vapi
/usr/share/vala-0.52/vapi/polkit-agent-1.deps
/usr/share/vala-0.52/vapi/polkit-agent-1.vapi
/usr/share/vala-0.52/vapi/polkit-gobject-1.deps
/usr/share/vala-0.52/vapi/polkit-gobject-1.vapi
/usr/share/vala-0.52/vapi/poppler-glib.deps
/usr/share/vala-0.52/vapi/poppler-glib.vapi
/usr/share/vala-0.52/vapi/posix.vapi
/usr/share/vala-0.52/vapi/purple.deps
/usr/share/vala-0.52/vapi/purple.vapi
/usr/share/vala-0.52/vapi/raptor.vapi
/usr/share/vala-0.52/vapi/rasqal.deps
/usr/share/vala-0.52/vapi/rasqal.vapi
/usr/share/vala-0.52/vapi/readline.vapi
/usr/share/vala-0.52/vapi/rest-0.7.deps
/usr/share/vala-0.52/vapi/rest-0.7.vapi
/usr/share/vala-0.52/vapi/rest-extras-0.7.deps
/usr/share/vala-0.52/vapi/rest-extras-0.7.vapi
/usr/share/vala-0.52/vapi/sdl2-android.deps
/usr/share/vala-0.52/vapi/sdl2-android.vapi
/usr/share/vala-0.52/vapi/sdl2-ios.deps
/usr/share/vala-0.52/vapi/sdl2-ios.vapi
/usr/share/vala-0.52/vapi/sdl2-windows.deps
/usr/share/vala-0.52/vapi/sdl2-windows.vapi
/usr/share/vala-0.52/vapi/sdl2-winrt.deps
/usr/share/vala-0.52/vapi/sdl2-winrt.vapi
/usr/share/vala-0.52/vapi/sdl2.vapi
/usr/share/vala-0.52/vapi/sqlite3.vapi
/usr/share/vala-0.52/vapi/taglib_c.vapi
/usr/share/vala-0.52/vapi/tiff.vapi
/usr/share/vala-0.52/vapi/tokyocabinet.vapi
/usr/share/vala-0.52/vapi/udisks2.deps
/usr/share/vala-0.52/vapi/udisks2.vapi
/usr/share/vala-0.52/vapi/unique-1.0.deps
/usr/share/vala-0.52/vapi/unique-1.0.vapi
/usr/share/vala-0.52/vapi/v4l2.vapi
/usr/share/vala-0.52/vapi/webkit-1.0.deps
/usr/share/vala-0.52/vapi/webkit-1.0.vapi
/usr/share/vala-0.52/vapi/webkit2gtk-4.0.deps
/usr/share/vala-0.52/vapi/webkit2gtk-4.0.vapi
/usr/share/vala-0.52/vapi/webkit2gtk-web-extension-4.0.deps
/usr/share/vala-0.52/vapi/webkit2gtk-web-extension-4.0.vapi
/usr/share/vala-0.52/vapi/x11.vapi
/usr/share/vala-0.52/vapi/xcb-icccm.deps
/usr/share/vala-0.52/vapi/xcb-icccm.vapi
/usr/share/vala-0.52/vapi/xcb.vapi
/usr/share/vala-0.52/vapi/xtst.deps
/usr/share/vala-0.52/vapi/xtst.vapi
/usr/share/vala-0.52/vapi/zlib.vapi
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.52.vapi
/usr/share/vala/vapi/valadoc-0.52.deps
/usr/share/vala/vapi/valadoc-0.52.vapi
/usr/share/valadoc-0.52/icons/abstractclass.svg
/usr/share/valadoc-0.52/icons/abstractmethod.svg
/usr/share/valadoc-0.52/icons/abstractproperty.svg
/usr/share/valadoc-0.52/icons/class.svg
/usr/share/valadoc-0.52/icons/coll_close.svg
/usr/share/valadoc-0.52/icons/coll_open.svg
/usr/share/valadoc-0.52/icons/constant.svg
/usr/share/valadoc-0.52/icons/constructor.svg
/usr/share/valadoc-0.52/icons/delegate.svg
/usr/share/valadoc-0.52/icons/devhelpstyle.css
/usr/share/valadoc-0.52/icons/enum.svg
/usr/share/valadoc-0.52/icons/enumvalue.svg
/usr/share/valadoc-0.52/icons/errorcode.svg
/usr/share/valadoc-0.52/icons/errordomain.svg
/usr/share/valadoc-0.52/icons/field.svg
/usr/share/valadoc-0.52/icons/interface.svg
/usr/share/valadoc-0.52/icons/method.svg
/usr/share/valadoc-0.52/icons/namespace.svg
/usr/share/valadoc-0.52/icons/package.svg
/usr/share/valadoc-0.52/icons/packages.svg
/usr/share/valadoc-0.52/icons/property.svg
/usr/share/valadoc-0.52/icons/scripts.js
/usr/share/valadoc-0.52/icons/signal.svg
/usr/share/valadoc-0.52/icons/staticmethod.svg
/usr/share/valadoc-0.52/icons/struct.svg
/usr/share/valadoc-0.52/icons/style.css
/usr/share/valadoc-0.52/icons/tip.svg
/usr/share/valadoc-0.52/icons/virtualmethod.svg
/usr/share/valadoc-0.52/icons/virtualproperty.svg
/usr/share/valadoc-0.52/icons/warning.svg
/usr/share/valadoc-0.52/icons/wikistyle.css

%files dev
%defattr(-,root,root,-)
/usr/include/vala-0.52/vala.h
/usr/include/vala-0.52/valagee.h
/usr/include/valadoc-0.52/valadoc.h
/usr/lib64/libvala-0.52.so
/usr/lib64/libvaladoc-0.52.so
/usr/lib64/pkgconfig/libvala-0.52.pc
/usr/lib64/pkgconfig/valadoc-0.52.pc
/usr/lib64/pkgconfig/vapigen-0.52.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvala-0.52.so.0
/usr/lib64/libvala-0.52.so.0.0.0
/usr/lib64/libvaladoc-0.52.so.0
/usr/lib64/libvaladoc-0.52.so.0.0.0
/usr/lib64/vala-0.52/libvalaccodegen.so
/usr/lib64/valadoc-0.52/doclets/devhelp/libdoclet.so
/usr/lib64/valadoc-0.52/doclets/gtkdoc/libdoclet.so
/usr/lib64/valadoc-0.52/doclets/html/libdoclet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vala-gen-introspect-0.52.1
/usr/share/man/man1/vala-gen-introspect.1
/usr/share/man/man1/valac-0.52.1
/usr/share/man/man1/valac.1
/usr/share/man/man1/valadoc-0.52.1
/usr/share/man/man1/valadoc.1
/usr/share/man/man1/vapigen-0.52.1
/usr/share/man/man1/vapigen.1
