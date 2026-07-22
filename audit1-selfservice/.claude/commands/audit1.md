---
description: Auditoria amostra (segurança) — roda 100% local, não envia nada para fora
---

Leia o arquivo `audit1-selfservice/AUDIT1.md` e execute a auditoria amostra neste projeto,
seguindo-o à risca.

Se não encontrar `audit1-selfservice/AUDIT1.md`, procure `AUDIT1.md` na raiz e use esse.

Regras inegociáveis:
- NÃO envie nada para fora desta máquina (sem web, sem upload, sem e-mail).
- Somente leitura no código — não altere nada.
- Pare de procurar ao confirmar o 2º crítico (exceto perigo catastrófico já visto).
- Gere o relatório `RELATORIO_AMOSTRA.md` nesta pasta (fora da cópia do código).

Alvo da auditoria: $ARGUMENTS (se vazio, use a subpasta `projeto/`; se não existir, pergunte qual pasta auditar).
