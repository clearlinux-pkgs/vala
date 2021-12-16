#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : vala
Version  : 0.54.5
Release  : 60
URL      : https://download.gnome.org/sources/vala/0.54/vala-0.54.5.tar.xz
Source0  : https://download.gnome.org/sources/vala/0.54/vala-0.54.5.tar.xz
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
%setup -q -n vala-0.54.5
cd %{_builddir}/vala-0.54.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1639687216
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
export SOURCE_DATE_EPOCH=1639687216
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/vala
cp %{_builddir}/vala-0.54.5/COPYING %{buildroot}/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/vala-0.54/gen-introspect-0.54

%files bin
%defattr(-,root,root,-)
/usr/bin/vala
/usr/bin/vala-0.54
/usr/bin/vala-gen-introspect
/usr/bin/vala-gen-introspect-0.54
/usr/bin/valac
/usr/bin/valac-0.54
/usr/bin/valadoc
/usr/bin/valadoc-0.54
/usr/bin/vapigen
/usr/bin/vapigen-0.54

%files data
%defattr(-,root,root,-)
/usr/share/devhelp/books/vala-0.54/Attributes.html
/usr/share/devhelp/books/vala-0.54/Classes.html
/usr/share/devhelp/books/vala-0.54/Concepts.html
/usr/share/devhelp/books/vala-0.54/Delegates.html
/usr/share/devhelp/books/vala-0.54/Enumerated_types__Enums_.html
/usr/share/devhelp/books/vala-0.54/Errors.html
/usr/share/devhelp/books/vala-0.54/Expressions.html
/usr/share/devhelp/books/vala-0.54/GIDL_metadata_format.html
/usr/share/devhelp/books/vala-0.54/GIR_metadata_format.html
/usr/share/devhelp/books/vala-0.54/Generics.html
/usr/share/devhelp/books/vala-0.54/Interfaces.html
/usr/share/devhelp/books/vala-0.54/Methods.html
/usr/share/devhelp/books/vala-0.54/Namespaces.html
/usr/share/devhelp/books/vala-0.54/Overview.html
/usr/share/devhelp/books/vala-0.54/Preprocessor.html
/usr/share/devhelp/books/vala-0.54/Statements.html
/usr/share/devhelp/books/vala-0.54/Structs.html
/usr/share/devhelp/books/vala-0.54/Types.html
/usr/share/devhelp/books/vala-0.54/default.css
/usr/share/devhelp/books/vala-0.54/index.html
/usr/share/devhelp/books/vala-0.54/vala-0.54.devhelp2
/usr/share/vala-0.54/vapi/SDL2_gfx.deps
/usr/share/vala-0.54/vapi/SDL2_gfx.vapi
/usr/share/vala-0.54/vapi/SDL2_image.deps
/usr/share/vala-0.54/vapi/SDL2_image.vapi
/usr/share/vala-0.54/vapi/SDL2_mixer.deps
/usr/share/vala-0.54/vapi/SDL2_mixer.vapi
/usr/share/vala-0.54/vapi/SDL2_net.deps
/usr/share/vala-0.54/vapi/SDL2_net.vapi
/usr/share/vala-0.54/vapi/SDL2_ttf.deps
/usr/share/vala-0.54/vapi/SDL2_ttf.vapi
/usr/share/vala-0.54/vapi/alsa.deps
/usr/share/vala-0.54/vapi/alsa.vapi
/usr/share/vala-0.54/vapi/atk.deps
/usr/share/vala-0.54/vapi/atk.vapi
/usr/share/vala-0.54/vapi/atspi-2.deps
/usr/share/vala-0.54/vapi/atspi-2.vapi
/usr/share/vala-0.54/vapi/avahi-client.vapi
/usr/share/vala-0.54/vapi/avahi-gobject.deps
/usr/share/vala-0.54/vapi/avahi-gobject.vapi
/usr/share/vala-0.54/vapi/bzlib.vapi
/usr/share/vala-0.54/vapi/cairo-gobject.deps
/usr/share/vala-0.54/vapi/cairo-gobject.vapi
/usr/share/vala-0.54/vapi/cairo-xcb.deps
/usr/share/vala-0.54/vapi/cairo-xcb.vapi
/usr/share/vala-0.54/vapi/cairo.vapi
/usr/share/vala-0.54/vapi/ccss-1.vapi
/usr/share/vala-0.54/vapi/clutter-1.0.deps
/usr/share/vala-0.54/vapi/clutter-1.0.vapi
/usr/share/vala-0.54/vapi/clutter-gdk-1.0.deps
/usr/share/vala-0.54/vapi/clutter-gdk-1.0.vapi
/usr/share/vala-0.54/vapi/clutter-gst-2.0.deps
/usr/share/vala-0.54/vapi/clutter-gst-2.0.vapi
/usr/share/vala-0.54/vapi/clutter-gst-3.0.deps
/usr/share/vala-0.54/vapi/clutter-gst-3.0.vapi
/usr/share/vala-0.54/vapi/clutter-gtk-0.10.deps
/usr/share/vala-0.54/vapi/clutter-gtk-0.10.vapi
/usr/share/vala-0.54/vapi/clutter-gtk-1.0.deps
/usr/share/vala-0.54/vapi/clutter-gtk-1.0.vapi
/usr/share/vala-0.54/vapi/clutter-x11-1.0.deps
/usr/share/vala-0.54/vapi/clutter-x11-1.0.vapi
/usr/share/vala-0.54/vapi/cogl-1.0.deps
/usr/share/vala-0.54/vapi/cogl-1.0.vapi
/usr/share/vala-0.54/vapi/cogl-pango-1.0.deps
/usr/share/vala-0.54/vapi/cogl-pango-1.0.vapi
/usr/share/vala-0.54/vapi/curses.vapi
/usr/share/vala-0.54/vapi/dbus-glib-1.vapi
/usr/share/vala-0.54/vapi/enchant-2.vapi
/usr/share/vala-0.54/vapi/enchant.vapi
/usr/share/vala-0.54/vapi/fuse.deps
/usr/share/vala-0.54/vapi/fuse.vapi
/usr/share/vala-0.54/vapi/gconf-2.0.vapi
/usr/share/vala-0.54/vapi/gdesktopenums-3.0.vapi
/usr/share/vala-0.54/vapi/gdk-2.0.deps
/usr/share/vala-0.54/vapi/gdk-2.0.vapi
/usr/share/vala-0.54/vapi/gdk-3.0.deps
/usr/share/vala-0.54/vapi/gdk-3.0.vapi
/usr/share/vala-0.54/vapi/gdk-pixbuf-2.0.deps
/usr/share/vala-0.54/vapi/gdk-pixbuf-2.0.vapi
/usr/share/vala-0.54/vapi/gdk-x11-2.0.deps
/usr/share/vala-0.54/vapi/gdk-x11-2.0.vapi
/usr/share/vala-0.54/vapi/gdk-x11-3.0.deps
/usr/share/vala-0.54/vapi/gdk-x11-3.0.vapi
/usr/share/vala-0.54/vapi/gdl-1.0.deps
/usr/share/vala-0.54/vapi/gdl-1.0.vapi
/usr/share/vala-0.54/vapi/gdl-3.0.deps
/usr/share/vala-0.54/vapi/gdl-3.0.vapi
/usr/share/vala-0.54/vapi/geocode-glib-1.0.deps
/usr/share/vala-0.54/vapi/geocode-glib-1.0.vapi
/usr/share/vala-0.54/vapi/gio-2.0.deps
/usr/share/vala-0.54/vapi/gio-2.0.vapi
/usr/share/vala-0.54/vapi/gio-unix-2.0.deps
/usr/share/vala-0.54/vapi/gio-unix-2.0.vapi
/usr/share/vala-0.54/vapi/gio-windows-2.0.deps
/usr/share/vala-0.54/vapi/gio-windows-2.0.vapi
/usr/share/vala-0.54/vapi/glib-2.0.vapi
/usr/share/vala-0.54/vapi/gmodule-2.0.deps
/usr/share/vala-0.54/vapi/gmodule-2.0.vapi
/usr/share/vala-0.54/vapi/gnet-2.0.deps
/usr/share/vala-0.54/vapi/gnet-2.0.vapi
/usr/share/vala-0.54/vapi/gnome-desktop-2.0.deps
/usr/share/vala-0.54/vapi/gnome-desktop-2.0.vapi
/usr/share/vala-0.54/vapi/gnome-desktop-3.0.deps
/usr/share/vala-0.54/vapi/gnome-desktop-3.0.vapi
/usr/share/vala-0.54/vapi/gnome-vfs-2.0.vapi
/usr/share/vala-0.54/vapi/gnu.deps
/usr/share/vala-0.54/vapi/gnu.vapi
/usr/share/vala-0.54/vapi/gnutls.vapi
/usr/share/vala-0.54/vapi/gobject-2.0.deps
/usr/share/vala-0.54/vapi/gobject-2.0.vapi
/usr/share/vala-0.54/vapi/gobject-introspection-1.0.deps
/usr/share/vala-0.54/vapi/gobject-introspection-1.0.vapi
/usr/share/vala-0.54/vapi/goocanvas-2.0.deps
/usr/share/vala-0.54/vapi/goocanvas-2.0.vapi
/usr/share/vala-0.54/vapi/goocanvas.deps
/usr/share/vala-0.54/vapi/goocanvas.vapi
/usr/share/vala-0.54/vapi/graphene-1.0.deps
/usr/share/vala-0.54/vapi/graphene-1.0.vapi
/usr/share/vala-0.54/vapi/graphene-gobject-1.0.deps
/usr/share/vala-0.54/vapi/graphene-gobject-1.0.vapi
/usr/share/vala-0.54/vapi/gsl.vapi
/usr/share/vala-0.54/vapi/gst-editing-services-1.0.deps
/usr/share/vala-0.54/vapi/gst-editing-services-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-allocators-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-allocators-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-app-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-app-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-audio-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-audio-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-bad-allocators-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-bad-allocators-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-base-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-base-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-check-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-check-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-controller-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-controller-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-fft-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-fft-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-net-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-net-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-pbutils-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-pbutils-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-play-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-play-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-player-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-player-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-riff-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-riff-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-rtp-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-rtp-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-rtsp-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-rtsp-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-rtsp-server-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-rtsp-server-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-sdp-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-sdp-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-tag-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-tag-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-video-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-video-1.0.vapi
/usr/share/vala-0.54/vapi/gstreamer-webrtc-1.0.deps
/usr/share/vala-0.54/vapi/gstreamer-webrtc-1.0.vapi
/usr/share/vala-0.54/vapi/gtk+-2.0.deps
/usr/share/vala-0.54/vapi/gtk+-2.0.vapi
/usr/share/vala-0.54/vapi/gtk+-3.0.deps
/usr/share/vala-0.54/vapi/gtk+-3.0.vapi
/usr/share/vala-0.54/vapi/gtk+-unix-print-2.0.deps
/usr/share/vala-0.54/vapi/gtk+-unix-print-2.0.vapi
/usr/share/vala-0.54/vapi/gtk+-unix-print-3.0.deps
/usr/share/vala-0.54/vapi/gtk+-unix-print-3.0.vapi
/usr/share/vala-0.54/vapi/gtk4-unix-print.deps
/usr/share/vala-0.54/vapi/gtk4-unix-print.vapi
/usr/share/vala-0.54/vapi/gtk4.deps
/usr/share/vala-0.54/vapi/gtk4.vapi
/usr/share/vala-0.54/vapi/gtkmozembed.deps
/usr/share/vala-0.54/vapi/gtkmozembed.vapi
/usr/share/vala-0.54/vapi/gtksourceview-2.0.deps
/usr/share/vala-0.54/vapi/gtksourceview-2.0.vapi
/usr/share/vala-0.54/vapi/gudev-1.0.deps
/usr/share/vala-0.54/vapi/gudev-1.0.vapi
/usr/share/vala-0.54/vapi/hal.deps
/usr/share/vala-0.54/vapi/hal.vapi
/usr/share/vala-0.54/vapi/harfbuzz-gobject.deps
/usr/share/vala-0.54/vapi/harfbuzz-gobject.vapi
/usr/share/vala-0.54/vapi/hildon-1.deps
/usr/share/vala-0.54/vapi/hildon-1.vapi
/usr/share/vala-0.54/vapi/hildon-fm-2.deps
/usr/share/vala-0.54/vapi/hildon-fm-2.vapi
/usr/share/vala-0.54/vapi/javascriptcoregtk-4.0.vapi
/usr/share/vala-0.54/vapi/json-glib-1.0.deps
/usr/share/vala-0.54/vapi/json-glib-1.0.vapi
/usr/share/vala-0.54/vapi/libarchive.deps
/usr/share/vala-0.54/vapi/libarchive.vapi
/usr/share/vala-0.54/vapi/libbonoboui-2.0.vapi
/usr/share/vala-0.54/vapi/libdaemon.vapi
/usr/share/vala-0.54/vapi/libepc-1.0.vapi
/usr/share/vala-0.54/vapi/libesmtp.vapi
/usr/share/vala-0.54/vapi/libftdi.deps
/usr/share/vala-0.54/vapi/libftdi.vapi
/usr/share/vala-0.54/vapi/libgeoclue-2.0.deps
/usr/share/vala-0.54/vapi/libgeoclue-2.0.vapi
/usr/share/vala-0.54/vapi/libglade-2.0.deps
/usr/share/vala-0.54/vapi/libglade-2.0.vapi
/usr/share/vala-0.54/vapi/libgnome-2.0.vapi
/usr/share/vala-0.54/vapi/libgnome-menu-3.0.deps
/usr/share/vala-0.54/vapi/libgnome-menu-3.0.vapi
/usr/share/vala-0.54/vapi/libgnome-menu.vapi
/usr/share/vala-0.54/vapi/libgnomeui-2.0.deps
/usr/share/vala-0.54/vapi/libgnomeui-2.0.vapi
/usr/share/vala-0.54/vapi/libgrss.deps
/usr/share/vala-0.54/vapi/libgrss.vapi
/usr/share/vala-0.54/vapi/libgsf-1.deps
/usr/share/vala-0.54/vapi/libgsf-1.vapi
/usr/share/vala-0.54/vapi/libgvc.vapi
/usr/share/vala-0.54/vapi/libmagic.vapi
/usr/share/vala-0.54/vapi/libnl-1.vapi
/usr/share/vala-0.54/vapi/libnl-2.0.deps
/usr/share/vala-0.54/vapi/libnl-2.0.vapi
/usr/share/vala-0.54/vapi/libnl-3.0.deps
/usr/share/vala-0.54/vapi/libnl-3.0.vapi
/usr/share/vala-0.54/vapi/libnotify.deps
/usr/share/vala-0.54/vapi/libnotify.vapi
/usr/share/vala-0.54/vapi/liboobs-1.vapi
/usr/share/vala-0.54/vapi/libosso.vapi
/usr/share/vala-0.54/vapi/libpanelapplet-2.0.deps
/usr/share/vala-0.54/vapi/libpanelapplet-2.0.vapi
/usr/share/vala-0.54/vapi/libpeas-1.0.deps
/usr/share/vala-0.54/vapi/libpeas-1.0.vapi
/usr/share/vala-0.54/vapi/libpeas-gtk-1.0.deps
/usr/share/vala-0.54/vapi/libpeas-gtk-1.0.vapi
/usr/share/vala-0.54/vapi/libpq.vapi
/usr/share/vala-0.54/vapi/libsexy.deps
/usr/share/vala-0.54/vapi/libsexy.vapi
/usr/share/vala-0.54/vapi/libsoup-2.4.deps
/usr/share/vala-0.54/vapi/libsoup-2.4.vapi
/usr/share/vala-0.54/vapi/libunwind-generic.vapi
/usr/share/vala-0.54/vapi/libusb-1.0.deps
/usr/share/vala-0.54/vapi/libusb-1.0.vapi
/usr/share/vala-0.54/vapi/libusb.vapi
/usr/share/vala-0.54/vapi/libwnck-1.0.deps
/usr/share/vala-0.54/vapi/libwnck-1.0.vapi
/usr/share/vala-0.54/vapi/libwnck-3.0.deps
/usr/share/vala-0.54/vapi/libwnck-3.0.vapi
/usr/share/vala-0.54/vapi/libxml-2.0.vapi
/usr/share/vala-0.54/vapi/linux.deps
/usr/share/vala-0.54/vapi/linux.vapi
/usr/share/vala-0.54/vapi/loudmouth-1.0.vapi
/usr/share/vala-0.54/vapi/lua.vapi
/usr/share/vala-0.54/vapi/mysql.vapi
/usr/share/vala-0.54/vapi/orc-0.4.vapi
/usr/share/vala-0.54/vapi/packagekit-glib2.deps
/usr/share/vala-0.54/vapi/packagekit-glib2.vapi
/usr/share/vala-0.54/vapi/pango.deps
/usr/share/vala-0.54/vapi/pango.vapi
/usr/share/vala-0.54/vapi/pangocairo.deps
/usr/share/vala-0.54/vapi/pangocairo.vapi
/usr/share/vala-0.54/vapi/pixman-1.vapi
/usr/share/vala-0.54/vapi/polkit-agent-1.deps
/usr/share/vala-0.54/vapi/polkit-agent-1.vapi
/usr/share/vala-0.54/vapi/polkit-gobject-1.deps
/usr/share/vala-0.54/vapi/polkit-gobject-1.vapi
/usr/share/vala-0.54/vapi/poppler-glib.deps
/usr/share/vala-0.54/vapi/poppler-glib.vapi
/usr/share/vala-0.54/vapi/posix.vapi
/usr/share/vala-0.54/vapi/purple.deps
/usr/share/vala-0.54/vapi/purple.vapi
/usr/share/vala-0.54/vapi/raptor.vapi
/usr/share/vala-0.54/vapi/rasqal.deps
/usr/share/vala-0.54/vapi/rasqal.vapi
/usr/share/vala-0.54/vapi/readline.vapi
/usr/share/vala-0.54/vapi/rest-0.7.deps
/usr/share/vala-0.54/vapi/rest-0.7.vapi
/usr/share/vala-0.54/vapi/rest-extras-0.7.deps
/usr/share/vala-0.54/vapi/rest-extras-0.7.vapi
/usr/share/vala-0.54/vapi/sdl2-android.deps
/usr/share/vala-0.54/vapi/sdl2-android.vapi
/usr/share/vala-0.54/vapi/sdl2-ios.deps
/usr/share/vala-0.54/vapi/sdl2-ios.vapi
/usr/share/vala-0.54/vapi/sdl2-windows.deps
/usr/share/vala-0.54/vapi/sdl2-windows.vapi
/usr/share/vala-0.54/vapi/sdl2-winrt.deps
/usr/share/vala-0.54/vapi/sdl2-winrt.vapi
/usr/share/vala-0.54/vapi/sdl2.vapi
/usr/share/vala-0.54/vapi/sqlite3.vapi
/usr/share/vala-0.54/vapi/taglib_c.vapi
/usr/share/vala-0.54/vapi/tiff.vapi
/usr/share/vala-0.54/vapi/tokyocabinet.vapi
/usr/share/vala-0.54/vapi/udisks2.deps
/usr/share/vala-0.54/vapi/udisks2.vapi
/usr/share/vala-0.54/vapi/unique-1.0.deps
/usr/share/vala-0.54/vapi/unique-1.0.vapi
/usr/share/vala-0.54/vapi/v4l2.vapi
/usr/share/vala-0.54/vapi/webkit2gtk-4.0.deps
/usr/share/vala-0.54/vapi/webkit2gtk-4.0.vapi
/usr/share/vala-0.54/vapi/webkit2gtk-web-extension-4.0.deps
/usr/share/vala-0.54/vapi/webkit2gtk-web-extension-4.0.vapi
/usr/share/vala-0.54/vapi/x11.vapi
/usr/share/vala-0.54/vapi/xcb-icccm.deps
/usr/share/vala-0.54/vapi/xcb-icccm.vapi
/usr/share/vala-0.54/vapi/xcb.vapi
/usr/share/vala-0.54/vapi/xtst.deps
/usr/share/vala-0.54/vapi/xtst.vapi
/usr/share/vala-0.54/vapi/zlib.vapi
/usr/share/vala/Makefile.vapigen
/usr/share/vala/vapi/libvala-0.54.vapi
/usr/share/vala/vapi/valadoc-0.54.deps
/usr/share/vala/vapi/valadoc-0.54.vapi
/usr/share/valadoc-0.54/icons/abstractclass.svg
/usr/share/valadoc-0.54/icons/abstractmethod.svg
/usr/share/valadoc-0.54/icons/abstractproperty.svg
/usr/share/valadoc-0.54/icons/class.svg
/usr/share/valadoc-0.54/icons/coll_close.svg
/usr/share/valadoc-0.54/icons/coll_open.svg
/usr/share/valadoc-0.54/icons/constant.svg
/usr/share/valadoc-0.54/icons/constructor.svg
/usr/share/valadoc-0.54/icons/delegate.svg
/usr/share/valadoc-0.54/icons/devhelpstyle.css
/usr/share/valadoc-0.54/icons/enum.svg
/usr/share/valadoc-0.54/icons/enumvalue.svg
/usr/share/valadoc-0.54/icons/errorcode.svg
/usr/share/valadoc-0.54/icons/errordomain.svg
/usr/share/valadoc-0.54/icons/field.svg
/usr/share/valadoc-0.54/icons/interface.svg
/usr/share/valadoc-0.54/icons/method.svg
/usr/share/valadoc-0.54/icons/namespace.svg
/usr/share/valadoc-0.54/icons/package.svg
/usr/share/valadoc-0.54/icons/packages.svg
/usr/share/valadoc-0.54/icons/property.svg
/usr/share/valadoc-0.54/icons/scripts.js
/usr/share/valadoc-0.54/icons/signal.svg
/usr/share/valadoc-0.54/icons/staticmethod.svg
/usr/share/valadoc-0.54/icons/struct.svg
/usr/share/valadoc-0.54/icons/style.css
/usr/share/valadoc-0.54/icons/tip.svg
/usr/share/valadoc-0.54/icons/virtualmethod.svg
/usr/share/valadoc-0.54/icons/virtualproperty.svg
/usr/share/valadoc-0.54/icons/warning.svg
/usr/share/valadoc-0.54/icons/wikistyle.css

%files dev
%defattr(-,root,root,-)
/usr/include/vala-0.54/vala.h
/usr/include/vala-0.54/valagee.h
/usr/include/valadoc-0.54/valadoc.h
/usr/lib64/libvala-0.54.so
/usr/lib64/libvaladoc-0.54.so
/usr/lib64/pkgconfig/libvala-0.54.pc
/usr/lib64/pkgconfig/valadoc-0.54.pc
/usr/lib64/pkgconfig/vapigen-0.54.pc
/usr/lib64/pkgconfig/vapigen.pc
/usr/share/aclocal/*.m4

%files lib
%defattr(-,root,root,-)
/usr/lib64/libvala-0.54.so.0
/usr/lib64/libvala-0.54.so.0.0.0
/usr/lib64/libvaladoc-0.54.so.0
/usr/lib64/libvaladoc-0.54.so.0.0.0
/usr/lib64/vala-0.54/libvalaccodegen.so
/usr/lib64/valadoc-0.54/doclets/devhelp/libdoclet.so
/usr/lib64/valadoc-0.54/doclets/gtkdoc/libdoclet.so
/usr/lib64/valadoc-0.54/doclets/html/libdoclet.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/vala/caeb68c46fa36651acf592771d09de7937926bb3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/vala-gen-introspect-0.54.1
/usr/share/man/man1/vala-gen-introspect.1
/usr/share/man/man1/valac-0.54.1
/usr/share/man/man1/valac.1
/usr/share/man/man1/valadoc-0.54.1
/usr/share/man/man1/valadoc.1
/usr/share/man/man1/vapigen-0.54.1
/usr/share/man/man1/vapigen.1
