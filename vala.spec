#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vala
Version  : 0.56.3
Release  : 67
URL      : https://download.gnome.org/sources/vala/0.56/vala-0.56.3.tar.xz
Source0  : https://download.gnome.org/sources/vala/0.56/vala-0.56.3.tar.xz
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
%setup -q -n vala-0.56.3
cd %{_builddir}/vala-0.56.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1662314134
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1662314134
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vala
cp %{_builddir}/vala-%{version}/COPYING %{buildroot}/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3 || :
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/vala-0.56/gen-introspect-0.56

%files bin
%defattr(-,root,root,-)
/usr/bin/vala
/usr/bin/vala-0.56
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.56
/usr/bin/valac
/usr/bin/valac-0.56
/usr/bin/valadoc
/usr/bin/valadoc-0.56
/usr/bin/vapigen
/usr/bin/vapigen-0.56

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/vala-0.56/Attributes.html
/usr/share/devhelp/books/vala-0.56/Classes.html
/usr/share/devhelp/books/vala-0.56/Concepts.html
/usr/share/devhelp/books/vala-0.56/Delegates.html
/usr/share/devhelp/books/vala-0.56/Enumerated_types__Enums_.html
/usr/share/devhelp/books/vala-0.56/Errors.html
/usr/share/devhelp/books/vala-0.56/Expressions.html
/usr/share/devhelp/books/vala-0.56/GIDL_metadata_format.html
/usr/share/devhelp/books/vala-0.56/GIR_metadata_format.html
/usr/share/devhelp/books/vala-0.56/Generics.html
/usr/share/devhelp/books/vala-0.56/Interfaces.html
/usr/share/devhelp/books/vala-0.56/Methods.html
/usr/share/devhelp/books/vala-0.56/Namespaces.html
/usr/share/devhelp/books/vala-0.56/Overview.html
/usr/share/devhelp/books/vala-0.56/Preprocessor.html
/usr/share/devhelp/books/vala-0.56/Statements.html
/usr/share/devhelp/books/vala-0.56/Structs.html
/usr/share/devhelp/books/vala-0.56/Types.html
/usr/share/devhelp/books/vala-0.56/default.css
/usr/share/devhelp/books/vala-0.56/index.html
/usr/share/devhelp/books/vala-0.56/vala-0.56.devhelp2
/usr/share/vala-0.56/vapi/SDL2_gfx.deps
/usr/share/vala-0.56/vapi/SDL2_gfx.vapi
/usr/share/vala-0.56/vapi/SDL2_image.deps
/usr/share/vala-0.56/vapi/SDL2_image.vapi
/usr/share/vala-0.56/vapi/SDL2_mixer.deps
/usr/share/vala-0.56/vapi/SDL2_mixer.vapi
/usr/share/vala-0.56/vapi/SDL2_net.deps
/usr/share/vala-0.56/vapi/SDL2_net.vapi
/usr/share/vala-0.56/vapi/SDL2_ttf.deps
/usr/share/vala-0.56/vapi/SDL2_ttf.vapi
/usr/share/vala-0.56/vapi/alsa.deps
/usr/share/vala-0.56/vapi/alsa.vapi
/usr/share/vala-0.56/vapi/atk.deps
/usr/share/vala-0.56/vapi/atk.vapi
/usr/share/vala-0.56/vapi/atspi-2.deps
/usr/share/vala-0.56/vapi/atspi-2.vapi
/usr/share/vala-0.56/vapi/avahi-client.vapi
/usr/share/vala-0.56/vapi/avahi-gobject.deps
/usr/share/vala-0.56/vapi/avahi-gobject.vapi
/usr/share/vala-0.56/vapi/bzlib.vapi
/usr/share/vala-0.56/vapi/cairo-gobject.deps
/usr/share/vala-0.56/vapi/cairo-gobject.vapi
/usr/share/vala-0.56/vapi/cairo-xcb.deps
/usr/share/vala-0.56/vapi/cairo-xcb.vapi
/usr/share/vala-0.56/vapi/cairo.vapi
/usr/share/vala-0.56/vapi/ccss-1.vapi
/usr/share/vala-0.56/vapi/clutter-1.0.deps
/usr/share/vala-0.56/vapi/clutter-1.0.vapi
/usr/share/vala-0.56/vapi/clutter-gdk-1.0.deps
/usr/share/vala-0.56/vapi/clutter-gdk-1.0.vapi
/usr/share/vala-0.56/vapi/clutter-gst-2.0.deps
/usr/share/vala-0.56/vapi/clutter-gst-2.0.vapi
/usr/share/vala-0.56/vapi/clutter-gst-3.0.deps
/usr/share/vala-0.56/vapi/clutter-gst-3.0.vapi
/usr/share/vala-0.56/vapi/clutter-gtk-0.10.deps
/usr/share/vala-0.56/vapi/clutter-gtk-0.10.vapi
/usr/share/vala-0.56/vapi/clutter-gtk-1.0.deps
/usr/share/vala-0.56/vapi/clutter-gtk-1.0.vapi
/usr/share/vala-0.56/vapi/clutter-x11-1.0.deps
/usr/share/vala-0.56/vapi/clutter-x11-1.0.vapi
/usr/share/vala-0.56/vapi/cogl-1.0.deps
/usr/share/vala-0.56/vapi/cogl-1.0.vapi
/usr/share/vala-0.56/vapi/cogl-pango-1.0.deps
/usr/share/vala-0.56/vapi/cogl-pango-1.0.vapi
/usr/share/vala-0.56/vapi/curses.vapi
/usr/share/vala-0.56/vapi/dbus-glib-1.vapi
/usr/share/vala-0.56/vapi/enchant-2.vapi
/usr/share/vala-0.56/vapi/enchant.vapi
/usr/share/vala-0.56/vapi/fuse.deps
/usr/share/vala-0.56/vapi/fuse.vapi
/usr/share/vala-0.56/vapi/gconf-2.0.vapi
/usr/share/vala-0.56/vapi/gdesktopenums-3.0.vapi
/usr/share/vala-0.56/vapi/gdk-2.0.deps
/usr/share/vala-0.56/vapi/gdk-2.0.vapi
/usr/share/vala-0.56/vapi/gdk-3.0.deps
/usr/share/vala-0.56/vapi/gdk-3.0.vapi
/usr/share/vala-0.56/vapi/gdk-pixbuf-2.0.deps
/usr/share/vala-0.56/vapi/gdk-pixbuf-2.0.vapi
/usr/share/vala-0.56/vapi/gdk-x11-2.0.deps
/usr/share/vala-0.56/vapi/gdk-x11-2.0.vapi
/usr/share/vala-0.56/vapi/gdk-x11-3.0.deps
/usr/share/vala-0.56/vapi/gdk-x11-3.0.vapi
/usr/share/vala-0.56/vapi/gdl-1.0.deps
/usr/share/vala-0.56/vapi/gdl-1.0.vapi
/usr/share/vala-0.56/vapi/gdl-3.0.deps
/usr/share/vala-0.56/vapi/gdl-3.0.vapi
/usr/share/vala-0.56/vapi/geocode-glib-1.0.deps
/usr/share/vala-0.56/vapi/geocode-glib-1.0.vapi
/usr/share/vala-0.56/vapi/geocode-glib-2.0.deps
/usr/share/vala-0.56/vapi/geocode-glib-2.0.vapi
/usr/share/vala-0.56/vapi/gio-2.0.deps
/usr/share/vala-0.56/vapi/gio-2.0.vapi
/usr/share/vala-0.56/vapi/gio-unix-2.0.deps
/usr/share/vala-0.56/vapi/gio-unix-2.0.vapi
/usr/share/vala-0.56/vapi/gio-windows-2.0.deps
/usr/share/vala-0.56/vapi/gio-windows-2.0.vapi
/usr/share/vala-0.56/vapi/glib-2.0.vapi
/usr/share/vala-0.56/vapi/gmodule-2.0.deps
/usr/share/vala-0.56/vapi/gmodule-2.0.vapi
/usr/share/vala-0.56/vapi/gnet-2.0.deps
/usr/share/vala-0.56/vapi/gnet-2.0.vapi
/usr/share/vala-0.56/vapi/gnome-bg-4.deps
/usr/share/vala-0.56/vapi/gnome-bg-4.vapi
/usr/share/vala-0.56/vapi/gnome-desktop-2.0.deps
/usr/share/vala-0.56/vapi/gnome-desktop-2.0.vapi
/usr/share/vala-0.56/vapi/gnome-desktop-3.0.deps
/usr/share/vala-0.56/vapi/gnome-desktop-3.0.vapi
/usr/share/vala-0.56/vapi/gnome-desktop-4.deps
/usr/share/vala-0.56/vapi/gnome-desktop-4.vapi
/usr/share/vala-0.56/vapi/gnome-rr-4.deps
/usr/share/vala-0.56/vapi/gnome-rr-4.vapi
/usr/share/vala-0.56/vapi/gnome-vfs-2.0.vapi
/usr/share/vala-0.56/vapi/gnu.deps
/usr/share/vala-0.56/vapi/gnu.vapi
/usr/share/vala-0.56/vapi/gnutls.vapi
/usr/share/vala-0.56/vapi/gobject-2.0.deps
/usr/share/vala-0.56/vapi/gobject-2.0.vapi
/usr/share/vala-0.56/vapi/gobject-introspection-1.0.deps
/usr/share/vala-0.56/vapi/gobject-introspection-1.0.vapi
/usr/share/vala-0.56/vapi/goocanvas-2.0.deps
/usr/share/vala-0.56/vapi/goocanvas-2.0.vapi
/usr/share/vala-0.56/vapi/goocanvas.deps
/usr/share/vala-0.56/vapi/goocanvas.vapi
/usr/share/vala-0.56/vapi/graphene-1.0.deps
/usr/share/vala-0.56/vapi/graphene-1.0.vapi
/usr/share/vala-0.56/vapi/graphene-gobject-1.0.deps
/usr/share/vala-0.56/vapi/graphene-gobject-1.0.vapi
/usr/share/vala-0.56/vapi/gsl.vapi
/usr/share/vala-0.56/vapi/gst-editing-services-1.0.deps
/usr/share/vala-0.56/vapi/gst-editing-services-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-allocators-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-allocators-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-app-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-app-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-audio-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-audio-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-bad-allocators-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-bad-allocators-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-base-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-base-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-check-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-check-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-controller-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-controller-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-fft-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-fft-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-net-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-net-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-pbutils-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-pbutils-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-play-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-play-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-player-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-player-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-riff-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-riff-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-rtp-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-rtp-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-rtsp-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-rtsp-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-rtsp-server-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-rtsp-server-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-sdp-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-sdp-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-tag-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-tag-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-video-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-video-1.0.vapi
/usr/share/vala-0.56/vapi/gstreamer-webrtc-1.0.deps
/usr/share/vala-0.56/vapi/gstreamer-webrtc-1.0.vapi
/usr/share/vala-0.56/vapi/gtk+-2.0.deps
/usr/share/vala-0.56/vapi/gtk+-2.0.vapi
/usr/share/vala-0.56/vapi/gtk+-3.0.deps
/usr/share/vala-0.56/vapi/gtk+-3.0.vapi
/usr/share/vala-0.56/vapi/gtk+-unix-print-2.0.deps
/usr/share/vala-0.56/vapi/gtk+-unix-print-2.0.vapi
/usr/share/vala-0.56/vapi/gtk+-unix-print-3.0.deps
/usr/share/vala-0.56/vapi/gtk+-unix-print-3.0.vapi
/usr/share/vala-0.56/vapi/gtk4-unix-print.deps
/usr/share/vala-0.56/vapi/gtk4-unix-print.vapi
/usr/share/vala-0.56/vapi/gtk4-wayland.deps
/usr/share/vala-0.56/vapi/gtk4-wayland.vapi
/usr/share/vala-0.56/vapi/gtk4-x11.deps
/usr/share/vala-0.56/vapi/gtk4-x11.vapi
/usr/share/vala-0.56/vapi/gtk4.deps
/usr/share/vala-0.56/vapi/gtk4.vapi
/usr/share/vala-0.56/vapi/gtkmozembed.deps
/usr/share/vala-0.56/vapi/gtkmozembed.vapi
/usr/share/vala-0.56/vapi/gtksourceview-2.0.deps
/usr/share/vala-0.56/vapi/gtksourceview-2.0.vapi
/usr/share/vala-0.56/vapi/gudev-1.0.deps
/usr/share/vala-0.56/vapi/gudev-1.0.vapi
/usr/share/vala-0.56/vapi/hal.deps
/usr/share/vala-0.56/vapi/hal.vapi
/usr/share/vala-0.56/vapi/harfbuzz-gobject.deps
/usr/share/vala-0.56/vapi/harfbuzz-gobject.vapi
/usr/share/vala-0.56/vapi/hildon-1.deps
/usr/share/vala-0.56/vapi/hildon-1.vapi
/usr/share/vala-0.56/vapi/hildon-fm-2.deps
/usr/share/vala-0.56/vapi/hildon-fm-2.vapi
/usr/share/vala-0.56/vapi/javascriptcoregtk-4.0.vapi
/usr/share/vala-0.56/vapi/javascriptcoregtk-4.1.vapi
/usr/share/vala-0.56/vapi/javascriptcoregtk-5.0.vapi
/usr/share/vala-0.56/vapi/json-glib-1.0.deps
/usr/share/vala-0.56/vapi/json-glib-1.0.vapi
/usr/share/vala-0.56/vapi/libarchive.deps
/usr/share/vala-0.56/vapi/libarchive.vapi
/usr/share/vala-0.56/vapi/libbonoboui-2.0.vapi
/usr/share/vala-0.56/vapi/libdaemon.vapi
/usr/share/vala-0.56/vapi/libepc-1.0.vapi
/usr/share/vala-0.56/vapi/libesmtp.vapi
/usr/share/vala-0.56/vapi/libftdi.deps
/usr/share/vala-0.56/vapi/libftdi.vapi
/usr/share/vala-0.56/vapi/libgeoclue-2.0.deps
/usr/share/vala-0.56/vapi/libgeoclue-2.0.vapi
/usr/share/vala-0.56/vapi/libglade-2.0.deps
/usr/share/vala-0.56/vapi/libglade-2.0.vapi
/usr/share/vala-0.56/vapi/libgnome-2.0.vapi
/usr/share/vala-0.56/vapi/libgnome-menu-3.0.deps
/usr/share/vala-0.56/vapi/libgnome-menu-3.0.vapi
/usr/share/vala-0.56/vapi/libgnome-menu.vapi
/usr/share/vala-0.56/vapi/libgnomeui-2.0.deps
/usr/share/vala-0.56/vapi/libgnomeui-2.0.vapi
/usr/share/vala-0.56/vapi/libgrss.deps
/usr/share/vala-0.56/vapi/libgrss.vapi
/usr/share/vala-0.56/vapi/libgsf-1.deps
/usr/share/vala-0.56/vapi/libgsf-1.vapi
/usr/share/vala-0.56/vapi/libgvc.vapi
/usr/share/vala-0.56/vapi/libmagic.vapi
/usr/share/vala-0.56/vapi/libnl-1.vapi
/usr/share/vala-0.56/vapi/libnl-2.0.deps
/usr/share/vala-0.56/vapi/libnl-2.0.vapi
/usr/share/vala-0.56/vapi/libnl-3.0.deps
/usr/share/vala-0.56/vapi/libnl-3.0.vapi
/usr/share/vala-0.56/vapi/libnotify.deps
/usr/share/vala-0.56/vapi/libnotify.vapi
/usr/share/vala-0.56/vapi/liboobs-1.vapi
/usr/share/vala-0.56/vapi/libosso.vapi
/usr/share/vala-0.56/vapi/libpanelapplet-2.0.deps
/usr/share/vala-0.56/vapi/libpanelapplet-2.0.vapi
/usr/share/vala-0.56/vapi/libpeas-1.0.deps
/usr/share/vala-0.56/vapi/libpeas-1.0.vapi
/usr/share/vala-0.56/vapi/libpeas-gtk-1.0.deps
/usr/share/vala-0.56/vapi/libpeas-gtk-1.0.vapi
/usr/share/vala-0.56/vapi/libpq.vapi
/usr/share/vala-0.56/vapi/libsexy.deps
/usr/share/vala-0.56/vapi/libsexy.vapi
/usr/share/vala-0.56/vapi/libsoup-2.4.deps
/usr/share/vala-0.56/vapi/libsoup-2.4.vapi
/usr/share/vala-0.56/vapi/libsoup-3.0.deps
/usr/share/vala-0.56/vapi/libsoup-3.0.vapi
/usr/share/vala-0.56/vapi/libunwind-generic.vapi
/usr/share/vala-0.56/vapi/libusb-1.0.deps
/usr/share/vala-0.56/vapi/libusb-1.0.vapi
/usr/share/vala-0.56/vapi/libusb.vapi
/usr/share/vala-0.56/vapi/libwnck-1.0.deps
/usr/share/vala-0.56/vapi/libwnck-1.0.vapi
/usr/share/vala-0.56/vapi/libwnck-3.0.deps
/usr/share/vala-0.56/vapi/libwnck-3.0.vapi
/usr/share/vala-0.56/vapi/libxml-2.0.vapi
/usr/share/vala-0.56/vapi/linux.deps
/usr/share/vala-0.56/vapi/linux.vapi
/usr/share/vala-0.56/vapi/loudmouth-1.0.vapi
/usr/share/vala-0.56/vapi/lua.vapi
/usr/share/vala-0.56/vapi/mysql.vapi
/usr/share/vala-0.56/vapi/orc-0.4.vapi
/usr/share/vala-0.56/vapi/packagekit-glib2.deps
/usr/share/vala-0.56/vapi/packagekit-glib2.vapi
/usr/share/vala-0.56/vapi/pango.deps
/usr/share/vala-0.56/vapi/pango.vapi
/usr/share/vala-0.56/vapi/pangocairo.deps
/usr/share/vala-0.56/vapi/pangocairo.vapi
/usr/share/vala-0.56/vapi/pixman-1.vapi
/usr/share/vala-0.56/vapi/polkit-agent-1.deps
/usr/share/vala-0.56/vapi/polkit-agent-1.vapi
/usr/share/vala-0.56/vapi/polkit-gobject-1.deps
/usr/share/vala-0.56/vapi/polkit-gobject-1.vapi
/usr/share/vala-0.56/vapi/poppler-glib.deps
/usr/share/vala-0.56/vapi/poppler-glib.vapi
/usr/share/vala-0.56/vapi/posix.vapi
/usr/share/vala-0.56/vapi/purple.deps
/usr/share/vala-0.56/vapi/purple.vapi
/usr/share/vala-0.56/vapi/raptor.vapi
/usr/share/vala-0.56/vapi/rasqal.deps
/usr/share/vala-0.56/vapi/rasqal.vapi
/usr/share/vala-0.56/vapi/readline.vapi
/usr/share/vala-0.56/vapi/rest-0.7.deps
/usr/share/vala-0.56/vapi/rest-0.7.vapi
/usr/share/vala-0.56/vapi/rest-1.0.deps
/usr/share/vala-0.56/vapi/rest-1.0.vapi
/usr/share/vala-0.56/vapi/rest-extras-0.7.deps
/usr/share/vala-0.56/vapi/rest-extras-0.7.vapi
/usr/share/vala-0.56/vapi/rest-extras-1.0.deps
/usr/share/vala-0.56/vapi/rest-extras-1.0.vapi
/usr/share/vala-0.56/vapi/sdl2-android.deps
/usr/share/vala-0.56/vapi/sdl2-android.vapi
/usr/share/vala-0.56/vapi/sdl2-ios.deps
/usr/share/vala-0.56/vapi/sdl2-ios.vapi
/usr/share/vala-0.56/vapi/sdl2-windows.deps
/usr/share/vala-0.56/vapi/sdl2-windows.vapi
/usr/share/vala-0.56/vapi/sdl2-winrt.deps
/usr/share/vala-0.56/vapi/sdl2-winrt.vapi
/usr/share/vala-0.56/vapi/sdl2.vapi
/usr/share/vala-0.56/vapi/sqlite3.vapi
/usr/share/vala-0.56/vapi/taglib_c.vapi
/usr/share/vala-0.56/vapi/tiff.vapi
/usr/share/vala-0.56/vapi/tokyocabinet.vapi
/usr/share/vala-0.56/vapi/udisks2.deps
/usr/share/vala-0.56/vapi/udisks2.vapi
/usr/share/vala-0.56/vapi/unique-1.0.deps
/usr/share/vala-0.56/vapi/unique-1.0.vapi
/usr/share/vala-0.56/vapi/v4l2.vapi
/usr/share/vala-0.56/vapi/wayland-client.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-4.0.deps
/usr/share/vala-0.56/vapi/webkit2gtk-4.0.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-4.1.deps
/usr/share/vala-0.56/vapi/webkit2gtk-4.1.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-5.0.deps
/usr/share/vala-0.56/vapi/webkit2gtk-5.0.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-4.0.deps
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-4.0.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-4.1.deps
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-4.1.vapi
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-5.0.deps
/usr/share/vala-0.56/vapi/webkit2gtk-web-extension-5.0.vapi
/usr/share/vala-0.56/vapi/x11.vapi
/usr/share/vala-0.56/vapi/xcb-icccm.deps
/usr/share/vala-0.56/vapi/xcb-icccm.vapi
/usr/share/vala-0.56/vapi/xcb.vapi
/usr/share/vala-0.56/vapi/xtst.deps
/usr/share/vala-0.56/vapi/xtst.vapi
/usr/share/vala-0.56/vapi/zlib.vapi
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.56.vapi
/usr/share/vala/vapi/valadoc-0.56.deps
/usr/share/vala/vapi/valadoc-0.56.vapi
/usr/share/valadoc-0.56/icons/abstractclass.svg
/usr/share/valadoc-0.56/icons/abstractmethod.svg
/usr/share/valadoc-0.56/icons/abstractproperty.svg
/usr/share/valadoc-0.56/icons/class.svg
/usr/share/valadoc-0.56/icons/coll_close.svg
/usr/share/valadoc-0.56/icons/coll_open.svg
/usr/share/valadoc-0.56/icons/constant.svg
/usr/share/valadoc-0.56/icons/constructor.svg
/usr/share/valadoc-0.56/icons/delegate.svg
/usr/share/valadoc-0.56/icons/devhelpstyle.css
/usr/share/valadoc-0.56/icons/enum.svg
/usr/share/valadoc-0.56/icons/enumvalue.svg
/usr/share/valadoc-0.56/icons/errorcode.svg
/usr/share/valadoc-0.56/icons/errordomain.svg
/usr/share/valadoc-0.56/icons/field.svg
/usr/share/valadoc-0.56/icons/interface.svg
/usr/share/valadoc-0.56/icons/method.svg
/usr/share/valadoc-0.56/icons/namespace.svg
/usr/share/valadoc-0.56/icons/package.svg
/usr/share/valadoc-0.56/icons/packages.svg
/usr/share/valadoc-0.56/icons/property.svg
/usr/share/valadoc-0.56/icons/scripts.js
/usr/share/valadoc-0.56/icons/signal.svg
/usr/share/valadoc-0.56/icons/staticmethod.svg
/usr/share/valadoc-0.56/icons/struct.svg
/usr/share/valadoc-0.56/icons/style.css
/usr/share/valadoc-0.56/icons/tip.svg
/usr/share/valadoc-0.56/icons/virtualmethod.svg
/usr/share/valadoc-0.56/icons/virtualproperty.svg
/usr/share/valadoc-0.56/icons/warning.svg
/usr/share/valadoc-0.56/icons/wikistyle.css

%files dev
%defattr(-,root,root,-)
/usr/include/vala-0.56/vala.h
/usr/include/vala-0.56/valagee.h
/usr/include/valadoc-0.56/valadoc.h
/usr/lib64/libvala-0.56.so
/usr/lib64/libvaladoc-0.56.so
/usr/lib64/pkgconfig/libvala-0.56.pc
/usr/lib64/pkgconfig/valadoc-0.56.pc
/usr/lib64/pkgconfig/vapigen-0.56.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvala-0.56.so.0
/usr/lib64/libvala-0.56.so.0.0.0
/usr/lib64/libvaladoc-0.56.so.0
/usr/lib64/libvaladoc-0.56.so.0.0.0
/usr/lib64/vala-0.56/libvalaccodegen.so
/usr/lib64/valadoc-0.56/doclets/devhelp/libdoclet.so
/usr/lib64/valadoc-0.56/doclets/gtkdoc/libdoclet.so
/usr/lib64/valadoc-0.56/doclets/html/libdoclet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vala-gen-introspect-0.56.1
/usr/share/man/man1/vala-gen-introspect.1
/usr/share/man/man1/valac-0.56.1
/usr/share/man/man1/valac.1
/usr/share/man/man1/valadoc-0.56.1
/usr/share/man/man1/valadoc.1
/usr/share/man/man1/vapigen-0.56.1
/usr/share/man/man1/vapigen.1
