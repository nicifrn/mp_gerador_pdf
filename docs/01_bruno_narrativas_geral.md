# Plano de trabalho – Gerador de folders em PDF para o projeto Narrativas

**Aluno:** Bruno (@brunoo2907) – Técnico Integrado em Informática

**Orientadores:** Prof. Bruno Gomes (@brunogomesifrn) e Entony (@franciscoentony) – NIC/IFRN

**Repositório:** https://github.com/nicifrn/mp_gerador_pdf

**Período:** 16/10/2026 a 10/12/2026 – 8 sprints de 1 semana (de sexta a quinta-feira)

**Projeto pai:** Narrativas – plataforma digital para registro, organização e difusão das narrativas populares do Rio Grande do Norte (resumo em [`docs/projeto_narrativas.md`](projeto_narrativas.md)).

**Trabalho escrito:** TCC no modelo do IFRN, seguindo as normas de [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md).

> **Leia este documento inteiro antes de começar a Sprint 1.** Ele é a referência completa do seu trabalho: tudo o que você vai programar, pesquisar e escrever está aqui, sprint por sprint. As *issues* do GitHub são o resumo de cada semana e sempre apontam para a seção correspondente deste documento. Se uma *issue* e este documento parecerem dizer coisas diferentes, **vale este documento**.

---

## Sumário

- [1. Como usar este documento e o quadro de tarefas](#como-usar)
- [2. A ideia do trabalho](#ideia)
- [3. Decisões já tomadas](#decisoes)
- [4. Cronograma](#cronograma)
- [5. Como trabalhar no repositório (fluxo do NIC)](#fluxo-git)
- [6. A estrutura de pastas que você vai construir](#estrutura)
- [7. Combinados que valem para todas as sprints](#combinados)
- [8. Como escrever o TCC](#escrita-geral)
- [Sprint 1 – Python: primeiros passos](#sprint-1-dev)
- [Sprint 2 – Python: listas, dicionários, funções e arquivos + Git](#sprint-2-dev)
- [Sprint 3 – Ambiente, primeiro PDF, acervo e modelo do folder](#sprint-3-dev)
- [Sprint 4 – Biblioteca 1: FPDF2](#sprint-4-dev)
- [Sprint 5 – Biblioteca 2: ReportLab](#sprint-5-dev)
- [Sprint 6 – Biblioteca 3: xhtml2pdf, e a WeasyPrint](#sprint-6-dev)
- [Sprint 7 – Medições, fidelidade do leiaute e gráficos](#sprint-7-dev)
- [Sprint 8 – Quadro comparativo, recomendação e fechamento](#sprint-8-dev)
- [9. Quadro-resumo](#quadro-resumo)
- [10. Riscos e planos B](#riscos)
- [11. Se sobrar tempo](#extras)
- [12. Referências mínimas do TCC](#referencias-minimas)

---

<a id="como-usar"></a>
## 1. Como usar este documento e o quadro de tarefas

### As *issues* e o quadro (kanban)

Eu cadastrei as suas tarefas como *issues* no repositório. Toda semana tem:

- **uma *issue* com a etiqueta `Desenvolvimento`**: o que você vai programar;
- **uma *issue* com a etiqueta `Escrita`**: o que você vai pesquisar e escrever no TCC. Na Sprint 1 é uma tarefa de preparação (abrir o documento e ler); da Sprint 2 em diante, cada semana tem a entrega de uma parte do TCC.

As *issues* de uma semana estão agrupadas em um **marco** (*milestone*) com o nome e a data da sprint, por exemplo `Sprint 04 – FPDF2 (06/11 a 12/11)`. A página **Milestones** do repositório mostra quanto de cada sprint já foi concluído.

O **quadro do projeto** (aba *Projects* do repositório) tem quatro colunas:

| Coluna | Quando o card fica aqui |
|---|---|
| **A fazer** | a tarefa ainda não começou |
| **Em andamento** | você está trabalhando nela. **Mova o card assim que começar** |
| **Em revisão** | você terminou e avisou os orientadores |
| **Concluído** | os orientadores aprovaram e fecharam a *issue* |

### Como cada sprint está organizada neste documento

Cada sprint tem duas partes, **Desenvolvimento** e **Escrita**, e cada uma tem um endereço próprio (`#sprint-4-dev`, `#sprint-4-escrita`), que é para onde as *issues* apontam.

A parte de desenvolvimento tem sempre quatro blocos:

- **O que você vai entregar**: em uma frase, o que precisa estar funcionando no fim da semana;
- **Passo a passo**: a lista numerada do que fazer, na ordem. Siga na ordem, sem pular;
- **Como saber que deu certo**: o que você deve ver na tela ou no arquivo. Se não vir isso, ainda não terminou;
- **Entrega da sprint**: a lista de conferência que também está na *issue*.

**Neste documento eu não te dou os programas prontos.** Eu te digo o que cada programa precisa fazer, em que ordem, quais funções das bibliotecas usar e onde procurar na documentação. Quem escreve o código é você, e é isso que faz o trabalho ser seu. Os trechos de código que aparecem aqui são **peças** (uma chamada de função, um esqueleto com comentários), não a solução montada.

### Como entregar

**Desenvolvimento:**

1. abra um *pull request* (PR) da sua *branch* para a `develop`, seguindo a [seção 5](#fluxo-git), com `Closes #N` na descrição (N é o número da *issue* da semana);
2. comente na *issue*: `@brunogomesifrn @franciscoentony entrega da Sprint N pronta para revisão – PR #X`;
3. mova o card para **Em revisão**.

Quando um de nós aprovar e fizer o *merge* do PR, a *issue* fecha sozinha e o card vai para **Concluído**. Se pedirmos ajustes no PR, faça os ajustes na mesma *branch* (o PR se atualiza sozinho) e comente de novo.

**Escrita:**

1. escreva no documento do Google Drive (veja a [seção 8](#escrita-geral));
2. nomeie a versão no histórico do Drive (*Arquivo → Histórico de versões → Nomear versão atual*), por exemplo `Entrega 1 – Introdução – 29/10`;
3. comente na *issue*: `@brunogomesifrn @franciscoentony Introdução pronta para revisão – versão "Entrega 1 – Introdução – 29/10"`;
4. mova o card para **Em revisão**.

Nós comentamos no próprio documento do Drive. Quando a seção estiver aprovada, fechamos a *issue*.

### Regras de ouro

- **Entregue no prazo, mesmo incompleto.** Trabalho pela metade dá para revisar; trabalho que não chega, não. Na *issue*, diga o que ficou faltando.
- **Terminou antes? Não comece a próxima sprint.** Use o tempo que sobrou para entender melhor o que fez e para adiantar a escrita.
- **Travou mais de 40 minutos no mesmo erro? Pare e peça ajuda.** Comente na *issue* da semana, marcando nós dois, com: o que você estava tentando fazer, o comando que rodou e **a mensagem de erro inteira, copiada e colada** (não um resumo dela, nem um print cortado). Pedir ajuda depois de 40 minutos não é desistir, é administrar o tempo.

---

<a id="ideia"></a>
## 2. A ideia do trabalho

Os protótipos de tela do portal Narrativas (você tem os prints em `docs/prototipos/`) já preveem dois botões na página de cada narrativa: **"Baixar PDF"** e **"Material Didático"**. A ideia é que qualquer pessoa (um professor, um aluno, um agente cultural) consiga imprimir a narrativa em um **folder** bonito, pronto para levar para a sala de aula.

Só que **ninguém ainda decidiu como esse PDF vai ser gerado**. A plataforma não tem nenhuma biblioteca de PDF escolhida, e existem várias opções em Python, bem diferentes entre si.

A pergunta que o seu trabalho responde é:

> **Qual biblioteca Python é a mais adequada para gerar o folder de narrativas do projeto Narrativas?**

Para responder, você vai desenhar **um modelo de folder** e depois implementar **esse mesmo folder** em **três bibliotecas diferentes**, comparando:

| O que é comparado | Como se mede |
|---|---|
| **Fidelidade ao leiaute** | uma lista de conferência com 10 itens, comparando cada PDF com o modelo desenhado |
| **Tempo de geração** | cronometrar a criação dos folders, repetindo várias vezes |
| **Tamanho do arquivo** | o tamanho em KB de cada PDF gerado |
| **Acentuação** | verificar se "coração", "vovó" e "sertão" saem certos no PDF |
| **Imagens** | verificar se a imagem aparece, no lugar certo e sem deformar |
| **Texto pesquisável** | conseguir usar Ctrl+F no PDF e achar uma palavra (isso importa para a acessibilidade) |
| **Facilidade de instalação** | quantos passos foram necessários e se deu algum erro |
| **Tamanho do código** | quantas linhas de Python foram necessárias para fazer o mesmo folder |

### O que este trabalho **não** é

**Não é "fazer o botão de PDF do site Narrativas".** A plataforma é o **contexto** que justifica a pergunta; o objeto do seu trabalho é a **comparação**. O seu trabalho também **não** altera o código da plataforma: ele acontece todo no seu repositório.

Também **não é** fazer o programa mais bonito possível. Os três programas precisam gerar **o mesmo folder**, para que a comparação seja justa.

Guarde esta frase, porque ela vale para o código e para o texto:

> O seu trabalho **não é** "fiz um programa que gera PDF". O seu trabalho é **"descobri qual biblioteca Python é a mais adequada para gerar o folder do projeto Narrativas, e provei com medições"**.

### O que o seu trabalho tem a favor

1. **Ele produz números.** Fidelidade, tempo, tamanho, acentuação: tudo medido, com tabelas e gráficos.
2. **Ele responde a uma pergunta real e em aberto.** A equipe do Narrativas **ainda não escolheu** biblioteca nenhuma, e a sua recomendação vai orientar a implementação futura.
3. **Ele tem um resultado que quase ninguém publica:** muito provavelmente uma das bibliotecas **não vai poder ser instalada** no ambiente do laboratório. Isso é informação valiosa para quem vai decidir, e é o tipo de coisa que só se descobre tentando.

---

<a id="decisoes"></a>
## 3. Decisões já tomadas

Para você não perder tempo escolhendo ferramenta:

| Item | Decisão |
|---|---|
| Linguagem | **Python 3** |
| Onde você trabalha | **computadores do laboratório (Windows)**. Não é possível instalar programas, mas o `pip install` e o Git funcionam |
| Editor | **VS Code** |
| Banco de dados | **nenhum.** As narrativas ficam em arquivos `.txt` |
| Bibliotecas comparadas | **FPDF2**, **ReportLab** e **xhtml2pdf**, mais a **WeasyPrint**, que é um caso à parte (veja a [Sprint 6](#sprint-6-dev)) |
| Leitura dos PDFs gerados | `pypdf` |
| Gráficos | `matplotlib` |
| Planilhas | módulo `csv`, que já vem com o Python |
| Testes | dois programas de verificação simples, com o comando `assert`, que já vem com o Python ([seção 5.5](#fluxo-git)) |
| Acervo de teste | 10 contos de ***Contos Populares do Brazil***, de **Sílvio Romero** (domínio público) |
| Imagens | Wikimedia Commons, com licença livre, ou fotos/desenhos seus |
| Repositório | `nicifrn/mp_gerador_pdf`, só seu, seguindo a política de desenvolvimento do NIC ([seção 5](#fluxo-git)) |
| Aprendizado de Python | **Curso em Vídeo** (Gustavo Guanabara), aulas selecionadas, nas Sprints 1 e 2 |
| Texto do TCC | **modelo de TCC do IFRN**, em um documento do Google Drive que eu compartilho com você |
| O que **não** entra | Docker, banco de dados, Django, front-end, inteligência artificial. Tudo isso vira "trabalho futuro" no TCC |

### Por que sem banco de dados?

Porque o objeto do trabalho é **gerar o PDF**, e não guardar as narrativas. Colocar um banco no meio acrescentaria semanas de trabalho e complexidade **sem mudar nenhum resultado** da comparação: as três bibliotecas receberiam exatamente os mesmos dados de qualquer forma.

**Isso não é uma falha do trabalho, é uma decisão de método**, e você vai escrevê-la na Metodologia do TCC, com essa justificativa. Na plataforma de verdade os dados virão do banco; aqui eles vêm de arquivos, e para a comparação dá no mesmo.

### Uso de inteligência artificial

- **Pode:** usar uma ferramenta de IA para entender uma mensagem de erro ou um conceito, como faria com um colega.
- **Não pode:** pedir para a IA escrever o código dos geradores ou o texto do TCC. O código e o texto têm de ser seus, e você precisa saber explicar cada linha na apresentação.
- **Nunca:** colocar no TCC uma referência que você não abriu e leu. Ferramentas de IA inventam referências com naturalidade.

---

<a id="cronograma"></a>
## 4. Cronograma

Cada sprint vai de **sexta a quinta-feira**. O prazo de tudo é a **quinta-feira** que fecha a sprint.

| Sprint | Período | Desenvolvimento | Escrita |
|---|---|---|---|
| 1 | 16/10 a 22/10 | Python: primeiros passos | Preparar o documento e ler para a Introdução |
| 2 | 23/10 a 29/10 | Python: listas, dicionários, funções, arquivos + Git | **Entrega 1:** Introdução e Objetivo geral |
| 3 | 30/10 a 05/11 | Ambiente, primeiro PDF, acervo de teste e modelo do folder | **Entrega 2:** Referencial – parte cultural e acessibilidade (2.1, 2.2, 2.5) |
| 4 | 06/11 a 12/11 | Biblioteca 1: FPDF2 | **Entrega 3:** Referencial – parte técnica e trabalhos relacionados (2.3, 2.4, 2.6) |
| 5 | 13/11 a 19/11 | Biblioteca 2: ReportLab | **Entrega 4:** Metodologia (3.1 a 3.5) |
| 6 | 20/11 a 26/11 | Biblioteca 3: xhtml2pdf + WeasyPrint | **Entrega 5:** Materiais e métodos (3.6) |
| 7 | 27/11 a 03/12 | Medições, fidelidade do leiaute e gráficos | **Entrega 6:** Resultados e discussão (4.1 a 4.5 e 4.7) |
| 8 | 04/12 a 10/12 | Quadro comparativo, recomendação e fechamento | **Entrega 7:** quadro e recomendação (4.6), Conclusão, Objetivos específicos, Resumo, *Abstract* e Título |

As duas primeiras semanas são só para **aprender Python** (e Git, no fim da Sprint 2). Da Sprint 3 em diante você trabalha no projeto, e **tudo termina em 10/12**.

**Feriados:** 02/11 (segunda, Sprint 3) e 20/11 (sexta, primeiro dia da Sprint 6). Nenhum prazo cai em feriado, mas nessas duas semanas o laboratório fica fechado um dia: **a semana tem um dia útil a menos**, então comece cedo.

**Três avisos sobre o cronograma:**

1. **A Sprint 3 é a mais cheia do desenvolvimento**, porque junta a preparação do ambiente com o acervo de teste. Comece pelas narrativas no primeiro dia e siga a ordem indicada nela.
2. **Os Resultados vencem em 03/12, na mesma semana das medições.** Por isso a Sprint 7 manda rodar as medições **até segunda-feira, 30/11**: a terça, a quarta e a quinta ficam para montar as tabelas e escrever. Quem deixa os Resultados para o fim não entrega.
3. **A última semana é cheia.** A Conclusão precisa estar escrita até **segunda-feira, 07/12**, para sobrar a terça, a quarta e a quinta para o Resumo, o *Abstract*, o Título e a revisão final.

**Uma vantagem do seu cronograma:** a parte técnica do Referencial (o formato PDF e a codificação de caracteres) vence no fim da Sprint 4, justamente quando você vai brigar com fontes e acentuação na FPDF2. Escreva essa parte **na mesma semana** em que estiver vivendo esse problema: sai muito mais fácil, e o texto fica muito melhor.

---

<a id="fluxo-git"></a>
## 5. Como trabalhar no repositório (fluxo do NIC)

O NIC tem uma política de desenvolvimento que vale para todos os projetos. Abaixo está o que ela significa no seu trabalho.

### 5.1 As *branches*

| *Branch* | Para que serve | Quem mexe |
|---|---|---|
| `main` | versão estável e aprovada | só os orientadores, no fim do trabalho |
| `develop` | onde as sprints aprovadas vão se juntando. É a *branch* padrão do repositório | ninguém envia direto: só entra por PR aprovado |
| `feature/...` | uma por sprint, onde você trabalha | você |

Nome das *branches* das sprints: `feature/` seguido do assunto, em minúsculas, sem acento e com hífen. Os nomes já estão definidos em cada sprint (por exemplo, `feature/gerador-fpdf2`). Se precisar corrigir algo de uma sprint que já foi aprovada, use `fix/` (por exemplo, `fix/acentuacao-reportlab`).

### 5.2 O ciclo de cada sprint

**No começo da sprint** (sexta-feira), crie a *branch* da semana a partir da `develop` atualizada:

```
git checkout develop
git pull
git checkout -b feature/nome-da-sprint
```

**Durante a semana**, envie o trabalho **ao fim de cada dia**. Código que só existe na máquina do laboratório não foi entregue, e a máquina pode ser formatada.

```
git status
git add .
git commit -m "feat: adiciona leitura das narrativas"
git push
```

Na primeira vez que der `git push` em uma *branch* nova, o Git pede `git push -u origin feature/nome-da-sprint`. Use exatamente o comando que ele mostrar.

**Antes do `git add .`, olhe sempre o `git status`.** Se aparecer `.venv/`, `saidas/` ou `__pycache__/`, o seu `.gitignore` está errado: corrija antes de continuar.

**No fim da sprint**, abra o PR (seção 5.4).

### 5.3 Mensagens de *commit*

Os *commits* devem ser **pequenos, objetivos e frequentes**: pelo menos 2 por semana. Use o padrão abaixo, com a mensagem em português e o verbo no presente:

```
feat: adiciona gerador de folder com FPDF2
fix: corrige caminho da imagem no xhtml2pdf
docs: registra instalação das bibliotecas
test: adiciona teste da leitura das narrativas
refactor: separa montagem do rodapé em uma função
```

| Prefixo | Quando usar |
|---|---|
| `feat:` | algo novo funcionando (um gerador, um script, uma narrativa) |
| `fix:` | correção de algo que estava errado |
| `docs:` | documentação, diário, `README.md`, prints |
| `test:` | testes |
| `refactor:` | reorganizar código sem mudar o que ele faz |

**Mensagens proibidas pela política do NIC:** `ajustes`, `mudanças`, `update`, `correções`. Se você não consegue dizer em uma frase o que o *commit* faz, ele está grande demais.

### 5.4 O *pull request* do fim da sprint

1. Confira se tudo foi enviado (`git status` deve dizer `nothing to commit`).
2. Rode as verificações (a partir da Sprint 3; veja a seção 5.5). Elas precisam terminar com a mensagem `Tudo certo`.
3. No GitHub, abra o repositório. Vai aparecer uma faixa amarela com o botão **Compare & pull request**. Se não aparecer: aba **Pull requests → New pull request**, com **base: `develop`** e **compare: a sua *branch***.
4. Preencha a descrição. O repositório já traz um modelo com estes campos, que a política do NIC exige:
   - **Objetivo:** o que esta sprint entrega, em uma ou duas frases;
   - **O que foi feito:** a lista do que foi implementado;
   - **Possíveis impactos:** o que muda para quem roda o projeto (uma biblioteca nova no `requirements.txt`, uma pasta nova);
   - **Evidências de teste:** a saída das verificações (copiada do terminal) e os prints do que foi gerado;
   - **Issue:** `Closes #N`, com o número da *issue* de desenvolvimento da semana.
5. Em **Reviewers**, marque `brunogomesifrn` e `franciscoentony`.
6. Comente na *issue* e mova o card para **Em revisão** (veja a [seção 1](#como-usar)).

**Você não faz o *merge* do seu próprio PR.** A política do NIC exige que pelo menos um revisor aprove antes da integração, e nenhum desenvolvedor aprova sozinho as próprias alterações. **Um PR por sprint**: não acumule duas sprints no mesmo PR.

### 5.5 Testes

A política do NIC pede que toda funcionalidade tenha testes compatíveis com a sua complexidade. No seu trabalho, isso significa **dois programas curtos de verificação**, na pasta `testes/`, que conferem sozinhos se as coisas estão no lugar:

- **`testes/verificar_narrativas.py` (Sprint 3):** confere se as 10 narrativas são lidas com todos os campos;
- **`testes/verificar_pdfs.py` (Sprints 4, 5 e 6):** confere se cada gerador criou os 10 PDFs e se nenhum está vazio.

Os dois usam só um comando do Python, o **`assert`**, que funciona assim:

```python
assert len(narrativas) == 10, "esperava 10 narrativas"
```

Se a condição for **verdadeira**, nada acontece e o programa segue. Se for **falsa**, o programa para na hora e mostra `AssertionError: esperava 10 narrativas`. Ou seja: se o programa chegar até a última linha e mostrar `Tudo certo`, todas as conferências passaram.

Cada sprint diz exatamente o que conferir. Rode sempre a partir da raiz do repositório, com o `.venv` ativo:

```
python testes\verificar_narrativas.py
python testes\verificar_pdfs.py
```

### 5.6 Segurança

Nunca envie para o repositório senhas, *tokens*, chaves ou arquivos `.env`. Neste trabalho você não deve precisar de nenhum deles; se algum dia precisar, comente na *issue* antes de enviar qualquer coisa.

---

<a id="estrutura"></a>
## 6. A estrutura de pastas que você vai construir

Você não precisa criar tudo de uma vez: cada sprint cria a sua parte. Esta é a figura final, para você saber aonde está indo. Tudo fica **na raiz do repositório** `mp_gerador_pdf/`:

```
mp_gerador_pdf/
├── .github/
│   └── pull_request_template.md   ← já existe (modelo do PR)
├── estudos/                  ← exercícios das Sprints 1 e 2
├── narrativas/               ← as narrativas, um arquivo .txt cada (Sprint 3)
│   ├── 01_nome_do_conto.txt
│   └── ...
├── imagens/                  ← as imagens de cada narrativa (Sprint 3)
│   └── creditos.md
├── modelo/                   ← o desenho do folder e a lista de conferência (Sprint 3)
│   ├── modelo_folder.png
│   └── checklist.md
├── geradores/
│   ├── ler_narrativas.py     ← Sprint 3
│   ├── fontes/               ← fontes TrueType (Sprint 4)
│   ├── gerar_fpdf2.py        ← Sprint 4
│   ├── gerar_reportlab.py    ← Sprint 5
│   ├── gerar_xhtml2pdf.py    ← Sprint 6
│   └── modelo_folder.html    ← Sprint 6
├── testes/
│   ├── verificar_narrativas.py  ← Sprint 3
│   └── verificar_pdfs.py        ← Sprints 4 a 6
├── saidas/                   ← os PDFs gerados (NÃO vão para o Git)
├── medir.py                  ← Sprint 7
├── graficos.py               ← Sprint 7
├── resultados/
│   ├── medicoes.csv          ← Sprint 7
│   ├── linhas_de_codigo.csv  ← Sprint 7
│   └── fidelidade.csv        ← Sprint 7
├── docs/
│   ├── 01_bruno_narrativas_geral.md   ← este documento (já existe)
│   ├── projeto_narrativas.md          ← já existe
│   ├── orientacoes_escrita_tcc.md     ← já existe
│   ├── prototipos/                    ← já existe (prints da plataforma)
│   ├── leituras.md           ← o seu fichamento de leituras (Sprint 1 em diante)
│   ├── ambiente.md           ← Sprint 3
│   ├── instalacao.md         ← Sprint 3
│   ├── diario.md             ← Sprint 1 em diante
│   ├── recomendacao.md       ← Sprint 8
│   └── evidencias/           ← prints de tela e gráficos
├── .gitignore
├── requirements.txt
└── README.md
```

---

<a id="combinados"></a>
## 7. Combinados que valem para todas as sprints

- **Diário (`docs/diario.md`):** no fim de cada sprint, escreva 3 linhas: o que funcionou, o que deu errado e o que aprendi. Leva cinco minutos e vai escrever a sua Conclusão por você no fim do trabalho. Use este formato:

  ```
  ## Sprint 4 – 06/11 a 12/11
  - Funcionou: ...
  - Deu errado: ...
  - Aprendi: ...
  ```

- **Anote todo erro que aparecer.** Neste trabalho, **erro é resultado**. Se uma biblioteca engoliu um acento, deformou a imagem ou não instalou, isso vai para uma tabela do TCC. Guarde a mensagem de erro inteira no diário.
- **Prints (`docs/evidencias/`):** sempre que algo funcionar (ou falhar de um jeito interessante), tire um print (`Win + Shift + S` no Windows). Dê nomes que digam o que é: `s04_folder_fpdf2_pagina1.png`. Eles viram figuras do TCC.
- **Anote o tempo.** Ao escrever cada gerador, anote no diário quantas horas você levou. Isso é um dado de "esforço de implementação".
- **Acompanhamento semanal:** no começo de cada sprint, você mostra aos orientadores o que fez na anterior, **rodando na tela**. A partir da Sprint 7, "está funcionando" não basta: tem que ter número.

---

<a id="escrita-geral"></a>
## 8. Como escrever o TCC

### 8.1 Onde escrever: o documento compartilhado no Google Drive

Na Sprint 1 eu compartilho com você um documento do Google Drive que **já está no modelo de TCC do IFRN** (capa, folha de rosto, resumo, sumário e as seções). Você não cria arquivo novo nem trabalha em cópia local.

- **Escreva sempre no documento compartilhado.** Nada de escrever no Word e colar depois: o histórico do Drive é o que nos permite ver o que mudou de uma semana para outra.
- **Não crie cópias** ("TCC v2", "TCC final", "TCC final revisado"). É a forma mais rápida de perder trabalho. O Drive já guarda tudo em **Arquivo → Histórico de versões**.
- **Marque cada entrega no histórico:** *Arquivo → Histórico de versões → Nomear versão atual*, com um rótulo como `Entrega 1 – Introdução – 29/10`.
- **Avise na *issue* quando entregar**, como explicado na [seção 1](#como-usar). Nós não ficamos olhando o documento: precisamos saber que há algo novo para ler.
- **Comentário se responde, não se apaga.** Responda a cada comentário dizendo o que você fez e só então marque como resolvido.
- **Resolva todos os comentários da entrega anterior antes de avisar sobre a próxima.**
- **Figuras e tabelas** vão dentro do documento, no lugar certo, com a identificação em cima e a fonte embaixo. Não mande imagem em anexo separado.
- **Não dê acesso ao documento a outras pessoas.**

### 8.2 As normas

Todas as regras de escrita e de ABNT estão em [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md): estrutura, citações, referências, figuras, tabelas, formatação, linguagem. **Leia esse arquivo inteiro na Sprint 1.** Este plano não repete as regras da ABNT; ele diz **o que pesquisar e o que escrever** em cada seção do seu trabalho.

> **Importante:** o que está neste plano são **orientações**, não o texto pronto. Não copie estas frases para o TCC. Elas dizem sobre o que é cada parágrafo; o texto tem de ser escrito por você, com as suas palavras e com as referências que você leu.

### 8.3 A estrutura do seu TCC

```
1 INTRODUÇÃO
1.1 Objetivo geral
1.2 Objetivos específicos
2 REFERENCIAL TEÓRICO
2.1 Narrativas populares e patrimônio cultural imaterial
2.2 Material didático impresso e difusão cultural
2.3 O formato PDF e a geração programática de documentos
2.4 Bibliotecas Python para geração de PDF
2.5 Acessibilidade de documentos digitais
2.6 Trabalhos relacionados
3 METODOLOGIA
3.1 Classificação da pesquisa
3.2 Pergunta de pesquisa
3.3 Desenho da comparação
3.4 O acervo de teste e o modelo do folder
3.5 Protocolo de medição
3.6 Materiais e métodos
4 RESULTADOS E DISCUSSÃO
4.1 Os folders gerados
4.2 Fidelidade ao leiaute
4.3 Desempenho e tamanho do arquivo
4.4 Acentuação, imagens e acessibilidade
4.5 Facilidade de instalação e esforço de implementação
4.6 Quadro comparativo e recomendação
4.7 Limitações do trabalho
5 CONCLUSÃO
REFERÊNCIAS
```

Tamanho de referência da parte textual: **de 25 a 35 páginas**, mais ou menos assim: Introdução, 2 a 3; Referencial, 8 a 10; Metodologia com Materiais e métodos, 6 a 8; Resultados, 7 a 10; Conclusão, 2.

### 8.4 Regras que valem para o texto inteiro

- **Toda afirmação técnica precisa de referência.**
- **Não empilhe citações.** Explique com as suas palavras, relacione os autores e amarre ao seu trabalho.
- **Nada de blog, Stack Overflow ou site sem autoria** nas Referências. Você vai usar muito esse tipo de material para resolver problemas de programação (isso é normal e esperado), mas ele não entra na lista de referências.
- **Nunca cite uma referência que você não leu.**
- **Crie a seção "Referências" no primeiro dia** e acrescente cada obra assim que ler. Deixar para o fim garante referência faltando e citação sem fonte.
- O Zotero e o Mendeley (gratuitos, funcionam no navegador) ajudam a montar as referências, mas confira cada entrada com a NBR 6023:2018: esses programas erram com frequência.
- **Meta:** de 15 a 25 referências, bem divididas entre a parte cultural e a parte técnica (lista mínima na [seção 12](#referencias-minimas)).
- **Fichamento:** tudo o que você ler vai para `docs/leituras.md`, no formato abaixo. É ele que transforma leitura em texto:

  ```
  ## BINDA; DA SILVA (2026)
  - Referência completa (ABNT): ...
  - Onde achei: (endereço)
  - Ideia principal, com as minhas palavras: ...
  - Trecho que posso citar (com página): "..." (p. X)
  - Vou usar na seção: 2.1
  ```

---

# Sprint 1 — 16/10 a 22/10/2026

<a id="sprint-1-dev"></a>
## Sprint 1 · Desenvolvimento: Python, primeiros passos

**O que você vai entregar:** o Python e o VS Code funcionando na máquina do laboratório, as aulas 1 a 10 do Mundo 1 do Curso em Vídeo assistidas e 4 exercícios do projeto resolvidos na pasta `estudos/sprint1/`.

Nesta semana e na próxima você **aprende Python**. Os exercícios não são aleatórios: cada um treina uma coisa que você vai usar no gerador de folders. Por isso, além dos exercícios das aulas, você vai fazer os exercícios **do projeto**, descritos abaixo.

### Passo a passo

**1. Confira o Python.** Abra o Prompt de Comando (tecle `Win`, digite `cmd`, Enter) e rode:

```
python --version
pip --version
```

Você deve ver algo como `Python 3.12.x` e uma linha começando com `pip`. Se aparecer "não é reconhecido como um comando interno", tente `py --version`. Se o `py` funcionar, **use `py` no lugar de `python` em todos os comandos deste documento** (por exemplo, `py -m pip install` no lugar de `pip install`). Anote no diário qual dos dois funcionou e a versão.

**2. Prepare o VS Code.**

1. Abra o VS Code e instale a extensão **Python** (da Microsoft): ícone de quadradinhos na barra da esquerda → pesquise "Python" → *Install*. Extensões do VS Code não precisam de permissão de administrador.
2. Crie a pasta `estudos\sprint1` dentro da sua pasta de usuário (por exemplo, `C:\Users\<seu-usuario>\mp_gerador_pdf_estudos\estudos\sprint1`). Na Sprint 2 você vai mover essa pasta para dentro do repositório.
3. No VS Code: *File → Open Folder* → escolha a pasta `mp_gerador_pdf_estudos`.
4. Abra o terminal do VS Code com `` Ctrl + ` `` (a tecla da crase). É nele que você vai rodar os programas: `python estudos\sprint1\ex01_titulo.py`.

> **Salve uma cópia no fim de cada dia** (pendrive ou o seu Google Drive). Nesta semana você ainda não usa o Git, e as máquinas do laboratório podem ser formatadas.

**3. Assista às aulas do Curso em Vídeo – Python 3, Mundo 1:** https://www.cursoemvideo.com/curso/python-3-mundo-1/

| Aula | Assunto | Por que importa no projeto |
|---|---|---|
| 1 e 2 | Seja um programador; para que serve o Python | visão geral |
| 4 | Primeiros comandos | `print` e `input` |
| 6 | Tipos primitivos e saída de dados | texto, números, `f-strings` |
| 7 | Operadores aritméticos | cálculo de tamanhos e médias |
| 8 | Utilizando módulos | `import`: você vai importar as bibliotecas de PDF |
| 9 | Manipulando texto | **a mais importante da semana**: `len`, `split`, `replace`, `upper`, `strip` são usados o tempo todo no gerador |
| 10 | Condições (parte 1) | `if` e `else` |

**Pule** as aulas 3 e 5 (instalação do Python e do PyCharm): o Python já está instalado e você vai usar o VS Code, não o PyCharm. A aula 11 (cores no terminal) é opcional.

Faça os exercícios propostos nas aulas 6, 7, 9 e 10. Salve cada um como `estudos/sprint1/aula09_ex022.py` (o número da aula e o número do exercício).

**4. Faça os exercícios do projeto.** Um arquivo para cada, em `estudos/sprint1/`:

- **`ex01_titulo.py`:** guarde em uma variável o texto `Narrativas do Rio Grande do Norte` e mostre-o na tela três vezes: normal, todo em maiúsculas e centralizado em 60 caracteres. *Pesquise:* os métodos `upper()` e `center()` de *strings* (aula 9).
- **`ex02_texto.py`:** guarde em uma variável um parágrafo de qualquer conto popular (copie de onde quiser) que tenha pelo menos um travessão (`—`) e umas reticências (`…`). O programa deve mostrar: quantos caracteres o texto tem; quantas palavras tem; o texto com o travessão trocado por um hífen (`-`) e as reticências trocadas por três pontos (`...`). *Pesquise:* `len()`, `split()` e `replace()`. **Guarde este exercício:** na Sprint 4 você vai entender por que essa troca existe.
- **`ex03_tamanho.py`:** peça ao usuário (com `input`) para colar um texto e diga se ele é **curto** (menos de 1.000 caracteres), **médio** (de 1.000 a 4.000) ou **longo** (mais de 4.000). *Pesquise:* `if`, `elif` e `else` (aula 10). Essa é exatamente a classificação que você vai usar para escolher as narrativas na Sprint 3.
- **`ex04_tempo.py`:** importe o módulo `time` e meça quanto tempo o Python leva para somar os números de 1 a 1.000.000. Mostre o resultado em milissegundos, com duas casas decimais. *Pesquise:* `time.perf_counter()` (aula 8 e a documentação do módulo `time`) e como formatar números em *f-string* com `:.2f`. Você vai usar exatamente isso para medir as bibliotecas na Sprint 7.

**5. Comece o diário.** Crie `estudos/diario_rascunho.md` com as 3 linhas da semana. Na Sprint 2 ele vira `docs/diario.md`.

### Como saber que deu certo

- `python --version` (ou `py --version`) mostra a versão do Python.
- Você roda qualquer um dos exercícios pelo terminal do VS Code e ele funciona.
- O `ex02_texto.py` mostra o texto com o travessão e as reticências trocados.
- O `ex04_tempo.py` mostra um tempo em milissegundos.

### Entrega da sprint

- [ ] Python e VS Code (com a extensão Python) funcionando.
- [ ] Aulas 1, 2, 4, 6, 7, 8, 9 e 10 do Mundo 1 assistidas.
- [ ] Exercícios das aulas 6, 7, 9 e 10 em `estudos/sprint1/`.
- [ ] Os 4 exercícios do projeto (`ex01` a `ex04`) funcionando.
- [ ] Rascunho do diário com as 3 linhas da semana.

Nesta sprint ainda não há PR: a pasta `estudos/` entra no repositório na Sprint 2. Para entregar, comente na *issue* com um print do terminal mostrando o `ex02` e o `ex04` rodando, e mova o card para **Em revisão**.

<a id="sprint-1-escrita"></a>
## Sprint 1 · Escrita: preparar o documento e ler para a Introdução

**O que você vai entregar:** o documento do TCC aberto e preparado, as normas lidas e as leituras da Introdução fichadas.

### Passo a passo

**1. Abra o documento do TCC** que eu compartilhei com você no Google Drive (o convite chega no seu e-mail). Preencha a capa e a folha de rosto com o seu nome, o curso, o nome dos orientadores e o título provisório: *Geração automatizada de folders em PDF a partir de narrativas populares: um comparativo entre bibliotecas Python*.

**2. Crie a seção "REFERÊNCIAS"** no fim do documento, ainda vazia. A partir de hoje, toda obra que você ler entra nela no mesmo dia.

**3. Leia as normas.** Leia [`docs/orientacoes_escrita_tcc.md`](orientacoes_escrita_tcc.md) inteiro, com atenção especial a: estrutura do trabalho, Introdução, objetivo geral, como citar e como referenciar.

**4. Leia o resumo do projeto pai** em [`docs/projeto_narrativas.md`](projeto_narrativas.md). Ele é o ponto de partida da sua Introdução e já traz referências que você vai reaproveitar.

**5. Pesquise e leia, fichando em `estudos/leituras_rascunho.md`** (na Sprint 2 ele vira `docs/leituras.md`), no formato da [seção 8.4](#escrita-geral):

- **as referências do projeto:** Bezerra (2026), Binda e Da Silva (2026), Dos Santos Fernandes e Martins (2026), Pires (2025), Reis (2023), Soave e Da Silva Lemos (2022). As referências completas estão no fim de `docs/projeto_narrativas.md`. Procure cada uma pelo título no **Google Acadêmico** (`scholar.google.com.br`); são artigos de revista e quase todos têm o PDF aberto. A de Soave e Da Silva Lemos (2022) é citada no texto do projeto, mas não aparece na lista do fim: procure-a no Google Acadêmico pelos sobrenomes dos autores e pelo ano, e monte você mesmo a referência completa;
- **a Convenção da UNESCO para a Salvaguarda do Patrimônio Cultural Imaterial (2003):** procure a versão em português no site do **IPHAN** (`gov.br/iphan`), pesquisando por "Convenção para a Salvaguarda do Patrimônio Cultural Imaterial". Leia os artigos 1 e 2 (finalidades e definições);
- **o Decreto nº 3.551, de 4 de agosto de 2000,** que instituiu o registro de bens culturais de natureza imaterial no Brasil: procure no portal da legislação federal (`planalto.gov.br`). É curto; leia inteiro;
- **a pesquisa TIC Educação, do Cetic.br** (`cetic.br`): abra a edição mais recente e procure os dados de **acesso à internet e de equipamentos nas escolas públicas**. Anote dois ou três números, com o ano e a página: eles sustentam o argumento de que o material impresso ainda é necessário.

### Como saber que deu certo

- O documento do Drive tem capa, folha de rosto e a seção de Referências criadas.
- O seu arquivo de leituras tem pelo menos **8 obras fichadas**, cada uma com a referência completa no formato ABNT.
- Você tem pelo menos 2 números da TIC Educação, com ano e página.

### Entrega

- [ ] Documento do Drive com capa, folha de rosto e seção de Referências.
- [ ] `docs/orientacoes_escrita_tcc.md` lido.
- [ ] Pelo menos 8 obras fichadas, com referência ABNT.
- [ ] As obras lidas lançadas na seção de Referências do documento.

Para entregar, comente na *issue* dizendo quantas obras você fichou e mova o card para **Em revisão**.

---

# Sprint 2 — 23/10 a 29/10/2026

<a id="sprint-2-dev"></a>
## Sprint 2 · Desenvolvimento: listas, dicionários, funções, arquivos e Git

**O que você vai entregar:** as aulas de repetição, listas, dicionários, funções e módulos assistidas; 5 exercícios do projeto resolvidos; e o seu **primeiro *pull request***, levando a pasta `estudos/` para o repositório.

Esta é a semana em que você aprende tudo o que falta para escrever o leitor de narrativas da Sprint 3 e os geradores das Sprints 4 a 6.

### Passo a passo

**1. Assista às aulas:**

| Curso | Aula | Assunto |
|---|---|---|
| [Mundo 2](https://www.cursoemvideo.com/curso/python-3-mundo-2/) | 12 | Condições aninhadas (`elif`) |
| Mundo 2 | 13 | Estrutura de repetição `for` |
| Mundo 2 | 14 | Estrutura de repetição `while` |
| [Mundo 3](https://www.cursoemvideo.com/curso/python-3-mundo-3/) | 17 | Listas (parte 1) |
| Mundo 3 | 19 | **Dicionários** (a mais importante da semana) |
| Mundo 3 | 20 e 21 | **Funções** (partes 1 e 2) |
| Mundo 3 | 22 | Módulos e pacotes |
| Mundo 3 | 23 | Tratamento de erros e exceções |

As aulas 15, 16 e 18 são opcionais. Faça os exercícios propostos nas aulas 13, 17, 19 e 20, em `estudos/sprint2/`.

O curso não ensina a **ler arquivos de texto**, que é o que você mais vai precisar. Para isso, leia a seção **7.2 – Leitura e escrita de arquivos** do tutorial oficial do Python, em português: https://docs.python.org/pt-br/3/tutorial/inputoutput.html. Preste atenção em duas coisas: o comando `with open(...)` e o parâmetro `encoding="utf-8"`.

**2. Faça os exercícios do projeto**, em `estudos/sprint2/`:

- **`ex05_listas.py`:** crie uma lista com 5 títulos de contos populares que você conheça. Com um `for`, mostre cada título numerado (`1. A Moura Torta`). Depois mostre quantos títulos há na lista. *Pesquise:* `enumerate()`.
- **`ex06_dicionario.py`:** crie um dicionário que represente **uma** narrativa, com as chaves `titulo`, `tipo`, `origem` e `publico`. Mostre na tela, em uma linha só, o tipo, a origem e o público separados por ` • ` (por exemplo, `Conto • Sergipe • Ensino Fundamental`). *Pesquise:* como acessar o valor de uma chave e como montar o texto com *f-string*.
- **`ex07_arquivo.py`:** este é o mais importante, porque é o ensaio do programa da Sprint 3.
  1. No VS Code, crie à mão o arquivo `estudos/sprint2/narrativa_teste.txt` com este conteúdo (o VS Code já salva em UTF-8):

     ```
     titulo: A Moura Torta
     tipo: Conto
     origem: Sergipe
     ---
     Era uma vez um príncipe que saiu pelo mundo...

     E no fim tudo acabou bem.
     ```
  2. Escreva o programa que abre esse arquivo com `with open(..., encoding="utf-8")` e lê todo o conteúdo com `.read()`;
  3. separe o conteúdo em duas partes na linha `---`. *Pesquise:* o método `split()` com o segundo parâmetro, `split("---", 1)`. Por que o `1`? Teste sem ele e com ele, e anote a diferença no diário;
  4. pegue a primeira parte (o cabeçalho), separe em linhas (`split("\n")`) e, para cada linha que tiver `:`, separe o rótulo do valor (`split(":", 1)`) e guarde em um dicionário. Use `strip()` para tirar os espaços sobrando;
  5. guarde a segunda parte (o texto) no mesmo dicionário, com a chave `texto`;
  6. mostre o dicionário na tela, e depois só o título e a quantidade de caracteres do texto.
- **`ex08_funcao.py`:** transforme o seu `ex03_tamanho.py` em uma **função** `classificar_tamanho(texto)`, que recebe um texto e **devolve** (com `return`, sem `print` dentro da função) `"curto"`, `"médio"` ou `"longo"`. Chame a função três vezes, com textos de tamanhos diferentes, e mostre os resultados.
- **`ex09_erros.py`:** tente abrir um arquivo que não existe (`nao_existe.txt`). Primeiro rode sem tratamento e **copie a mensagem de erro para o diário**. Depois trate o erro com `try` e `except FileNotFoundError`, mostrando uma mensagem amigável. Aprender a ler uma mensagem de erro (a última linha diz **o quê**, as linhas de cima dizem **onde**) é a habilidade mais útil das próximas seis semanas.

**3. Aprenda o básico de Git e GitHub.** Assista às aulas iniciais do Curso de Git e GitHub do Curso em Vídeo (https://www.cursoemvideo.com/curso/curso-de-git-e-github/), até a parte em que o repositório é enviado para o GitHub. Depois leia a [seção 5](#fluxo-git) deste documento inteira.

**4. Configure o Git** na máquina do laboratório (uma vez só por máquina), com o mesmo e-mail da sua conta do GitHub:

```
git config --global user.name "Seu Nome Completo"
git config --global user.email "seu-email-do-github@exemplo.com"
```

**5. Aceite o convite do repositório.** Você recebeu por e-mail um convite para o `nicifrn/mp_gerador_pdf`. Aceite-o (ou abra https://github.com/nicifrn/mp_gerador_pdf/invitations).

**6. Clone o repositório e crie a sua primeira *branch*:**

```
cd %USERPROFILE%
git clone https://github.com/nicifrn/mp_gerador_pdf.git
cd mp_gerador_pdf
git checkout develop
git checkout -b feature/estudos-python
```

Na primeira vez que o Git falar com o GitHub, abre uma janela do navegador pedindo login. Entre com a sua conta e autorize.

**7. Traga os seus estudos para o repositório.**

1. Copie a pasta `estudos` (com `sprint1` e `sprint2` dentro) para dentro de `mp_gerador_pdf`;
2. mova o rascunho do diário para `docs/diario.md` e o das leituras para `docs/leituras.md`;
3. crie o arquivo `.gitignore` na raiz do repositório, com este conteúdo:

   ```
   .venv/
   __pycache__/
   *.pyc
   saidas/
   ```
4. abra a pasta `mp_gerador_pdf` no VS Code (*File → Open Folder*). A partir de agora, **é sempre essa pasta que você abre**.

**8. Faça os seus primeiros *commits*,** um por assunto:

```
git status
git add .gitignore
git commit -m "feat: adiciona gitignore do projeto"
git add estudos
git commit -m "feat: adiciona exercícios de estudo de Python"
git add docs
git commit -m "docs: adiciona diário e fichamento de leituras"
git push -u origin feature/estudos-python
```

**9. Abra o seu primeiro PR**, para a `develop`, seguindo a [seção 5.4](#fluxo-git). Como é o primeiro, no campo **Issue** coloque as duas *issues* de desenvolvimento: `Closes #1` e `Closes #3` (a da Sprint 1 e a desta sprint).

### Como saber que deu certo

- O `ex07_arquivo.py` mostra o dicionário com `titulo`, `tipo`, `origem` e `texto`, com os acentos certos.
- O `ex08_funcao.py` mostra três classificações diferentes.
- No GitHub, a sua *branch* `feature/estudos-python` aparece com os três *commits*.
- O PR está aberto para a `develop`, com os dois orientadores como revisores.

### Entrega da sprint

- [ ] Aulas 12, 13 e 14 do Mundo 2 e 17, 19, 20, 21, 22 e 23 do Mundo 3 assistidas.
- [ ] Seção 7.2 do tutorial oficial lida.
- [ ] Exercícios das aulas e os 5 exercícios do projeto (`ex05` a `ex09`) em `estudos/sprint2/`.
- [ ] Git configurado e repositório clonado.
- [ ] `.gitignore`, `estudos/`, `docs/diario.md` e `docs/leituras.md` enviados em *commits* separados, com mensagens no padrão.
- [ ] PR aberto para a `develop`, com `Closes #1` e `Closes #3`.

<a id="sprint-2-escrita"></a>
## Sprint 2 · Escrita: Introdução e Objetivo geral (Entrega 1)

**Prazo: 29/10/2026**

A Introdução tem **cinco blocos de parágrafos, nesta ordem** (é a sequência definida nas orientações de escrita), e deve ocupar de **2 a 3 páginas**. Escreva no documento do Drive, nas seções `1 INTRODUÇÃO` e `1.1 Objetivo geral`.

### Bloco 1 – Contextualização (2 parágrafos)

**Pesquise sobre:** você já fez isso na Sprint 1. Releia os fichamentos de Bezerra (2026), Binda e Da Silva (2026), Pires (2025), Reis (2023), Soave e Da Silva Lemos (2022), da Convenção da UNESCO e do Decreto nº 3.551/2000.

**Escreva sobre:**

1. a importância das narrativas populares como forma de transmitir conhecimento, valores e identidade, e **a ameaça real de que elas se percam**: elas vivem na memória de pessoas idosas e desaparecem quando essas pessoas morrem. Esse é o argumento mais forte da sua Introdução;
2. o projeto Narrativas como resposta a isso: uma plataforma digital que registra e organiza esse acervo (use o resumo do projeto e as Humanidades Digitais, de Reis, 2023).

**Depois estreite para o seu assunto**, que é onde a maioria dos trabalhos erra: **preservar não basta, é preciso difundir**. Uma narrativa guardada em um banco de dados que ninguém lê está tão perdida quanto a que não foi registrada. É aí que entra o **material impresso**: o folder que um professor imprime e leva para a sala de aula alcança um público que talvez nunca entre no site.

### Bloco 2 – Problemática (2 parágrafos)

**Pesquise sobre:**

- o papel do material impresso na educação, especialmente em escolas públicas com acesso limitado à internet: use os números da **TIC Educação** que você anotou;
- a geração automática de documentos: por que gerar mil folders à mão é inviável. Procure no Google Acadêmico por "geração automática de documentos" e "document generation";
- os problemas mais comuns das bibliotecas de PDF: acentuação, fontes, imagens e dependências do sistema operacional. Nesta semana basta ler a página inicial da documentação de cada uma: FPDF2 (`py-pdf.github.io/fpdf2`), ReportLab (`docs.reportlab.com`), xhtml2pdf (`xhtml2pdf.readthedocs.io`) e WeasyPrint (`doc.courtbouillon.org/weasyprint`).

**Escreva sobre** o problema concreto: os protótipos de tela do portal Narrativas já preveem os botões "Baixar PDF" e "Material Didático", mas **a plataforma não tem nenhuma biblioteca de PDF escolhida**, e essa escolha não é trivial:

- há várias bibliotecas Python para isso, com formas de trabalhar **muito diferentes** entre si;
- elas se comportam de maneira diferente em coisas que importam muito em português: **acentuação** e **fontes**;
- algumas exigem **programas do sistema operacional** que nem sempre podem ser instalados;
- e o PDF gerado pode ou não ter **texto pesquisável**, o que decide se ele é acessível a quem usa leitor de tela.

Explique a consequência de escolher errado: a equipe descobre o problema **depois** de ter implementado, e refazer custa caro. E uma consequência mais grave: se o PDF sair com o texto quebrado ou sem texto selecionável, o material didático fica inutilizável para parte do público, justamente o oposto do que o projeto quer.

**Faça a ponte para o que ainda não se sabe:** não existe uma resposta pronta sobre qual biblioteca usar, porque a resposta depende do documento que se quer gerar. Um folder cultural, com imagem, texto longo em português, caixa com borda e rodapé repetido, exercita justamente os pontos em que essas bibliotecas se diferenciam. **É essa comparação, feita sobre um documento real do projeto, que o seu trabalho entrega.**

### Bloco 3 – Caminho para a solução (1 a 2 parágrafos)

**Pesquise sobre:**

- **o formato PDF:** o que é, por que virou o padrão para documentos que precisam sair iguais em qualquer computador e impressora, e o fato de ser uma norma aberta (**ISO 32000**). Procure "Portable Document Format ISO 32000" no Google Acadêmico e a página da norma no site da ISO (`iso.org`);
- **as duas formas de gerar PDF por programa:**
  - **desenhar por coordenadas:** o programa diz onde cada elemento fica na página (é assim na FPDF2);
  - **descrever o documento** e deixar a biblioteca encaixar, com blocos (ReportLab) ou com HTML e CSS (xhtml2pdf, WeasyPrint).

**Escreva sobre** as alternativas e essa diferença de abordagem, que é o eixo do seu trabalho. Mostre que não é só "uma biblioteca ou outra": são **maneiras diferentes de pensar o documento**, com vantagens diferentes (controle milimétrico de um lado, facilidade de mudar o leiaute do outro).

Justifique o recorte: comparar **três bibliotecas** (mais uma quarta, cuja instalação foi testada), gerando **o mesmo folder**, a partir do **mesmo acervo**, na **mesma máquina**, e medindo fidelidade, tempo, tamanho, acentuação, imagens, acessibilidade e esforço de implementação.

Diga também o que o trabalho **não** faz: edição de PDF, assinatura digital, PDF/A para arquivamento de longo prazo e geração a partir de banco de dados. Isso vira trabalho futuro. **Recorte declarado é recorte defendido.**

### Bloco 4 – Apresentação da solução (2 parágrafos)

Você ainda não fez nada disso. **Escreva no futuro** ("será desenhado", "serão comparadas") e, na revisão final (Sprint 8), passe para o passado.

**Escreva sobre:**

- o **modelo de folder** em A4 com dez elementos definidos (faixa de identificação, título, dados da narrativa, imagem com legenda, texto justificado, caixa de palavras-chave, rodapé com a fonte bibliográfica e numeração de páginas); o **acervo de teste com dez narrativas populares em domínio público**, de tamanhos variados; e o mesmo folder implementado em **três bibliotecas Python**;
- **por que o mesmo folder nas três:** porque assim a única coisa que muda entre elas é a biblioteca. Se cada uma gerasse um folder diferente, não daria para saber se a diferença veio da ferramenta ou do programador. **Essa é a decisão de método mais importante do trabalho** e merece uma frase de destaque já aqui;
- **como será avaliado:** uma **lista de conferência de dez itens**, escrita **antes** de gerar qualquer folder, com nota de 0 a 2 por item e justificativa escrita para toda nota diferente de 2; e medições automáticas de tempo (com repetições e mediana), tamanho do arquivo, número de páginas, extração de texto e verificação de palavras acentuadas;
- que **todas as narrativas são de domínio público** e que **as imagens têm licença livre**, com a origem de cada uma documentada, e que **não há dados de pessoas nem participantes de pesquisa**, o que dispensa submissão ao Comitê de Ética em Pesquisa.

### Bloco 5 – Vínculo com o projeto e escopo (1 parágrafo)

**Escreva sobre** o vínculo com o projeto Narrativas, do IFRN, que é um projeto institucional com equipe própria. Explique que:

- o seu trabalho é feito **em um repositório separado da plataforma**, sem alterar o código dela, o que é necessário porque o cadastro de narrativas ainda não existe no sistema;
- o seu escopo é **apenas a comparação das bibliotecas e a recomendação**;
- a **implementação do botão "Baixar PDF" na plataforma é trabalho futuro**, a cargo da equipe de desenvolvimento, que usará a sua recomendação como insumo.

Feche a Introdução com um parágrafo curto dizendo como o texto está organizado ("Na seção 2, ...; na seção 3, ...").

### 1.1 Objetivo geral

Uma **única frase**, com **uma única ação principal**, coerente com o título e com a futura conclusão. Modelo das orientações de escrita:

> "O objetivo principal do presente trabalho consiste no [ação] de [o quê] para [finalidade]."

- **O verbo principal não é "desenvolver".** Esse é o erro mais provável no seu caso, porque você vai passar seis semanas programando. Mas os programas são o **meio**; o que o trabalho entrega é a **resposta medida**. Verbos adequados: **comparar**, **avaliar**, **analisar**.
- Nomeie **o que** é comparado (bibliotecas Python de geração de PDF), **para que** (gerar folders de narrativas populares) e **em que dimensões** (fidelidade ao leiaute, desempenho e acessibilidade). Sem a terceira parte, o objetivo fica vago demais.
- **Não** empilhe ações. "Desenvolver, comparar, avaliar e implantar" são quatro objetivos, não um.
- **Não** prometa o que não vai medir. Você não vai testar impressão em papel; então não fale em "qualidade de impressão".

Deixe a seção `1.2 Objetivos específicos` com o título e uma linha "a ser escrito na Sprint 8".

### Entrega

- [ ] Os cinco blocos da Introdução escritos, na ordem, com citações.
- [ ] Objetivo geral em uma frase, com um verbo só.
- [ ] Todas as obras citadas lançadas nas Referências, no formato ABNT.
- [ ] Versão nomeada no histórico: `Entrega 1 – Introdução – 29/10`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 3 — 30/10 a 05/11/2026

<a id="sprint-3-dev"></a>
## Sprint 3 · Desenvolvimento: ambiente, primeiro PDF, acervo de teste e modelo do folder

**Branch:** `feature/ambiente-e-acervo`

**O que você vai entregar:** o ambiente virtual criado, as bibliotecas instaladas e documentadas, a estrutura de pastas, um primeiro PDF gerado com Python, as 10 narrativas em arquivos de texto com as imagens, o programa que lê as narrativas, a primeira verificação automática, o desenho do folder e a lista de conferência.

Esta é a sprint mais cheia do desenvolvimento, e é a base de todo o resto. Ela tem duas partes: a **Parte A** elimina todas as surpresas de ambiente agora, e não na semana em que você precisar entregar resultado; a **Parte B** monta o material sobre o qual as três bibliotecas vão trabalhar. Lembre que 02/11 (segunda) é feriado: a semana tem um dia útil a menos.

**Divida a semana assim:**

| Dia | O que fazer |
|---|---|
| sexta, 30/10 | Parte A inteira (do ambiente virtual ao `README.md`). Se sobrar tempo, comece a procurar o livro (passo B1) |
| terça, 03/11 | passos B1 a B4: o livro, as 10 narrativas e as imagens. É a parte que mais demora |
| quarta, 04/11 | passos B5 e B6: o leitor de narrativas e a verificação |
| quinta, 05/11 | passos B7 e B8: o modelo do folder e a lista de conferência; diário, *commits* e PR |

**Antes de tudo, atualize a `develop` e crie a *branch*** (veja a [seção 5.2](#fluxo-git)). A `develop` agora tem os seus estudos, que foram aprovados.

### Parte A — Ambiente e primeiro PDF

**A1. Crie o ambiente virtual.** Ele é uma "caixa" só deste projeto, onde as bibliotecas ficam instaladas sem bagunçar o Python da máquina. Na raiz do repositório, **no Prompt de Comando** (`cmd`, e não o PowerShell):

```
python -m venv .venv
.venv\Scripts\activate
```

Depois de ativar, o começo da linha passa a mostrar `(.venv)`. **Se não mostrar, o ambiente não está ativo**, e tudo o que você instalar vai para o lugar errado. Toda vez que abrir um terminal novo, ative de novo.

> No terminal do VS Code, abra o seletor de terminal (setinha ao lado do `+`) e escolha **Command Prompt**. No PowerShell, o `activate` costuma dar erro de "execução de scripts desabilitada".

**A2. Instale as bibliotecas, uma de cada vez, anotando tudo.** "Facilidade de instalação" é um dos critérios da comparação, então a instalação **já é coleta de dados**. Crie `docs/instalacao.md` e, para cada comando abaixo, anote: o comando; se instalou de primeira; se apareceu algum aviso (`WARNING`) ou erro; quanto tempo levou (olhe o relógio); e **quantos pacotes vieram junto**, contando os nomes da linha `Successfully installed ...` que o `pip` mostra no fim.

```
pip install fpdf2
pip install reportlab
pip install xhtml2pdf
pip install pypdf
pip install matplotlib
```

> Repare na diferença: a `xhtml2pdf` puxa vários pacotes junto (inclusive a própria ReportLab), enquanto a `fpdf2` vem quase sozinha. Esse número é um dado objetivo sobre o "peso" de cada opção.

**Não instale a WeasyPrint agora.** Ela é o assunto da Sprint 6.

Organize `docs/instalacao.md` em uma tabela:

```
| Biblioteca | Comando | Instalou de primeira? | Avisos/erros | Tempo | Pacotes que vieram junto |
|---|---|---|---|---|---|
| fpdf2 | pip install fpdf2 | sim | nenhum | 8 s | 3 (fpdf2, ...) |
```

**A3. Gere o `requirements.txt`**, que é a lista de tudo o que está instalado, com as versões:

```
pip freeze > requirements.txt
```

**A4. Crie as pastas do projeto** (veja a [seção 6](#estrutura)): `narrativas`, `imagens`, `modelo`, `geradores`, `testes`, `saidas`, `resultados` e `docs\evidencias`. *Pesquise:* o comando `mkdir` no Windows. O Git não guarda pastas vazias; por isso, coloque dentro de cada pasta vazia um arquivo `.gitkeep` vazio (menos na `saidas`, que não vai para o Git).

**A5. Gere o seu primeiro PDF.** Crie `estudos/sprint3/teste_pdf.py`. Antes de escrever, abra o tutorial da FPDF2 (`py-pdf.github.io/fpdf2/Tutorial-pt.html`, que tem versão em português) e leia o primeiro exemplo. O seu programa precisa, nesta ordem:

1. importar a classe `FPDF` do módulo `fpdf`;
2. criar o objeto do PDF e adicionar uma página (`add_page`);
3. escolher a fonte `Helvetica`, negrito, tamanho 20 (`set_font`);
4. escrever o título `Narrativas do Rio Grande do Norte`, centralizado (`cell`, com `align="C"`);
5. trocar para Helvetica normal, tamanho 12;
6. escrever o parágrafo `Teste de acentuação: coração, vovó, sertão, José, Iracema.` com `multi_cell` (ela quebra a linha sozinha quando o texto é longo);
7. salvar em `saidas/teste.pdf` (`output`) e mostrar uma mensagem na tela.

Rode com `python estudos\sprint3\teste_pdf.py` (com o `.venv` ativo) e abra o PDF com dois cliques: o Microsoft Edge abre PDF sem precisar instalar nada.

**A6. Faça três verificações no PDF.** Elas são um ensaio do que você vai fazer no trabalho inteiro:

- **os acentos saíram certos?** Olhe "coração", "vovó" e "sertão" com atenção;
- **dá para selecionar o texto com o mouse?** Se der, o texto é de verdade, e não uma imagem;
- **o Ctrl+F acha a palavra "sertão"?** Se achar, o PDF é pesquisável.

Anote as três respostas no diário. Tire um print e salve como `docs/evidencias/s03_primeiro_pdf.png`.

**A7. Teste os caracteres especiais.** Acrescente ao seu programa uma linha com `Travessão — reticências… aspas “curvas” seta →` e rode de novo. Essa frase de teste é sempre a mesma, e você vai repeti-la nas três bibliotecas. **Anote exatamente o que acontecer**: se der erro, copie a mensagem inteira para o diário; se sair um caractere estranho, tire um print. Não tente resolver agora: isso é o primeiro passo da Sprint 4, e o que você anotar aqui **é um achado do trabalho**.

**A8. Preencha `docs/ambiente.md`** com a configuração da máquina onde as medições oficiais serão feitas (a do laboratório que você usa sempre):

- processador e memória RAM: tecle `Win`, digite "Sobre o seu PC" e anote "Processador" e "RAM instalada";
- sistema operacional e versão: na mesma tela, "Edição" e "Versão";
- versão do Python (`python --version`);
- versão de cada biblioteca (`pip list`).

Isso vai para a seção Materiais e métodos do TCC. Sem isso, o trabalho não é reproduzível.

**A9. Comece o `README.md`** do repositório. Por enquanto, quatro partes (a política do NIC exige as quatro):

1. **o que é este projeto**, em três linhas;
2. **responsáveis:** você (aluno) e os dois orientadores, com os usuários do GitHub;
3. **instalação:** como criar o ambiente virtual e instalar com `pip install -r requirements.txt`;
4. **como rodar:** por enquanto, o `teste_pdf.py`; no fim da semana, acrescente o `ler_narrativas.py` e a verificação das narrativas (Parte B).

> **Se os acentos saírem errados ou aparecer `UnicodeEncodeError` (ou `FPDFUnicodeEncodingException`)**, não se assuste: isso acontece quando o texto tem algum caractere fora do conjunto que a fonte padrão conhece. **Anote o erro exato**; a solução está na Sprint 4.

### Parte B — O acervo de teste e o modelo do folder

**B1. Encontre o livro.** O acervo de teste vem de ***Contos Populares do Brazil***, de **Sílvio Romero** (com a grafia da época, "Brazil"). Sílvio Romero morreu em 1914, e a obra está em **domínio público**: pela Lei nº 9.610/1998, a obra entra em domínio público 70 anos contados de 1º de janeiro do ano seguinte à morte do autor. A primeira edição é de 1885 (Lisboa, Nova Livraria Internacional) e tem introdução e notas de Teófilo Braga, que morreu em 1924 e também está em domínio público.

Procure pelo título exato, `Contos populares do Brazil`, nesta ordem:

1. **Wikisource em português** (`pt.wikisource.org`): se estiver lá, o texto já está digitado, o que facilita muito;
2. **Internet Archive** (`archive.org`): tem digitalizações de edições antigas, muitas com o texto para baixar (opção "FULL TEXT");
3. **Biblioteca Brasiliana Guita e José Mindlin**, da USP (`digital.bbm.usp.br`);
4. portal **Domínio Público**, do MEC (`dominiopublico.gov.br`).

Use **uma única edição** do livro para todas as narrativas. **Anote no diário qual edição você usou** (cidade, editora, ano) e o endereço exato de onde baixou, porque isso vai para a referência de cada narrativa e para a Metodologia.

**B2. Escolha 10 contos**, com estes critérios:

- **tamanhos variados:** pelo menos **2 curtos** (menos de 1.000 caracteres), **4 médios** (de 1.000 a 4.000) e **2 longos** (mais de 4.000). Os outros 2 podem ser de qualquer tamanho. Isso é importante: o texto longo é o que faz o folder passar de uma página, e é aí que as bibliotecas se diferenciam. Use a sua função `classificar_tamanho` da Sprint 2 para conferir;
- **com bastante acentuação**, o que é fácil em português;
- **variados na origem:** o livro separa os contos por origem (europeia, indígena, africana e mestiça) e Romero costuma indicar onde coletou cada um (Sergipe, Pernambuco, Rio de Janeiro...). Escolha contos de mais de uma parte do livro.

**Pode modernizar a grafia?** Não. Transcreva o texto **como está na edição**, com a grafia da época ("Brazil", "elle", "pharmacia"). Isso não atrapalha a comparação (as três bibliotecas recebem o mesmo texto) e evita que você altere a obra.

**B3. Salve cada narrativa em um arquivo `.txt`**, dentro de `narrativas/`, exatamente neste formato:

```
titulo: (título do conto, como está no livro)
tipo: Conto popular
origem: (o lugar indicado por Romero; se não houver, "Brasil")
publico: Ensino Fundamental
palavras-chave: (3 a 5 palavras que resumem o conto, separadas por ponto e vírgula)
imagem: 01_nome_do_conto.jpg
fonte: ROMERO, Sílvio. Contos populares do Brazil. (complete com a edição que você usou e o "Disponível em: ... Acesso em: ...")
---
(o texto do conto, em um ou mais parágrafos, com uma linha em branco entre os parágrafos)
```

Três regras deste formato:

- **as sete primeiras linhas** são os dados da narrativa, no formato `rótulo: valor`, um por linha, **sempre com esses sete rótulos e nessa ordem**;
- **a linha com três traços (`---`)** separa os dados do texto;
- **tudo o que vem depois** é o texto da narrativa, com **uma linha em branco entre os parágrafos** (o gerador vai usar isso para separar os parágrafos).

Monte a referência do campo `fonte` seguindo a NBR 6023:2018 (modelo de livro em `docs/orientacoes_escrita_tcc.md`).

**Salve os arquivos em UTF-8.** No VS Code já é o padrão (confira no canto inferior direito: deve estar escrito `UTF-8`). Se errar isso, os acentos viram símbolos estranhos quando o Python for ler.

Nomeie os arquivos com dois dígitos e o nome do conto, sem acento e sem espaço: `01_a_moura_torta.txt`, `02_...`.

**B4. Arrume uma imagem para cada narrativa**, em `imagens/`, com o mesmo número e nome do arquivo da narrativa (`01_a_moura_torta.jpg`).

**A imagem também precisa ter licença livre.** Use o **Wikimedia Commons** (`commons.wikimedia.org`), que informa a licença de cada imagem (procure por temas do conto: "sertão", "casa de taipa", "onça"...), ou fotografias e desenhos seus. Prefira imagens em domínio público ou com licença **CC0**, **CC BY** ou **CC BY-SA**.

Crie `imagens/creditos.md` com uma tabela: arquivo, autor, licença, endereço de onde baixou e data. Isso vai para o TCC.

**Padronize o tamanho:** todas as imagens em **JPG**, com **cerca de 800 pixels de largura**. Para redimensionar sem instalar nada, abra a imagem no **Paint** → *Redimensionar* → *Pixels* → largura 800, com "Manter taxa de proporção" marcado. Se as imagens forem muito diferentes entre si, você não vai saber se uma diferença no PDF foi da biblioteca ou da imagem.

**B5. Escreva o leitor de narrativas** em `geradores/ler_narrativas.py`. Você já fez quase tudo isso no `ex07_arquivo.py` da Sprint 2. Agora organize em **duas funções**:

- **`ler_narrativa(caminho)`:** recebe o caminho de **um** arquivo `.txt` e devolve **um dicionário** com os sete campos do cabeçalho, mais a chave `texto` (o texto da narrativa, sem espaços sobrando no começo e no fim) e a chave `arquivo` (só o nome do arquivo, como `01_a_moura_torta.txt`). *Pesquise:* `os.path.basename`;
- **`ler_todas()`:** percorre a pasta `narrativas/`, chama `ler_narrativa` para cada arquivo que termina em `.txt`, **em ordem alfabética**, e devolve uma **lista de dicionários**. *Pesquise:* `os.listdir`, `sorted`, `str.endswith` e `os.path.join`.

No fim do arquivo, acrescente o bloco abaixo, que só roda quando você executa o arquivo diretamente (e não quando outro programa o importa):

```python
if __name__ == "__main__":
    # para cada narrativa de ler_todas(), mostre em uma linha:
    # o nome do arquivo | o título | a quantidade de caracteres do texto
    ...
```

Rode **a partir da raiz do repositório**: `python geradores\ler_narrativas.py`. Você deve ver 10 linhas, uma por narrativa.

> **Erros comuns:** `ValueError: not enough values to unpack` significa que algum arquivo está sem a linha `---`. `UnicodeDecodeError` significa que algum arquivo não foi salvo em UTF-8. `FileNotFoundError` quase sempre significa que você rodou o programa de dentro da pasta errada: rode sempre da raiz do repositório.

**B6. Escreva a primeira verificação automática** em `testes/verificar_narrativas.py`. Ela confere sozinha, em um segundo, aquilo que você levaria vários minutos para conferir abrindo arquivo por arquivo. Antes de começar, releia a explicação do `assert` na [seção 5.5](#fluxo-git).

Use este esqueleto e troque cada comentário numerado por uma linha com `assert`:

```python
import os
import sys

sys.path.insert(0, "geradores")   # deixa o Python encontrar o ler_narrativas.py
from ler_narrativas import ler_todas

CAMPOS = ["titulo", "tipo", "origem", "publico", "palavras-chave", "imagem", "fonte", "texto"]

narrativas = ler_todas()

# 1. confira que vieram 10 narrativas

for narrativa in narrativas:
    nome = narrativa["arquivo"]
    for campo in CAMPOS:
        # 2. confira que o campo está no dicionário da narrativa
        ...
    # 3. confira que o texto tem mais de 100 caracteres
    # 4. confira que o arquivo da imagem existe na pasta imagens/

print("Tudo certo:", len(narrativas), "narrativas verificadas.")
```

*Pesquise:* o operador `in` com dicionários (`"titulo" in narrativa`), `len()`, `os.path.join` e `os.path.exists`. Use o `nome` na mensagem de cada `assert`, para saber **qual** arquivo deu problema, por exemplo: `f"{nome}: falta o campo {campo}"`.

Rode com `python testes\verificar_narrativas.py`. **Ele precisa terminar mostrando `Tudo certo: 10 narrativas verificadas.`**

Para ter certeza de que a verificação funciona de verdade, faça uma sabotagem de propósito: renomeie temporariamente uma das imagens (por exemplo, `01_a_moura_torta.jpg` para `x.jpg`), rode de novo e veja aparecer o `AssertionError` com o nome da narrativa. Depois desfaça a troca. Uma verificação que nunca falha não verifica nada.

**B7. Desenhe o modelo do folder.** Este é o passo mais importante da semana, e **não é programação**: é desenho.

Você precisa de **um desenho de como o folder deve ficar**, porque é contra esse desenho que as três bibliotecas vão ser comparadas. Sem ele, "fidelidade ao leiaute" vira opinião.

Antes de desenhar, abra os prints em `docs/prototipos/` e veja como a página de uma narrativa foi pensada no portal: cores, a forma como título, tipo e origem aparecem, onde ficam os botões "Baixar PDF" e "Material Didático". O seu folder deve **conversar visualmente** com essa página.

Desenhe no **`app.diagrams.net`** (funciona no navegador, sem instalar nada). Comece com uma página A4: *File → Page Setup → A4*, retrato.

**O folder deve ser A4, retrato, e ter estes 10 elementos**, que são exatamente os itens da lista de conferência:

| # | Elemento | Detalhe |
|---|---|---|
| 1 | Faixa colorida no topo | azul-escuro (cor `#143C6E`), com o texto "Narrativas do Rio Grande do Norte" em branco e negrito |
| 2 | Título da narrativa | grande (18 pt), em negrito, centralizado, abaixo da faixa |
| 3 | Linha de dados | tipo • origem • público, centralizada, em fonte menor (9 pt) e cinza |
| 4 | Imagem | centralizada, largura de 10 cm, sem deformar |
| 5 | Legenda da imagem | fonte pequena (8 pt), itálico, centralizada, logo abaixo da imagem |
| 6 | Texto da narrativa | 11 pt, justificado, com espaço entre os parágrafos |
| 7 | Caixa de palavras-chave | com borda, no fim do texto, com "Palavras-chave:" em negrito |
| 8 | Rodapé com a fonte | a referência de onde a narrativa foi tirada, em fonte pequena (7 pt), cinza |
| 9 | Número da página | no canto direito do rodapé, no formato "Página 1" |
| 10 | Repetição em várias páginas | se o texto for longo, a faixa do topo e o rodapé se repetem na página 2 |

Margens: 2 cm à esquerda e à direita. **Fonte: DejaVu Sans em todo o folder** (normal, negrito e itálico). Ela é gratuita, tem todos os caracteres do português e vem junto com o `matplotlib`, que você já instalou. Usar a mesma fonte nas três bibliotecas é parte de "o folder tem que ser o mesmo": se cada biblioteca usasse uma fonte, o tamanho do arquivo e a aparência mudariam por causa da fonte, e não da biblioteca. No desenho, use a fonte mais parecida que o diagrams.net oferecer (Verdana ou Helvetica) e escreva no canto da página "Fonte: DejaVu Sans".

Desenhe **duas páginas**, para mostrar o item 10. Exporte como `modelo/modelo_folder.png` (*File → Export as → PNG*).

**B8. Escreva a lista de conferência** em `modelo/checklist.md`, com os 10 itens acima (copie a tabela) e a regra de pontuação:

- **2 pontos:** saiu igual ao modelo;
- **1 ponto:** saiu parecido, mas com diferença visível (cor errada, posição deslocada, tamanho diferente);
- **0 ponto:** não saiu, ou saiu errado a ponto de atrapalhar.

Assim cada biblioteca pode fazer de 0 a 20 pontos. **Escreva essa regra agora, antes de gerar qualquer folder.** Se você escrever depois de ver os resultados, acaba criando uma régua que favorece a biblioteca de que mais gostou. Isso tem nome, **viés**, e invalida a comparação. **A partir do PR desta sprint, o `checklist.md` não muda mais.**

**Ao longo da semana, faça *commits* separados por assunto** (`docs: registra instalação das bibliotecas`, `feat: adiciona primeiro teste de geração de PDF`, `feat: adiciona acervo de narrativas`, `feat: adiciona leitor de narrativas`, `test: adiciona verificação das narrativas`, `docs: adiciona modelo do folder e lista de conferência`...) e, no fim, abra **um** PR para a `develop`.

### Como saber que deu certo

- O terminal mostra `(.venv)` no começo da linha, e o `pip list` mostra `fpdf2`, `reportlab`, `xhtml2pdf`, `pypdf` e `matplotlib`.
- O arquivo `saidas/teste.pdf` existe, abre, os acentos estão certos e o Ctrl+F acha "sertão".
- O `git status` **não** mostra `.venv/` nem `saidas/`.
- `python geradores\ler_narrativas.py` lista as 10 narrativas, com os títulos certos e os acentos corretos na tela.
- `python testes\verificar_narrativas.py` mostra `Tudo certo: 10 narrativas verificadas.`
- A pasta `imagens/` tem 10 imagens, e `imagens/creditos.md` diz a licença de cada uma.
- `modelo/modelo_folder.png` existe e mostra claramente os 10 elementos, em duas páginas, e `modelo/checklist.md` está escrito.

### Entrega da sprint

- [ ] Ambiente virtual criado e as cinco bibliotecas instaladas.
- [ ] `docs/instalacao.md` com a tabela da instalação de cada biblioteca.
- [ ] `requirements.txt` e estrutura de pastas criados.
- [ ] `estudos/sprint3/teste_pdf.py` funcionando, com print em `docs/evidencias/`, e o teste do travessão anotado no diário.
- [ ] `docs/ambiente.md` preenchido e `README.md` com as quatro primeiras partes.
- [ ] 10 narrativas em `narrativas/`, com tamanhos variados e o campo `fonte` completo; edição do livro e endereço anotados no diário.
- [ ] 10 imagens em `imagens/`, com as licenças em `imagens/creditos.md`.
- [ ] `geradores/ler_narrativas.py` funcionando e `testes/verificar_narrativas.py` terminando com `Tudo certo`.
- [ ] `modelo/modelo_folder.png` (duas páginas) e `modelo/checklist.md` com os 10 itens e a regra de pontuação.
- [ ] Diário da semana.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-3-escrita"></a>
## Sprint 3 · Escrita: Referencial Teórico, parte cultural e acessibilidade (Entrega 2)

**Prazo: 05/11/2026** (02/11 é feriado: a semana tem um dia útil a menos)

**O que você vai entregar:** os comentários da Entrega 1 resolvidos, a lista de leitura do Referencial e as seções **2.1, 2.2 e 2.5** escritas.

### Antes de escrever

**1. Resolva os comentários da Introdução.** Responda a cada um dizendo o que você mudou, e só então marque como resolvido.

**2. Assista ao vídeo sobre Referencial Teórico** antes de começar a pesquisar: https://youtu.be/8Qztq1Q5vb0

**3. Entenda o seu Referencial.** Ele tem **duas metades**, e as duas são necessárias:

- a metade **cultural** (narrativas, patrimônio, material didático), que justifica *por que* o trabalho importa;
- a metade **técnica** (PDF, bibliotecas, acessibilidade), que sustenta *o que* você mediu.

Muitos trabalhos técnicos esquecem a primeira e ficam parecendo manual. Muitos trabalhos culturais esquecem a segunda e ficam sem base para os resultados. **O seu precisa das duas.**

**4. Monte a lista de leitura** em `docs/leituras.md`, em uma seção nova chamada `## Lista de leitura do Referencial`, com **pelo menos 12 obras candidatas**, separadas pelas seções do TCC (2.1 a 2.6). Para cada uma, só a referência e onde achou. As sugestões das seções 2.1, 2.2 e 2.5 estão logo abaixo; as das seções 2.3, 2.4 e 2.6, na [Sprint 4](#sprint-4-escrita). Leia as duas agora para saber o que procurar.

Onde procurar:

- **Google Acadêmico** (`scholar.google.com.br`);
- **SciELO** (`scielo.org`);
- **SBC OpenLib** (`sol.sbc.org.br`), para os trabalhos de computação;
- **BDTD** (`bdtd.ibict.br`), para TCCs, dissertações e teses;
- **Memoria – repositório institucional do IFRN** (`memoria.ifrn.edu.br`) e o **repositório da UFRN** (`repositorio.ufrn.br`), para trabalhos sobre a cultura do Rio Grande do Norte;
- **Portal de Periódicos da CAPES**, acessando pela rede do IFRN.

**5. Leia e fiche** as obras das seções 2.1, 2.2 e 2.5 em `docs/leituras.md`, e só então comece a escrever.

Seções **2.1, 2.2 e 2.5**. Comece o capítulo 2 com um parágrafo curto dizendo o que ele apresenta. Vá do geral para o específico e escreva **apenas sobre o que reaparece** na Metodologia ou nos Resultados.

### 2.1 Narrativas populares e patrimônio cultural imaterial (cerca de 1 página)

**Pesquise:** as referências do projeto (Bezerra, 2026; Binda e Da Silva, 2026; Dos Santos Fernandes e Martins, 2026; Pires, 2025); a **Convenção da UNESCO de 2003**; o **Decreto nº 3.551/2000**; e trabalhos sobre folclore e cultura popular brasileira. Para a cultura do Rio Grande do Norte, procure no repositório do IFRN e no da UFRN. Procure também por um texto sobre **Sílvio Romero e os estudos de folclore no Brasil**, porque é dele o seu acervo.

**Escreva:** o que é patrimônio cultural imaterial e por que narrativas orais fazem parte dele; por que esse patrimônio é frágil; e o que se entende por salvaguarda. **Seja breve e vá direto ao ponto.** O erro comum aqui é escrever cinco páginas sobre cultura popular e esquecer que o trabalho é sobre geração de PDF.

Termine amarrando ao seu tema: **registrar não é suficiente, é preciso difundir**, e o material impresso é uma das formas de difusão.

### 2.2 Material didático impresso e difusão cultural (cerca de 1 página)

**Pesquise:** o papel do material impresso na educação básica; o uso de temas da cultura local em sala de aula (procure na **BNCC**, a Base Nacional Comum Curricular, em `basenacionalcomum.mec.gov.br`, os trechos sobre cultura, diversidade e patrimônio); e os dados de acesso à internet nas escolas (**TIC Educação**, do Cetic.br).

**Escreva:** por que, mesmo com tudo disponível na internet, o material impresso continua tendo função, principalmente onde a conexão é ruim ou os equipamentos são poucos. Esse é o argumento que justifica o seu trabalho existir, e ele precisa estar fundamentado **com dado, não com opinião**.

Explique também o que é um **folder** como peça de comunicação: documento curto, visual, feito para circular e ser lido rapidamente. Isso justifica as escolhas do seu modelo (imagem grande, texto justificado, palavras-chave em destaque).

### 2.5 Acessibilidade de documentos digitais (cerca de 1 página)

**Pesquise:** **acessibilidade digital** e leitores de tela; a **Lei Brasileira de Inclusão (Lei nº 13.146/2015)**, no portal `planalto.gov.br` (procure os artigos sobre acesso à informação e comunicação); as **WCAG** (Diretrizes de Acessibilidade para Conteúdo Web, do W3C, com tradução em português); o **eMAG** (Modelo de Acessibilidade em Governo Eletrônico, em `gov.br`); e o **PDF/UA** (ISO 14289), que é a norma de acessibilidade específica para PDF.

**Escreva:** por que um PDF pode ser inacessível, e qual é o mínimo para ele não ser: o texto precisa existir **como texto** (e não como desenho), para que o leitor de tela consiga ler.

**Amarre ao seu trabalho:** o projeto Narrativas quer democratizar o acesso ao patrimônio cultural. Um material didático que uma pessoa cega não consegue ler contraria esse objetivo. **É por isso que "texto pesquisável" é um dos seus critérios de comparação**, e não um detalhe técnico.

Seja honesto sobre o alcance: você vai verificar apenas se o texto é extraível, que é o requisito mais básico. Acessibilidade completa em PDF envolve muito mais (estrutura de marcação, ordem de leitura, texto alternativo das imagens). **Diga isso**, e deixe a verificação completa como trabalho futuro.

### Entrega

- [ ] Comentários da Entrega 1 todos respondidos e resolvidos.
- [ ] Lista de leitura com pelo menos 12 obras, separadas por seção, em `docs/leituras.md` (envie no PR da semana).
- [ ] Parágrafo de abertura do capítulo 2 e seções 2.1, 2.2 e 2.5 escritos, com citações.
- [ ] Pelo menos 8 obras diferentes citadas nessas três seções, todas lançadas nas Referências.
- [ ] Versão nomeada: `Entrega 2 – Referencial parte 1 – 05/11`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 4 — 06/11 a 12/11/2026

<a id="sprint-4-dev"></a>
## Sprint 4 · Desenvolvimento: biblioteca 1, o folder com FPDF2

**Branch:** `feature/gerador-fpdf2`

**O que você vai entregar:** um programa que gera o folder completo, para as 10 narrativas, usando a biblioteca FPDF2, e a verificação automática dos PDFs gerados.

**Como essa biblioteca pensa:** você diz **onde** cada coisa vai, como se estivesse desenhando em uma folha com uma régua. A página A4 tem 210 mm de largura e 297 mm de altura, e você trabalha em milímetros. É a forma mais direta de entender, e a que dá mais trabalho quando o leiaute é complicado.

**Documentação:** https://py-pdf.github.io/fpdf2/ (tem tutorial em português). Deixe aberta a semana inteira.

### A regra que vale para as Sprints 4, 5 e 6

Os três geradores precisam ter **a mesma "cara" por fora**, porque o programa de medição da Sprint 7 vai chamar os três do mesmo jeito:

- uma função **`gerar_folder(narrativa, caminho_saida)`**, que recebe **um** dicionário de narrativa (o que o `ler_narrativa` devolve) e o caminho do PDF a criar, e **só** gera aquele PDF (sem `print`, sem `input`);
- um bloco `if __name__ == "__main__":` que lê todas as narrativas com `ler_todas()` e chama `gerar_folder` para cada uma, salvando em `saidas/<biblioteca>/` com o mesmo nome do `.txt`, trocando a extensão para `.pdf`.

**E o folder tem que ser o MESMO nas três:** mesmas cores, mesmos tamanhos de fonte, mesma fonte, mesma ordem dos elementos. Se você "caprichar" em uma biblioteca e não na outra, a comparação não vale. Se descobrir uma melhoria, aplique nas três.

### Passo a passo

**1. Resolva a questão da fonte antes de qualquer coisa.** Volte ao que você anotou na Sprint 3 sobre a frase `Travessão — reticências… aspas “curvas” seta →`. As fontes que já vêm na FPDF2 (Helvetica, Times, Courier) só conhecem um conjunto limitado de caracteres.

1. Rode de novo o teste da Sprint 3 com a Helvetica e anote: **quais caracteres da frase deram erro ou saíram errados**. A seta (`→`) quase certamente vai falhar. Copie a mensagem de erro inteira para o diário;
2. agora pegue a **DejaVu Sans**, que tem todos esses caracteres e vem com o `matplotlib`. Descubra onde ela está rodando, com o `.venv` ativo:

   ```
   python -c "import matplotlib, os; print(os.path.join(matplotlib.get_data_path(), 'fonts', 'ttf'))"
   ```

   Abra essa pasta no Explorador de Arquivos e copie `DejaVuSans.ttf`, `DejaVuSans-Bold.ttf` e `DejaVuSans-Oblique.ttf` para `geradores/fontes/`;
3. na documentação da FPDF2, leia a página **"Unicode"** (ou "Fontes e Unicode") e descubra como **registrar** uma fonte TrueType (`add_font`) e como usá-la (`set_font`). Você vai registrar os três arquivos com o mesmo nome de família (`"DejaVu"`) e estilos diferentes (`""`, `"B"` e `"I"`);
4. rode o teste com a DejaVu e confirme que a frase inteira sai certa.

**Registre no diário as duas situações** (com a fonte padrão e com a DejaVu). Essa dificuldade é exatamente um dos pontos da sua comparação: nas próximas sprints você vai ver se as outras bibliotecas têm o mesmo problema.

**2. Entenda as peças da FPDF2 que você vai usar.** Para cada uma, ache na documentação o que ela faz e quais parâmetros recebe:

| Peça | Para que serve no folder |
|---|---|
| `class Folder(FPDF)` com os métodos `header()` e `footer()` | a FPDF2 chama esses dois métodos **sozinha, em toda página nova**. É assim que a faixa e o rodapé se repetem (item 10) |
| `set_fill_color` e `rect(..., style="F")` | o retângulo azul da faixa (item 1) |
| `set_text_color`, `set_font` | cor e fonte de cada texto |
| `set_y`, `set_x`, `ln` | posicionar o "cursor" e pular linhas |
| `cell` | uma linha de texto (texto da faixa, número da página) |
| `multi_cell` | texto que pode quebrar em várias linhas (título, texto, legenda, rodapé). Tem `align` (`"C"`, `"J"`, `"L"`) e `border` |
| `image(caminho, x=..., w=...)` | a imagem (item 4) |
| `set_auto_page_break(auto=True, margin=...)` | quebra a página sozinha quando o texto chega perto do rodapé |
| `page_no()` | o número da página atual (item 9) |
| `output(caminho)` | salva o PDF |

**3. Escreva o gerador** em `geradores/gerar_fpdf2.py`, **por partes, testando cada uma** antes de passar para a próxima. Este é o esqueleto; o corpo é com você:

```python
import os
from fpdf import FPDF
from ler_narrativas import ler_todas

AZUL = (20, 60, 110)       # #143C6E
CINZA = (110, 110, 110)


class Folder(FPDF):

    def header(self):
        # item 1: retângulo azul de 210 mm x 18 mm no topo da página,
        #         com "Narrativas do Rio Grande do Norte" em branco, negrito, centralizado
        # no fim, volte a cor do texto para preto e posicione o cursor abaixo da faixa
        ...

    def footer(self):
        # itens 8 e 9: a uns 18 mm do fim da página, a fonte bibliográfica
        #              (7 pt, cinza) e o "Página N" à direita (8 pt)
        # dica: guarde a fonte bibliográfica em um atributo do objeto
        #       (self.fonte_bibliografica) antes de adicionar a primeira página
        ...


def gerar_folder(narrativa, caminho_saida):
    # 1. crie o Folder, registre as três fontes DejaVu, guarde a fonte bibliográfica
    # 2. ligue a quebra automática de página, deixando espaço para o rodapé
    # 3. adicione a primeira página
    # 4. item 2: título
    # 5. item 3: linha de dados (tipo • origem • publico)
    # 6. item 4: imagem centralizada, 100 mm de largura
    # 7. item 5: legenda
    # 8. item 6: texto, um multi_cell por parágrafo, justificado, com espaço entre eles
    # 9. item 7: caixa de palavras-chave com borda
    # 10. salve o PDF
    ...


if __name__ == "__main__":
    # crie a pasta saidas/fpdf2 (os.makedirs com exist_ok=True)
    # para cada narrativa, gere o folder e mostre o nome do arquivo gerado
    ...
```

Ordem sugerida: primeiro só a faixa e o título, e gere **uma** narrativa; abra o PDF; depois acrescente a linha de dados; abra de novo; e assim por diante. Programa grande escrito de uma vez só dá erro em vinte lugares ao mesmo tempo.

**Como centralizar a imagem:** se a página tem 210 mm e a imagem 100 mm, quanto deve valer o `x`? Faça a conta com papel antes de programar.

**Como separar os parágrafos:** no arquivo `.txt`, os parágrafos estão separados por uma linha em branco, ou seja, por `"\n\n"`. Pense em qual método de *string* separa o texto nesse ponto.

**4. Cuidados que vão te economizar horas:**

- **rode sempre a partir da raiz do repositório:** `python geradores\gerar_fpdf2.py`. Se der `ModuleNotFoundError: No module named 'ler_narrativas'`, você rodou de outra pasta;
- **a imagem pode deformar.** Informar só a largura (`w`) mantém a proporção, que é o certo. Se você informar a largura **e** a altura (`h`), a imagem estica. **Teste as duas formas, tire print das duas e anote**: é o item "imagens" da sua comparação;
- **o `multi_cell` dá erro se uma palavra for maior que a largura disponível.** É raro em texto normal, mas pode acontecer com um endereço de internet longo no rodapé. Se acontecer, anote e pesquise a solução na documentação;
- **texto justificado** é `align="J"`. Compare visualmente com `align="L"` e veja qual fica mais parecido com o seu modelo.

**5. Gere os 10 folders e abra todos, um por um.** É neste momento que você descobre que a narrativa curta ficou com muito espaço em branco, que a longa passou para a página 3 ou que uma imagem ficou desproporcional.

**Anote no diário tudo o que estiver diferente do modelo.** Essa anotação é o rascunho da sua avaliação de fidelidade, que acontece na Sprint 7. Confira o folder contra o `modelo/checklist.md` só para saber onde está; não dê a nota oficial ainda. Se algum item estiver muito longe, use o resto da semana para melhorar.

**6. Escreva a verificação dos PDFs** em `testes/verificar_pdfs.py`. Ela confere se o gerador realmente criou os 10 arquivos e se nenhum saiu vazio (um PDF de 0 bytes acontece quando o programa dá erro no meio da gravação). É o mesmo jeito de trabalhar da Sprint 3: troque cada comentário numerado por código.

```python
import os

BIBLIOTECAS = ["fpdf2"]   # na Sprint 5, acrescente "reportlab"; na Sprint 6, "xhtml2pdf"

for biblioteca in BIBLIOTECAS:
    pasta = os.path.join("saidas", biblioteca)
    # 1. confira (assert) que a pasta existe
    # 2. monte a lista só com os arquivos da pasta que terminam em ".pdf"
    # 3. confira que a lista tem 10 arquivos
    # 4. para cada arquivo da lista, confira que o tamanho é maior que zero
    print(biblioteca, "ok:", len(pdfs), "PDFs")

print("Tudo certo.")
```

*Pesquise:* `os.path.isdir`, `os.listdir`, `str.endswith` (você já usou na Sprint 3) e `os.path.getsize`. Chame a lista do passo 2 de `pdfs`, porque é esse o nome que o `print` usa.

A verificação confere o que **já foi gerado**, então a ordem é sempre: primeiro `python geradores\gerar_fpdf2.py`, depois `python testes\verificar_pdfs.py`. Faça a sabotagem de propósito, como na Sprint 3: apague um dos PDFs, rode a verificação, veja o erro, e gere de novo.

### Como saber que deu certo

- A pasta `saidas/fpdf2/` tem 10 arquivos PDF.
- Abrindo qualquer um: a faixa azul está no topo, a imagem aparece sem deformar, os acentos estão certos e há número de página.
- A narrativa longa ocupa mais de uma página, e **a faixa e o rodapé se repetem** na segunda.
- O Ctrl+F acha uma palavra do texto.
- `python testes\verificar_pdfs.py` mostra `fpdf2 ok: 10 PDFs` e `Tudo certo.`

### Entrega da sprint

- [ ] `geradores/gerar_fpdf2.py` gerando os 10 folders, com a função `gerar_folder(narrativa, caminho_saida)`.
- [ ] Fontes DejaVu em `geradores/fontes/`.
- [ ] Teste da fonte padrão × DejaVu registrado no diário, com a mensagem de erro.
- [ ] Teste da imagem com `w` e com `w` + `h`, com prints.
- [ ] Print de um folder longo (as duas páginas) em `docs/evidencias/`.
- [ ] Diferenças em relação ao modelo anotadas no diário.
- [ ] Tempo que você levou para escrever o gerador, anotado no diário.
- [ ] `testes/verificar_pdfs.py` terminando com `Tudo certo`.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-4-escrita"></a>
## Sprint 4 · Escrita: Referencial Teórico, parte técnica e trabalhos relacionados (Entrega 3)

**Prazo: 12/11/2026**

Seções **2.3, 2.4 e 2.6**. Aproveite: você está vivendo agora o problema da fonte e da acentuação. Escreva a seção 2.3 **nesta semana**, com o problema fresco na cabeça.

### 2.3 O formato PDF e a geração programática de documentos (1,5 a 2 páginas)

**Pesquise:** o que é o **PDF** (*Portable Document Format*), a norma **ISO 32000** e por que ele se tornou o padrão para documentos que precisam ser impressos iguais em qualquer lugar. Procure também sobre **codificação de caracteres** (**Unicode**, **UTF-8** e **Latin-1**, também chamado ISO-8859-1) e sobre **fontes embutidas** em PDF. Bons pontos de partida: livros de introdução à computação ou à editoração eletrônica na biblioteca do campus, e o site do Unicode Consortium (`unicode.org`).

**Escreva:** o que é o PDF e qual problema ele resolve (o documento sai igual em qualquer computador e impressora). Depois, dois conceitos que você vai usar no TCC inteiro:

- **fontes e codificação de caracteres.** Um PDF guarda texto, e o texto precisa de uma fonte que contenha os caracteres usados. Fontes antigas cobrem só um conjunto limitado de caracteres, que **inclui** os acentos do português, mas **não inclui** coisas como a seta e, dependendo da biblioteca, o travessão e as reticências tipográficas. É por isso que uma biblioteca pode "engolir" um caractere ou dar erro. **Explique o conceito aqui; o caso concreto que você viveu na Sprint 4 vai nos Resultados**;
- **texto real × imagem de texto.** Um PDF pode conter o texto de verdade (dá para selecionar, copiar e pesquisar) ou apenas o desenho dele. Isso decide se o documento é acessível (ligue com a seção 2.5, que você já escreveu).

Depois, a **geração programática**: por que gerar documentos por programa, em vez de fazer à mão, quando o conteúdo vem de um acervo que cresce.

### 2.4 Bibliotecas Python para geração de PDF (2 páginas)

**Pesquise:** a documentação oficial da **FPDF2** (`py-pdf.github.io/fpdf2`), da **ReportLab** (`docs.reportlab.com`, especialmente o "ReportLab User Guide"), da **xhtml2pdf** (`xhtml2pdf.readthedocs.io`) e da **WeasyPrint** (`doc.courtbouillon.org/weasyprint`). Leia em cada uma a página de apresentação e a de instalação. Procure também comparações já publicadas entre elas (no Google Acadêmico: "PDF generation Python library comparison").

**Escreva:** apresente cada biblioteca em um parágrafo (o que é, como funciona, de onde veio, que licença tem) e, principalmente, **organize-as pelas duas formas de trabalhar**:

- **por coordenadas:** o programa diz a posição de cada elemento (FPDF2);
- **por descrição:** o programa descreve o conteúdo e a biblioteca encaixa na página, seja com blocos (ReportLab), seja com HTML e CSS (xhtml2pdf, WeasyPrint).

**Essa classificação é o eixo do seu TCC.** Ela explica quase todos os resultados que você vai apresentar: por que uma exige mais linhas de código, por que outra lida melhor com texto longo, por que outra é mais fácil de mudar.

Fale também sobre as **dependências**: algumas bibliotecas são Python puro e instalam com um comando; outras precisam de programas do sistema operacional. Na página de instalação da WeasyPrint, procure o que ela exige no Windows. **Fundamente isso aqui**, porque é o que vai explicar o caso da WeasyPrint nos Resultados.

> **Atenção:** a documentação oficial serve para **descrever a ferramenta**. Para **fundamentar conceito** (o que é PDF, o que é Unicode, o que é acessibilidade), use livro ou artigo, não a documentação.

### 2.6 Trabalhos relacionados (1,5 a 2 páginas)

**Pesquise:** trabalhos que **comparem bibliotecas ou ferramentas** de geração de documentos; trabalhos sobre **geração automática de material didático**; e trabalhos sobre **acervos digitais de cultura popular** que ofereçam material para *download*. Onde procurar: SBC OpenLib, BDTD, repositório do IFRN e de outros institutos federais, Google Acadêmico e SciELO. Termos de busca: "geração de relatórios em PDF", "comparação de bibliotecas Python", "geração automática de documentos", "acervo digital cultura popular", "report generation library comparison".

**Escreva:** de **3 a 4 trabalhos**, um parágrafo cada, dizendo: o que foi comparado ou feito, **como foi avaliado** (esta é a informação que mais importa para você) e qual a limitação. Feche com um **quadro comparativo** entre eles e o seu trabalho, com colunas como: o que foi comparado; quantas ferramentas; critérios usados; havia critério definido antes?; houve medição repetida?; domínio de aplicação.

**Esse quadro é o argumento de originalidade do seu TCC.** Preste atenção a um ponto provável: comparações de bibliotecas de PDF costumam aparecer em blogs e tutoriais, com opinião e sem medição. Se for esse o caso do que você encontrar, **diga isso explicitamente**: a sua contribuição passa a ser justamente fazer a comparação **com método** (critério escrito antes, medições repetidas, o mesmo folder nas três bibliotecas e um documento real de um projeto real).

**E se você não achar quase nada?** Não invente. Escreva que a literatura acadêmica sobre o assunto é escassa, que o material disponível é majoritariamente técnico e não avaliado, e **amplie a busca** para trabalhos sobre comparação de bibliotecas de software em geral ou sobre geração de relatórios. Use os trabalhos mais próximos que encontrar e diga em que eles se diferenciam do seu.

### Entrega

- [ ] Seções 2.3, 2.4 e 2.6 escritas, com citações.
- [ ] Quadro comparativo dos trabalhos relacionados, com identificação em cima e fonte embaixo.
- [ ] Comentários da Entrega 2 todos resolvidos.
- [ ] Todas as obras citadas nas Referências.
- [ ] Versão nomeada: `Entrega 3 – Referencial parte 2 – 12/11`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 5 — 13/11 a 19/11/2026

<a id="sprint-5-dev"></a>
## Sprint 5 · Desenvolvimento: biblioteca 2, o mesmo folder com ReportLab

**Branch:** `feature/gerador-reportlab`

**O que você vai entregar:** o **mesmo folder**, gerado pela biblioteca ReportLab, para as 10 narrativas, conferido pela verificação dos PDFs.

**Como essa biblioteca pensa:** você monta uma **lista de blocos** (um parágrafo, uma imagem, um espaço) e entrega para a biblioteca, que se encarrega de encaixar tudo nas páginas. É diferente da FPDF2, em que você diz as coordenadas. Essa diferença de pensamento é um dos assuntos mais interessantes do seu TCC.

**Documentação:** https://docs.reportlab.com/ . O capítulo que mais importa é o do **PLATYPUS** ("Page Layout and Typography Using Scripts"), no *ReportLab User Guide*.

### Passo a passo

**1. Repita o teste dos caracteres especiais.** Gere um PDF mínimo com a fonte padrão da ReportLab (`Helvetica`) e a frase `Travessão — reticências… aspas “curvas” seta →`. Anote no diário o que acontece com cada caractere. Atenção: a ReportLab **pode não dar erro** e simplesmente desenhar um quadradinho preto ou nada no lugar do caractere. Olhe com atenção, com zoom.

Depois registre a DejaVu Sans. *Pesquise:* `pdfmetrics.registerFont` e `TTFont` (em `reportlab.pdfbase`) e, para que `<b>` e `<i>` funcionem dentro dos parágrafos com a fonte nova, `registerFontFamily`. Compare com o que foi preciso fazer na FPDF2.

**2. Entenda as peças da ReportLab que você vai usar:**

| Peça | Para que serve no folder |
|---|---|
| `SimpleDocTemplate` | o documento: tamanho da página (`A4`) e margens |
| `ParagraphStyle` | um "estilo" (fonte, tamanho, cor, alinhamento, espaçamento). Você define uma vez e aplica em vários parágrafos |
| `Paragraph` | um bloco de texto, que quebra linhas sozinho |
| `Spacer` | um espaço em branco vertical |
| `Image` | a imagem. Atenção ao parâmetro `kind="proportional"` |
| `Table` e `TableStyle` | uma tabela. **Serve para fazer a caixa com borda** (item 7), com uma tabela de uma célula só |
| `doc.build(blocos, onFirstPage=..., onLaterPages=...)` | monta o PDF. As duas funções passadas são chamadas a cada página, e é nelas que você desenha a faixa e o rodapé |
| `canvas.setFillColor`, `canvas.rect`, `canvas.drawCentredString`, `canvas.drawString`, `canvas.drawRightString` | desenhar dentro da função de cabeçalho e rodapé |
| `cm` (em `reportlab.lib.units`) e `colors` (em `reportlab.lib`) | medidas e cores |

**Atenção a uma diferença importante:** na ReportLab, o ponto (0, 0) da página fica **embaixo, à esquerda**, e não em cima, como na FPDF2. Para desenhar a faixa no topo, você precisa calcular a posição a partir da altura da página.

**3. Escreva o gerador** em `geradores/gerar_reportlab.py`, com a mesma "cara" por fora (veja a regra no início da Sprint 4). Esqueleto:

```python
import os
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
# importe também o que precisar de reportlab.lib.styles, reportlab.lib.enums,
# reportlab.platypus e reportlab.pdfbase
from ler_narrativas import ler_todas

LARGURA, ALTURA = A4
AZUL = colors.Color(20 / 255, 60 / 255, 110 / 255)


def registrar_fontes():
    # registre DejaVu, DejaVu-Bold e DejaVu-Oblique e a família
    ...


def montar_estilos():
    # crie e devolva os estilos: TituloFolder, Dados, Legenda, Corpo, Chaves
    # com os mesmos tamanhos e cores do modelo
    ...


def cabecalho_rodape(canvas, doc):
    # chamada pela ReportLab em TODA página
    # itens 1, 8 e 9: faixa azul no topo, fonte bibliográfica e "Página N" no rodapé
    # dica: canvas.saveState() no começo e canvas.restoreState() no fim
    ...


def gerar_folder(narrativa, caminho_saida):
    # 1. registre as fontes e monte os estilos
    # 2. crie o SimpleDocTemplate com as margens (deixe espaço para a faixa e o rodapé)
    # 3. monte a lista de blocos, na ordem dos itens 2 a 7
    # 4. chame doc.build com a função de cabeçalho e rodapé nas duas opções
    ...


if __name__ == "__main__":
    # igual à FPDF2, salvando em saidas/reportlab
    ...
```

Como na FPDF2: **construa por partes**, gerando uma narrativa e abrindo o PDF a cada passo.

**Como a função de cabeçalho e rodapé sabe qual é a fonte bibliográfica?** Ela recebe o `doc`. Pense em como guardar a fonte bibliográfica no `doc` antes do `build`, como você fez com o objeto da FPDF2.

**4. Quatro armadilhas desta biblioteca. Todas viram anotação no diário:**

- **o `Paragraph` entende algumas marcações de HTML**, como `<b>` para negrito. Isso é ótimo, mas significa que um texto com `<` ou `&` **dá erro ou some**. **Teste de propósito**: coloque um `&` no texto de uma narrativa (em uma cópia, não no original), veja o que acontece e anote. Depois *pesquise* a função `escape` do módulo `xml.sax.saxutils` e use-a no texto das narrativas;
- **o `kind="proportional"` na imagem** faz ela caber na caixa sem deformar. Sem ele, ela estica para o tamanho exato que você pediu. Teste os dois jeitos, com print;
- **a caixa com borda não existe pronta:** teve de ser feita com uma tabela de uma célula. Anote isso como "esforço de implementação";
- **o rodapé desenhado com `drawString` não quebra linha.** Se a fonte bibliográfica for longa, ela passa da margem. Anote o que acontece e como você resolveu (por exemplo, cortando o texto ou usando um `Paragraph` desenhado no `canvas`; *pesquise:* `Paragraph.wrapOn` e `drawOn`).

**5. Gere os 10 folders**, coloque lado a lado com os da FPDF2 e compare. **Tire um print das duas versões do mesmo folder, lado a lado.** Essa é provavelmente uma das melhores figuras do seu TCC.

**6. Acrescente a ReportLab na verificação:** em `testes/verificar_pdfs.py`, a lista fica `BIBLIOTECAS = ["fpdf2", "reportlab"]`. Rode e confira que as duas aparecem com `ok`.

### Como saber que deu certo

- A pasta `saidas/reportlab/` tem 10 PDFs.
- O folder está **visualmente igual** ao da FPDF2 (pequenas diferenças são esperadas, e são justamente o objeto do estudo).
- A narrativa longa passa de página, com faixa e rodapé repetidos.
- `python testes\verificar_pdfs.py` mostra `fpdf2 ok` e `reportlab ok`, com 10 PDFs cada, e `Tudo certo.`

### Entrega da sprint

- [ ] `geradores/gerar_reportlab.py` gerando os 10 folders, com a função `gerar_folder(narrativa, caminho_saida)`.
- [ ] Teste dos caracteres especiais com a fonte padrão e com a DejaVu, anotado.
- [ ] As quatro armadilhas testadas e anotadas no diário, com prints.
- [ ] Print do mesmo folder nas duas bibliotecas, lado a lado.
- [ ] Tempo que você levou para escrever o gerador, anotado.
- [ ] `testes/verificar_pdfs.py` com a ReportLab, terminando com `Tudo certo`.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-5-escrita"></a>
## Sprint 5 · Escrita: Metodologia (Entrega 4)

**Prazo: 19/11/2026**

Seções **3.1 a 3.5**: como o trabalho é conduzido. Linguagem impessoal. Como você ainda não terminou, **escreva no futuro** ("serão comparadas") onde for o caso e passe para o passado na Sprint 8. De 4 a 5 páginas.

**Antes de escrever:** abra a pasta com metodologias de outros trabalhos já orientados e leia pelo menos duas: https://drive.google.com/drive/folders/1OwAjk47aQWuRKLf-ktesizSax9csEtXO?usp=sharing

### 3.1 Classificação da pesquisa

**Pesquise:** GIL, Antonio Carlos. *Como elaborar projetos de pesquisa*. 6. ed. São Paulo: Atlas, 2017; e PRODANOV, Cleber Cristiano; FREITAS, Ernani Cesar de. *Metodologia do trabalho científico*. 2. ed. Novo Hamburgo: Feevale, 2013 (este tem PDF gratuito no site da Feevale). Leia os capítulos sobre classificação das pesquisas.

**Escreva** a classificação pelos quatro critérios, **justificando cada um** com uma frase que ligue o critério ao seu trabalho:

- **natureza:** aplicada, porque gera conhecimento para uma decisão concreta da equipe do projeto Narrativas;
- **objetivos:** exploratória e descritiva, porque descreve e compara o comportamento das bibliotecas em uma situação ainda não estudada nesse contexto;
- **abordagem:** quantitativa, com apoio qualitativo: as notas, os tempos e os tamanhos são números, e a análise das dificuldades de implementação é qualitativa;
- **procedimentos:** **experimental**, combinada com pesquisa bibliográfica. Você muda uma coisa (a biblioteca), mantém todo o resto igual (o mesmo folder, o mesmo acervo, a mesma máquina, a mesma fonte) e observa o efeito.

Diga **o que variou e o que foi mantido fixo**: variou a biblioteca; foram mantidos o modelo do folder, a fonte, o acervo, a máquina, a lista de conferência e o protocolo de medição.

### 3.2 Pergunta de pesquisa

Enuncie a pergunta principal em uma frase e, abaixo dela, **as perguntas menores** que os Resultados vão responder uma a uma. Reescreva com as suas palavras:

- qual biblioteca reproduz com mais fidelidade o modelo de folder definido?
- como as bibliotecas se comportam em desempenho e tamanho do arquivo, e isso muda conforme o tamanho da narrativa?
- todas geram um PDF com texto pesquisável e com a acentuação correta?
- e a pergunta prática, que fecha o trabalho: **qual delas o projeto Narrativas deve adotar, e em que condição essa resposta mudaria?**

Todas serão respondidas na Conclusão, **com recomendação explícita**.

### 3.3 Desenho da comparação

Este é o coração da sua Metodologia. **Escreva:**

- **o mesmo folder nas três bibliotecas**, com a justificativa: assim a única variável é a biblioteca. Se os folders fossem diferentes, não daria para saber se a diferença veio da ferramenta ou de quem programou. Dedique um parágrafo inteiro a isso, incluindo a decisão de usar **a mesma fonte** (DejaVu Sans) nas três;
- **o mesmo acervo** nas três, com as mesmas dez narrativas;
- **a mesma máquina, na mesma sessão de medição**;
- **a lista de conferência foi escrita ANTES** de qualquer folder ser gerado. Explique por quê: se o critério fosse escrito depois, ele acabaria favorecendo a biblioteca de que o autor mais gostou. Isso é uma proteção contra viés, e declarar que você a tomou vale muito;
- **a avaliação da fidelidade feita item por item, nas três bibliotecas ao mesmo tempo**, com uma justificativa escrita para toda nota diferente de 2, o que deixa cada nota conferível por qualquer leitor;
- **a ausência de banco de dados:** o objeto do trabalho é a geração do PDF; as narrativas foram armazenadas em arquivos de texto porque um banco acrescentaria complexidade sem alterar nenhum resultado, já que as bibliotecas receberiam os mesmos dados de qualquer forma. **Escreva isso como decisão de método consciente**, e não como limitação.

Faça uma **figura** com o desenho do experimento: o acervo (arquivos `.txt` e imagens) → o leitor de narrativas → os três geradores → os PDFs → as medições automáticas e a avaliação pela lista de conferência → o quadro comparativo. Use o `app.diagrams.net`, exporte como PNG e insira com identificação em cima e fonte embaixo ("Fonte: elaborado pelo autor (2026)").

### 3.4 O acervo de teste e o modelo do folder

**Escreva:**

- **de onde vieram as narrativas:** a obra, o autor, a edição e **por que está em domínio público** (Lei nº 9.610/1998, que você vai lançar nas Referências). Informe quantas são, a variação de tamanho entre elas (o menor e o maior número de caracteres) e **por que a variação importa**: as narrativas longas são as que fazem o folder passar de página, que é onde as bibliotecas mais se diferenciam. Diga também que a grafia original da edição foi mantida;
- **de onde vieram as imagens** e qual a licença de cada uma (pode ser um quadro, a partir do `imagens/creditos.md`);
- **o modelo do folder:** apresente a figura do modelo (`modelo/modelo_folder.png`) e descreva os dez elementos. Justifique as escolhas: por que A4, por que imagem grande, por que caixa de palavras-chave, por que as cores conversam com o protótipo da plataforma. Cada elemento foi escolhido porque exercita algo diferente nas bibliotecas; diga isso;
- **a lista de conferência e a escala de 0 a 2**, com o significado de cada nota (pode ser um quadro).

### 3.5 Protocolo de medição

Descreva como as medições **serão** feitas (na Sprint 7), **justificando cada escolha**, não apenas declarando:

- cada folder será gerado **6 vezes**, e a primeira execução será descartada, porque a primeira é sempre a mais lenta: o programa ainda está carregando coisas na memória (**aquecimento**);
- será usada a **mediana**, e não a média, porque a mediana não é distorcida por uma medição atípica;
- a máquina estará **sem outros programas abertos**;
- o texto do PDF será extraído com a biblioteca `pypdf`, e a acentuação será verificada procurando, no texto extraído, **todas as palavras acentuadas do texto original**;
- o esforço de implementação será medido pelo **número de linhas de código** de cada gerador, contadas sem linhas vazias e sem comentários e, no caso da biblioteca que usa HTML, **somando também as linhas do arquivo HTML**, para a comparação ser justa.

**Cada justificativa dessas é uma frase que mostra domínio do método**, e é o que separa um trabalho acadêmico de um relato.

### Entrega

- [ ] Seções 3.1 a 3.5 escritas.
- [ ] Figura do desenho da comparação.
- [ ] Figura do modelo do folder e quadro da lista de conferência.
- [ ] Gil (2017), Prodanov e Freitas (2013) e a Lei nº 9.610/1998 nas Referências.
- [ ] Comentários da Entrega 3 todos resolvidos.
- [ ] Versão nomeada: `Entrega 4 – Metodologia – 19/11`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 6 — 20/11 a 26/11/2026

<a id="sprint-6-dev"></a>
## Sprint 6 · Desenvolvimento: biblioteca 3 (xhtml2pdf) e a quarta biblioteca (WeasyPrint)

**Branch:** `feature/gerador-xhtml2pdf`

**O que você vai entregar:** o mesmo folder feito a partir de HTML e CSS com a xhtml2pdf, e o registro do que aconteceu ao tentar usar a WeasyPrint.

Lembre que 20/11, o primeiro dia desta sprint (sexta), é feriado: a semana tem um dia útil a menos.

**Como essa biblioteca pensa:** você **não programa o leiaute**. Você escreve uma página HTML com CSS, como se fosse um site, e a biblioteca transforma em PDF. É uma forma completamente diferente das duas anteriores, e é o contraste mais interessante do seu trabalho.

**Documentação:** https://xhtml2pdf.readthedocs.io/ . Leia "Usage" e a parte sobre **CSS suportado**, **`@page`**, **`@frame`** e **`@font-face`**.

### Parte A — xhtml2pdf

**1. Se você não conhece HTML e CSS,** comece pelo básico, uma hora no máximo: o tutorial de HTML e o de CSS da MDN, em português (`developer.mozilla.org/pt-BR/docs/Learn`). Você só precisa de: `div`, `h1`, `p`, `img`, atributos `class` e `id`, e as propriedades de CSS `font-size`, `font-weight`, `font-style`, `color`, `background-color`, `text-align`, `border`, `padding`, `margin`.

**2. Repita o teste dos caracteres especiais**, como nas outras duas: um HTML mínimo, com a frase de teste, convertido com a fonte padrão. Anote o que acontece. Depois, descubra na documentação como usar a DejaVu Sans com `@font-face`. **Atenção:** o caminho do arquivo da fonte provavelmente vai precisar ser **absoluto**, como o das imagens (veja a armadilha abaixo).

**3. Escreva o modelo em HTML** em `geradores/modelo_folder.html`. É um HTML comum, com **marcadores** no lugar dos dados, que o Python vai trocar pelos dados de cada narrativa. Use estes marcadores: `{titulo}`, `{tipo}`, `{origem}`, `{publico}`, `{imagem}`, `{paragrafos}`, `{palavras}`, `{fonte}`, `{caminho_fontes}`.

O que o HTML precisa ter, item por item:

| Item | Como fazer em HTML/CSS |
|---|---|
| Página A4 e margens | regra `@page` com `size: a4 portrait` e `margin` |
| 1 – Faixa no topo, **em todas as páginas** | um `div` com fundo azul. Para ele se repetir em todas as páginas, *pesquise* na documentação os **frames estáticos**: `@frame` com `-pdf-frame-content` |
| 2, 3 – Título e linha de dados | `h1` e um `div` com classe própria |
| 4, 5 – Imagem e legenda | `img` com `width` e um `div` para a legenda |
| 6 – Texto | um `p` por parágrafo, com `text-align: justify` |
| 7 – Caixa de palavras-chave | um `div` com `border` e `padding` |
| 8, 9 – Rodapé com fonte e número da página | outro frame estático, no rodapé, com a fonte bibliográfica e a marcação `<pdf:pagenumber>` |
| Fonte | `@font-face` com a DejaVu e `font-family` no `body` |

Comece com um HTML **sem marcadores**, com os dados de uma narrativa escritos à mão, e abra-o primeiro no navegador para ver a estrutura. Só depois converta com a xhtml2pdf e, por último, troque os dados pelos marcadores.

**4. Escreva o gerador** em `geradores/gerar_xhtml2pdf.py`, com a mesma "cara" por fora. O que ele faz, na ordem:

1. lê o arquivo `geradores/modelo_folder.html` **uma vez**, no começo do programa, para uma variável (com `encoding="utf-8"`);
2. em `gerar_folder`: monta o HTML dos parágrafos, transformando cada parágrafo do texto em `<p class="corpo">...</p>` e juntando tudo em uma *string* (*pesquise:* `"".join(...)`);
3. troca cada marcador pelo dado da narrativa (*pesquise:* `str.replace`, que pode ser encadeado: `modelo.replace(...).replace(...)`). Para `{imagem}` e `{caminho_fontes}`, use **caminhos absolutos** (*pesquise:* `os.path.abspath`);
4. abre o arquivo de saída em modo binário (`"wb"`) e chama `pisa.CreatePDF(html, dest=arquivo, encoding="utf-8")`;
5. confere o resultado: o objeto devolvido tem o atributo `err`. Se for diferente de zero, mostre uma mensagem de erro.

**5. Três armadilhas desta biblioteca:**

- **o caminho da imagem precisa ser absoluto.** Se você usar caminho relativo, a imagem simplesmente não aparece, **e não dá erro**, o que é pior. Teste com caminho relativo de propósito, tire print e anote;
- **ela entende só uma parte do CSS.** Coisas comuns em sites (*flexbox*, *grid*, sombras, cantos arredondados) **não funcionam**. Descobrir o que funciona e o que não funciona é parte do trabalho: **anote cada coisa que você tentou e não deu certo**, em uma lista no diário;
- **texto com `<` ou `&` quebra o HTML**, como na ReportLab. *Pesquise:* a função `escape` do módulo `html` e use-a nos dados das narrativas.

**6. Compare com as outras duas.** O texto justificado ficou igual? A faixa ficou da mesma cor e se repete na página 2? A caixa de palavras-chave ficou do mesmo tamanho? A imagem ficou no mesmo lugar? **Tire um print do mesmo folder nas três bibliotecas, lado a lado.**

**7. Anote o tempo de escrita e a sua impressão sobre a facilidade.** Foi mais fácil ou mais difícil que as outras? Por quê? Se você já sabia HTML e CSS, isso conta, e é uma observação legítima para o TCC, desde que você diga que é a sua percepção, e não uma medida.

**8. Acrescente a xhtml2pdf na verificação:** `BIBLIOTECAS = ["fpdf2", "reportlab", "xhtml2pdf"]` em `testes/verificar_pdfs.py`. Rode e confira as três com `ok`.

### Parte B — A quarta biblioteca: WeasyPrint

A WeasyPrint também gera PDF a partir de HTML e CSS, com suporte a CSS bem mais moderno que a xhtml2pdf. Ela é muito bem avaliada, mas tem uma particularidade que é o objeto desta parte.

**1. Leia a página de instalação da WeasyPrint** (`doc.courtbouillon.org/weasyprint/stable/first_steps.html`), na parte de Windows. Anote o que ela diz que é necessário além do `pip`.

**2. Tente instalar e usar,** com o `.venv` ativo:

```
pip install weasyprint
```

Anote no `docs/instalacao.md`, como fez com as outras: tempo, avisos, pacotes. Depois crie `estudos/sprint6/teste_weasyprint.py`, que importa a classe `HTML` do módulo `weasyprint` e gera um PDF a partir de uma *string* HTML mínima (*pesquise* o primeiro exemplo da documentação: `HTML(string=...).write_pdf(...)`). Rode.

**O que provavelmente vai acontecer:** no Windows, a WeasyPrint precisa de programas auxiliares do sistema (as bibliotecas **Pango**, que vêm com o **GTK**) que **não vêm pelo `pip`** e exigem um instalador, justamente o que as máquinas do laboratório não permitem. O `pip install` costuma terminar sem erro, mas na hora de importar ou usar aparece uma mensagem dizendo que uma biblioteca (`gobject-2.0-0` ou parecida) não pôde ser carregada.

**3. Seja qual for o resultado, ele é um achado do trabalho:**

- **se instalar e funcionar:** implemente o folder nela também (`geradores/gerar_weasyprint.py`, com a mesma "cara" por fora, reaproveitando o seu HTML) e ela entra na comparação como quarta biblioteca;
- **se não funcionar:** **copie a mensagem de erro inteira**, tire um print (`docs/evidencias/s06_weasyprint_erro.png`) e registre em `docs/instalacao.md` exatamente o que você tentou, em que ordem, e o que apareceu. **Não tente instalar o GTK** nem procurar outro jeito de contornar: a pergunta é se ela funciona **neste ambiente**, e a resposta "não" já é a resposta. Depois desinstale com `pip uninstall weasyprint` e **não** a inclua no `requirements.txt`.

**Não esconda isso, e não trate como fracasso.** "Facilidade de instalação" é um dos critérios de comparação previstos desde o começo, e a equipe do Narrativas precisa saber que essa biblioteca não serve em um ambiente Windows sem privilégios de administração. **Esse é um dos resultados mais úteis do seu trabalho**, porque é o tipo de coisa que só se descobre tentando.

### Como saber que deu certo

- A pasta `saidas/xhtml2pdf/` tem 10 PDFs, visualmente parecidos com os das outras duas.
- A imagem aparece (se não aparecer, é o caminho relativo).
- O que aconteceu com a WeasyPrint está registrado por escrito, com print e com a mensagem de erro inteira.
- `python testes\verificar_pdfs.py` mostra as três bibliotecas com `ok` e `Tudo certo.`

### Entrega da sprint

- [ ] `geradores/gerar_xhtml2pdf.py` e `geradores/modelo_folder.html` gerando os 10 folders.
- [ ] Teste dos caracteres especiais com a fonte padrão e com a DejaVu, anotado.
- [ ] Lista do que funcionou e do que não funcionou no CSS, no diário.
- [ ] As três armadilhas testadas e anotadas, com prints.
- [ ] Tentativa com a WeasyPrint documentada em `docs/instalacao.md`, com print e mensagem de erro.
- [ ] Print do mesmo folder nas três bibliotecas, lado a lado.
- [ ] Tempo de escrita do gerador e impressão sobre a facilidade, anotados.
- [ ] `testes/verificar_pdfs.py` com as três bibliotecas, terminando com `Tudo certo`.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-6-escrita"></a>
## Sprint 6 · Escrita: Materiais e métodos (Entrega 5)

**Prazo: 26/11/2026**

Seção **3.6**. Vale a analogia das orientações de escrita: **lista de ingredientes** (materiais) mais **modo de preparo** (métodos). Esta seção é o que permite (ou impede) outra pessoa repetir o seu trabalho. De 2 a 3 páginas. Aqui você já pode escrever **no passado**: as três bibliotecas estão prontas.

### Materiais

Para **cada** item: **o que é** (uma ou duas frases), **para que foi usado** e **qual a versão** (está no seu `docs/ambiente.md` e no `requirements.txt`). Pode ser um quadro.

| Ferramenta | O que dizer além da versão |
|---|---|
| Python | linguagem usada nos três geradores |
| **FPDF2** | biblioteca de geração de PDF por coordenadas |
| **ReportLab** | biblioteca de geração de PDF por blocos |
| **xhtml2pdf** | biblioteca que converte HTML e CSS em PDF |
| **WeasyPrint** | quarta biblioteca; **a instalação foi tentada e o uso não foi possível** (ver Resultados) |
| `pypdf` | extração do texto dos PDFs gerados, para verificar acessibilidade e acentuação |
| `matplotlib` | geração dos gráficos; também forneceu a fonte DejaVu Sans |
| DejaVu Sans | fonte usada em todos os folders, com a licença dela |
| Módulos `csv`, `os`, `time` e `statistics` | já vêm com o Python: planilhas, arquivos, cronometragem e estatística |
| Git e GitHub | versionamento, com o fluxo de *branches* e revisão por *pull request* do NIC |
| VS Code e diagrams.net | edição do código e desenho do modelo e das figuras |

**Duas justificativas são obrigatórias:**

1. **por que essas bibliotecas, e não outras.** O critério foi: serem gratuitas, serem usadas em projetos reais e **poderem ser instaladas apenas com `pip`**, porque o ambiente disponível não permite instalar programas. Declare esse critério: ele é legítimo, é realista e explica por que ferramentas que dependem de um programa externo (como as que usam o `wkhtmltopdf` ou um navegador) ficaram de fora;
2. **por que arquivos de texto e não banco de dados** (retome em uma frase o que escreveu na 3.3).

**Ambiente de execução (sem isto o trabalho não é reproduzível):** processador, memória RAM, sistema operacional e versão, versão do Python e versão exata de cada biblioteca. A **data das medições** você acrescenta na Sprint 8, copiando de `docs/ambiente.md`.

### Métodos

**a) O acervo.** Quantas narrativas, de onde vieram, como foram organizadas nos arquivos. **Mostre a estrutura de um arquivo** como figura (um print do VS Code com um `.txt` aberto, cortando o texto da narrativa).

**b) O leitor de narrativas.** Em um parágrafo, como o `ler_narrativas.py` transforma cada arquivo em um dicionário, e como os três geradores recebem exatamente os mesmos dados.

**c) Os três geradores.** Um parágrafo por biblioteca, dizendo **como o folder foi construído nela**, com um trecho curto de código quando ele esclarecer (no máximo 10 linhas, como figura ou quadro). Seja preciso, e use o que você anotou no diário:

- **FPDF2:** a faixa e o rodapé foram feitos sobrescrevendo os métodos `header` e `footer`; o texto foi posicionado com `multi_cell`; **a fonte padrão precisou ser trocada pela DejaVu Sans** (diga por quê);
- **ReportLab:** os elementos foram montados como uma lista de blocos e entregues ao documento, que cuidou da paginação; a faixa e o rodapé foram desenhados por uma função chamada a cada página; **a caixa com borda precisou ser feita com uma tabela de uma célula**; o texto precisou ser "escapado" por causa das marcações;
- **xhtml2pdf:** o folder foi descrito em um arquivo HTML com CSS, e os dados foram substituídos no modelo antes da conversão; **os caminhos da imagem e da fonte precisaram ser absolutos**; parte do CSS não é suportada (diga o que você tentou e não funcionou).

"Foi utilizado `multi_cell` com alinhamento justificado" é informação reproduzível; "o texto foi formatado adequadamente" não é.

**d) As verificações automáticas.** Em duas frases: o que os dois programas de verificação conferem (a leitura das dez narrativas, com todos os campos, e a criação dos dez PDFs de cada biblioteca) e por que eles existem (garantir que uma mudança em um gerador não quebrou a leitura nem a geração).

**e) As medições automáticas e a avaliação da fidelidade.** Por enquanto, escreva um parágrafo curto dizendo que serão feitas conforme o protocolo da seção 3.5. Você completa na Sprint 8.

### Entrega

- [ ] Seção 3.6 escrita, com o quadro de materiais e as versões.
- [ ] As duas justificativas obrigatórias.
- [ ] Ambiente de execução completo (menos a data da medição).
- [ ] Um parágrafo por gerador, com o que foi específico de cada biblioteca.
- [ ] Figura da estrutura de um arquivo de narrativa.
- [ ] Comentários da Entrega 4 todos resolvidos.
- [ ] Versão nomeada: `Entrega 5 – Materiais e métodos – 26/11`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 7 — 27/11 a 03/12/2026

<a id="sprint-7-dev"></a>
## Sprint 7 · Desenvolvimento: medições, fidelidade do leiaute e gráficos

**Branch:** `feature/medicoes-e-graficos`

**O que você vai entregar:** um programa que mede sozinho o tempo, o tamanho, as páginas, a acentuação e o texto pesquisável dos PDFs das três bibliotecas, com uma planilha de resultados; a contagem de linhas de código; a nota de fidelidade de cada biblioteca; e os quatro gráficos do TCC.

Até aqui você olhou os folders. Agora você vai **medir**. É esta sprint que transforma o trabalho em pesquisa.

**Os Resultados do TCC vencem nesta mesma quinta-feira.** Por isso a ordem e os dias importam:

| Dia | O que fazer |
|---|---|
| sexta, 27/11, e segunda, 30/11 | Parte A: escrever o `medir.py` e rodar a medição oficial **até segunda** |
| terça, 01/12 | Parte B: a avaliação da fidelidade |
| quarta, 02/12 | Parte C: os gráficos; diário, *commits* e PR |
| quinta, 03/12 | só a escrita dos Resultados |

### Parte A — As medições objetivas

**A1. Entenda o que vai ser medido, e por quê:**

| Medida | Como se mede | Por que importa |
|---|---|---|
| **Tempo de geração** | cronômetro em volta da chamada que gera o folder | se a plataforma gerar o PDF na hora do clique, o usuário espera |
| **Tamanho do arquivo** | `os.path.getsize` | arquivo grande demora para baixar e ocupa espaço no servidor |
| **Número de páginas** | quantidade de páginas do PDF, com o `pypdf` | mostra se a biblioteca aproveitou bem o espaço |
| **Texto pesquisável** | quantidade de caracteres extraídos do PDF com o `pypdf` | se não der para extrair, o PDF é inacessível para leitores de tela |
| **Acentuação** | quantas palavras acentuadas do texto original aparecem iguais no texto extraído | palavra com acento quebrado é erro grave em português |
| **Linhas de código** | contar as linhas de cada gerador | mede o esforço de implementação e de manutenção |

**A2. Escreva o programa de medição** em `medir.py`, na raiz do repositório. Ele é organizado em quatro funções e um `main`. Para cada uma, eu digo o que recebe, o que faz e o que devolve; o código é com você.

```python
import csv
import os
import statistics
import sys
import time
from pypdf import PdfReader

sys.path.insert(0, "geradores")
from ler_narrativas import ler_todas
import gerar_fpdf2
import gerar_reportlab
import gerar_xhtml2pdf

BIBLIOTECAS = {
    "fpdf2": gerar_fpdf2,
    "reportlab": gerar_reportlab,
    "xhtml2pdf": gerar_xhtml2pdf,
}
REPETICOES = 6
```

- **`medir_tempo(modulo, narrativa, caminho)`:** chama `modulo.gerar_folder(narrativa, caminho)` **6 vezes** (`REPETICOES`), cronometrando cada chamada com `time.perf_counter()` (como no seu `ex04` da Sprint 1), em milissegundos. **Descarta a primeira medição** e devolve a **mediana** e o **desvio-padrão** das outras cinco. *Pesquise:* `statistics.median`, `statistics.stdev` e como pegar uma lista sem o primeiro item (fatiamento, `lista[1:]`).
- **`analisar_pdf(caminho)`:** abre o PDF com `PdfReader` (*pesquise:* `PdfReader`, `pages` e `extract_text()` na documentação do pypdf, `pypdf.readthedocs.io`), junta o texto extraído de todas as páginas (`pagina.extract_text()`; se vier `None`, use texto vazio) e devolve **o número de páginas** e **o texto extraído**.
- **`palavras_acentuadas(texto)`:** devolve o **conjunto** de palavras do texto que têm pelo menos uma letra acentuada (`áàâãéêíóôõúüç` e as maiúsculas). Passos: separe o texto em palavras (`split()`); de cada palavra, tire a pontuação das pontas (*pesquise:* `strip` com um texto de caracteres, como `".,;:!?—…\"'()“”"`); guarde a palavra em minúsculas se ela tiver alguma letra acentuada (*pesquise:* `any(...)`). *Pesquise:* `set()`, para não contar a mesma palavra duas vezes.
- **`taxa_acentuacao(texto_pdf, texto_original)`:** pega as palavras acentuadas do texto **original** e conta quantas delas aparecem no texto **extraído do PDF** (em minúsculas). Devolve a proporção, de 0 a 1 (1 quer dizer que todas apareceram certas).
- **`main()`:** para cada narrativa e para cada biblioteca: monta o caminho de saída (`saidas/<biblioteca>/<nome>.pdf`), mede o tempo, mede o tamanho em KB, analisa o PDF e calcula a taxa de acentuação. Guarda tudo em um dicionário por combinação e, no fim, grava a lista de dicionários em `resultados/medicoes.csv`. *Pesquise:* `csv.DictWriter`, `writeheader` e `writerows`. Abra o arquivo com `newline=""` e `encoding="utf-8"`. Mostre uma linha na tela a cada combinação, para você acompanhar.

As colunas do `medicoes.csv` são, nesta ordem: `biblioteca`, `narrativa`, `caracteres` (do texto original), `tempo_ms`, `desvio_ms`, `tamanho_kb`, `paginas`, `texto_extraido` (quantidade de caracteres extraídos) e `acentos_ok` (a taxa). Arredonde os números para duas casas (*pesquise:* `round`).

**A3. Entenda duas decisões do programa.** As duas vão para o TCC (você já escreveu na 3.5):

- **por que repetir 6 vezes e descartar a primeira?** Porque a primeira execução ainda está carregando coisas na memória e é sempre a mais lenta. Isso se chama **aquecimento**. Uma medição de tempo feita uma vez só não vale nada;
- **por que a mediana, e não a média?** Porque a mediana não é estragada por uma medição esquisita, que acontece quando o Windows resolve fazer outra coisa no meio.

**A4. Rode as medições seguindo o protocolo, até segunda-feira (30/11).** Antes de rodar: **feche o navegador, o Drive e tudo o mais que estiver aberto**, deixando só o terminal. Rode `python medir.py`. Pode levar alguns minutos. **Esta é a medição oficial, a que vai para o TCC**: rode-a uma vez só, de ponta a ponta, no mesmo dia e na mesma máquina. Se precisar corrigir o programa e rodar de novo, renomeie o arquivo anterior (por exemplo, `medicoes_v1.csv`) em vez de apagá-lo, e anote no diário por que rodou de novo.

**A5. Conte as linhas de código** com um programinha seu, `contar_linhas.py`, que, para cada arquivo de gerador (e para o `modelo_folder.html`), conta as linhas que **não** estão vazias e **não** começam com `#` (no HTML, não começam com `<!--`), e grava `resultados/linhas_de_codigo.csv` com as colunas `arquivo` e `linhas`. Para a xhtml2pdf, **anote os dois números separados (Python e HTML) e o total**: metade do trabalho dela está no HTML, e sem somar a comparação fica injusta.

**A6. Olhe a planilha e desconfie de números estranhos.** Abra o `medicoes.csv` no Excel ou no Google Planilhas.

- Se alguma biblioteca aparecer com `texto_extraido` igual a zero, o PDF dela não é pesquisável. **Isso é um resultado importante**: confirme abrindo o arquivo e tentando o Ctrl+F;
- se `acentos_ok` der menos que 1, alguma palavra acentuada se perdeu na extração. Descubra **qual** (acrescente um `print` temporário no programa) e anote a palavra exata no diário. Pode ser problema da biblioteca ou só do jeito como o `pypdf` extraiu: abra o PDF e confira a palavra com os olhos;
- se um tempo for muito maior que os outros da mesma biblioteca, rode de novo e veja se se repete.

**A7. Registre o protocolo** no fim de `docs/ambiente.md`: quantas repetições, que a primeira foi descartada, que foi usada a mediana, que a máquina estava sem outros programas abertos e **a data e a hora da medição**.

> **Se `medir.py` der erro ao importar os geradores**, o motivo mais comum é que algum gerador executa código ao ser importado. Confira se o código que gera os 10 folders está **dentro** do `if __name__ == "__main__":`. Ele existe justamente para isso.

### Parte B — A fidelidade do leiaute

O tempo e o tamanho o computador mediu sozinho. **A fidelidade do leiaute quem avalia é você**, e por isso ela precisa de um método, senão vira opinião.

**B1. Monte a planilha de avaliação** em `resultados/fidelidade.csv`, com esta estrutura (as três últimas colunas são para as justificativas):

```
item,descricao,fpdf2,reportlab,xhtml2pdf,just_fpdf2,just_reportlab,just_xhtml2pdf
1,Faixa colorida no topo,,,,,,
2,Titulo grande e centralizado,,,,,,
3,Linha de dados em cinza,,,,,,
4,Imagem centralizada sem deformar,,,,,,
5,Legenda da imagem em italico,,,,,,
6,Texto justificado com espaco entre paragrafos,,,,,,
7,Caixa de palavras-chave com borda,,,,,,
8,Rodape com a fonte bibliografica,,,,,,
9,Numero da pagina,,,,,,
10,Faixa e rodape repetidos na pagina 2,,,,,,
```

**B2. Escolha a narrativa da avaliação:** a **mais longa** do acervo, porque só ela permite avaliar o item 10. Anote no diário qual foi.

**B3. Avalie, item por item.** Abra, lado a lado: o `modelo/modelo_folder.png` e os três PDFs **da mesma narrativa**. Dê a nota de cada item conforme a regra do `modelo/checklist.md`: **2** igual, **1** parecido com diferença visível, **0** não saiu ou saiu errado.

**Duas regras para a avaliação ser honesta:**

- **avalie um item por vez, nas três bibliotecas**, em vez de avaliar uma biblioteca inteira e depois a outra. Assim você compara o mesmo detalhe de uma vez e fica mais consistente;
- **escreva uma justificativa curta para toda nota diferente de 2.** "1 – a cor da faixa ficou mais clara que no modelo" é útil; "1" sozinho não é. Essas justificativas viram o texto da discussão dos resultados e são o que permite a qualquer leitor conferir as suas notas.

**B4. Some as notas.** Cada biblioteca faz de 0 a 20 pontos. Escreva os totais no diário.

Na reunião de acompanhamento da semana, mostre aos orientadores a planilha com as justificativas: conferimos com você os itens em que a nota ficou abaixo de 2.

### Parte C — Os gráficos

**C1. Faça os gráficos** com `graficos.py`, que lê as duas planilhas e gera as figuras com o `matplotlib`. **Gráfico feito por programa é reproduzível; print de planilha não é.** Faça quatro:

- **Gráfico 1 – fidelidade do leiaute:** três barras, uma por biblioteca, com a nota de 0 a 20. É a figura que resume o trabalho;
- **Gráfico 2 – tempo de geração:** três barras, com a média dos tempos medianos de cada biblioteca, em milissegundos, e a barra de erro (*pesquise* o parâmetro `yerr` de `plt.bar`);
- **Gráfico 3 – tamanho do arquivo:** três barras, com o tamanho médio em KB;
- **Gráfico 4 – tempo por tamanho da narrativa:** no eixo horizontal, o número de caracteres da narrativa; no vertical, o tempo; uma linha por biblioteca, com os pontos marcados. **Este é o gráfico mais interessante**, porque mostra se alguma biblioteca fica desproporcionalmente lenta com texto grande. *Pesquise:* `plt.plot` com `marker="o"` e `label`, e `plt.legend`. Lembre de **ordenar** os pontos pelo número de caracteres antes de desenhar a linha.

Organize o `graficos.py` em **uma função por gráfico**, mais uma função que lê as planilhas. As peças do `matplotlib` que você vai usar:

| Peça | Para que serve |
|---|---|
| `plt.figure(figsize=(6, 4))` | começa um gráfico novo, com tamanho |
| `plt.bar(nomes, valores)` | gráfico de barras |
| `plt.plot(x, y, marker="o", label=...)` | gráfico de linha |
| `plt.xlabel`, `plt.ylabel` | nome de cada eixo, **com a unidade** |
| `plt.ylim(0, ...)` | faz o eixo começar em zero |
| `plt.savefig("docs/evidencias/grafico1_fidelidade.png", dpi=150, bbox_inches="tight")` | salva a imagem |
| `plt.close()` | fecha o gráfico, para o próximo começar limpo |

**Não coloque título dentro do gráfico** (`plt.title`): no TCC, o título vai na identificação em cima da figura, segundo a ABNT. Escreva o que é cada eixo **e a unidade**, e faça o eixo vertical começar em zero.

### Como saber que deu certo

- `python medir.py` roda até o fim e cria `resultados/medicoes.csv` com **30 linhas** (10 narrativas × 3 bibliotecas), mais o cabeçalho.
- Os tempos fazem sentido (de alguns milissegundos a poucos segundos por folder), e `resultados/linhas_de_codigo.csv` existe.
- Você consegue responder, olhando a planilha: qual biblioteca é mais rápida? Qual gera o arquivo menor? Alguma perdeu acento? Alguma não tem texto pesquisável?
- `resultados/fidelidade.csv` está preenchido, com as justificativas das notas diferentes de 2.
- Os quatro gráficos estão em `docs/evidencias/`, gerados pelo `python graficos.py`.

### Entrega da sprint

- [ ] `medir.py` funcionando e `resultados/medicoes.csv` com as 30 linhas (medição oficial até 30/11).
- [ ] `contar_linhas.py` e `resultados/linhas_de_codigo.csv`.
- [ ] Protocolo de medição, com data e hora, em `docs/ambiente.md`.
- [ ] Qualquer número estranho investigado e explicado no diário.
- [ ] `resultados/fidelidade.csv` completo, com notas e justificativas, e as notas totais no diário.
- [ ] `graficos.py` gerando os quatro gráficos.
- [ ] As duas verificações terminando com `Tudo certo`.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-7-escrita"></a>
## Sprint 7 · Escrita: Resultados e discussão (Entrega 6)

**Prazo: 03/12/2026**

Seções **4.1 a 4.5 e 4.7**. A seção 4.6 (quadro e recomendação) fica para a Sprint 8. É a parte mais importante do TCC: de 7 a 10 páginas. Organize respondendo às **perguntas de pesquisa** da seção 3.2, na mesma ordem.

Como as medições terminam na segunda-feira (30/11), **comece a montar as tabelas na terça** e escreva a discussão na quarta e na quinta.

### Antes de escrever: monte as tabelas

**1. Crie no documento a estrutura do capítulo 4**, com os títulos das seções 4.1 a 4.7 (veja a [seção 8.3](#escrita-geral)).

**2. Monte as tabelas** com os números de `resultados/medicoes.csv`, seguindo as regras de tabela das orientações de escrita (identificação em cima, fonte embaixo, sem bordas laterais, e "Fonte: dados da pesquisa (2026)"):

- **na 4.3, "Desempenho e tamanho do arquivo por biblioteca":** uma linha por biblioteca e as colunas tempo mediano (ms), desvio (ms), tamanho médio (KB) e média de páginas. Para cada biblioteca, **calcule a média das 10 narrativas** (pode ser no Google Planilhas, com a função `MÉDIA`);
- **na 4.4, "Acentuação e texto pesquisável por biblioteca":** uma linha por biblioteca e as colunas taxa de acentuação (média), caracteres extraídos em relação ao original (%) e resultado do teste dos caracteres especiais com a fonte padrão (o que você anotou nas Sprints 4, 5 e 6);
- **na 4.5, "Instalação e esforço de implementação por biblioteca":** uma linha por biblioteca **incluindo a WeasyPrint** e as colunas pacotes instalados junto, problemas na instalação, linhas de código (Python + HTML) e horas para escrever o gerador.

- **na 4.2, "Fidelidade ao leiaute por biblioteca":** os dez itens nas linhas, as três bibliotecas nas colunas, com as notas de `resultados/fidelidade.csv` e o total.

> **Regra sem exceção:** toda figura, tabela ou quadro é **anunciado no texto antes** de aparecer e **explicado depois**. Nada de duas figuras seguidas sem texto entre elas.

### 4.1 Os folders gerados

Comece mostrando o produto. A melhor figura do seu TCC provavelmente é esta: **o mesmo folder, gerado pelas três bibliotecas, lado a lado** (você tirou esse print na Sprint 6). Deixe o leitor ver a diferença antes de explicá-la. Retome em uma ou duas frases os números do acervo (dez narrativas, tamanhos, origem).

### 4.2 Fidelidade ao leiaute

Tabela com os dez itens nas linhas e as três bibliotecas nas colunas, com as notas e o total. Depois, o Gráfico 1.

**Discuta item por item, com foco no que foi diferente.** Onde as três tiraram 2, uma frase resolve. Onde alguma tirou 0 ou 1, **explique o mecanismo**: não basta dizer "a caixa de palavras-chave ficou diferente"; diga *por que*: a biblioteca não tem um elemento pronto para isso, ou o CSS usado não é suportado. Use as justificativas da planilha e retome a classificação da seção 2.4 (coordenadas × descrição).

**Mostre que a nota não é só impressão:** diga que a lista de conferência foi escrita antes de qualquer folder ser gerado e que toda nota diferente de 2 tem justificativa (pode ir em uma coluna da tabela ou em um quadro logo abaixo).

### 4.3 Desempenho e tamanho do arquivo

Monte a tabela da 4.3 (veja "Antes de escrever") e acrescente os Gráficos 2, 3 e 4. Depois discuta:

- **qual é a mais rápida, e se a diferença tem importância prática.** Este é o ponto mais fácil de errar. Se todas gerarem o folder em menos de um segundo, **diga com todas as letras que o tempo não é critério de decisão neste caso**: o usuário não percebe a diferença. Essa é uma conclusão honesta e valiosa, muito melhor do que fingir que 80 ms contra 200 ms muda alguma coisa para quem clica no botão;
- **o comportamento com narrativas maiores**, com o Gráfico 4: alguma biblioteca fica desproporcionalmente lenta com texto longo? Se sim, o tempo volta a importar, porque o acervo vai crescer;
- **o tamanho do arquivo**, que importa para quem tem internet ruim (retome o que escreveu na 2.2). Se uma biblioteca gerar arquivos muito maiores, investigue por quê (normalmente é o jeito como a imagem ou a fonte é embutida) e diga.

### 4.4 Acentuação, imagens e acessibilidade

Os três andam juntos, porque respondem a "o folder funciona de verdade?".

- **Acentuação:** o resultado da verificação automática (a taxa) e, principalmente, **o caso concreto que você viveu**: a fonte padrão não cobria certos caracteres da frase de teste, o que exigiu registrar a DejaVu Sans. Compare o que aconteceu nas três bibliotecas (deu erro? sumiu em silêncio? apareceu um quadradinho?). **Explique o mecanismo** usando o conceito de codificação de caracteres da seção 2.3: é a melhor amarração entre teoria e resultado do seu TCC;
- **imagens:** se alguma biblioteca deformou a imagem quando você informou largura e altura, mostre a figura. Uma imagem esticada é um erro que o leitor entende na hora;
- **acessibilidade:** para cada biblioteca, se o texto do PDF é extraível e quanto foi extraído em relação ao original. Retome o argumento da seção 2.5: um material didático que o leitor de tela não lê contraria o objetivo de democratizar o acesso.

### 4.5 Facilidade de instalação e esforço de implementação

Monte a tabela da 4.5 e discuta as linhas de código e o tempo de escrita de cada gerador, e **declare a limitação junto**: a ordem em que você implementou influencia o resultado, porque na terceira biblioteca você já sabia exatamente o que fazer. Reconhecer isso vale mais do que esconder.

**E aqui vem o resultado que dá caráter ao seu trabalho: o caso da WeasyPrint.** Apresente-o com destaque, em parágrafo próprio:

- o que você tentou fazer, na ordem;
- a mensagem de erro exata (o print vale como figura);
- o motivo: a biblioteca depende de programas do sistema operacional que não vêm pelo `pip` e exigem instalador (retome a seção 2.4);
- **a consequência prática para o projeto:** em um ambiente Windows sem privilégios de administração, como os laboratórios do instituto, essa biblioteca não é uma opção viável, **por mais bem avaliada que seja tecnicamente em outros contextos**.

Seja preciso e justo: você **não** está dizendo que a WeasyPrint é ruim. Está dizendo que, **neste ambiente**, ela não pôde ser usada. A diferença entre as duas afirmações é grande, e escrever a segunda mostra maturidade.

### 4.7 Limitações do trabalho

Subseção curta e honesta. Quatro pontos bastam:

- **um único modelo de folder foi testado.** Outro leiaute, com duas colunas ou muitas imagens, poderia mudar a ordem das bibliotecas;
- **a avaliação de fidelidade envolve julgamento** e foi feita por um único avaliador, ainda que com critério escrito antes e com justificativa para cada nota;
- **o acervo é pequeno** (dez narrativas) e as medições foram feitas em uma única máquina;
- **o tempo de implementação sofre efeito da ordem** em que as bibliotecas foram programadas.

Note que várias dessas limitações são atenuadas por o estudo ser **comparativo**: a mesma limitação incide sobre as três bibliotecas. Diga isso, sem usar o argumento para varrer tudo para debaixo do tapete.

### Entrega

- [ ] Estrutura do capítulo 4 criada e as tabelas (4.2, 4.3, 4.4 e 4.5) com os números da medição oficial.
- [ ] Seções 4.1 a 4.5 e 4.7 escritas.
- [ ] Todas as tabelas e os quatro gráficos no texto, anunciados antes e explicados depois.
- [ ] Caso da WeasyPrint em parágrafo próprio, com a figura do erro.
- [ ] Comentários das entregas anteriores todos resolvidos.
- [ ] Versão nomeada: `Entrega 6 – Resultados – 03/12`.
- [ ] Comentário na *issue*, marcando os orientadores, e card em **Em revisão**.

---

# Sprint 8 — 04/12 a 10/12/2026

<a id="sprint-8-dev"></a>
## Sprint 8 · Desenvolvimento: quadro comparativo, recomendação e fechamento

**Branch:** `feature/fechamento`

**O que você vai entregar:** o quadro que responde à pergunta do trabalho, a recomendação para a equipe do Narrativas, o `README.md` completo e a apresentação.

É nesta semana que o trabalho deixa de ser "três programas que geram PDF" e passa a ser uma pesquisa com resposta. **Faça o desenvolvimento nos dois primeiros dias (sexta, 04/12, e segunda, 07/12)**, para sobrar o resto da semana para a escrita, que é pesada.

### Passo a passo

**1. Confira os números antes de montar o quadro.** Abra `resultados/medicoes.csv`, `resultados/fidelidade.csv` e `resultados/linhas_de_codigo.csv` e confira se são os da medição oficial da Sprint 7 (a data e a hora estão em `docs/ambiente.md`). **Não rode as medições de novo**: todos os números do TCC saem dessa medição. Se mudou algum gerador depois dela, anote no diário o que mudou e por quê.

**2. Monte o quadro comparativo** em `docs/recomendacao.md`. É a figura mais importante do seu trabalho:

| Critério | FPDF2 | ReportLab | xhtml2pdf | WeasyPrint |
|---|---|---|---|---|
| Como se programa | coordenadas | blocos | HTML e CSS | HTML e CSS |
| Fidelidade ao leiaute (0–20) | | | | não avaliado |
| Tempo médio de geração (ms) | | | | não avaliado |
| Tamanho médio do arquivo (KB) | | | | não avaliado |
| Caracteres especiais com a fonte padrão | | | | não avaliado |
| Acentuação com a DejaVu Sans | | | | não avaliado |
| Imagem sem deformar | | | | não avaliado |
| PDF com texto pesquisável | | | | não avaliado |
| Instalação (pacotes e problemas) | | | | **não foi possível usar no ambiente** |
| Linhas de código do gerador | | | | não avaliado |

**3. Escreva a recomendação** no mesmo arquivo, abaixo do quadro, em meia página, respondendo à pergunta do trabalho: **qual biblioteca a equipe do Narrativas deve usar, e por quê**. Ela precisa ter três coisas:

- **um número que a sustente.** "Recomendo a X porque fez 18 de 20 pontos de fidelidade, contra 14 da Y, gerando o folder na metade do tempo" é uma recomendação; "recomendo a X porque achei melhor" não é;
- **uma condição em que a resposta mudaria.** Por exemplo: "se a equipe precisar mudar o leiaute com frequência e tiver quem saiba CSS, a xhtml2pdf pode compensar, apesar da nota menor";
- **honestidade sobre o que não foi medido.** Você testou um folder, em uma máquina, com 10 narrativas.

**4. Complete o `README.md`.** Ele precisa permitir que outra pessoa repita tudo, e a política do NIC exige instalação, execução, arquitetura básica e responsáveis:

1. o que é este trabalho, em três linhas, e o link para a recomendação;
2. responsáveis (você e os orientadores);
3. o que precisa ter instalado (só o Python 3, e qual versão você usou);
4. como criar o ambiente virtual e instalar (`pip install -r requirements.txt`);
5. como o arquivo de uma narrativa é organizado (mostre um exemplo, curto);
6. como gerar os folders com cada biblioteca;
7. como rodar as verificações, as medições e os gráficos;
8. **arquitetura básica:** o que tem em cada pasta e como os programas se ligam (narrativas → `ler_narrativas.py` → geradores → `saidas/` → `medir.py` → `resultados/` → `graficos.py`);
9. a origem e a licença das narrativas, das imagens e da fonte.

**Teste o seu próprio README:** apague as pastas `.venv` e `saidas`, siga o seu texto do zero, como se fosse outra pessoa, e veja se funciona. É a única forma de saber que ele está completo.

**5. Limpe o repositório.** Não podem estar no repositório: `.venv/`, `__pycache__/`, `saidas/` e arquivos de teste soltos fora de `estudos/`. Rode `git status` e confira.

**6. Monte a apresentação** (10 minutos, no Google Apresentações):

1. o problema: o protótipo da tela com o botão "Baixar PDF";
2. a pergunta do trabalho;
3. o modelo do folder que você desenhou;
4. o mesmo folder feito pelas três bibliotecas, lado a lado;
5. o gráfico de fidelidade e o de tempo;
6. o caso da WeasyPrint;
7. o quadro comparativo e a recomendação.

**7. Abra o último PR** para a `develop`. Depois de aprovado, nós fazemos a integração da `develop` na `main` e registramos a versão final (`v1.0`).

### Como saber que deu certo

- O quadro comparativo está preenchido, sem nenhuma célula vazia.
- Você consegue responder, em uma frase e com números, qual biblioteca a equipe deve usar.
- Você seguiu o seu `README.md` do zero e funcionou.

### Entrega da sprint

- [ ] Números conferidos com a medição oficial da Sprint 7.
- [ ] `docs/recomendacao.md` com o quadro comparativo e a recomendação.
- [ ] `README.md` completo e testado do zero.
- [ ] Repositório limpo.
- [ ] Apresentação montada (link no comentário da *issue*).
- [ ] Diário da última sprint.
- [ ] PR aberto para a `develop`, com `Closes #` da *issue* da semana.

<a id="sprint-8-escrita"></a>
## Sprint 8 · Escrita: quadro e recomendação, Conclusão, Objetivos específicos, Resumo e Título (Entrega 7)

**Prazo: 10/12/2026.** A seção 4.6 e a Conclusão até **segunda-feira, 07/12**; o resto até quinta.

### Antes de tudo: atualize o que mudou

- **Confira os números** de todas as tabelas e gráficos com os da medição oficial (Sprint 7), um por um.
- **Passe para o passado** tudo o que foi escrito no futuro (Introdução, bloco 4; Metodologia).
- **Complete a 3.6**: acrescente a data das medições e os itens (e) dos métodos (como as medições e a avaliação de fidelidade foram feitas).

### 4.6 Quadro comparativo e recomendação

O quadro final (o de `docs/recomendacao.md`), com uma linha por critério e uma coluna por biblioteca, incluindo a WeasyPrint com "não avaliado" e o motivo. **Este quadro é a contribuição prática do seu trabalho**: é o que a equipe do Narrativas vai olhar para decidir.

Depois dele, **a recomendação**, em um parágrafo, com três partes:

1. **qual biblioteca**, com o número que sustenta a escolha;
2. **em que condição a resposta mudaria**;
3. **o que ainda precisa ser verificado** antes da implementação definitiva na plataforma.

Não fuja da recomendação. Um trabalho aplicado que termina em "cada uma tem suas vantagens" desperdiça tudo o que mediu.

### 5 Conclusão (cerca de 2 páginas)

Curta e direta. Nada de resultado, conceito ou citação que não tenha aparecido antes. **Escreva, nesta ordem:**

1. **retomada do problema e do objetivo geral**, afirmando que foi alcançado, **com o motivo e com número**: "[...] uma vez que a comparação das três bibliotecas, sobre um mesmo modelo de folder e um acervo de dez narrativas, resultou em X, Y e Z pontos de fidelidade ao leiaute";
2. **um comentário por objetivo específico**, na mesma ordem, cada um apontando o resultado que o comprova (escreva os objetivos específicos primeiro, logo abaixo);
3. **resposta direta a cada pergunta de pesquisa** da seção 3.2, uma ou duas frases cada. E responda mesmo a última: **recomende uma biblioteca** para o projeto Narrativas;
4. **contribuições:** um modelo de folder para as narrativas do projeto, com critérios de avaliação documentados; a comparação medida de três bibliotecas sobre um documento real, com método declarado; a constatação de que uma quarta biblioteca é inviável no ambiente dos laboratórios do instituto; e três geradores com código aberto no repositório, que a equipe pode reaproveitar;
5. **limitações e dificuldades:** retome brevemente as limitações e acrescente as dificuldades reais do desenvolvimento: as fontes e a acentuação, o caminho das imagens, o CSS não suportado, a tentativa frustrada de instalação, e o fato de você ter aprendido Python durante o próprio trabalho. **É aqui que o `docs/diario.md` se paga**: se você escreveu as três linhas toda semana, este parágrafo se escreve sozinho;
6. **trabalhos futuros**, concretos e ligados ao que você encontrou:
   - implementar o botão "Baixar PDF" na plataforma Narrativas com a biblioteca recomendada (o principal);
   - gerar o folder a partir do banco de dados da plataforma, quando o cadastro de narrativas existir;
   - avaliar a acessibilidade completa do PDF, conforme a norma PDF/UA, e não apenas a extração do texto;
   - testar leiautes mais complexos, com duas colunas e várias imagens;
   - avaliar a impressão física dos folders, com papel e cores reais;
   - produzir a versão "Material Didático", com atividades pedagógicas, como já previsto nos protótipos da plataforma.

**Não escreva** que "a biblioteca X é a melhor" sem dizer em qual critério, sobre qual documento e em que ambiente. E não generalize para "geração de PDF em Python" o que você mediu com um folder, dez narrativas e uma máquina.

**Teste:** leia o objetivo geral e, em seguida, a primeira frase da Conclusão. Se as duas não falarem exatamente da mesma coisa, uma das duas está errada.

### 1.2 Objetivos específicos

Ficaram para o final de propósito: precisam descrever o que foi **realmente alcançado**.

- de 4 a 5 itens, verbo no infinitivo, letra minúscula no início, ponto e vírgula no fim de cada um e ponto no último;
- na **mesma ordem** das etapas da Metodologia e das seções dos Resultados;
- cada um **verificável**: na Conclusão, você mostra com número que foi atingido;
- "instalar a biblioteca X" não é objetivo específico, é tarefa.

**O que cada item deve cobrir** (redija com as suas palavras):

1. a revisão da literatura sobre patrimônio cultural imaterial, material didático impresso e geração programática de documentos;
2. a definição de um modelo de folder para as narrativas do projeto e de uma lista de critérios para avaliá-lo;
3. a implementação do mesmo folder em três bibliotecas Python, sobre um acervo comum de narrativas de domínio público;
4. a medição e a comparação de fidelidade ao leiaute, tempo de geração, tamanho do arquivo, acentuação, imagens e acessibilidade do PDF;
5. a recomendação, com base nos resultados, da biblioteca mais adequada à plataforma Narrativas.

### Resumo, *Abstract* e palavras-chave

O Resumo é escrito **por último**, com o texto já aprovado. Parágrafo único, de 150 a 500 palavras, impessoal, sem citações, sem siglas pouco conhecidas e sem mencionar figuras ou tabelas (NBR 6028:2021). Uma ou duas frases para cada item:

1. **contexto e problema:** a difusão de narrativas populares em material impresso e a ausência de uma escolha técnica para gerar esse material;
2. **objetivo:** o que o trabalho se propôs a comparar;
3. **método:** um modelo de folder, três bibliotecas Python, um acervo de dez narrativas de domínio público, lista de critérios definida previamente e medições repetidas;
4. **resultados:** os números principais (a nota de fidelidade de cada biblioteca, a diferença de tempo) e o caso da biblioteca que não pôde ser usada;
5. **conclusão:** a recomendação e o encaminhamento (a implementação na plataforma como trabalho futuro).

**Coloque números no resumo.** Resumo sem número é resumo fraco, e é ele que faz o avaliador decidir se lê o resto.

O ***Abstract*** é a versão em inglês. Os termos técnicos têm forma consagrada em inglês (*layout fidelity*, *rendering*, *accessibility*, *open source*): use-os, e não a tradução literal. Não entregue tradução automática sem revisar frase por frase.

**Palavras-chave** (3 a 5), separadas por ponto e vírgula. Campo semântico: geração de documentos; PDF; bibliotecas Python; patrimônio cultural imaterial; material didático. Escolha termos pelos quais alguém **procuraria** o seu trabalho.

### Título

**A última coisa a ser definida.** Ele deve dizer **o que foi feito** e **em que contexto**, e ser coerente com o objetivo geral. O título provisório:

> *Geração automatizada de folders em PDF a partir de narrativas populares: um comparativo entre bibliotecas Python.*

tem as três partes de um bom título: a ação (geração automatizada), o contexto (narrativas populares) e o recorte (comparativo entre bibliotecas). **Ajuste-o para refletir o que o trabalho realmente entregou**: se a fidelidade ao leiaute foi o critério decisivo, por exemplo, isso pode aparecer no título. Proponha a versão final no comentário da *issue*; nós aprovamos junto com o texto. Evite títulos genéricos ("Gerador de PDF em Python") e evite prometer mais do que o trabalho mede.

### Revisão final

Além do checklist de `docs/orientacoes_escrita_tcc.md`:

- [ ] O objetivo geral, os objetivos específicos, as perguntas de pesquisa, as seções dos Resultados e os parágrafos da Conclusão estão na mesma ordem e falam das mesmas coisas?
- [ ] Todos os números do Resumo, dos Resultados e da Conclusão são **exatamente** os da medição oficial? (Erro mais comum: mudar um número nos Resultados e esquecer de atualizar o Resumo.)
- [ ] Está escrito que a lista de conferência foi definida **antes** de gerar os folders?
- [ ] Toda nota de fidelidade diferente de 2 tem justificativa no texto?
- [ ] Está declarado por que não foi usado banco de dados, e por que a mesma fonte foi usada nas três bibliotecas?
- [ ] O caso da WeasyPrint está apresentado **como resultado**, e formulado de modo justo?
- [ ] Toda tabela e figura é citada no texto antes de aparecer e explicada depois?
- [ ] Todas as tabelas e figuras têm identificação em cima, centralizada, e fonte embaixo?
- [ ] Os gráficos informam o que é cada eixo e a unidade?
- [ ] A origem das narrativas está informada, com a justificativa do domínio público? E a licença das imagens e da fonte?
- [ ] O ambiente de execução está completo (processador, memória, sistema operacional, versões, data da medição)?
- [ ] Há pelo menos um resultado contra a sua própria expectativa, ou uma dificuldade sua, relatados honestamente?
- [ ] As limitações estão declaradas?
- [ ] As siglas (PDF, CSS, HTML, UTF-8, BNCC, UNESCO) foram escritas por extenso na primeira vez que aparecem?
- [ ] A numeração das seções está sem ponto depois do número?
- [ ] O texto está impessoal e no passado?
- [ ] O endereço do repositório (`https://github.com/nicifrn/mp_gerador_pdf`) está no texto, na seção 3.6?
- [ ] Todos os comentários dos orientadores foram respondidos e resolvidos?
- [ ] A versão final foi nomeada no histórico do Drive: `Entrega 7 – Versão final – 10/12`?

### Entrega

- [ ] Números conferidos com a medição oficial e textos passados para o passado.
- [ ] Seção 4.6 e Conclusão escritas até 07/12.
- [ ] Objetivos específicos, Resumo, *Abstract*, palavras-chave e Título.
- [ ] Revisão final feita, item por item.
- [ ] Versão nomeada: `Entrega 7 – Versão final – 10/12`.
- [ ] Comentário na *issue*, marcando os orientadores, com a proposta de título, e card em **Em revisão**.

---

<a id="quadro-resumo"></a>
## 9. Quadro-resumo

| Sprint | Período | Desenvolvimento | O que você aprende | Escrita |
|---|---|---|---|---|
| 1 | 16/10 a 22/10 | Python: primeiros passos | variáveis, texto, `if`, módulos | preparar documento e ler |
| 2 | 23/10 a 29/10 | Python: estruturas + Git | listas, dicionários, funções, arquivos, Git, PR | Introdução e Objetivo geral |
| 3 | 30/10 a 05/11 | Ambiente, primeiro PDF, acervo e modelo do folder | ambiente virtual, `pip`, primeiro PDF, domínio público, licenças, verificação com `assert` | Referencial 2.1, 2.2, 2.5 |
| 4 | 06/11 a 12/11 | FPDF2 | leiaute por coordenadas, fontes e Unicode | Referencial 2.3, 2.4, 2.6 |
| 5 | 13/11 a 19/11 | ReportLab | leiaute por blocos, estilos, paginação automática | Metodologia |
| 6 | 20/11 a 26/11 | xhtml2pdf + WeasyPrint | leiaute por HTML e CSS, dependências do sistema | Materiais e métodos |
| 7 | 27/11 a 03/12 | Medições, fidelidade e gráficos | cronometragem, mediana, extração de texto, avaliação com critério, gráficos | Resultados |
| 8 | 04/12 a 10/12 | Quadro, recomendação, README | síntese, decisão fundamentada, reprodutibilidade | Conclusão, Resumo e Título |

### Relação entre o código e o texto

| Seção do TCC | Sprints que geram o conteúdo |
|---|---|
| Referencial Teórico | leituras das Sprints 1 a 4 |
| Metodologia | 3 (acervo, modelo, lista de conferência) e 7 (protocolo de medição) |
| Materiais e métodos | 3 a 6 (ferramentas, acervo, como cada folder foi feito) |
| Resultados | 4 a 6 (caracteres especiais, WeasyPrint) e 7 (medições, fidelidade e gráficos) |
| Conclusão | `docs/diario.md` acumulado e `docs/recomendacao.md` |

**Nunca apague uma medição, e não mude a lista de conferência depois da Sprint 3.** A confiabilidade do seu trabalho inteiro está nesses dois lugares.

---

<a id="riscos"></a>
## 10. Riscos e planos B

| Risco | Sinal de alerta | O que fazer |
|---|---|---|
| Python ainda difícil no fim da Sprint 2 | `ex07_arquivo.py` não funciona | Na Sprint 3, faça primeiro o `ex07`, com ajuda pela *issue*, antes de instalar as bibliotecas. O `ler_narrativas.py` da Parte B depende dele |
| Máquina do laboratório formatada | `.venv` sumiu | Normal: o código está no GitHub. Clone de novo, recrie o `.venv` e rode `pip install -r requirements.txt` |
| Não achar o livro de Sílvio Romero com o texto digitado | Sprint 3 sem os textos na terça-feira (03/11) | Use uma digitalização em imagem e transcreva os contos curtos à mão; para os longos, escolha os que estiverem disponíveis em texto em qualquer uma das fontes indicadas |
| Achar e transcrever as narrativas demora | Sprint 3 chegando na quarta (04/11) sem os textos | Reduza para **6 narrativas**, **mantendo a variedade de tamanhos** (2 curtas, 2 médias, 2 longas). Seis bem escolhidas valem mais que dez no chute. Declare isso na Metodologia |
| Não achar imagens com licença livre | Sprint 3 | Use fotos ou desenhos seus. Registre a origem de qualquer jeito |
| Uma biblioteca não consegue fazer um dos 10 itens | Sprints 4 a 6 | **Não force.** Registre como nota 0 ou 1 no item e explique o motivo. É resultado, não fracasso |
| A WeasyPrint não funciona | Sprint 6 | **Já é o esperado.** Documente com print e siga com três bibliotecas |
| Gerador atrasado | Sprint terminando sem os 10 folders | Entregue o PR no prazo com o que tiver, diga na *issue* o que faltou e termine na semana seguinte **antes** de começar a próxima biblioteca. As medições da Sprint 7 dependem dos três geradores |
| Medições atrasadas na Sprint 7 | Segunda-feira (30/11) sem o `medicoes.csv` | Peça ajuda na *issue* no mesmo dia. A avaliação de fidelidade já é feita em uma narrativa só; se faltar tempo, deixe os gráficos 3 e 4 para o primeiro dia da Sprint 8 (sexta, 04/12) |

**Se algo tiver de ser cortado, corte largura, não profundidade.** É melhor ter três bibliotecas bem comparadas com 6 narrativas do que quatro comparadas às pressas. O que **não** pode faltar: o modelo do folder, a lista de conferência, as medições e o quadro final.

---

<a id="extras"></a>
## 11. Se sobrar tempo (opcional)

Só depois de a sprint da semana estar entregue e de a escrita estar em dia:

- **E1.** Fazer o texto da narrativa em **duas colunas**, como em folder de verdade, e comparar quanto trabalho isso dá em cada biblioteca. É um ótimo item extra, porque separa muito bem as três.
- **E2.** Acrescentar um **QR Code** no rodapé, apontando para a página do portal Narrativas (biblioteca `qrcode`, instalada pelo `pip`).
- **E3.** Gerar uma **segunda versão do folder**, em preto e branco, pensada para impressão econômica em escola pública, e comparar o tamanho do arquivo.
- **E4.** Testar o que acontece quando a imagem é muito grande (por exemplo, 4.000 pixels de largura): alguma biblioteca reduz a imagem sozinha? O arquivo fica enorme?
- **E5.** Verificar se os PDFs gerados têm os **metadados** preenchidos (título, autor), que ajudam na organização do acervo e na acessibilidade. *Pesquise:* `PdfReader(...).metadata`.

---

<a id="referencias-minimas"></a>
## 12. Referências mínimas do TCC

- **2 obras de metodologia científica:** Gil (2017) e Prodanov e Freitas (2013);
- **3 a 4 obras sobre patrimônio cultural imaterial e narrativas populares** (seção 2.1): várias já estão em `docs/projeto_narrativas.md`; aproveite-as;
- **a obra de Sílvio Romero** usada como acervo;
- **2 obras sobre material didático impresso e difusão cultural** (seção 2.2), com pelo menos uma fonte de dados sobre conectividade nas escolas (TIC Educação);
- **2 a 3 fontes sobre o formato PDF e codificação de caracteres** (seção 2.3);
- **a documentação oficial das quatro bibliotecas** (seção 2.4): serve para descrever a ferramenta, não para fundamentar conceito;
- **2 fontes sobre acessibilidade digital** (seção 2.5), incluindo a Lei nº 13.146/2015;
- **3 a 4 trabalhos relacionados** (seção 2.6);
- **a legislação citada:** Lei nº 9.610/1998 (direitos autorais, que justifica o uso das narrativas), Lei nº 13.146/2015 e Decreto nº 3.551/2000.

Registre a referência completa de **tudo** o que ler, na seção de Referências do documento do Drive, desde o primeiro dia.
