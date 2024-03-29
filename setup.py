from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Mi primer paquete de Python'
LONG_DESCRIPTION = 'Mi primer paquete de Python con una descripción ligeramente más larga'

# Configurando
setup(
    name="primer_paquete_ux_isa_3",  # Corregido: eliminado espacio en blanco extra
    version=VERSION,
    author="isa_belle7",
    author_email="isabellajib5@gmail.com",  # Corregido: sin < y >
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[''],  # añade cualquier paquete adicional que debe ser instalado junto con tu paquete. Ej: 'caer'
    keywords=['python', 'primer paquete'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
