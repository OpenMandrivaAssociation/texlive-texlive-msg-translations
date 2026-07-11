%global tl_name texlive-msg-translations
%global tl_revision 78661

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	translations of the TeX Live installer and TeX Live Manager
Group:		Publishing
URL:		https://www.ctan.org/pkg/texlive-msg-translations
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-msg-translations.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package contains the translated messages of the TeX Live installer
and TeX Live Manager. For information on creating or updating
translations, see https://tug.org/texlive/doc.html#install-tl-xlate.

