Name:		texlive-collection-langcyrillic
Epoch:		1
Version:	69727
Release:	1
Summary:	Cyrillic
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcyrillic.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex
Requires:	texlive-babel-bulgarian
Requires:	texlive-babel-russian
Requires:	texlive-babel-serbian
Requires:	texlive-babel-serbianc
Requires:	texlive-babel-ukraineb
Requires:	texlive-cmcyr
Requires:	texlive-cyrillic
Requires:	texlive-cyrillic-bin
Requires:	texlive-cyrplain
Requires:	texlive-disser
Requires:	texlive-eskd
Requires:	texlive-eskdx
Requires:	texlive-gost
Requires:	texlive-hyphen-belarusian
Requires:	texlive-hyphen-bulgarian
Requires:	texlive-hyphen-mongolian
Requires:	texlive-hyphen-russian
Requires:	texlive-hyphen-serbian
Requires:	texlive-hyphen-ukrainian
Requires:	texlive-lcyw
Requires:	texlive-lh
Requires:	texlive-lhcyr
Requires:	texlive-lshort-bulgarian
Requires:	texlive-lshort-mongol
Requires:	texlive-lshort-russian
Requires:	texlive-lshort-ukr
Requires:	texlive-mongolian-babel
Requires:	texlive-montex
Requires:	texlive-mpman-ru
Requires:	texlive-pst-eucl-translation-bg
Requires:	texlive-ruhyphen
Requires:	texlive-russ
Requires:	texlive-serbian-apostrophe
Requires:	texlive-serbian-date-lat
Requires:	texlive-serbian-def-cyr
Requires:	texlive-serbian-lig
Requires:	texlive-t2
Requires:	texlive-texlive-ru
Requires:	texlive-texlive-sr
Requires:	texlive-ukrhyph

%description
Support for Cyrillic scripts (Bulgarian, Russian, Serbian,
Ukrainian), even if Latin alphabets may also be used.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c

%build

%install
