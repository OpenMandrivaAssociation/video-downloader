Name:		video-downloader
Version:	0.12.12
Release:	1
Summary:	Download videos from websites like YouTube and many others
Group:		Multimedia/Internet
License:	GPLv3+
URL:		https://github.com/Unrud/video-downloader
Source0:	https://github.com/Unrud/video-downloader/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:	appstream-util
BuildRequires:  gettext
BuildRequires:	librsvg2
BuildRequires:	meson
BuildRequires:	gtk4
BuildRequires:  pkgconfig(libadwaita-1)
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk4)

Requires:	python-xlib
Requires: gtk4
Requires: hicolor-icon-theme
Requires: %{_lib}adwaita1_0
Requires: librsvg2
Requires: yt-dlp

%description
Download videos from websites with an easy-to-use interface. Provides the
following features:

- Convert videos to MP3
- Supports password-protected and private videos
- Download single videos or whole playlists
- Automatically selects a video format based on your preferred resolution

Based on yt-dlp.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/
%{_datadir}/applications/*.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/icons/hicolor/*/*/*.svg
%{_metainfodir}/*.xml
