Summary:	mops - free 3D modeling environment for the RenderMan Interface
Summary(pl):	mops - darmowe ¶rodowisko modelowania 3D do interfejsu RenderMan
Name:		mops
Version:	0.42
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://www.ebusinessrevolution.com/mops/%{name}-%{version}d-src.tar.gz
URL:		http://www.ebusinessrevolution.com/mops/
BuildRequires:	Togl-devel >= 1.5
BuildRequires:	BMRT >= 2.5
#Requires:
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
The Mops is a free 3D modeling environment for the RenderMan
Interface.

%description -l pl
Mops jest darmowym ¶rodowiskiem modelowanie 3D do interfejsu
RenderMan.

%prep
%setup -q -n %{name}
#%patch

%build
#./configure --prefix=%{_prefix}
cd src; mv -f Makefile.shared Makefile
%{__make} \
    CC="%{__cc}" \
    CFLAGS="%{rpmcflags} -DMOPSHAVETEMPNAM"\
    BINDIR=%{_bindir}\
    DOCDIR=%{_docdir}\
    LIBDIR=%{_libdir}\
    TOGLINCDIR=%{_includedir}\
    TOGLOBJECT=%{_libdir}\
    TCLINCDIR=%{_includedir}\
    TKINCDIR=%{_includedir}\
    TKLIB=%{_libdir}\
    TCLLIB=%{_libdir}\
    RIINCDIR=%{_includedir} \
    RIBUOTLIB=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
