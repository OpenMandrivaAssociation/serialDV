%define major 1
%define libname %mklibname %{name} %{major}
%define devname %mklibname -d %{name}

Name:           serialDV
Version:        1.1.4
Release:        1%{?dist}
Summary:        Library for audio de-/encoding with ABME3000 based devices
License:        GPL-3.0-only
Group:          Development/Libraries/C and C++
URL:            https://github.com/f4exb/serialDV
#Git-Clone:     https://github.com/f4exb/serialDV.git
Source0:	https://github.com/f4exb/serialDV/archive/v%{version}.tar.gz
BuildRequires:  cmake

%description
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.

%package -n	%{devname}
Summary:        Development files for libserialdv
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.
This subpackage contains libraries and header files for developing
applications that want to make use of libserialdv.

%package -n %{libname}
Summary:        Library for audio de-/encoding with ABME3000 based devices
Group:		System/Libraries

%description -n %{libname}
A library that provides an interface for audio encoding and decoding with
AMBE3000 based devices in packet mode over a serial link.


%package doc
Summary:        Documentation for AMBE3000 based devices

%description doc
Documentation for AMBE3000 based devices

%prep
%autosetup

%build
%cmake
%make_build

%install
%make_install -C build

%files -n %{libname}
%{_libdir}/libserialdv.so.%{major}*

%files -n %{devname}
%license LICENSE
%{_bindir}/dvtest
%{_includedir}/serialdv/
%{_libdir}/libserialdv.so

%files doc
%doc Readme.md
