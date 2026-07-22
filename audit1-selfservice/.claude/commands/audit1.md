---
description: Auditoria amostra (segurança) — somente leitura, resultado local. Uso: /audit1 <diretorio-projeto>
---

Leia o arquivo `audit1-selfservice/AUDIT1.md` e execute a auditoria amostra, seguindo-o à risca.

Se não encontrar `audit1-selfservice/AUDIT1.md`, procure `AUDIT1.md` na raiz e use esse.

Regras inegociáveis:
- NÃO envie nada para fora desta máquina (sem web, sem upload, sem e-mail).
- Somente leitura na pasta do projeto — NÃO altere, mova ou apague nada dentro dela.
- Pare de procurar ao confirmar o 2º crítico (exceto perigo catastrófico já visto).
- Gere o relatório `RELATORIO_AMOSTRA_<projeto>.md` (nome inclui a pasta auditada) nesta pasta (a raiz da auditoria), FORA da pasta do projeto — assim vários projetos não se sobrescrevem.

Alvo da auditoria: $ARGUMENTS (o `<diretorio-projeto>` a auditar, no mesmo nível do kit). Se vazio, pergunte qual pasta de projeto auditar.
