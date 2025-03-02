from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.text import Text

def compare_files(file1, file2):
    try:
        with open(file1, 'r', encoding='utf-8') as f1, open(file2, 'r', encoding='utf-8') as f2:
            content1 = f1.readlines()
            content2 = f2.readlines()
        
        differences = []
        for i, (line1, line2) in enumerate(zip(content1, content2), start=1):
            if line1 != line2:
                differences.append((i, line1.strip(), line2.strip()))
        
        if len(content1) > len(content2):
            differences.append((f"Fișier1 are linii suplimentare de la linia {len(content2) + 1}:",))
            differences.extend([(i + len(content2) + 1, line.strip(), "") for i, line in enumerate(content1[len(content2):])])
        elif len(content2) > len(content1):
            differences.append((f"Fișier2 are linii suplimentare de la linia {len(content1) + 1}:",))
            differences.extend([(i + len(content1) + 1, "", line.strip()) for i, line in enumerate(content2[len(content1):])])

        console = Console()
        if differences:
            table = Table(title="Diferențe găsite", show_header=True, header_style="bold magenta")
            table.add_column("Linia", justify="right", style="cyan", no_wrap=True, width=10)
            table.add_column("Fișier1", style="magenta")
            table.add_column("Fișier2", style="green")

            for diff in differences:
                if len(diff) == 1:
                    table.add_row(diff[0], "", "")
                else:
                    table.add_row(str(diff[0]), diff[1], diff[2])

            console.print(Panel(table, title="Comparare Fișiere", border_style="blue"))
        else:
            console.print(Panel(Text("Fișierele sunt identice.", style="bold green"), title="Comparare Fișiere", border_style="blue"))
    except FileNotFoundError as e:
        console.print(Panel(Text(f"Eroare: {e}", style="bold red"), title="Eroare", border_style="red"))
    except Exception as e:
        console.print(Panel(Text(f"A apărut o eroare: {e}", style="bold red"), title="Eroare", border_style="red"))

# Exemplu de utilizare
file1 = "generate.txt"
file2 = "generate1.txt"
compare_files(file1, file2)
