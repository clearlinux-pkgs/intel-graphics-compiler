#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : intel-graphics-compiler
Version  : 1.0.3041
Release  : 41
URL      : https://github.com/intel/intel-graphics-compiler/archive/igc-1.0.3041.tar.gz
Source0  : https://github.com/intel/intel-graphics-compiler/archive/igc-1.0.3041.tar.gz
Summary  : Intel(R) Graphics Compiler for OpenCL(TM)
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: intel-graphics-compiler-bin = %{version}-%{release}
Requires: intel-graphics-compiler-lib = %{version}-%{release}
Requires: intel-graphics-compiler-license = %{version}-%{release}
Requires: opencl-clang
BuildRequires : bison-dev
BuildRequires : buildreq-cmake
BuildRequires : flex
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : llvm-extras
BuildRequires : nose
BuildRequires : opencl-clang
BuildRequires : opencl-clang-dev
Patch1: warn-as-error-if-evil.patch

%description
IGA - Intel Graphics Assembler
[Build On Windows]
Prerequisite:
Visaul Studio version >= 2012
CMake version >= 2.8

%package bin
Summary: bin components for the intel-graphics-compiler package.
Group: Binaries
Requires: intel-graphics-compiler-license = %{version}-%{release}

%description bin
bin components for the intel-graphics-compiler package.


%package dev
Summary: dev components for the intel-graphics-compiler package.
Group: Development
Requires: intel-graphics-compiler-lib = %{version}-%{release}
Requires: intel-graphics-compiler-bin = %{version}-%{release}
Provides: intel-graphics-compiler-devel = %{version}-%{release}
Requires: intel-graphics-compiler = %{version}-%{release}

%description dev
dev components for the intel-graphics-compiler package.


%package lib
Summary: lib components for the intel-graphics-compiler package.
Group: Libraries
Requires: intel-graphics-compiler-license = %{version}-%{release}

%description lib
lib components for the intel-graphics-compiler package.


%package license
Summary: license components for the intel-graphics-compiler package.
Group: Default

%description license
license components for the intel-graphics-compiler package.


%prep
%setup -q -n intel-graphics-compiler-igc-1.0.3041
cd %{_builddir}/intel-graphics-compiler-igc-1.0.3041
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1576878949
unset LD_AS_NEEDED
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%cmake .. -DIGC_PREFERRED_LLVM_VERSION=9
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1576878949
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/intel-graphics-compiler
cp %{_builddir}/intel-graphics-compiler-igc-1.0.3041/IGC/BiFModule/Implementation/ExternalLibraries/libclc/LICENSE.TXT %{buildroot}/usr/share/package-licenses/intel-graphics-compiler/e92d77d1b61e0abf19a638a33635e8885ba36afd
cp %{_builddir}/intel-graphics-compiler-igc-1.0.3041/LICENSE.md %{buildroot}/usr/share/package-licenses/intel-graphics-compiler/1c5acacbd2594f1ff922d56805c4e2caecfdac08
pushd clr-build
%make_install
popd
## Remove excluded files
rm -f %{buildroot}/usr/lib64/libcommon_clang.so
## install_append content
rm %{buildroot}/usr/include/igc/cif/cif/builtins/*.cpp
rm %{buildroot}/usr/include/igc/cif/cif/builtins/memory/buffer/impl/*.cpp
rm %{buildroot}/usr/include/igc/cif/cif/export/*.cpp
rm %{buildroot}/usr/include/igc/cif/cif/helpers/*.cpp
rm %{buildroot}/usr/include/igc/cif/cif/import/*.cpp
rm %{buildroot}/usr/include/igc/cif/cif/os/*/*.cpp
rm %{buildroot}/usr/include/igc/ocl_igc_interface/impl/*.cpp



## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/GenX_IR
/usr/bin/iga64

%files dev
%defattr(-,root,root,-)
/usr/include/iga/iga.h
/usr/include/iga/iga.hpp
/usr/include/iga/igaEncoderWrapper.hpp
/usr/include/iga/iga_bxml_enums.hpp
/usr/include/iga/iga_bxml_ops.hpp
/usr/include/iga/iga_types_ext.hpp
/usr/include/iga/iga_types_swsb.hpp
/usr/include/iga/igad.h
/usr/include/iga/igax.hpp
/usr/include/iga/kv.h
/usr/include/iga/kv.hpp
/usr/include/igc/cif/CMakeLists.txt
/usr/include/igc/cif/cif/CMakeLists.txt
/usr/include/igc/cif/cif/builtins/builtins_registry.h
/usr/include/igc/cif/cif/builtins/memory/buffer/buffer.h
/usr/include/igc/cif/cif/builtins/memory/buffer/impl/buffer_impl.h
/usr/include/igc/cif/cif/common/cif.h
/usr/include/igc/cif/cif/common/cif_main.h
/usr/include/igc/cif/cif/common/coder.h
/usr/include/igc/cif/cif/common/compatibility.h
/usr/include/igc/cif/cif/common/id.h
/usr/include/igc/cif/cif/common/library_api.h
/usr/include/igc/cif/cif/common/library_handle.h
/usr/include/igc/cif/cif/export/build/binary_version.h
/usr/include/igc/cif/cif/export/cif_impl.h
/usr/include/igc/cif/cif/export/cif_main_impl.h
/usr/include/igc/cif/cif/export/interface_creator.h
/usr/include/igc/cif/cif/export/library_api.h
/usr/include/igc/cif/cif/export/muiltiversion.h
/usr/include/igc/cif/cif/export/pimpl_base.h
/usr/include/igc/cif/cif/export/registry.h
/usr/include/igc/cif/cif/helpers/error.h
/usr/include/igc/cif/cif/helpers/memory.h
/usr/include/igc/cif/cif/import/cif_main.h
/usr/include/igc/cif/cif/import/library_api.h
/usr/include/igc/cif/cif/macros/disable.h
/usr/include/igc/cif/cif/macros/enable.h
/usr/include/igc/cif/cif/os/lin/lin_library_handle.h
/usr/include/igc/cif/cif/os/win/win_library_handle.h
/usr/include/igc/cif/readme.txt
/usr/include/igc/igc.opencl.h
/usr/include/igc/ocl_igc_interface/code_type.h
/usr/include/igc/ocl_igc_interface/fcl_ocl_device_ctx.h
/usr/include/igc/ocl_igc_interface/fcl_ocl_translation_ctx.h
/usr/include/igc/ocl_igc_interface/gt_system_info.h
/usr/include/igc/ocl_igc_interface/igc_features_and_workarounds.h
/usr/include/igc/ocl_igc_interface/igc_ocl_device_ctx.h
/usr/include/igc/ocl_igc_interface/igc_ocl_translation_ctx.h
/usr/include/igc/ocl_igc_interface/impl/fcl_ocl_device_ctx_impl.h
/usr/include/igc/ocl_igc_interface/impl/fcl_ocl_translation_ctx_impl.h
/usr/include/igc/ocl_igc_interface/impl/gt_system_info_impl.h
/usr/include/igc/ocl_igc_interface/impl/igc_features_and_workarounds_impl.h
/usr/include/igc/ocl_igc_interface/impl/igc_ocl_device_ctx_impl.h
/usr/include/igc/ocl_igc_interface/impl/igc_ocl_translation_ctx_impl.h
/usr/include/igc/ocl_igc_interface/impl/ocl_gen_binary_impl.h
/usr/include/igc/ocl_igc_interface/impl/ocl_translation_output_impl.h
/usr/include/igc/ocl_igc_interface/impl/platform_impl.h
/usr/include/igc/ocl_igc_interface/ocl_gen_binary.h
/usr/include/igc/ocl_igc_interface/ocl_translation_output.h
/usr/include/igc/ocl_igc_interface/platform.h
/usr/include/igc/ocl_igc_interface/platform_helper.h
/usr/include/igc/ocl_igc_shared/device_enqueue/DeviceEnqueueInternalTypes.h
/usr/include/igc/ocl_igc_shared/device_enqueue/device_enqueue_internal_types.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_g10.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_g7.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_g75.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_g8.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_g9.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_list.h
/usr/include/igc/ocl_igc_shared/executable_format/patch_shared.h
/usr/include/igc/ocl_igc_shared/executable_format/program_debug_data.h
/usr/include/igc/ocl_igc_shared/gtpin/gtpin_driver_common.h
/usr/include/igc/ocl_igc_shared/gtpin/gtpin_driver_common_bti.h
/usr/include/igc/ocl_igc_shared/gtpin/gtpin_ocl_interface.h
/usr/include/visa/RelocationInfo.h
/usr/lib64/pkgconfig/igc-opencl.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libiga64.so
/usr/lib64/libiga64.so.1
/usr/lib64/libiga64.so.1.0.1
/usr/lib64/libigc.so
/usr/lib64/libigc.so.1
/usr/lib64/libigc.so.1.0.1
/usr/lib64/libigdfcl.so
/usr/lib64/libigdfcl.so.1
/usr/lib64/libigdfcl.so.1.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/intel-graphics-compiler/1c5acacbd2594f1ff922d56805c4e2caecfdac08
/usr/share/package-licenses/intel-graphics-compiler/e92d77d1b61e0abf19a638a33635e8885ba36afd
