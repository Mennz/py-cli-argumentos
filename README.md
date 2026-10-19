# Organizador de pasta por extensão

Script de linha de comando em Python que olha os arquivos de uma pasta e separa
cada um numa subpasta com o nome da extensão (`txt/`, `jpg/`, etc). Tem um modo
de simulação que só mostra o que seria feito, e pede confirmação antes de
mover os arquivos de verdade.

## O que pratiquei

- `argparse` para argumento posicional (`pasta`) e flag (`--dry-run`)
- `os.listdir` e `os.path.isfile` para separar arquivo de subpasta
- Agrupar valores num dicionário de listas
- `os.makedirs` com `exist_ok` e `shutil.move`
- Confirmação com `input()` antes de uma ação que não dá pra desfazer fácil

## Como rodar

```
python organizador.py <caminho-da-pasta>
```

Só mostrar o que seria movido, sem mexer em nada:

```
python organizador.py <caminho-da-pasta> --dry-run
```
