#language: pt

Funcionalidade: Delete Domain
  As an common user
  I want to access the site
  So that I can see the admin page

  Cenario: Cadastrar admin
    Dado que eu esteja na pagina de cadastro
    E preencha o campo username com "Wiski"
    E preencha o campo firstname com "Maria"
    E preencha o campo Company/Dept. Name com "Mickey Mouse Corporation S.A"
    E preencha o campo Password com "123456"
    E preencha o campo Confirma Password com "123456"
    E preencha o campo Data de Admissão com "2019-06-26"
    E preencha o campo Email ID com "mickey@mail.com"
    E preencha o campo Country com "Brazil"
    E preencha o campo Area de Interesse com "Tester"
    Quando clicar no botão Salvar
    Entao mensagem de sucesso é apresentada
