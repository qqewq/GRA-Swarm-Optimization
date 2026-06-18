from setuptools import setup, find_packages

setup(
    name="gra-swarm-optimization",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "matplotlib>=3.4.0",
        "sympy>=1.9",
        "torch>=1.9.0",
        "networkx>=2.6",
    ],
    author="GRA-Swarm Team",
    description="Рой ИИ-агентов по GRA-Обнуленке для рекурсивной оптимизации",
)
