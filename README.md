# Security Audit — Amostra Gratuita / Free Sample

> **Uma verificação de segurança que você roda no seu próprio ambiente, com o seu Claude.
> Código aberto — leia cada linha antes de rodar.**
>
> *A quick security check you run in your own environment, with your own Claude.
> Open source — read every line before running it.*

---

## 🇧🇷 Português

Olá! Meu nome é **Humberto Spatz** — desenvolvo sistemas e produtos há mais de 30 anos. No último ano
venho trabalhando intensamente com ferramentas de IA para desenvolvimento (hoje, Claude Code).

A ideia de que "basta um comando e a IA entrega o sistema pronto" é fantasia para quem é da área. A IA
resolveu boa parte da escrita mecânica de funções — mas **lógica, segurança e arquitetura ainda são
responsabilidade do humano**. Disso nasceu este procedimento de auditoria.

### O que é isto

Uma **amostra gratuita** de auditoria de segurança. Ela faz uma varredura rápida em busca dos problemas
críticos mais graves e mais comuns, e **para nos 2 primeiros que encontrar** — o suficiente para você
ver, em minutos, se o seu sistema esconde riscos sérios.

### Por que você pode confiar

- **É código aberto.** Leia [`audit1-selfservice/AUDIT1.md`](audit1-selfservice/AUDIT1.md) antes de
  rodar — você vê exatamente o que ele faz. Nada de caixa-preta.
- **Somente leitura.** Não altera, move ou apaga nada no seu código.
- **O resultado fica com você.** O relatório é um arquivo local. **Eu (consultor) não recebo seu código
  nem o relatório**, e nada é publicado.
- **Transparência:** como o Claude é um serviço da Anthropic, os arquivos lidos são processados nos
  servidores da Anthropic, conforme a política de dados da **sua** conta — como em qualquer uso do
  Claude. Se privacidade for crítica, use uma conta/modo sem retenção para treinamento.

### Como usar

Você precisa do **Claude Code** (CLI, VS Code ou Claude Code App). Passo a passo completo em
[`audit1-selfservice/LEIA-PRIMEIRO.md`](audit1-selfservice/LEIA-PRIMEIRO.md). Resumo:

1. Crie uma pasta nova (ex.: `AUDITORIA-AMOSTRA`) e copie para dentro dela **a pasta do projeto** que
   quer auditar — com o **nome real** dela (ex.: `MeuSistema`) e com o `.git`. É uma **cópia isolada**;
   o original nunca é tocado.
2. Copie a pasta `audit1-selfservice` (deste repositório) **no mesmo nível** do projeto:
   ```
   AUDITORIA-AMOSTRA/
   ├── MeuSistema/            <- seu projeto (nome real, com .git)
   └── audit1-selfservice/    <- este kit
   ```
3. Abra o Claude Code nessa pasta e rode (troque `<diretorio-projeto>` pelo nome real, ex.: `MeuSistema`):
   ```
   Leia audit1-selfservice/AUDIT1.md e execute a auditoria na pasta <diretorio-projeto>.
   ```
4. O resultado é **`RELATORIO_AMOSTRA_<projeto>.md`** (ex.: `RELATORIO_AMOSTRA_MeuSistema.md`), gerado
   **fora** da pasta do projeto (o projeto **não é tocado** — somente leitura), com até **2 problemas
   encontrados** (se houver) e a gravidade.

> **Vários projetos?** Não precisa apagar nada nem criar outra pasta: copie o próximo projeto (ex.:
> `MeuSistema2`) para a mesma pasta, ao lado, e rode apontando pra ele. Como o relatório leva o nome do
> projeto, um não sobrescreve o outro.

### Quer a auditoria completa?

A amostra é só o começo. A auditoria completa cobre **segurança, lógica de funcionamento, banco de dados
e infraestrutura**, com verificação dupla de cada achado e plano de correção priorizado.

📩 **Contato:** Humberto Spatz — humberto@spatz.com.br

---

## 🇬🇧 English

Hi! My name is **Humberto Spatz** — I've been building software and products for over 30 years. Over the
past year I've been working intensively with AI development tools (these days, Claude Code).

The idea that "one prompt and the AI delivers a finished system" is a fantasy for anyone in the field.
AI has solved much of the mechanical function-writing — but **logic, security and architecture are still
the human's responsibility**. This audit procedure was born out of that.

### What this is

A **free sample** security audit. It runs a quick scan for the most severe and most common critical
problems, and **stops at the first 2 it finds** — enough to show you, in minutes, whether your system is
hiding serious risks.

### Why you can trust it

- **It's open source.** Read [`audit1-selfservice/AUDIT1.md`](audit1-selfservice/AUDIT1.md) before
  running it — you see exactly what it does. No black box.
- **Read-only.** It never changes, moves or deletes anything in your code.
- **The result stays with you.** The report is a local file. **I (the consultant) don't receive your
  code or the report**, and nothing is published.
- **Transparency:** since Claude is an Anthropic service, the files it reads are processed on Anthropic's
  servers under **your** account's data policy — as with any use of Claude. If privacy is critical, use
  an account/mode without training retention.

### How to use

You need **Claude Code** (CLI, VS Code or the Claude Code App). Full walkthrough in
[`audit1-selfservice/LEIA-PRIMEIRO.md`](audit1-selfservice/LEIA-PRIMEIRO.md). In short:

1. Create a new folder (e.g. `AUDIT-SAMPLE`) and copy **the project folder** you want to audit into it —
   with its **real name** (e.g. `MySystem`) and its `.git`. It's an **isolated copy** — the original is
   never touched.
2. Copy the `audit1-selfservice` folder (from this repo) **at the same level** as the project:
   ```
   AUDIT-SAMPLE/
   ├── MySystem/              <- your project (real name, with .git)
   └── audit1-selfservice/    <- this kit
   ```
3. Open Claude Code in that folder and run (replace `<project-dir>` with the real name, e.g. `MySystem`):
   ```
   Read audit1-selfservice/AUDIT1.md and run the audit on the <project-dir> folder.
   ```
4. The output is **`RELATORIO_AMOSTRA_<project>.md`** (e.g. `RELATORIO_AMOSTRA_MySystem.md`), generated
   **outside** the project folder (the project is **never touched** — read-only), with up to **2 issues
   found** (if any) and the severity.

> **Multiple projects?** No need to delete anything or create another folder: copy the next project
> (e.g. `MySystem2`) into the same folder, side by side, and run pointing at it. Since each report is
> named after its project, one never overwrites another.

### Want the full audit?

The sample is just the beginning. The full audit covers **security, application logic, database and
infrastructure**, with double verification of each finding and a prioritized remediation plan.

📩 **Contact:** Humberto Spatz — humberto@spatz.com.br

---

*Licença / License: veja [`LICENSE`](LICENSE). Fornecido "como está", sem garantias. / Provided "as is",
without warranty.*
