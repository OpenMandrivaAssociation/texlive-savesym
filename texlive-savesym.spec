Name:		texlive-savesym
Version:	31565
Release:	2
Summary:	Redefine symbols where names conflict
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/savesym/savesym.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/savesym.r%{version}.tar.xz
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
%autosetup -p1 -c

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
