%global tl_name savesym
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Redefine symbols where names conflict
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/savesym/savesym.sty
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/savesym.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
There are a number of symbols (e.g., \Square) that are defined by
several packages. In order to typeset all the variants in a document, we
have to give the glyph a unique name. To do that, we define
\savesymbol{XXX}, which renames a symbol from \XXX to \origXXX, and
\restoresymbols{yyy}{XXX}, which renames \origXXX back to \XXX and
defines a new command, \yyyXXX, which corresponds to the most recently
loaded version of \XXX.

