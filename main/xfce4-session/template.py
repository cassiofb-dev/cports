pkgname = "xfce4-session"
pkgver = "4.20.2"
pkgrel = 0
build_style = "gnu_configure"
hostmakedepends = [
    "automake",
    "gettext-devel",
    "glib-devel",
    "iceauth",
    "pkgconf",
    "polkit-devel",
    "slibtool",
    "xfce4-dev-tools",
]
makedepends = [
    "glib-devel",
    "gtk+3-devel",
    "gtk-layer-shell-devel",
    "libsm-devel",
    "libwnck-devel",
    "libxfce4ui-devel",
    "libxfce4util-devel",
    "libxfce4windowing-devel",
    "polkit-devel",
    "xfconf-devel",
]
depends = ["iceauth"]
pkgdesc = "Xfce desktop session"
license = "GPL-2.0-or-later"
url = "https://docs.xfce.org/xfce/xfce4-session/start"
source = f"$(XFCE_SITE)/xfce/xfce4-session/{pkgver[:-2]}/xfce4-session-{pkgver}.tar.bz2"
sha256 = "a0b80b7136515bc3c0c54fa859ad420365e29b715b6da0b58a2d2781bfbe73c3"
