import argparse

parser = argparse.ArgumentParser(description="organiza arquivos de uma pasta em subpastas por extensao")
parser.add_argument("pasta", help="caminho da pasta a organizar")
parser.add_argument("--dry-run", action="store_true", help="so mostra o que seria feito, sem mover nada")

args = parser.parse_args()

print(f"pasta: {args.pasta}")
print(f"dry-run: {args.dry_run}")
