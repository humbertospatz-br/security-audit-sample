# Auditoria Amostra (Audit-1) — Como Rodar no Seu Ambiente

> **Você tem controle total.** A auditoria roda no SEU ambiente e o relatório fica LOCAL, na sua
> máquina. **Nós (consultores) não recebemos** seu código nem o resultado — o kit não envia nada
> para nós nem publica nada em lugar nenhum.
>
> **Transparência (importante):** como o Claude é um serviço da Anthropic, os arquivos que ele lê
> são processados nos servidores da Anthropic, conforme a política de dados da conta que você usar.
> Isso vale para qualquer uso do Claude. Se privacidade for crítica, use uma conta/modo **sem
> retenção para treinamento** (ex.: planos de time/empresa). O que garantimos aqui é que o kit não
> manda nada para os consultores e não expõe o resultado.

---

## O que é

Uma **amostra gratuita** de auditoria técnica. Ela faz uma varredura rápida procurando os
problemas mais graves e mais comuns — principalmente de **segurança** — e para assim que
encontra os primeiros. O objetivo é te mostrar, em minutos, se o seu sistema tem riscos
críticos escondidos.

Não é a auditoria completa — é a prova de que vale a pena fazer a completa.

## Requisitos

- Claude Code instalado (CLI, VS Code ou Claude Code App).
- O código do projeto que você quer auditar, acessível na máquina.

## Preparação (importante — protege o seu projeto)

Para **não mexer em nada** no seu projeto original nem na configuração do seu Claude, a auditoria
roda numa pasta separada, com a **cópia do seu projeto e o kit lado a lado**:

1. Crie uma pasta nova, ex.: `AUDITORIA-AMOSTRA`.
2. Copie para dentro dela **a pasta do projeto que você quer auditar** — com o **nome real dela**
   (ex.: `MeuSistema`).
   - **Copie o `.git` junto** (o histórico é usado para detectar segredos versionados).
   - Pode deixar de fora `node_modules/`, `vendor/`, `dist/` (não são analisados mesmo).
3. Copie **a pasta `audit1-selfservice`** (este kit) para dentro também — **no mesmo nível do projeto**.

Deve ficar assim:
```
AUDITORIA-AMOSTRA/
├── MeuSistema/            <- cópia do seu projeto (nome real, com .git)
└── audit1-selfservice/    <- este kit (no mesmo nível do projeto)
```

> **O audit NÃO altera nada na pasta do projeto.** É **somente leitura** e grava o relatório
> **FORA** dela — na raiz de `AUDITORIA-AMOSTRA`. Seu projeto (original e cópia) fica intacto.
> Pode inclusive pôr **vários projetos** lado a lado e auditar um de cada vez.

## Como rodar (2 formas)

Abra o Claude Code na pasta `AUDITORIA-AMOSTRA` e troque `<diretorio-projeto>` pelo nome da pasta do
seu projeto (ex.: `MeuSistema`).

**Forma A — mais simples (recomendada):**
```
Leia audit1-selfservice/AUDIT1.md e execute a auditoria na pasta <diretorio-projeto>.
```
Ao final, o relatório estará em `RELATORIO_AMOSTRA.md`, na raiz de `AUDITORIA-AMOSTRA` (fora da pasta do projeto).

**Forma B — comando:**
1. Copie `audit1-selfservice/.claude` para dentro de `AUDITORIA-AMOSTRA` (fica `AUDITORIA-AMOSTRA/.claude/commands/audit1.md`).
2. Rode:
   ```
   /audit1 <diretorio-projeto>
   ```

## O que a auditoria vai fazer

- Ler seus arquivos de código (somente leitura — **não altera nada**).
- Procurar problemas críticos de segurança e lógica.
- **Parar assim que confirmar os 2 primeiros críticos** (é uma amostra, não a varredura completa).
- Gerar um relatório de 1 página, em linguagem clara, em `RELATORIO_AMOSTRA.md`.

## O que a auditoria NÃO vai fazer

- ❌ Enviar o resultado para os consultores ou publicar em qualquer lugar (o relatório fica só com você).
- ❌ Alterar, mover ou apagar seu código.
- ❌ Executar seu sistema (é análise estática — só leitura).
- ❌ Auditar tudo — é uma amostra; a completa cobre muito mais.

## Depois de rodar

O relatório termina com um contato. Se quiser a auditoria **completa** (segurança, lógica,
banco de dados, infraestrutura — com múltiplos verificadores e plano de correção priorizado),
fale com a gente.

---

**Kit gerado para:** ______________________  (preenchido pelo consultor)
**Validade da amostra:** ____ / ____ / ______
**Contato:** Humberto Spatz — humberto@spatz.com.br
