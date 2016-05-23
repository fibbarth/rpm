###########NUNCA GERAR O PACOTE EM PRODUÇÃO OU HOMOLOGAÇÃO###########
###########SOMENTE GERAR PACOTE EM DESENVOLVIMENTO###########
#Dado um número de versão MAJOR.MINOR.PATCH, incremente a:
#versão Maior(MAJOR): quando fizer mudanças incompatíveis na API,
#versão Menor(MINOR): quando adicionar funcionalidades mantendo compatibilidade, e
#versão de Correção(PATCH): quando corrigir falhas mantendo compatibilidade.
#Rótulos adicionais para pré-lançamento(pre-release) e metadados de construção(build) estão disponíveis como extensão ao formato MAJOR.MINOR.PATCH.

#Versão do pacote seguindo as regras acima
%define version 1.2.8
#Release que será liberado o pacote
%define release homologaweb
#Revisão para fazer o export
%define revision HEAD
#nome do pacote é usado para criar o RPM
%define name fiscais
#Resumo do que é o pacote
%define summary Sistema de Fiscais
#Destino final da instalação do pacote
%define dest /website/fiscal
#Branch de onde será feito o export do produto
%define branch http://path/to/branch
#Autor do pacote
%define author 'Felipe Barth'
#Define onde será feita a Build
%define buildroot /home/fbarth/rpm

Name: %{name}
Summary: %{summary} - Revision %{revision}
Vendor: ASAV/GTI
Release: %{release}
License: Proprietary
Group:   Desenvolvimento Web
Version: %{version}
Source: %{_rpmfilename}
BuildArch: noarch
Distribution: Proprietary
Prefix: %{dest}
BuildRoot: %{buildroot}

%description
Pacote %{name} para instalação no ambiente de Homologação
Gerado por %{author}
Branch %{branch} 
Revisão %{revision}
 
%build
rm -rf %{buildroot}/%{dest}
curl "email.php?token=token&email=fibbarth@gmail.com&assunto=Gerado_pacote_em_homologaweb&mensagem=Pacote_Revison_%{revision}_%{version}"

%install
mkdir -p %{buildroot}/%{dest}
svn export %{branch} -r %{revision} --username username --password 0000 --non-interactive --force %{buildroot}/%{dest}
 
%clean
rm -rf %{buildroot}/%{dest}
 
%files
%defattr (-,wwwrun,www)
%attr(0775,wwwrun,www) %{dest}
%config(noreplace) %attr(0775,wwwrun,www) %{dest}/.htaccess
%config(noreplace) %attr(0775,wwwrun,www) %{dest}/inc.config.php

%post 
curl "email.php?token=token&email=fibbarth@gmail.com&assunto=Gerado_pacote_em_homologaweb&mensagem=Pacote_Revison_%{revision}_%{version}"

