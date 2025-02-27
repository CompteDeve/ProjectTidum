!/bin/bash
# Vérifier si l'IP est fournie
if [ -z "$1" ]; then
    echo "Erreur : Aucun IP fourni."
    exit 1
fi
# Définir l'adresse IP
IP=$1
# Exécuter le scan Nmap
echo "Scan de $IP en cours..."
nmap -p- "$IP"
