# ----------------------------------------------------------------------------------------------------------------
# DESCRIÇÃO DO SISTEMA DE CRIAÇÃO/EDIÇÃO DE REGRAS

## Acessos, Permissões e Funcionalidades
Um usuário (servidor) é criado e alocado a uma equipe, podendo então acessar o sistema.
O usuário pode ver todas as regras de todas as equipes, mas pode editar regras apenas da própria equipe.
Um usuário pode criar uma nova regra, que será automaticamente vinculada (controlada por) à sua equipe.

## Criação de Regra
Um usuário cria uma nova regra, no formato de "tabela" e a salva. 
O usuário pode testar ao mesmo tempo o comportamento da regra colocando exemplos para teste.
Ao clicar em salvar, o sistema deve verificar se a escrita da regra é válida [formato JDM válido] e salvar apenas no caso de validade.
Ao salvar, o sistema deve criar e salvar um novo schema para a regra.
A nova regra deve ser commitada e uma nova versão do projeto deve ser configurada. 

## Edição de Regra
Um usuário acessa uma regra existente e edita os campos no formato de tabela.
O usuário pode testar ao mesmo tempo o comportamento da regra colocando exemplos para teste.
Ao clicar em salvar, o sistema deve verificar se a escrita da regra é válida [formato JDM válido] e salvar apenas no caso de validade.
Ao salvar, o sistema deve sobrescrever o schema existente com a nova versão [de forma que o diff mostre apenas as partes alteradas].
A nova regra deve ser commitada e ------uma nova versão do projeto deve ser configurada-----[?]. 

## Exportação de regras
O usuário pode acessar uma regra e exportá-la em 2 formatos: o formato de tabela ou o formato "escrito" [pdf].

## Funcionalidades de usuário com "papel de" chefia
Criação de cadastro para servidor novo da equipe.
Edição de cadastros.

# ----------------------------------------------------------------------------------------------------------------
# MODELAGEM ER

- Usuários organizados em equipes
- Cada equipe controla um certo conjunto de regras

**ENTIDADES PRINCIPAIS**

    SERVIDOR
        * nome
        * login único
        * senha

    EQUIPE
        * id numérico único
        * sigla única

    REGRA
        * id único
        * nome
        * descrição
        * path [.json]

    RELACIONAMENTOS
        * um servidor está alocado em uma única equipe
        * uma regra é controlada por uma única equipe
        * um servidor edita/cria [trabalha em] diversas regras
        * uma regra pode ser editada por diversos servidores
        * um servidor pode chefiar uma única equipe

    ESQUEMA ER - ENTIDADES PRINCIPAIS
        * !(./ER.png)

**OUTRAS ENTIDADES [AUXILIARES]**

    PACOTE_VERSAO
    _para catálogo de versões_
        * tag (única)
        * git_sha (ponteiro imutável para o commit)
        * descrição da mudança
        * publicada_em, publicada_por

    EVENTO_EDICAO
    _para log/auditoria de modificações_
        * servidor
        * regra alterada
        * timestamp
        * acao executada (criação | edição)
        * descrição da alteração
        * git_sha (ponteiro para o commit)

    RELACIONAMENTOS
        * um servidor publica versões de pacote (1:N)
        * uma versão de pacote altera diversas regras [e uma regra pode ser alterada por diversas versões] (N:N)
        * um servidor realiza eventos de modificação (1:N)
        * um evento de moficação está relacionado a uma regra (1:1)


# ----------------------------------------------------------------------------------------------------------------
# BANCO DE DADOS

Será feito também um banco de dados para gerenciar no sistema: os usuários e seus papeis, os metadados das regras, os logs de auditoria e catálogos de versionamento.

    * Usuários e papéis — servidor, equipe, chefia/membro, autenticação.
    * Metadados das regras — id, nome, descrição, equipe responsável, path do JDM.
    * Auditoria/Log — quem salvou/publicou, quando, em qual commit.
    * Catálogo de versões — tags/releases [PACOTE_VERSAO: tag, identificador git (ponteiro p/ o commmit --> sha), anotações, quem publicou].

O conteúdo executável das regras é os grafos JDM [descritos em arquivos JSON]. Esses grafos serão armazenados fora do banco, permitindo o versionamento nativo do git, que é um dos principais pontos deste projeto e da ferramenta escolhida (GoRules). O banco apenas conterá um catálogo de regras, que aponta para seus respectivos arquivos.


# ----------------------------------------------------------------------------------------------------------------
# APLICAÇÃO DAS REGRAS

O projeto deve fornecer 2 formas de aplicação das regras:
    * aplicação de regra via CLI: instalação do pacote em outro projeto e aplicação das regras via terminal de comando.
    * aplicação de regra via python: instalação do pacote em outro projeto, com funções pré-prontas simplificadas de aplicação das regras.

Os mecanismos de aplicação das regras devem:
    * receber uma base como parâmetro [csv ou excel]
    * receber uma ou mais regras como parâmetro para aplicação
    * [opcional] receber uma versão do projeto para aplicação como parâmetro
    * [?] receber o formato de retorno da base como parâmetro (csv/excel...)
    * retornar a base com as colunas adicionais

Além disso, esses mecanismos devem fornecer funções/expressões adicionais para:
    * indicar todas as regras existentes [nome da regra e descrição]
    * mostrar histórico de versões do "pacote de regras" [tag + descrição da mudança]
    * [?] gerar pdf ou tabela de uma regra escolhida para visualização



