# GORULES
SITE: https://docs.gorules.io/


## O QUE É OPEN-SOURCE?

- ZEN Engine: É o motor de execução de regras de negócio de alta performance escrito inteiramente em Rust. Ele é responsável por ler, compilar e executar as regras.

- ZEN Expression Language: A linguagem criada por eles para escrever as expressões e condições lógicas.

- JDM (JSON Decision Model): O padrão de arquivo (schema) em formato JSON utilizado para mapear as árvores de decisão, tabelas e fluxos. O formato é aberto, permitindo controle de versão fácil via Git.

- GoRules CLI: Uma interface de linha de comando para validar regras localmente, rodar testes e integrar com esteiras de CI/CD (GitHub Actions, GitLab CI, Azure DevOps). Ele permite rodar testes em lotes de regras e verificar se os arquivos JDM estão válidos antes de subi-los para produção, sendo a base gratuita para integrar o GoRules em esteiras de CI/CD.

- GoRules MCP Server (Model Context Protocol): Uma ferramenta recente que permite integrar o GoRules com agentes de IA locais ou remotos. A IA consegue ler suas políticas, sugerir alterações, rodar testes e explicar como uma decisão foi tomada dentro do seu ambiente de desenvolvimento.

- JDM EDITOR: biblioteca de código (um componente React) [npm install @gorules/jdm-editor] que permite que você pegue toda a interface visual de criação de regras da GoRules e a embale dentro do seu próprio sistema ou portal interno. Você tem as "peças de lego" da tela. Porém, o backend para salvar esses JSONs no banco de dados, o controle de versão (quem editou o quê), os testes em lote, e a tela de login/acessos... tudo isso você que terá que construir.

- STANDALONE EDITOR: aplicação desktop/web autônoma, também construída em cima do JDM Editor, que serve simplesmente como um aplicativo gratuito para abrir, editar visualmente e salvar arquivos .json de decisão. É uma ferramenta de uso isolado (standalone). Você acessa uma página (ou roda ele localmente no seu computador), clica em "Abrir arquivo", seleciona um arquivo .json do seu computador, e a tela visual de edição aparece. [docker run -p 3000:3000 gorules/editor]


## O QUE NÃO É OPEN-SOURCE?

- BRMS: É o produto "pronto para usar". Você já tem um painel web hospedado por eles (ou instalado na sua nuvem) com versionamento, logs, ambiente de homologação/produção e controle de senhas de toda a empresa.