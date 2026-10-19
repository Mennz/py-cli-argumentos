import argparse
import os

parser = argparse.ArgumentParser(description="organiza arquivos de uma pasta em subpastas por extensao")
parser.add_argument("pasta", help="caminho da pasta a organizar")
parser.add_argument("--dry-run", action="store_true", help="so mostra o que seria feito, sem mover nada")

args = parser.parse_args()

arquivos = [
    nome for nome in os.listdir(args.pasta)
    if os.path.isfile(os.path.join(args.pasta, nome))
]

grupos = {}
for nome in arquivos:
    extensao = os.path.splitext(nome)[1].lower().lstrip(".")
    if extensao == "":
        extensao = "sem_extensao"

    if extensao not in grupos:
        grupos[extensao] = []
    grupos[extensao].append(nome)

if not grupos:
    print("nenhum arquivo para organizar")
else:
    for extensao, lista in grupos.items():
        print(f"\n{extensao} ({len(lista)}):")
        for nome in lista:
            print(f"  {nome}  ->  {extensao}/{nome}")

    if args.dry_run:
        print("\n(dry-run, nada foi movido)")
