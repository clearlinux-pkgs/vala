#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vala
Version  : 0.40.7
Release  : 5
URL      : https://download.gnome.org/sources/vala/0.40/vala-0.40.7.tar.xz
Source0  : https://download.gnome.org/sources/vala/0.40/vala-0.40.7.tar.xz
Summary  : The Vala compiler library
Group    : Development/Tools
License  : LGPL-2.1
Requires: vala-bin
Requires: vala-lib
Requires: vala-license
Requires: vala-man
Requires: vala-data
BuildRequires : bison
BuildRequires : dbus
BuildRequires : dbus-dev
BuildRequires : flex
BuildRequires : help2man
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(gmodule-2.0)
BuildRequires : pkgconfig(gobject-2.0)
BuildRequires : pkgconfig(libgvc)

%description
Vala is a programming language that aims to bring modern programming
language features to GNOME developers without imposing any additional
runtime requirements and without using a different ABI compared to
applications and libraries written in C.

%package bin
Summary: bin components for the vala package.
Group: Binaries
Requires: vala-data
Requires: vala-license
Requires: vala-man

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
Requires: vala-lib
Requires: vala-bin
Requires: vala-data
Provides: vala-devel

%description dev
dev components for the vala package.


%package lib
Summary: lib components for the vala package.
Group: Libraries
Requires: vala-data
Requires: vala-license

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
%setup -q -n vala-0.40.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530083224
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1530083224
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/vala
cp COPYING %{buildroot}/usr/share/doc/vala/COPYING
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/vala-0.40/gen-introspect-0.40

%files bin
%defattr(-,root,root,-)
/usr/bin/vala
/usr/bin/vala-0.40
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.40
/usr/bin/valac
/usr/bin/valac-0.40
/usr/bin/valadoc
/usr/bin/valadoc-0.40
/usr/bin/vapigen
/usr/bin/vapigen-0.40

%files data
%defattr(-,root,root,-)
/usr/share/vala-0.40/vapi/alsa.deps
/usr/share/vala-0.40/vapi/alsa.vapi
/usr/share/vala-0.40/vapi/atk.vapi
/usr/share/vala-0.40/vapi/atspi-2.deps
/usr/share/vala-0.40/vapi/atspi-2.vapi
/usr/share/vala-0.40/vapi/avahi-client.vapi
/usr/share/vala-0.40/vapi/avahi-gobject.deps
/usr/share/vala-0.40/vapi/avahi-gobject.vapi
/usr/share/vala-0.40/vapi/bzlib.vapi
/usr/share/vala-0.40/vapi/cairo-xcb.deps
/usr/share/vala-0.40/vapi/cairo-xcb.vapi
/usr/share/vala-0.40/vapi/cairo.vapi
/usr/share/vala-0.40/vapi/ccss-1.vapi
/usr/share/vala-0.40/vapi/clutter-1.0.deps
/usr/share/vala-0.40/vapi/clutter-1.0.vapi
/usr/share/vala-0.40/vapi/clutter-gdk-1.0.deps
/usr/share/vala-0.40/vapi/clutter-gdk-1.0.vapi
/usr/share/vala-0.40/vapi/clutter-gst-1.0.deps
/usr/share/vala-0.40/vapi/clutter-gst-1.0.vapi
/usr/share/vala-0.40/vapi/clutter-gst-2.0.deps
/usr/share/vala-0.40/vapi/clutter-gst-2.0.vapi
/usr/share/vala-0.40/vapi/clutter-gst-3.0.deps
/usr/share/vala-0.40/vapi/clutter-gst-3.0.vapi
/usr/share/vala-0.40/vapi/clutter-gtk-0.10.deps
/usr/share/vala-0.40/vapi/clutter-gtk-0.10.vapi
/usr/share/vala-0.40/vapi/clutter-gtk-1.0.deps
/usr/share/vala-0.40/vapi/clutter-gtk-1.0.vapi
/usr/share/vala-0.40/vapi/clutter-x11-1.0.deps
/usr/share/vala-0.40/vapi/clutter-x11-1.0.vapi
/usr/share/vala-0.40/vapi/cogl-1.0.deps
/usr/share/vala-0.40/vapi/cogl-1.0.vapi
/usr/share/vala-0.40/vapi/cogl-pango-1.0.deps
/usr/share/vala-0.40/vapi/cogl-pango-1.0.vapi
/usr/share/vala-0.40/vapi/curses.vapi
/usr/share/vala-0.40/vapi/dbus-glib-1.vapi
/usr/share/vala-0.40/vapi/enchant.vapi
/usr/share/vala-0.40/vapi/fuse.deps
/usr/share/vala-0.40/vapi/fuse.vapi
/usr/share/vala-0.40/vapi/gconf-2.0.vapi
/usr/share/vala-0.40/vapi/gdk-2.0.deps
/usr/share/vala-0.40/vapi/gdk-2.0.vapi
/usr/share/vala-0.40/vapi/gdk-3.0.deps
/usr/share/vala-0.40/vapi/gdk-3.0.vapi
/usr/share/vala-0.40/vapi/gdk-pixbuf-2.0.deps
/usr/share/vala-0.40/vapi/gdk-pixbuf-2.0.vapi
/usr/share/vala-0.40/vapi/gdk-x11-2.0.deps
/usr/share/vala-0.40/vapi/gdk-x11-2.0.vapi
/usr/share/vala-0.40/vapi/gdk-x11-3.0.deps
/usr/share/vala-0.40/vapi/gdk-x11-3.0.vapi
/usr/share/vala-0.40/vapi/gdl-1.0.deps
/usr/share/vala-0.40/vapi/gdl-1.0.vapi
/usr/share/vala-0.40/vapi/gdl-3.0.deps
/usr/share/vala-0.40/vapi/gdl-3.0.vapi
/usr/share/vala-0.40/vapi/gdu-gtk.deps
/usr/share/vala-0.40/vapi/gdu-gtk.vapi
/usr/share/vala-0.40/vapi/gdu.deps
/usr/share/vala-0.40/vapi/gdu.vapi
/usr/share/vala-0.40/vapi/gedit-2.20.deps
/usr/share/vala-0.40/vapi/gedit-2.20.vapi
/usr/share/vala-0.40/vapi/geocode-glib-1.0.deps
/usr/share/vala-0.40/vapi/geocode-glib-1.0.vapi
/usr/share/vala-0.40/vapi/gio-2.0.vapi
/usr/share/vala-0.40/vapi/gio-unix-2.0.deps
/usr/share/vala-0.40/vapi/gio-unix-2.0.vapi
/usr/share/vala-0.40/vapi/gio-windows-2.0.deps
/usr/share/vala-0.40/vapi/gio-windows-2.0.vapi
/usr/share/vala-0.40/vapi/glib-2.0.vapi
/usr/share/vala-0.40/vapi/gmodule-2.0.vapi
/usr/share/vala-0.40/vapi/gnet-2.0.deps
/usr/share/vala-0.40/vapi/gnet-2.0.vapi
/usr/share/vala-0.40/vapi/gnome-desktop-2.0.deps
/usr/share/vala-0.40/vapi/gnome-desktop-2.0.vapi
/usr/share/vala-0.40/vapi/gnome-vfs-2.0.vapi
/usr/share/vala-0.40/vapi/gnutls.vapi
/usr/share/vala-0.40/vapi/gobject-2.0.vapi
/usr/share/vala-0.40/vapi/gobject-introspection-1.0.vapi
/usr/share/vala-0.40/vapi/goocanvas.deps
/usr/share/vala-0.40/vapi/goocanvas.vapi
/usr/share/vala-0.40/vapi/graphene-1.0.deps
/usr/share/vala-0.40/vapi/graphene-1.0.vapi
/usr/share/vala-0.40/vapi/gsl.vapi
/usr/share/vala-0.40/vapi/gst-editing-services-1.0.deps
/usr/share/vala-0.40/vapi/gst-editing-services-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-allocators-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-allocators-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-app-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-app-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-app-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-app-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-audio-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-audio-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-audio-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-audio-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-bad-allocators-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-bad-allocators-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-base-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-base-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-base-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-base-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-cdda-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-cdda-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-check-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-check-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-check-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-check-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-controller-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-controller-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-controller-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-controller-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-dataprotocol-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-dataprotocol-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-fft-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-fft-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-fft-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-fft-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-interfaces-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-interfaces-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-net-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-net-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-net-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-net-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-netbuffer-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-netbuffer-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-pbutils-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-pbutils-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-pbutils-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-pbutils-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-player-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-player-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-riff-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-riff-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-riff-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-riff-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-rtp-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-rtp-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-rtp-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-rtp-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-rtsp-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-rtsp-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-rtsp-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-rtsp-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-rtsp-server-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-rtsp-server-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-sdp-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-sdp-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-sdp-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-sdp-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-tag-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-tag-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-tag-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-tag-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-video-0.10.deps
/usr/share/vala-0.40/vapi/gstreamer-video-0.10.vapi
/usr/share/vala-0.40/vapi/gstreamer-video-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-video-1.0.vapi
/usr/share/vala-0.40/vapi/gstreamer-webrtc-1.0.deps
/usr/share/vala-0.40/vapi/gstreamer-webrtc-1.0.vapi
/usr/share/vala-0.40/vapi/gtk+-2.0.deps
/usr/share/vala-0.40/vapi/gtk+-2.0.vapi
/usr/share/vala-0.40/vapi/gtk+-3.0.deps
/usr/share/vala-0.40/vapi/gtk+-3.0.vapi
/usr/share/vala-0.40/vapi/gtk+-4.0.deps
/usr/share/vala-0.40/vapi/gtk+-4.0.vapi
/usr/share/vala-0.40/vapi/gtk+-unix-print-2.0.deps
/usr/share/vala-0.40/vapi/gtk+-unix-print-2.0.vapi
/usr/share/vala-0.40/vapi/gtk+-unix-print-3.0.deps
/usr/share/vala-0.40/vapi/gtk+-unix-print-3.0.vapi
/usr/share/vala-0.40/vapi/gtk+-unix-print-4.0.deps
/usr/share/vala-0.40/vapi/gtk+-unix-print-4.0.vapi
/usr/share/vala-0.40/vapi/gtkmozembed.deps
/usr/share/vala-0.40/vapi/gtkmozembed.vapi
/usr/share/vala-0.40/vapi/gtksourceview-2.0.deps
/usr/share/vala-0.40/vapi/gtksourceview-2.0.vapi
/usr/share/vala-0.40/vapi/gudev-1.0.deps
/usr/share/vala-0.40/vapi/gudev-1.0.vapi
/usr/share/vala-0.40/vapi/hal.deps
/usr/share/vala-0.40/vapi/hal.vapi
/usr/share/vala-0.40/vapi/hildon-1.deps
/usr/share/vala-0.40/vapi/hildon-1.vapi
/usr/share/vala-0.40/vapi/hildon-fm-2.deps
/usr/share/vala-0.40/vapi/hildon-fm-2.vapi
/usr/share/vala-0.40/vapi/javascriptcoregtk-4.0.vapi
/usr/share/vala-0.40/vapi/json-glib-1.0.deps
/usr/share/vala-0.40/vapi/json-glib-1.0.vapi
/usr/share/vala-0.40/vapi/libarchive.deps
/usr/share/vala-0.40/vapi/libarchive.vapi
/usr/share/vala-0.40/vapi/libbonoboui-2.0.vapi
/usr/share/vala-0.40/vapi/libdaemon.vapi
/usr/share/vala-0.40/vapi/libepc-1.0.vapi
/usr/share/vala-0.40/vapi/libesmtp.vapi
/usr/share/vala-0.40/vapi/libftdi.deps
/usr/share/vala-0.40/vapi/libftdi.vapi
/usr/share/vala-0.40/vapi/libgda-4.0.deps
/usr/share/vala-0.40/vapi/libgda-4.0.vapi
/usr/share/vala-0.40/vapi/libgda-report-4.0.deps
/usr/share/vala-0.40/vapi/libgda-report-4.0.vapi
/usr/share/vala-0.40/vapi/libgeoclue-2.0.deps
/usr/share/vala-0.40/vapi/libgeoclue-2.0.vapi
/usr/share/vala-0.40/vapi/libglade-2.0.deps
/usr/share/vala-0.40/vapi/libglade-2.0.vapi
/usr/share/vala-0.40/vapi/libgnome-2.0.vapi
/usr/share/vala-0.40/vapi/libgnome-menu-3.0.deps
/usr/share/vala-0.40/vapi/libgnome-menu-3.0.vapi
/usr/share/vala-0.40/vapi/libgnome-menu.vapi
/usr/share/vala-0.40/vapi/libgnomeui-2.0.deps
/usr/share/vala-0.40/vapi/libgnomeui-2.0.vapi
/usr/share/vala-0.40/vapi/libgrss.deps
/usr/share/vala-0.40/vapi/libgrss.vapi
/usr/share/vala-0.40/vapi/libgsf-1.deps
/usr/share/vala-0.40/vapi/libgsf-1.vapi
/usr/share/vala-0.40/vapi/libgvc.vapi
/usr/share/vala-0.40/vapi/libmagic.vapi
/usr/share/vala-0.40/vapi/libnl-1.vapi
/usr/share/vala-0.40/vapi/libnl-2.0.deps
/usr/share/vala-0.40/vapi/libnl-2.0.vapi
/usr/share/vala-0.40/vapi/libnl-3.0.deps
/usr/share/vala-0.40/vapi/libnl-3.0.vapi
/usr/share/vala-0.40/vapi/libnotify.deps
/usr/share/vala-0.40/vapi/libnotify.vapi
/usr/share/vala-0.40/vapi/liboobs-1.vapi
/usr/share/vala-0.40/vapi/libosso.vapi
/usr/share/vala-0.40/vapi/libpanelapplet-2.0.deps
/usr/share/vala-0.40/vapi/libpanelapplet-2.0.vapi
/usr/share/vala-0.40/vapi/libpeas-1.0.deps
/usr/share/vala-0.40/vapi/libpeas-1.0.vapi
/usr/share/vala-0.40/vapi/libpeas-gtk-1.0.deps
/usr/share/vala-0.40/vapi/libpeas-gtk-1.0.vapi
/usr/share/vala-0.40/vapi/libpq.vapi
/usr/share/vala-0.40/vapi/libsexy.deps
/usr/share/vala-0.40/vapi/libsexy.vapi
/usr/share/vala-0.40/vapi/libsoup-2.2.vapi
/usr/share/vala-0.40/vapi/libsoup-2.4.deps
/usr/share/vala-0.40/vapi/libsoup-2.4.vapi
/usr/share/vala-0.40/vapi/libusb-1.0.deps
/usr/share/vala-0.40/vapi/libusb-1.0.vapi
/usr/share/vala-0.40/vapi/libusb.vapi
/usr/share/vala-0.40/vapi/libwnck-1.0.deps
/usr/share/vala-0.40/vapi/libwnck-1.0.vapi
/usr/share/vala-0.40/vapi/libwnck-3.0.deps
/usr/share/vala-0.40/vapi/libwnck-3.0.vapi
/usr/share/vala-0.40/vapi/libxml-2.0.vapi
/usr/share/vala-0.40/vapi/linux.deps
/usr/share/vala-0.40/vapi/linux.vapi
/usr/share/vala-0.40/vapi/loudmouth-1.0.vapi
/usr/share/vala-0.40/vapi/lua.vapi
/usr/share/vala-0.40/vapi/mx-1.0.deps
/usr/share/vala-0.40/vapi/mx-1.0.vapi
/usr/share/vala-0.40/vapi/mysql.vapi
/usr/share/vala-0.40/vapi/orc-0.4.vapi
/usr/share/vala-0.40/vapi/packagekit-glib2.deps
/usr/share/vala-0.40/vapi/packagekit-glib2.vapi
/usr/share/vala-0.40/vapi/pango.deps
/usr/share/vala-0.40/vapi/pango.vapi
/usr/share/vala-0.40/vapi/pangocairo.deps
/usr/share/vala-0.40/vapi/pangocairo.vapi
/usr/share/vala-0.40/vapi/pixman-1.vapi
/usr/share/vala-0.40/vapi/polkit-agent-1.deps
/usr/share/vala-0.40/vapi/polkit-agent-1.vapi
/usr/share/vala-0.40/vapi/polkit-gobject-1.deps
/usr/share/vala-0.40/vapi/polkit-gobject-1.vapi
/usr/share/vala-0.40/vapi/poppler-glib.deps
/usr/share/vala-0.40/vapi/poppler-glib.vapi
/usr/share/vala-0.40/vapi/posix.vapi
/usr/share/vala-0.40/vapi/purple.deps
/usr/share/vala-0.40/vapi/purple.vapi
/usr/share/vala-0.40/vapi/raptor.vapi
/usr/share/vala-0.40/vapi/rasqal.deps
/usr/share/vala-0.40/vapi/rasqal.vapi
/usr/share/vala-0.40/vapi/readline.vapi
/usr/share/vala-0.40/vapi/rest-0.6.deps
/usr/share/vala-0.40/vapi/rest-0.6.vapi
/usr/share/vala-0.40/vapi/rest-0.7.deps
/usr/share/vala-0.40/vapi/rest-0.7.vapi
/usr/share/vala-0.40/vapi/rest-extras-0.6.deps
/usr/share/vala-0.40/vapi/rest-extras-0.6.vapi
/usr/share/vala-0.40/vapi/rest-extras-0.7.deps
/usr/share/vala-0.40/vapi/rest-extras-0.7.vapi
/usr/share/vala-0.40/vapi/sdl-gfx.deps
/usr/share/vala-0.40/vapi/sdl-gfx.vapi
/usr/share/vala-0.40/vapi/sdl-image.deps
/usr/share/vala-0.40/vapi/sdl-image.vapi
/usr/share/vala-0.40/vapi/sdl-mixer.deps
/usr/share/vala-0.40/vapi/sdl-mixer.vapi
/usr/share/vala-0.40/vapi/sdl-net.deps
/usr/share/vala-0.40/vapi/sdl-net.vapi
/usr/share/vala-0.40/vapi/sdl-ttf.deps
/usr/share/vala-0.40/vapi/sdl-ttf.vapi
/usr/share/vala-0.40/vapi/sdl.vapi
/usr/share/vala-0.40/vapi/sqlite3.vapi
/usr/share/vala-0.40/vapi/taglib_c.vapi
/usr/share/vala-0.40/vapi/tiff.vapi
/usr/share/vala-0.40/vapi/tokyocabinet.vapi
/usr/share/vala-0.40/vapi/tracker-indexer-module-1.0.vapi
/usr/share/vala-0.40/vapi/twitter-glib-1.0.deps
/usr/share/vala-0.40/vapi/twitter-glib-1.0.vapi
/usr/share/vala-0.40/vapi/udisks2.deps
/usr/share/vala-0.40/vapi/udisks2.vapi
/usr/share/vala-0.40/vapi/unique-1.0.deps
/usr/share/vala-0.40/vapi/unique-1.0.vapi
/usr/share/vala-0.40/vapi/v4l2.vapi
/usr/share/vala-0.40/vapi/vte-2.90.deps
/usr/share/vala-0.40/vapi/vte-2.90.vapi
/usr/share/vala-0.40/vapi/vte.deps
/usr/share/vala-0.40/vapi/vte.vapi
/usr/share/vala-0.40/vapi/webkit-1.0.deps
/usr/share/vala-0.40/vapi/webkit-1.0.vapi
/usr/share/vala-0.40/vapi/webkit2gtk-4.0.deps
/usr/share/vala-0.40/vapi/webkit2gtk-4.0.vapi
/usr/share/vala-0.40/vapi/webkit2gtk-web-extension-4.0.deps
/usr/share/vala-0.40/vapi/webkit2gtk-web-extension-4.0.vapi
/usr/share/vala-0.40/vapi/x11.vapi
/usr/share/vala-0.40/vapi/xcb-icccm.vapi
/usr/share/vala-0.40/vapi/xcb.vapi
/usr/share/vala-0.40/vapi/xtst.deps
/usr/share/vala-0.40/vapi/xtst.vapi
/usr/share/vala-0.40/vapi/zlib.vapi
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.40.vapi
/usr/share/vala/vapi/valadoc-0.40.deps
/usr/share/vala/vapi/valadoc-0.40.vapi
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
/usr/include/vala-0.40/vala.h
/usr/include/vala-0.40/valagee.h
/usr/include/valadoc-0.40/valadoc.h
/usr/lib64/libvala-0.40.so
/usr/lib64/libvaladoc-0.40.so
/usr/lib64/pkgconfig/libvala-0.40.pc
/usr/lib64/pkgconfig/valadoc-0.40.pc
/usr/lib64/pkgconfig/vapigen-0.40.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvala-0.40.so.0
/usr/lib64/libvala-0.40.so.0.0.0
/usr/lib64/libvaladoc-0.40.so.0
/usr/lib64/libvaladoc-0.40.so.0.0.0
/usr/lib64/vala-0.40/libvalaccodegen.so
/usr/lib64/valadoc/doclets/devhelp/libdoclet.so
/usr/lib64/valadoc/doclets/gtkdoc/libdoclet.so
/usr/lib64/valadoc/doclets/html/libdoclet.so

%files license
%defattr(-,root,root,-)
/usr/share/doc/vala/COPYING

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/vala-gen-introspect-0.40.1
/usr/share/man/man1/vala-gen-introspect.1
/usr/share/man/man1/valac-0.40.1
/usr/share/man/man1/valac.1
/usr/share/man/man1/valadoc-0.40.1
/usr/share/man/man1/valadoc.1
/usr/share/man/man1/vapigen-0.40.1
/usr/share/man/man1/vapigen.1
