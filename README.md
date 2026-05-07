# Escarcelle — Flatpak packaging

> [Français](#français) | [English](#english)

---

## Français

**Escarcelle** est un logiciel de gestion pour les épiceries sociales et solidaires, développé par Softinnov en partenariat avec l'ANDES. Il suit les produits de l'entrée en stock jusqu'au bénéficiaire final, gère les tarifications, les budgets des bénéficiaires, les commandes fournisseurs et produit des statistiques.

Ce dépôt contient le packaging Flatpak non officiel d'Escarcelle, maintenu par l'[AFGES](https://afges.org).

### Installation via Flatpakref (recommandé)

Ouvrez le fichier [`.flatpakref`](https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakref) depuis GNOME Logiciels ou Discover, ou via la commande :

```bash
flatpak install https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakref
```

Cela ajoute automatiquement le dépôt et installe l'application en une seule étape. Les mises à jour sont ensuite reçues automatiquement via :

```bash
flatpak update
```

### Installation via le dépôt Flatpak (méthode alternative)

Ajoutez d'abord le dépôt avec le fichier [`.flatpakrepo`](https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakrepo) depuis GNOME Logiciels ou Discover, ou via :

```bash
flatpak remote-add --if-not-exists escarcelle https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakrepo
flatpak install escarcelle net.escarcelle.Cashdesk
```

### Installation via bundle (méthode alternative)

Téléchargez le fichier `.flatpak` depuis les [releases GitHub](../../releases) puis :

```bash
flatpak install --bundle net.escarcelle.Cashdesk.flatpak
```

### Construction locale

Prérequis : `flatpak`, `flatpak-builder`

```bash
make build      # Construit le Flatpak
make install    # Construit et installe pour l'utilisateur courant
make run        # Lance l'application
make bundle     # Génère le fichier .flatpak et le dépôt OSTree local
make clean      # Supprime les artefacts de build
```

---

## English

**Escarcelle** is a management application for social and solidarity grocery stores, developed by Softinnov in partnership with ANDES. It tracks products from inventory entry to final beneficiary, manages pricing, beneficiary budgets, supplier orders, and generates statistics.

This repository contains the unofficial Flatpak packaging for Escarcelle, maintained by [AFGES](https://afges.org).

### Install via Flatpakref (recommended)

Open the [`.flatpakref`](https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakref) file from GNOME Software or Discover, or run:

```bash
flatpak install https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakref
```

This adds the repository and installs the application in one step. Updates are then received automatically via:

```bash
flatpak update
```

### Install via the Flatpak repository (alternative)

Add the repository first using the [`.flatpakrepo`](https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakrepo) file from GNOME Software or Discover, or run:

```bash
flatpak remote-add --if-not-exists escarcelle https://afges.github.io/escarcelle/net.escarcelle.Cashdesk.flatpakrepo
flatpak install escarcelle net.escarcelle.Cashdesk
```

### Install via bundle (alternative)

Download the `.flatpak` file from [GitHub Releases](../../releases) then:

```bash
flatpak install --bundle net.escarcelle.Cashdesk.flatpak
```

### Local build

Requirements: `flatpak`, `flatpak-builder`

```bash
make build      # Build the Flatpak
make install    # Build and install for the current user
make run        # Run the application
make bundle     # Generate the .flatpak bundle and local OSTree repository
make clean      # Remove build artifacts
```
