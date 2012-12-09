# revision 25209
# category Collection
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-collection-langcyrillic
Epoch:		1
Version:	20120224
Release:	1
Summary:	Cyrillic
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/collection-langcyrillic.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires:	texlive-cmcyr
Requires:	texlive-cyrillic
Requires:	texlive-cyrillic-bin
Requires:	texlive-cyrplain
Requires:	texlive-disser
Requires:	texlive-eskd
Requires:	texlive-eskdx
Requires:	texlive-gost
Requires:	texlive-lcyw
Requires:	texlive-lh
Requires:	texlive-lhcyr
Requires:	texlive-ruhyphen
Requires:	texlive-russ
Requires:	texlive-t2
Requires:	texlive-ukrhyph
Requires:	texlive-hyphen-bulgarian
Requires:	texlive-hyphen-russian
Requires:	texlive-hyphen-ukrainian
Requires:	texlive-collection-basic
Requires:	texlive-collection-latex

%description
Support for typesetting Cyrillic.

#-----------------------------------------------------------------------
%files

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install


%changelog
* Fri Feb 24 2012 Paulo Andrade <pcpa@mandriva.com.br> 1:20120224-1
+ Revision: 780343
- Update to latest release.
- Import texlive-collection-langcyrillic
- Import texlive-collection-langcyrillic

