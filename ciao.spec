%define shortversion 1.10
%define ciaolibdir %{_libdir}/ciao-%{shortversion}

Name:		ciao
Version:	1.10p8
Release:	%mkrel 4
Source:		http://www.clip.dia.fi.upm.es/~clip/Software/Ciao/ciao-%{version}.tar.gz
URL:		http://www.ciaohome.org/
Summary:	Prolog development environment
License:	GPLv2+
Group:		Development/Other
Patch0:		ciao-makefile-destdir.patch
Patch1:		ciao-dotprofile.patch
BuildRequires:	emacs
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
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

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
make CIAOROOT=%_prefix LIBDIR=%{_libdir} SRC=`pwd` DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644

%install
rm -Rf %{buildroot}
make DESTDIR=%{buildroot} CIAOROOT=%{_prefix} LIBDIR=%{_libdir} SRC=`pwd` \
     DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644 install

pushd ciaoc
make DESTDIR=%{buildroot} CIAOROOT=%{_prefix} LIBDIR=%{_libdir} SRC=`pwd`/.. \
     DOCROOT=%{_defaultdocdir}/%{name}-%{version} EXECMODE=755 DATAMODE=644 install
popd

%{__mkdir_p} %{buildroot}%{_mandir}/man1 %{buildroot}%{_infodir}

mv %{buildroot}%{_defaultdocdir}/%{name}-%{version}/ciao.info %{buildroot}%{_infodir}
mv %{buildroot}%{_defaultdocdir}/%{name}-%{version}/manl/ciao.l %{buildroot}%{_mandir}/man1/ciao.1

mv %{buildroot}%{_defaultdocdir}/%{name}-%{version} local_doc

%{__mkdir_p} %{buildroot}%{_sysconfdir}/profile.d
mv %{buildroot}%{ciaolibdir}/DOTprofile %{buildroot}%{_sysconfdir}/profile.d/ciao.sh
mv %{buildroot}%{ciaolibdir}/DOTcshrc %{buildroot}%{_sysconfdir}/profile.d/ciao.csh
rm %{buildroot}%{_libdir}/DOTprofile %{buildroot}%{_libdir}/DOTcshrc
rm %{buildroot}%{_libdir}/NewUser

%clean
rm -Rf %{buildroot}

%files
%defattr(-,root,root)
%doc local_doc/*
%config(noreplace) %{_sysconfdir}/profile.d/ciao.sh
%config(noreplace) %{_sysconfdir}/profile.d/ciao.csh
%{ciaolibdir}/*
%{_libdir}/*.elc
%{_libdir}/*.el
%{_bindir}/*
%{_includedir}/ciao_prolog.h
%{_infodir}/ciao.info*
%{_mandir}/man1/ciao.1*


%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.10p8-4mdv2011.0
+ Revision: 617037
- the mass rebuild of 2010.0 packages

* Thu Sep 10 2009 Thierry Vignaud <tv@mandriva.org> 1.10p8-3mdv2010.0
+ Revision: 437031
- rebuild

* Mon Mar 16 2009 Nicolas Vigier <nvigier@mandriva.com> 1.10p8-2mdv2009.1
+ Revision: 355716
- install ciaoc

* Tue Feb 24 2009 Nicolas Vigier <nvigier@mandriva.com> 1.10p8-1mdv2009.1
+ Revision: 344509
- import ciao


