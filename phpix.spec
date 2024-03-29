# TODO:
# - make some fine default index.php
# - multiuser configuration??
# - install apache config
#
Summary:	phpix2 - web-based photo album
Summary(pl.UTF-8):	phpix2 - album fotografii na WWW
Name:		phpix
Version:	2.1
Release:	0.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://dl.sourceforge.net/phpix2/%{name}-%{version}.tar.gz
# Source0-md5:	c8b59979a9f90e8edfa7aaecde4d8af1
Source1:	%{name}-apache.conf
URL:		http://phpix2.sourceforge.net/
Requires:	php(exif)
Requires:	webserver
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_phpdir		/usr/share/%{name}
%define		_phpdatadir	/var/lib/%{name}

%description
PHPix2 is a web-based photo album. It generates thumbnails and scales
images automatically, so all you have to do is upload the originals.

%description -l pl.UTF-8
PHPix2 jest opartym na WWW albumem fotografii. Generuje miniaturki i
skaluje rysunki automatycznie, więc wszystko co musisz zrobić to
upload oryginałów.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_phpdir},%{_phpdatadir}/{albums,cache},%{_sysconfdir}/%{name}}

install *.{gif,jpg} $RPM_BUILD_ROOT%{_phpdir}
install view.php $RPM_BUILD_ROOT%{_phpdir}
install common.inc $RPM_BUILD_ROOT%{_phpdir}
install dfl_config.inc $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/config.inc
install dfl_style.css $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/style.css

install convert.sh $RPM_BUILD_ROOT%{_phpdir}/convert

# links for configuration
ln -s %{_sysconfdir}/%{name}/config.inc $RPM_BUILD_ROOT%{_phpdir}/config.inc
ln -s %{_sysconfdir}/%{name}/style.css $RPM_BUILD_ROOT%{_phpdir}/style.css

# links for data:
ln -s %{_phpdatadir}/albums $RPM_BUILD_ROOT%{_phpdir}/albums
ln -s %{_phpdatadir}/cache $RPM_BUILD_ROOT%{_phpdir}/cache

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog HISTORY README TODO
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/config.inc
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/style.css
%dir %{_phpdir}
%attr(755,http,http) %{_phpdir}/convert
%{_phpdir}/albums
%{_phpdir}/cache
%{_phpdir}/*.php
%{_phpdir}/*.css
%{_phpdir}/*.inc
%{_phpdir}/*.gif
%{_phpdir}/*.jpg
%dir %{_phpdatadir}
%attr(750,root,http) %dir %{_phpdatadir}/albums
%attr(750,http,http) %dir %{_phpdatadir}/cache
