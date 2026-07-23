#!/usr/bin/env python3
"""
MEDIR — conte o tamanho do seu sistema E o mix de LINGUAGENS (sem preco).

Aberto de proposito: LEIA e rode voce mesmo. So conta CODIGO PROPRIO (pula framework/vendor/gerado).
**Nao calcula preco**: a medicao e transparente; o preco voce solicita ao consultor com estes numeros.
O mix de linguagens importa porque a REGUA da auditoria e DIFERENTE por linguagem (PHP/JS != .NET != C).

Exclusoes: `excludes.txt` (diretorios) + `excludes-files.txt` (arquivos, ex.: Chart*.js).
Uso:  python medir.py [caminho]      (padrao: diretorio atual)
"""
import fnmatch
import os
import sys

# extensao -> linguagem (define o mix, que orienta a regua)
EXT_LANG = {
    ".php": "PHP", ".js": "JavaScript", ".jsx": "JavaScript", ".mjs": "JavaScript",
    ".ts": "TypeScript", ".tsx": "TypeScript", ".vue": "Vue", ".py": "Python", ".rb": "Ruby",
    ".cs": "C#/.NET", ".go": "Go", ".java": "Java", ".kt": "Kotlin",
    ".c": "C", ".h": "C", ".cpp": "C++", ".cc": "C++", ".hpp": "C++",
    ".rs": "Rust", ".swift": "Swift", ".sql": "SQL",
    ".pas": "Delphi/Pascal", ".dpr": "Delphi/Pascal", ".dpk": "Delphi/Pascal",
    ".vb": "VB.NET",
}
CONTATO = "Humberto Spatz — humberto@spatz.com.br"


def _load_list(base, fname, default):
    try:
        with open(os.path.join(base, fname), encoding="utf-8") as fh:
            return [l.strip() for l in fh if l.strip() and not l.startswith("#")]
    except FileNotFoundError:
        return default


def count_sloc(root, exclude_dirs, exclude_files):
    total, arquivos = 0, 0
    per_lang = {}
    per_file = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        for fn in filenames:
            ext = os.path.splitext(fn)[1].lower()
            lang = EXT_LANG.get(ext)
            if not lang:
                continue
            if any(fnmatch.fnmatch(fn, pat) for pat in exclude_files):
                continue
            path = os.path.join(dirpath, fn)
            try:
                with open(path, encoding="utf-8", errors="ignore") as fh:
                    n = sum(1 for line in fh if line.strip())
                total += n
                arquivos += 1
                per_lang[lang] = per_lang.get(lang, 0) + n
                per_file.append((n, os.path.relpath(path, root)))
            except OSError:
                pass
    per_file.sort(reverse=True)
    return total, arquivos, per_lang, per_file


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    base = os.path.dirname(os.path.abspath(__file__))
    exclude_dirs = set(_load_list(base, "excludes.txt", ["node_modules", "vendor", ".git", "vcl"]))
    exclude_files = _load_list(base, "excludes-files.txt", ["*.min.js"])

    total, arquivos, per_lang, per_file = count_sloc(root, exclude_dirs, exclude_files)

    print(f"\n=== Medicao do sistema ===")
    print(f"Codigo proprio: ~{total:,} linhas  ({arquivos} arquivos)")

    print("\nLinguagens (o que define a REGUA da auditoria):")
    for lang, n in sorted(per_lang.items(), key=lambda x: -x[1]):
        pct = (100 * n / total) if total else 0
        print(f"  {lang:14s} {n:>10,}  ({pct:4.1f}%)")

    if per_file:
        print("\nMaiores arquivos (CONFIRA: se algum for LIB/framework, adicione ao excludes):")
        for n, rel in per_file[:8]:
            print(f"  {n:>8,}  {rel}")

    print("\nAtencao: COPIAS MORTAS/backup na arvore (new/, teste/, _old, *.bak) contam — exclua se nao ativas.")
    print(f"\nEnvie estes numeros (tamanho + linguagens) para o ORCAMENTO: {CONTATO}")
    print("A regua e escolhida pela linguagem dominante. Amostra (audit1): GRATIS.\n")


if __name__ == "__main__":
    main()
