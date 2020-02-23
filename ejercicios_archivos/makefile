CC = python3
ARCHPY = main.py
ARCH_MASTER = art_Maestro.csv
ARCH_NOV = art_Novedades.csv
ARCH_ERRORES = art_LogErrores.txt
ARCH_MASTER_ACTUAL = art_Maestro_Actualizado.csv

run: $(ARCHPY) $(ARCH_MASTER) $(ARCH_NOV)
	$(CC) $(ARCHPY)

del: $(ARCH_ERRORES) $(ARCH_MASTER_ACTUAL)
	rm -f $(ARCH_ERRORES) $(ARCH_MASTER_ACTUAL)

check: $(ARCH_ERRORES) $(ARCH_MASTER_ACTUAL)
	cat $(ARCH_ERRORES)
	cat $(ARCH_MASTER_ACTUAL)

see: $(ARCH_MASTER) $(ARCH_NOV)
	cat $(ARCH_MASTER)
	cat $(ARCH_NOV)


