import argparse
import os

parser = argparse.ArgumentParser(description="organiza arquivos de uma pasta em subpastas por extensao")
parser.add_argument("pasta", help="caminho da pasta a organizar")
parser.add_argument("--dry-run", action="store_true", help="so mostra o que seria feito, sem mover nada")

args = parser.parse_args()

# listdir pega pasta e arquivo junto, por isso o isfile
arquivos = [
    nome for nome in os.listdir(args.pasta)
    if os.path.isfile(os.path.join(args.pasta, nome))
]

print(f"{len(arquivos)} arquivo(s) encontrado(s) em {args.pasta}")
for nome in arquivos:
    print(f" - {nome}")
