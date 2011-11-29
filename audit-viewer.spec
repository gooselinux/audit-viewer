Summary: Audit event viewer
Name: audit-viewer
Version: 0.5.1
Release: 3%{?dist}
License: GPLv2
Group: Applications/System
URL: https://fedorahosted.org/audit-viewer/
Source0: https://fedorahosted.org/releases/a/u/audit-viewer/audit-viewer-%{version}.tar.bz2
Patch0: audit-viewer-0.5.1-export.patch
Patch1: audit-viewer-0.5.1-charts.patch
# Upstream changeset 467bd1382d592b29c6e2d20afd91c64ea2a3c81a
Patch2: audit-viewer-0.5.1-date-field.patch
# Upstream changeset 22497aedc623722e09af8687b600d83b5c990a4d
Patch3: audit-viewer-0.5.1-chart-labels.patch
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires: desktop-file-utils, gettext, intltool, python
Requires: audit-libs-python, gnome-python2-gnome, gnome-python2-rsvg
Requires: pygtk2-libglade, pychart, python-gtkextra, python-sexy, usermode
Requires: usermode-gtk

%description
A graphical utility for viewing and summarizing audit events.

%prep
%setup -q
%patch0 -p1 -b .export
%patch1 -p1 -b .charts
%patch2 -p1 -b .date-field
%patch3 -p1 -b .chart-labels

%build
%configure --disable-update-mimedb
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-fedora INSTALL='install -p'

%find_lang audit-viewer

desktop-file-install --vendor=fedora \
	--dir $RPM_BUILD_ROOT/%{_datadir}/applications --delete-original \
	$RPM_BUILD_ROOT/%{_datadir}/applications/audit-viewer.desktop

%post
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :
update-mime-database %{_datadir}/mime &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files -f audit-viewer.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING ChangeLog NEWS README
%{_bindir}/audit-viewer
%{_datadir}/applications/fedora-audit-viewer.desktop
%{_datadir}/audit-viewer
%{_datadir}/mime/packages/audit-viewer.xml
%{_libexecdir}/audit-viewer-server
%{_libexecdir}/audit-viewer-server-real
%{_mandir}/man8/audit-viewer.8*
%config(noreplace) %{_sysconfdir}/pam.d/audit-viewer-server
%config(noreplace) %{_sysconfdir}/security/console.apps/audit-viewer-server

%changelog
* Wed Mar 31 2010 Miloslav Trmač <mitr@redhat.com> - 0.5.1-3
- Fix chart display if any of the labels contain '/'
- Include 'date' among field names for making reports
  Resolves: #578547

* Fri Jan 15 2010 Miloslav Trmač <mitr@redhat.com> - 0.5.1-2
- Fix crash when exporting list view
  Resolves: #555797
- Fix invisible (too small) charts
  Related: #555798

* Thu Oct  1 2009 Miloslav Trmač <mitr@redhat.com> - 0.5.1-1
- Update to audit-viewer-0.5.1.

* Tue Sep 15 2009 Miloslav Trmač <mitr@redhat.com> - 0.5-2
- BuildRequires: intltool

* Tue Sep 15 2009 Miloslav Trmač <mitr@redhat.com> - 0.5-1
- Update to audit-viewer-0.5.
- Preserve timestamps of some installed files.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 01 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4-2
- Rebuild for Python 2.6

* Tue Oct 28 2008 Miloslav Trmač <mitr@redhat.com> - 0.4-1
- Update to audit-viewer-0.4.

* Tue Aug 26 2008 Miloslav Trmač <mitr@redhat.com> - 0.3-2
- s/Requires: gnome-python2/&-gnome/
  Resolves: #460031

* Wed Jun 25 2008 Miloslav Trmač <mitr@redhat.com> - 0.3-1
- Update to audit-viewer-0.3.

* Fri Apr 18 2008 Miloslav Trmač <mitr@redhat.com> - 0.2-2
- Add URL:
- Modify .desktop file installation to conform to guidelines
- Add missing BuildRequires:

* Tue Apr 15 2008 Miloslav Trmač <mitr@redhat.com> - 0.2-1
- Update to audit-viewer-0.2.

* Fri Feb  1 2008 Miloslav Trmač <mitr@redhat.com>
- Initial package.
