# Auditoria Amostra — Resultado

**Projeto:** [nome detectado]
**Data:** [YYYY-MM-DD]
**Tipo:** Amostra gratuita (varredura rápida de problemas críticos)
**Execução:** relatório gerado localmente. Não foi enviado aos consultores nem publicado.

---

## Nota preliminar do sistema: **[X] / 10**

> Nota PRELIMINAR, baseada em AMOSTRA. O sistema **não foi auditado por completo** — a busca parou
> nos primeiros problemas críticos. A nota real, após auditoria completa, pode ser menor.

## Resumo em uma frase

[Ex.: "Encontramos 2 falhas críticas de segurança em minutos, sem varrer nem 10% do sistema."]

---

## 🔴 Crítico #1 — [título em linguagem de negócio]

**O que é:** [explique o risco como quem fala com o dono do negócio, não com o programador.]

**Onde:** `caminho/arquivo.ext:linha`

**Evidência:**
```
[trecho real do código — qualquer segredo MASCARADO, ex.: sk_live_51H****9aQ]
```

**O que pode acontecer:** [consequência concreta: vazar dados de clientes, invasão, prejuízo.]

**Como se corrige:** [1-3 linhas de direção. Não precisa entregar o patch — só mostrar o caminho.]

---

## 🔴 Crítico #2 — [tipo do problema, SEM localização]

**O que é:** [tipo do risco em linguagem de negócio.]

**O que pode acontecer:** [consequência concreta.]

**Localização exata e detalhe técnico:** disponíveis no **relatório completo**.

---

## Além destes

Durante a amostra percebemos indícios de **outros pontos** que merecem investigação, mas a varredura
foi interrompida de propósito (isto é só uma amostra). A auditoria completa vai a fundo em todos.

## Alcance desta amostra

- **Varrido:** [linguagens/pastas cobertas na varredura rápida].
- **NÃO varrido:** [o resto do sistema, dependências, comportamento em execução, banco de dados,
  infraestrutura]. Isto é uma amostra, não a auditoria completa.
- **Método:** análise estática (somente leitura). Nada foi executado.

---

## Próximo passo — Auditoria Completa

A auditoria completa cobre **segurança da informação, lógica de funcionamento, banco de dados e
infraestrutura**, com **verificação dupla** de cada achado (nada de falso alarme) e um **plano de
correção priorizado** por gravidade e esforço.

**Fale com a gente:**
Humberto Spatz — humberto@spatz.com.br

---

*Amostra executada no ambiente do cliente. Relatório local — não enviado aos consultores nem publicado.
Processamento do Claude conforme a política de dados da Anthropic da conta utilizada.*
