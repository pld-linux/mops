Summary:	mops
Summary(pl):	mops
Name:		mops	
Version:	0.42
Release:	1
Copyright:	GPL
Group:		Applications/Graphics
Group(pl):	Aplikacje/Grafika
Source0:	%{name}-%{version}d-src.tar.gz
BuildRequires:	Togl-devel >= 1.5
BuildRequires:	BMRT >= 2.5
#Requires:	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_prefix	/usr/X11R6

%description

%description -l pl

%prep
%setup -q -n %{name}

#%patch

%build
#./configure --prefix=%{_prefix}
cd src;mv Makefile.shared Makefile
%{__make} \
    CC="gcc" \
    CFLAGS="$RPM_OPT_FLAGS -DMOPSHAVETEMPNAM"\
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
##    RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%attr(,,)
