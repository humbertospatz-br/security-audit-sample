#!/usr/bin/env python3
"""
MEDIR — conte o tamanho do seu sistema (SEM preco).

Aberto de proposito: LEIA este arquivo e rode voce mesmo. So conta CODIGO PROPRIO
(pula framework/vendor/gerado — ver excludes.txt). **Nao calcula preco**: a medicao e
transparente; o preco voce solicita ao consultor com este numero. Aprovado, voce recebe
um token que desbloqueia a auditoria (a REGUA da auditoria e o que fica protegido —
a medicao, nao).

Uso:  python medir.py [caminho]      (padrao: diretorio atual)
Requisitos: so Python 3. (Se tiver scc/cloc, pode usar pra conferir.)
"""
import os
import sys

CODE_EXT = {
    ".php", ".js", ".ts", ".jsx", ".tsx", ".vue", ".py", ".rb",
    ".cs", ".go", ".java", ".kt", ".c", ".cpp", ".h", ".hpp", ".sql",
}
CONTATO = "Humberto Spatz — humberto@spatz.com.br"


def load_excludes(base):
    """Le excludes.txt: diretorios de framework/terceiro/gerado que NAO contam."""
    path = os.path.join(base, "excludes.txt")
    try:
        with open(path, encoding="utf-8") as fh:
            return {l.strip() for l in fh if l.strip() and not l.startswith("#")}
    except FileNotFoundError:
        return {"node_modules", "vendor", ".git", "dist", "build", "vcl"}


def count_sloc(root, excludes):
    """Conta linhas nao-vazias dos arquivos de codigo, pulando os diretorios excluidos."""
    total, arquivos = 0, 0
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in excludes]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() in CODE_EXT:
                try:
                    with open(os.path.join(dirpath, fn), encoding="utf-8", errors="ignore") as fh:
                        total += sum(1 for line in fh if line.strip())
                        arquivos += 1
                except OSError:
                    pass
    return total, arquivos


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    base = os.path.dirname(os.path.abspath(__file__))
    excludes = load_excludes(base)
    sloc, arquivos = count_sloc(root, excludes)

    print(f"\n=== Medicao do sistema ===")
    print(f"Codigo proprio: ~{sloc:,} linhas  ({arquivos} arquivos)")
    print(f"Diretorios pulados (framework/terceiro/gerado): {', '.join(sorted(excludes))}")
    print()
    print("Este numero e a MEDICAO (aberta). Para receber seu ORCAMENTO, envie-o para:")
    print(f"  {CONTATO}")
    print("Aprovado, voce recebe um token que desbloqueia a auditoria pelo MCP.")
    print("A amostra (audit1) e GRATIS.\n")


if __name__ == "__main__":
    main()
