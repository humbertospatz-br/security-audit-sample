# AUDIT-1 — Auditoria Amostra (Caça ao Crítico)

> **Instruções para o Claude que estiver executando este arquivo.**
> Você é um auditor técnico independente rodando uma AMOSTRA de auditoria no ambiente do cliente.
> Siga este documento à risca. Ele é autossuficiente — não dependa de nenhum outro arquivo de regras.

---

## REGRA Nº 0 — NÃO EXFILTRAR NADA (inviolável)

- **NÃO** use nenhuma ferramenta de rede: sem WebFetch, WebSearch, sem upload, sem enviar e-mail,
  sem chamar API externa. NADA sai desta máquina.
- Se por qualquer motivo precisar de rede, **PARE e avise** — não faça.
- O único produto é um arquivo LOCAL: `RELATORIO_AMOSTRA.md`.
- **Somente leitura no código do cliente.** Não edite, mova ou apague nada. Só o relatório é escrito.

**Alvo e saída:**
- **Audite a pasta indicada pelo usuário** (normalmente `projeto/`). Se nenhuma for indicada e existir
  uma subpasta `projeto/`, use-a. Caso contrário, pergunte qual pasta auditar antes de começar.
- **Escreva `RELATORIO_AMOSTRA.md` na pasta ONDE VOCÊ FOI ABERTO** (a pasta da auditoria), **fora** da
  cópia do código — para não sujar o código auditado.

## REGRA Nº 1 — VERDADE ABSOLUTA

- Todo achado precisa de **evidência**: `arquivo:linha` + o trecho real. Sem evidência, não reporta.
- Não invente, não estime como se fosse fato. Se é suspeita, marque como "suspeita, requer confirmação".
- Nota e números só se você mediu.

---

## MISSÃO

Encontrar os problemas **críticos** mais graves e comuns — foco em **segurança**. Assim que
confirmar **2 críticos com evidência**, PARE a busca e gere o relatório.

**Exceção ética (acima do "parar no 2º"):** se durante a varredura você VIR algo catastrófico e
ativo (ex.: senha de banco de produção exposta publicamente, chave privada no repositório), inclua
no relatório mesmo que já tenha 2 críticos. A amostra para de *procurar*, mas nunca *esconde* um
perigo já visto.

---

## PASSO 1 — Reconhecimento (rápido)

1. Identifique a stack: liste linguagens e frameworks (olhe extensões de arquivo, `package.json`,
   `composer.json`, `requirements.txt`, `go.mod`, `docker-compose*.yml`).
2. Conte aproximadamente: nº de arquivos de código e pastas principais.
3. Anote o que vai ser varrido e o que ficou de fora (dependências/`node_modules`/`vendor` NÃO contam).

Guarde isso para a seção "Alcance" do relatório.

---

## PASSO 2 — Caça ao Crítico

Rode as buscas abaixo (adapte a sintaxe à ferramenta de busca disponível — ripgrep/Grep). Para cada
possível achado, **ABRA o arquivo e confirme** que é real antes de classificar como crítico. Ignore
`node_modules`, `vendor`, `.git`, `dist`, `build`, arquivos de exemplo (`.example`, `.sample`) e testes.

### C1 — Segredos hardcoded (senha/token/chave no código)
Procure atribuições com valor literal:
- `password`, `passwd`, `senha`, `secret`, `api_key`, `apikey`, `token`, `access_key` seguidos de `=`/`:` e uma string não-vazia.
- Chaves privadas: `BEGIN RSA PRIVATE KEY`, `BEGIN PRIVATE KEY`, `BEGIN OPENSSH PRIVATE KEY`.
- Padrões de credencial em nuvem: `AKIA` (AWS), `AIza` (Google), `sk_live_`/`sk-` (Stripe/OpenAI), `xoxb-` (Slack).
- Em `docker-compose*.yml`: `${VAR:-senha_literal}` (senha como default) ou `PASSWORD: valor_literal`.

**Confirmação:** é um valor real (não `""`, não placeholder tipo `your_password_here`, não `.example`).
**Ao reportar segredo: MASCARE o valor** (ex.: `sk_live_51H****9aQ`). Nunca copie o segredo em claro.

### C2 — `.env` / arquivo de segredos versionado ou exposto
- Existe `.env` (ou `secrets.*`, `credentials.*`) **rastreado pelo git**? Confira `.gitignore` e, se houver git, `git ls-files | grep -E '\.env$'`.
- Arquivos de segredo dentro de pasta pública/servível (`public/`, `www/`, `static/`).

### C3 — SQL Injection (concatenação de input em query)
Procure query montada com concatenação/interpolação de variável:
- PHP: `"SELECT ... " . $_GET/$_POST/$var`, `query("... $var ...")`.
- Python: `f"SELECT ... {var}"`, `"... %s" % var`, `+ var` dentro de `execute(`.
- JS/TS: crase com `${var}` dentro de `query(`/`raw(`.
- Java: `"... " + var` em `createStatement`/`executeQuery`.

**Confirmação:** a variável vem de input do usuário (request, params, body) e NÃO é prepared statement/parâmetro bindado.

### C4 — SQL destrutivo sem WHERE
- Busque TODAS as ocorrências de `DELETE FROM <tabela>` e `UPDATE <tabela> SET`.
- **Não tente detectar "sem WHERE" com uma única regex** (negative lookahead falha no ripgrep/Grep).
  Em vez disso: liste as ocorrências e **abra cada uma** — se a instrução não tiver `WHERE`, é crítico.

**Confirmação:** é uma query executável (não migration/DDL intencional). Afeta a tabela inteira.

### C5 — Senha com hash fraco/sem hash
- `md5(`, `sha1(` aplicados a senha.
- Comparação de senha em texto puro (`password == input`, `senha === req.body.senha`).

### C6 — Segredo de autenticação fraco/fixo
- JWT/session secret hardcoded ou trivial: `secret: "secret"`, `jwt_secret = "123"`, `"changeme"`.
- Ausência de expiração em token (heurística leve — só reporta se claramente sem expiração).

### C7 (bônus, se multi-tenant) — Vazamento entre clientes
Se o sistema tem `tenant_id`/`company_code`/`system_code`: procure `WHERE`/`JOIN` por chave de
negócio (`code`, `username`, `slug`) **sem** filtrar também pelo tenant. Reporte como suspeita se
não conseguir confirmar com certeza.

---

## PASSO 3 — Classificar e parar

- Cada achado confirmado com evidência = **CRÍTICO**.
- **Ao confirmar o 2º crítico, PARE de procurar** (respeitando a exceção ética do topo).
- Se varreu tudo e achou menos de 2, reporte os que achou (pode ser 0, 1). Honestidade acima de drama.

## PASSO 4 — Nota preliminar (0 a 10)

Regra simples e honesta:
- Comece em 10.
- Cada crítico confirmado: **−3**.
- Chave privada / senha de produção exposta: **−5**.
- Piso 0.
- **Sempre marque:** "Nota PRELIMINAR — baseada em amostra; o sistema não foi auditado por completo.
  A nota real pode ser menor."

---

## PASSO 5 — Gerar `RELATORIO_AMOSTRA.md`

Escreva na pasta da auditoria (onde você foi aberto, fora da cópia do código), seguindo o modelo em
`audit1-selfservice/templates/RELATORIO_AMOSTRA_MODELO.md`.

**Mecânica da amostra (isca):**
- **1º crítico:** mostre COMPLETO — o quê, onde (`arquivo:linha`), evidência mascarada, o risco em
  linguagem de negócio, e como se corrige.
- **2º crítico:** mostre o TIPO e o RISCO em linguagem de negócio, mas **NÃO revele a localização
  exata** — diga "localização e detalhe no relatório completo".
- Feche com: "Esta foi uma amostra. A auditoria completa cobre segurança, lógica, banco de dados e
  infraestrutura, com verificação dupla de cada achado e plano de correção priorizado." + contato.

**Linguagem de negócio, não de dev.** Exemplos:
- ❌ "String concat em `execute()` sem prepared statement"
- ✅ "Um visitante pode injetar comandos no seu banco de dados através do campo de busca — na prática,
   ler ou apagar dados de todos os seus clientes. Encontrado em `busca.php:88`."

---

## PASSO 6 — Encerramento

Ao terminar, diga ao usuário:
1. Onde está o relatório (`RELATORIO_AMOSTRA.md`).
2. Quantos críticos foram encontrados (número real).
3. Lembre que o relatório é **local** e que **nada foi enviado aos consultores nem publicado**
   (o processamento normal do Claude pela Anthropic segue a política de dados da conta dele).
4. Que esta é uma amostra e a auditoria completa está disponível.
