import argparse
import os
import shutil

parser = argparse.ArgumentParser(description="organiza arquivos de uma pasta em subpastas por extensao")
parser.add_argument("pasta", help="caminho da pasta a organizar")
parser.add_argument("--dry-run", action="store_true", help="so mostra o que seria feito, sem mover nada")

args = parser.parse_args()

arquivos = [
    # listdir traz pasta e arquivo junto, por isso o isfile
    nome for nome in os.listdir(args.pasta)
    if os.path.isfile(os.path.join(args.pasta, nome))
]

grupos = {}
for nome in arquivos:
    # splitext devolve o ponto junto (".txt"), por isso o lstrip
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
    else:
        resposta = input("\nmover os arquivos acima? (s/n) ")
        if resposta.lower() == "s":
            for extensao, lista in grupos.items():
                pasta_destino = os.path.join(args.pasta, extensao)
                os.makedirs(pasta_destino, exist_ok=True)
                for nome in lista:
                    origem = os.path.join(args.pasta, nome)
                    shutil.move(origem, os.path.join(pasta_destino, nome))
            print("arquivos movidos")
        else:
            print("cancelado")
