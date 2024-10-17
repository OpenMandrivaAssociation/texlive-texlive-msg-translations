Name:		texlive-texlive-msg-translations
Version:	63700
Release:	2
Summary:	translations of the TeX Live installer and TeX Live Manager
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/texlive-msg-translations
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/texlive-msg-translations.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package contains the translated messages of the TeX Live
installer and TeX Live Manager. For information on creating or
updating translations, see
http://tug.org/texlive/doc.html#install-tl-xlate.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
