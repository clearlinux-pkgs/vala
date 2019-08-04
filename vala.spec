#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vala
Version  : 0.44.6
Release  : 26
URL      : https://download.gnome.org/sources/vala/0.44/vala-0.44.6.tar.xz
Source0  : https://download.gnome.org/sources/vala/0.44/vala-0.44.6.tar.xz
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
%setup -q -n vala-0.44.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1564946278
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1564946278
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vala
cp COPYING %{buildroot}/usr/share/package-licenses/vala/COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/vala-0.44/gen-introspect-0.44

%files bin
%defattr(-,root,root,-)
/usr/bin/vala
/usr/bin/vala-0.44
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.44
/usr/bin/valac
/usr/bin/valac-0.44
/usr/bin/valadoc
/usr/bin/valadoc-0.44
/usr/bin/vapigen
/usr/bin/vapigen-0.44

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/vala-0.44/Attributes.html
/usr/share/devhelp/books/vala-0.44/Classes.html
/usr/share/devhelp/books/vala-0.44/Concepts.html
/usr/share/devhelp/books/vala-0.44/Delegates.html
/usr/share/devhelp/books/vala-0.44/Enumerated_types__Enums_.html
/usr/share/devhelp/books/vala-0.44/Errors.html
/usr/share/devhelp/books/vala-0.44/Expressions.html
/usr/share/devhelp/books/vala-0.44/GIDL_metadata_format.html
/usr/share/devhelp/books/vala-0.44/GIR_metadata_format.html
/usr/share/devhelp/books/vala-0.44/Generics.html
/usr/share/devhelp/books/vala-0.44/Interfaces.html
/usr/share/devhelp/books/vala-0.44/Methods.html
/usr/share/devhelp/books/vala-0.44/Namespaces.html
/usr/share/devhelp/books/vala-0.44/Overview.html
/usr/share/devhelp/books/vala-0.44/Preprocessor.html
/usr/share/devhelp/books/vala-0.44/Statements.html
/usr/share/devhelp/books/vala-0.44/Structs.html
/usr/share/devhelp/books/vala-0.44/Types.html
/usr/share/devhelp/books/vala-0.44/default.css
/usr/share/devhelp/books/vala-0.44/index.html
/usr/share/devhelp/books/vala-0.44/vala-0.44.devhelp2
/usr/share/vala-0.44/vapi/alsa.deps
/usr/share/vala-0.44/vapi/alsa.vapi
/usr/share/vala-0.44/vapi/atk.vapi
/usr/share/vala-0.44/vapi/atspi-2.deps
/usr/share/vala-0.44/vapi/atspi-2.vapi
/usr/share/vala-0.44/vapi/avahi-client.vapi
/usr/share/vala-0.44/vapi/avahi-gobject.deps
/usr/share/vala-0.44/vapi/avahi-gobject.vapi
/usr/share/vala-0.44/vapi/bzlib.vapi
/usr/share/vala-0.44/vapi/cairo-xcb.deps
/usr/share/vala-0.44/vapi/cairo-xcb.vapi
/usr/share/vala-0.44/vapi/cairo.vapi
/usr/share/vala-0.44/vapi/ccss-1.vapi
/usr/share/vala-0.44/vapi/clutter-1.0.deps
/usr/share/vala-0.44/vapi/clutter-1.0.vapi
/usr/share/vala-0.44/vapi/clutter-gdk-1.0.deps
/usr/share/vala-0.44/vapi/clutter-gdk-1.0.vapi
/usr/share/vala-0.44/vapi/clutter-gst-2.0.deps
/usr/share/vala-0.44/vapi/clutter-gst-2.0.vapi
/usr/share/vala-0.44/vapi/clutter-gst-3.0.deps
/usr/share/vala-0.44/vapi/clutter-gst-3.0.vapi
/usr/share/vala-0.44/vapi/clutter-gtk-0.10.deps
/usr/share/vala-0.44/vapi/clutter-gtk-0.10.vapi
/usr/share/vala-0.44/vapi/clutter-gtk-1.0.deps
/usr/share/vala-0.44/vapi/clutter-gtk-1.0.vapi
/usr/share/vala-0.44/vapi/clutter-x11-1.0.deps
/usr/share/vala-0.44/vapi/clutter-x11-1.0.vapi
/usr/share/vala-0.44/vapi/cogl-1.0.deps
/usr/share/vala-0.44/vapi/cogl-1.0.vapi
/usr/share/vala-0.44/vapi/cogl-pango-1.0.deps
/usr/share/vala-0.44/vapi/cogl-pango-1.0.vapi
/usr/share/vala-0.44/vapi/curses.vapi
/usr/share/vala-0.44/vapi/dbus-glib-1.vapi
/usr/share/vala-0.44/vapi/enchant.vapi
/usr/share/vala-0.44/vapi/fuse.deps
/usr/share/vala-0.44/vapi/fuse.vapi
/usr/share/vala-0.44/vapi/gconf-2.0.vapi
/usr/share/vala-0.44/vapi/gdesktopenums-3.0.vapi
/usr/share/vala-0.44/vapi/gdk-2.0.deps
/usr/share/vala-0.44/vapi/gdk-2.0.vapi
/usr/share/vala-0.44/vapi/gdk-3.0.deps
/usr/share/vala-0.44/vapi/gdk-3.0.vapi
/usr/share/vala-0.44/vapi/gdk-pixbuf-2.0.deps
/usr/share/vala-0.44/vapi/gdk-pixbuf-2.0.vapi
/usr/share/vala-0.44/vapi/gdk-x11-2.0.deps
/usr/share/vala-0.44/vapi/gdk-x11-2.0.vapi
/usr/share/vala-0.44/vapi/gdk-x11-3.0.deps
/usr/share/vala-0.44/vapi/gdk-x11-3.0.vapi
/usr/share/vala-0.44/vapi/gdl-1.0.deps
/usr/share/vala-0.44/vapi/gdl-1.0.vapi
/usr/share/vala-0.44/vapi/gdl-3.0.deps
/usr/share/vala-0.44/vapi/gdl-3.0.vapi
/usr/share/vala-0.44/vapi/gedit-2.20.deps
/usr/share/vala-0.44/vapi/gedit-2.20.vapi
/usr/share/vala-0.44/vapi/geocode-glib-1.0.deps
/usr/share/vala-0.44/vapi/geocode-glib-1.0.vapi
/usr/share/vala-0.44/vapi/gio-2.0.vapi
/usr/share/vala-0.44/vapi/gio-unix-2.0.deps
/usr/share/vala-0.44/vapi/gio-unix-2.0.vapi
/usr/share/vala-0.44/vapi/gio-windows-2.0.deps
/usr/share/vala-0.44/vapi/gio-windows-2.0.vapi
/usr/share/vala-0.44/vapi/glib-2.0.vapi
/usr/share/vala-0.44/vapi/gmodule-2.0.vapi
/usr/share/vala-0.44/vapi/gnet-2.0.deps
/usr/share/vala-0.44/vapi/gnet-2.0.vapi
/usr/share/vala-0.44/vapi/gnome-desktop-2.0.deps
/usr/share/vala-0.44/vapi/gnome-desktop-2.0.vapi
/usr/share/vala-0.44/vapi/gnome-desktop-3.0.deps
/usr/share/vala-0.44/vapi/gnome-desktop-3.0.vapi
/usr/share/vala-0.44/vapi/gnome-vfs-2.0.vapi
/usr/share/vala-0.44/vapi/gnutls.vapi
/usr/share/vala-0.44/vapi/gobject-2.0.vapi
/usr/share/vala-0.44/vapi/gobject-introspection-1.0.vapi
/usr/share/vala-0.44/vapi/goocanvas-2.0.deps
/usr/share/vala-0.44/vapi/goocanvas-2.0.vapi
/usr/share/vala-0.44/vapi/goocanvas.deps
/usr/share/vala-0.44/vapi/goocanvas.vapi
/usr/share/vala-0.44/vapi/graphene-1.0.deps
/usr/share/vala-0.44/vapi/graphene-1.0.vapi
/usr/share/vala-0.44/vapi/gsl.vapi
/usr/share/vala-0.44/vapi/gst-editing-services-1.0.deps
/usr/share/vala-0.44/vapi/gst-editing-services-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-allocators-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-allocators-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-app-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-app-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-audio-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-audio-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-bad-allocators-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-bad-allocators-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-base-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-base-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-check-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-check-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-controller-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-controller-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-fft-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-fft-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-net-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-net-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-pbutils-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-pbutils-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-player-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-player-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-riff-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-riff-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-rtp-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-rtp-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-rtsp-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-rtsp-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-rtsp-server-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-rtsp-server-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-sdp-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-sdp-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-tag-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-tag-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-video-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-video-1.0.vapi
/usr/share/vala-0.44/vapi/gstreamer-webrtc-1.0.deps
/usr/share/vala-0.44/vapi/gstreamer-webrtc-1.0.vapi
/usr/share/vala-0.44/vapi/gtk+-2.0.deps
/usr/share/vala-0.44/vapi/gtk+-2.0.vapi
/usr/share/vala-0.44/vapi/gtk+-3.0.deps
/usr/share/vala-0.44/vapi/gtk+-3.0.vapi
/usr/share/vala-0.44/vapi/gtk+-unix-print-2.0.deps
/usr/share/vala-0.44/vapi/gtk+-unix-print-2.0.vapi
/usr/share/vala-0.44/vapi/gtk+-unix-print-3.0.deps
/usr/share/vala-0.44/vapi/gtk+-unix-print-3.0.vapi
/usr/share/vala-0.44/vapi/gtk4-unix-print.deps
/usr/share/vala-0.44/vapi/gtk4-unix-print.vapi
/usr/share/vala-0.44/vapi/gtk4.deps
/usr/share/vala-0.44/vapi/gtk4.vapi
/usr/share/vala-0.44/vapi/gtkmozembed.deps
/usr/share/vala-0.44/vapi/gtkmozembed.vapi
/usr/share/vala-0.44/vapi/gtksourceview-2.0.deps
/usr/share/vala-0.44/vapi/gtksourceview-2.0.vapi
/usr/share/vala-0.44/vapi/gudev-1.0.deps
/usr/share/vala-0.44/vapi/gudev-1.0.vapi
/usr/share/vala-0.44/vapi/hal.deps
/usr/share/vala-0.44/vapi/hal.vapi
/usr/share/vala-0.44/vapi/hildon-1.deps
/usr/share/vala-0.44/vapi/hildon-1.vapi
/usr/share/vala-0.44/vapi/hildon-fm-2.deps
/usr/share/vala-0.44/vapi/hildon-fm-2.vapi
/usr/share/vala-0.44/vapi/javascriptcoregtk-4.0.vapi
/usr/share/vala-0.44/vapi/json-glib-1.0.deps
/usr/share/vala-0.44/vapi/json-glib-1.0.vapi
/usr/share/vala-0.44/vapi/libarchive.deps
/usr/share/vala-0.44/vapi/libarchive.vapi
/usr/share/vala-0.44/vapi/libbonoboui-2.0.vapi
/usr/share/vala-0.44/vapi/libdaemon.vapi
/usr/share/vala-0.44/vapi/libepc-1.0.vapi
/usr/share/vala-0.44/vapi/libesmtp.vapi
/usr/share/vala-0.44/vapi/libftdi.deps
/usr/share/vala-0.44/vapi/libftdi.vapi
/usr/share/vala-0.44/vapi/libgeoclue-2.0.deps
/usr/share/vala-0.44/vapi/libgeoclue-2.0.vapi
/usr/share/vala-0.44/vapi/libglade-2.0.deps
/usr/share/vala-0.44/vapi/libglade-2.0.vapi
/usr/share/vala-0.44/vapi/libgnome-2.0.vapi
/usr/share/vala-0.44/vapi/libgnome-menu-3.0.deps
/usr/share/vala-0.44/vapi/libgnome-menu-3.0.vapi
/usr/share/vala-0.44/vapi/libgnome-menu.vapi
/usr/share/vala-0.44/vapi/libgnomeui-2.0.deps
/usr/share/vala-0.44/vapi/libgnomeui-2.0.vapi
/usr/share/vala-0.44/vapi/libgrss.deps
/usr/share/vala-0.44/vapi/libgrss.vapi
/usr/share/vala-0.44/vapi/libgsf-1.deps
/usr/share/vala-0.44/vapi/libgsf-1.vapi
/usr/share/vala-0.44/vapi/libgvc.vapi
/usr/share/vala-0.44/vapi/libmagic.vapi
/usr/share/vala-0.44/vapi/libnl-1.vapi
/usr/share/vala-0.44/vapi/libnl-2.0.deps
/usr/share/vala-0.44/vapi/libnl-2.0.vapi
/usr/share/vala-0.44/vapi/libnl-3.0.deps
/usr/share/vala-0.44/vapi/libnl-3.0.vapi
/usr/share/vala-0.44/vapi/libnotify.deps
/usr/share/vala-0.44/vapi/libnotify.vapi
/usr/share/vala-0.44/vapi/liboobs-1.vapi
/usr/share/vala-0.44/vapi/libosso.vapi
/usr/share/vala-0.44/vapi/libpanelapplet-2.0.deps
/usr/share/vala-0.44/vapi/libpanelapplet-2.0.vapi
/usr/share/vala-0.44/vapi/libpeas-1.0.deps
/usr/share/vala-0.44/vapi/libpeas-1.0.vapi
/usr/share/vala-0.44/vapi/libpeas-gtk-1.0.deps
/usr/share/vala-0.44/vapi/libpeas-gtk-1.0.vapi
/usr/share/vala-0.44/vapi/libpq.vapi
/usr/share/vala-0.44/vapi/libsexy.deps
/usr/share/vala-0.44/vapi/libsexy.vapi
/usr/share/vala-0.44/vapi/libsoup-2.4.deps
/usr/share/vala-0.44/vapi/libsoup-2.4.vapi
/usr/share/vala-0.44/vapi/libusb-1.0.deps
/usr/share/vala-0.44/vapi/libusb-1.0.vapi
/usr/share/vala-0.44/vapi/libusb.vapi
/usr/share/vala-0.44/vapi/libwnck-1.0.deps
/usr/share/vala-0.44/vapi/libwnck-1.0.vapi
/usr/share/vala-0.44/vapi/libwnck-3.0.deps
/usr/share/vala-0.44/vapi/libwnck-3.0.vapi
/usr/share/vala-0.44/vapi/libxml-2.0.vapi
/usr/share/vala-0.44/vapi/linux.deps
/usr/share/vala-0.44/vapi/linux.vapi
/usr/share/vala-0.44/vapi/loudmouth-1.0.vapi
/usr/share/vala-0.44/vapi/lua.vapi
/usr/share/vala-0.44/vapi/mysql.vapi
/usr/share/vala-0.44/vapi/orc-0.4.vapi
/usr/share/vala-0.44/vapi/packagekit-glib2.deps
/usr/share/vala-0.44/vapi/packagekit-glib2.vapi
/usr/share/vala-0.44/vapi/pango.deps
/usr/share/vala-0.44/vapi/pango.vapi
/usr/share/vala-0.44/vapi/pangocairo.deps
/usr/share/vala-0.44/vapi/pangocairo.vapi
/usr/share/vala-0.44/vapi/pixman-1.vapi
/usr/share/vala-0.44/vapi/polkit-agent-1.deps
/usr/share/vala-0.44/vapi/polkit-agent-1.vapi
/usr/share/vala-0.44/vapi/polkit-gobject-1.deps
/usr/share/vala-0.44/vapi/polkit-gobject-1.vapi
/usr/share/vala-0.44/vapi/poppler-glib.deps
/usr/share/vala-0.44/vapi/poppler-glib.vapi
/usr/share/vala-0.44/vapi/posix.vapi
/usr/share/vala-0.44/vapi/purple.deps
/usr/share/vala-0.44/vapi/purple.vapi
/usr/share/vala-0.44/vapi/raptor.vapi
/usr/share/vala-0.44/vapi/rasqal.deps
/usr/share/vala-0.44/vapi/rasqal.vapi
/usr/share/vala-0.44/vapi/readline.vapi
/usr/share/vala-0.44/vapi/rest-0.7.deps
/usr/share/vala-0.44/vapi/rest-0.7.vapi
/usr/share/vala-0.44/vapi/rest-extras-0.7.deps
/usr/share/vala-0.44/vapi/rest-extras-0.7.vapi
/usr/share/vala-0.44/vapi/sdl-gfx.deps
/usr/share/vala-0.44/vapi/sdl-gfx.vapi
/usr/share/vala-0.44/vapi/sdl-image.deps
/usr/share/vala-0.44/vapi/sdl-image.vapi
/usr/share/vala-0.44/vapi/sdl-mixer.deps
/usr/share/vala-0.44/vapi/sdl-mixer.vapi
/usr/share/vala-0.44/vapi/sdl-net.deps
/usr/share/vala-0.44/vapi/sdl-net.vapi
/usr/share/vala-0.44/vapi/sdl-ttf.deps
/usr/share/vala-0.44/vapi/sdl-ttf.vapi
/usr/share/vala-0.44/vapi/sdl.vapi
/usr/share/vala-0.44/vapi/sqlite3.vapi
/usr/share/vala-0.44/vapi/taglib_c.vapi
/usr/share/vala-0.44/vapi/tiff.vapi
/usr/share/vala-0.44/vapi/tokyocabinet.vapi
/usr/share/vala-0.44/vapi/udisks2.deps
/usr/share/vala-0.44/vapi/udisks2.vapi
/usr/share/vala-0.44/vapi/unique-1.0.deps
/usr/share/vala-0.44/vapi/unique-1.0.vapi
/usr/share/vala-0.44/vapi/v4l2.vapi
/usr/share/vala-0.44/vapi/vte-2.90.deps
/usr/share/vala-0.44/vapi/vte-2.90.vapi
/usr/share/vala-0.44/vapi/vte.deps
/usr/share/vala-0.44/vapi/vte.vapi
/usr/share/vala-0.44/vapi/webkit-1.0.deps
/usr/share/vala-0.44/vapi/webkit-1.0.vapi
/usr/share/vala-0.44/vapi/webkit2gtk-4.0.deps
/usr/share/vala-0.44/vapi/webkit2gtk-4.0.vapi
/usr/share/vala-0.44/vapi/webkit2gtk-web-extension-4.0.deps
/usr/share/vala-0.44/vapi/webkit2gtk-web-extension-4.0.vapi
/usr/share/vala-0.44/vapi/x11.vapi
/usr/share/vala-0.44/vapi/xcb-icccm.deps
/usr/share/vala-0.44/vapi/xcb-icccm.vapi
/usr/share/vala-0.44/vapi/xcb.vapi
/usr/share/vala-0.44/vapi/xtst.deps
/usr/share/vala-0.44/vapi/xtst.vapi
/usr/share/vala-0.44/vapi/zlib.vapi
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.44.vapi
/usr/share/vala/vapi/valadoc-0.44.deps
/usr/share/vala/vapi/valadoc-0.44.vapi
/usr/share/valadoc/icons/abstractclass.png
/usr/share/valadoc/icons/abstractmethod.png
/usr/share/valadoc/icons/abstractproperty.png
/usr/share/valadoc/icons/class.png
/usr/share/valadoc/icons/coll_close.png
/usr/share/valadoc/icons/coll_open.png
/usr/share/valadoc/icons/constant.png
/usr/share/valadoc/icons/constructor.png
/usr/share/valadoc/icons/delegate.png
/usr/share/valadoc/icons/devhelpstyle.css
/usr/share/valadoc/icons/enum.png
/usr/share/valadoc/icons/enumvalue.png
/usr/share/valadoc/icons/errorcode.png
/usr/share/valadoc/icons/errordomain.png
/usr/share/valadoc/icons/field.png
/usr/share/valadoc/icons/interface.png
/usr/share/valadoc/icons/method.png
/usr/share/valadoc/icons/namespace.png
/usr/share/valadoc/icons/package.png
/usr/share/valadoc/icons/packages.png
/usr/share/valadoc/icons/property.png
/usr/share/valadoc/icons/scripts.js
/usr/share/valadoc/icons/signal.png
/usr/share/valadoc/icons/staticmethod.png
/usr/share/valadoc/icons/struct.png
/usr/share/valadoc/icons/style.css
/usr/share/valadoc/icons/tip.png
/usr/share/valadoc/icons/virtualmethod.png
/usr/share/valadoc/icons/virtualproperty.png
/usr/share/valadoc/icons/warning.png
/usr/share/valadoc/icons/wikistyle.css

%files dev
%defattr(-,root,root,-)
/usr/include/vala-0.44/vala.h
/usr/include/vala-0.44/valagee.h
/usr/include/valadoc-0.44/valadoc.h
/usr/lib64/libvala-0.44.so
/usr/lib64/libvaladoc-0.44.so
/usr/lib64/pkgconfig/libvala-0.44.pc
/usr/lib64/pkgconfig/valadoc-0.44.pc
/usr/lib64/pkgconfig/vapigen-0.44.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvala-0.44.so.0
/usr/lib64/libvala-0.44.so.0.0.0
/usr/lib64/libvaladoc-0.44.so.0
/usr/lib64/libvaladoc-0.44.so.0.0.0
/usr/lib64/vala-0.44/libvalaccodegen.so
/usr/lib64/valadoc/doclets/devhelp/libdoclet.so
/usr/lib64/valadoc/doclets/gtkdoc/libdoclet.so
/usr/lib64/valadoc/doclets/html/libdoclet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vala/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vala-gen-introspect-0.44.1
/usr/share/man/man1/vala-gen-introspect.1
/usr/share/man/man1/valac-0.44.1
/usr/share/man/man1/valac.1
/usr/share/man/man1/valadoc-0.44.1
/usr/share/man/man1/valadoc.1
/usr/share/man/man1/vapigen-0.44.1
/usr/share/man/man1/vapigen.1
