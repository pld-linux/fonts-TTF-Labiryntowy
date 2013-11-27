Summary:	Labyrinth alphabet font
Summary(pl.UTF-8):	Font alfabetu labiryntowego
Name:		fonts-TTF-Labiryntowy
Version:	1.52
Release:	1
License:	freeware
Group:		Fonts
Source0:	https://github.com/texrg/Labiryntowy/raw/master/Labiryntowy_pl.ttf
# Source0-md5:	88c4e403cb75603a8fb2cf8ad8bc21fd
Source1:	https://github.com/texrg/Labiryntowy/blob/master/opis.pdf
# Source1-md5:
URL:		https://github.com/texrg/Labiryntowy
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/TTF
Requires:	fontconfig >= 1:2.10.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ttffontsdir	%{_fontsdir}/TTF

%description
Font Labiryntowy was created as a practical realization of the
labyrinth alphabet idea. This font contains over 300 ligatures and
most of the characters needed to write the titles, names and
monograms.

%description -l pl.UTF-8
Font Labiryntowy_pl powstał jako praktyczna realizacja idei alfabetu
labiryntowego. Font ten zawiera ponad 300 ligatur i większość znaków
potrzebnych do wykonania tytułów, imion i monogramów.

%prep
%setup -q -c -T

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_ttffontsdir}

cp -p %{SOURCE0} $RPM_BUILD_ROOT%{_ttffontsdir}
cp -p %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst TTF

%postun
fontpostinst TTF

%files
%defattr(644,root,root,755)
%doc opis.pdf
%{_ttffontsdir}/Labiryntowy_pl.ttf
