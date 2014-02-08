# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/savesym/savesym.sty
# catalog-date 2007-01-14 15:20:52 +0100
# catalog-license lppl
# catalog-version 1.1
Name:		texlive-savesym
Version:	1.1
Release:	3
Summary:	Redefine symbols where names conflict
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/savesym/savesym.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savesym.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
There are a number of symbols (e.g., \Square) that are defined
by several packages. In order to typeset all the variants in a
document, we have to give the glyph a unique name. To do that,
we define \savesymbol{XXX}, which renames a symbol from \XXX to
\origXXX, and \restoresymbols{yyy}{XXX}, which renames \origXXX
back to \XXX and defines a new command, \yyyXXX, which
corresponds to the most recently loaded version of \XXX.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/savesym/savesym.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1-2
+ Revision: 755794
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.1-1
+ Revision: 719485
- texlive-savesym
- texlive-savesym
- texlive-savesym
- texlive-savesym

