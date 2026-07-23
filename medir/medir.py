#!/usr/bin/env python3
"""
MEDIR — conte o tamanho do seu sistema (SEM preco).

Aberto de proposito: LEIA este arquivo e rode voce mesmo. So conta CODIGO PROPRIO
(pula framework/vendor/gerado). **Nao calcula preco**: a medicao e transparente; o preco
voce solicita ao consultor com este numero. A REGUA da auditoria e o que fica protegido.

Exclusoes (edite os dois arquivos):
  - excludes.txt        -> nomes de DIRETORIO a pular (node_modules, vendor, vcl, PHPMailer...)
  - excludes-files.txt  -> padroes de ARQUIVO a pular (Chart*.js, class.phpmailer.php...) —
                           pega LIB SOLTA no meio do codigo (dir-exclude nao pega).

Uso:  python medir.py [caminho]      (padrao: diretorio atual)
"""
import fnmatch
import os
import sys

CODE_EXT = {
    ".php", ".js", ".ts", ".jsx", ".tsx", ".vue", ".py", ".rb",
    ".cs", ".go", ".java", ".kt", ".c", ".cpp", ".h", ".hpp", ".sql",
}
CONTATO = "Humberto Spatz — humberto@spatz.com.br"


def _load_list(base, fname, default):
    try:
        with open(os.path.join(base, fname), encoding="utf-8") as fh:
            return [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    except FileNotFoundError:
        return default


def count_sloc(root, exclude_dirs, exclude_files):
    """Conta linhas nao-vazias. Pula diretorios (nome) e arquivos (glob)."""
    total, arquivos = 0, 0
    per_file = []  # (linhas, caminho) — pra mostrar os maiores
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fn in filenames:
            if os.path.splitext(fn)[1].lower() not in CODE_EXT:
                continue
            if any(fnmatch.fnmatch(fn, pat) for pat in exclude_files):
                continue  # lib solta reconhecida por padrao de arquivo
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    n = sum(1 for line in fh if line.strip())
                total += n
                arquivos += 1
                per_file.append((n, os.path.relpath(path, root)))
            except OSError:
                pass
    per_file.sort(reverse=True)
    return total, arquivos, per_file


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    base = os.path.dirname(os.path.abspath(__file__))
    exclude_dirs = set(_load_list(base, "excludes.txt", ["node_modules", "vendor", ".git", "vcl"]))
    exclude_files = _load_list(base, "excludes-files.txt", ["*.min.js"])

    total, arquivos, per_file = count_sloc(root, exclude_dirs, exclude_files)

    print(f"\n=== Medicao do sistema ===")
    print(f"Codigo proprio: ~{total:,} linhas  ({arquivos} arquivos)")
    print(f"Dirs pulados:   {', '.join(sorted(exclude_dirs))}")
    print(f"Arquivos pulados (glob): {', '.join(exclude_files)}")

    if per_file:
        print("\nMaiores arquivos contados (CONFIRA: se algum for LIB/framework, adicione ao excludes):")
        for n, rel in per_file[:8]:
            print(f"  {n:>8,}  {rel}")

    print("\nAtencao: se houver COPIAS MORTAS/backup na arvore (ex.: new/, teste/, _old, *.bak),")
    print("elas contam como codigo proprio — adicione o diretorio ao excludes.txt se nao forem ativas.")

    print(f"\nEste numero e a MEDICAO (aberta). Para receber seu ORCAMENTO, envie-o para:")
    print(f"  {CONTATO}")
    print("Aprovado, voce recebe um token que desbloqueia a auditoria pelo MCP. Amostra (audit1): GRATIS.\n")


if __name__ == "__main__":
    main()
