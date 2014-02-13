%define _enable_debug_packages %{nil}
%define debug_package %{nil}

%define shortversion 1.10

Summary:	Prolog development environment
Name:		ciao
Version:	1.10p8
Release:	5
Url:		http://www.ciaohome.org/
Source0:	http://www.clip.dia.fi.upm.es/~clip/Software/Ciao/ciao-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Other
Patch0:		ciao-makefile-destdir.patch
Patch1:		ciao-dotprofile.patch
BuildRequires:	emacs

%description
Ciao is next generation multi-paradigm programming environment with a
unique set of features:

* Ciao offers a complete Prolog system, supporting ISO-Prolog, but its
  novel modular design allows both restricting and extending the language.
  As a result, it allows working with fully declarative subsets of Prolog
  and also to extend these subsets (or ISO-Prolog) both syntactically and
  semantically. Most importantly, these restrictions and extensions can
  be activated separately on each program module so that several
  extensions can coexist in the same application for different modules.

* Ciao also supports (through such extensions) programming with functions,
  higher-order (with predicate abstractions), constraints, and objects,
  as well as feature terms (records), persistence, several control rules
  (breadth-first search, iterative deepening, ...), concurrency
  (threads/engines), a good base for distributed execution (agents),
  and parallel execution. Libraries also support WWW programming,
  sockets, external interfaces (C, Java, TclTk, relational databases,
  etc.), etc.

* Ciao offers support for programming in the large with a robust
  module/object system, module-based separate/incremental compilation
  (automatically --no need for makefiles), an assertion language for
  declaring (optional) program properties (including types and modes,
  but also determinacy, non-failure, cost, etc.), automatic static
  inference and static/dynamic checking of such assertions, etc.

* Ciao also offers support for programming in the small producing small
  executables (including only those builtins used by the program) and
  support for writing scripts in Prolog.

* The Ciao programming environment includes a classical top-level and a
  rich emacs interface with an embeddable source-level debugger and a 
  number of execution visualization tools.

* The Ciao compiler (which can be run outside the top level shell)
  generates several forms of architecture-independent and stand-alone
  executables, which run with speed, efficiency and executable size
  which are very competitive with other commercial and academic
  Prolog/CLP systems. Library modules can be compiled into compact
  bytecode or C source files, and linked statically, dynamically, or
  autoloaded.

* The novel modular design of Ciao enables, in addition to modular 
  program development, effective global program analysis and static
  debugging and optimization via source to source program transformation.
  These tasks are performed by the Ciao preprocessor (ciaopp, 
  distributed separately).

* The Ciao programming environment also includes lpdoc, an automatic
  documentation generator for LP/CLP programs. It processes Prolog files
  adorned with (Ciao) assertions and machine-readable comments and
  generates manuals in many formats including postscript, pdf, texinfo,
  info, HTML, man, etc. , as well as on-line help, ascii README files,
  entries for indices of manuals (info, WWW, ...), and maintains WWW
  distribution sites.

%files
%doc local_doc/*
%config(noreplace) %{_sysconfdir}/profile.d/ciao.sh
%config(noreplace) %{_sysconfdir}/profile.d/ciao.csh
%{_libdir}/ciao-%{shortversion}/*
%{_libdir}/*.elc
%{_libdir}/*.el
%{_bindir}/*
%{_includedir}/ciao_prolog.h
%{_infodir}/ciao.info*
%{_mandir}/man1/ciao.1*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make CIAOROOT=%{_prefix} LIBDIR=%{_libdir} SRC=`pwd` DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644

%install
make DESTDIR=%{buildroot} CIAOROOT=%{_prefix} LIBDIR=%{_libdir} SRC=`pwd` \
     DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644 install

pushd ciaoc
make DESTDIR=%{buildroot} CIAOROOT=%{_prefix} LIBDIR=%{_libdir} SRC=`pwd`/.. \
     DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644 install
popd

mkdir -p %{buildroot}%{_mandir}/man1 %{buildroot}%{_infodir}

mv %{buildroot}%{_defaultdocdir}/%{name}-%{version}/ciao.info %{buildroot}%{_infodir}
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version}/manl/ciao.l %{buildroot}%{_mandir}/man1/ciao.1

mv %{buildroot}%{_defaultdocdir}/%{name}-%{version} local_doc

mkdir -p %{buildroot}%{_sysconfdir}/profile.d
mv %{buildroot}%{_libdir}/ciao-%{shortversion}/DOTprofile %{buildroot}%{_sysconfdir}/profile.d/ciao.sh
mv %{buildroot}%{_libdir}/ciao-%{shortversion}/DOTcshrc %{buildroot}%{_sysconfdir}/profile.d/ciao.csh
rm %{buildroot}%{_libdir}/DOTprofile %{buildroot}%{_libdir}/DOTcshrc
rm %{buildroot}%{_libdir}/NewUser

