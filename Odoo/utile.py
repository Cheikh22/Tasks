from comptable import journal,POURCENTAGE_TAXE

def transform_date_form(old_date):
    new_date = old_date.split('-')
    new_date.reverse()
    return '-'.join(new_date)


date = '08-01-2022'
date = transform_date_form(date)

input_1_1 = {
    "libelle": "Transfert: client ordinaire 37486414 vers client PRO 27777732",
    "reference": 'TR 1.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)

}

input_1_2 = {
    "libelle": "Transfert: client ordinaire 37486414 vers agence partenaire",
    "reference": 'TR 1.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50, 
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)

}

input_1_3 = {
    "libelle": "agence partenaire vers agence partenaire",
    "reference": 'TR 1.3',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50, 
    "commission_partenaire_recepteur": 30,
    "commission_partenaire_emetteur": 20,
    "taxe": round((50+30+20)*POURCENTAGE_TAXE, 2)

}

input_2_1 = {
    "libelle": "Transfert: client ordinaire 37486414 vers client occasionnel 44554411",
    "reference": 'TR 2.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)

}

input_2_2 = {
    "libelle": "Transfert: client ordinaire 37486414 vers client occasionnel 44554411",
    "reference": 'TR 2.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)

}
input_2_3 = {
    "libelle": "Transfert: client ordinaire 37486414 vers client occasionnel 44554411",
    "reference": 'TR 2.3',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "commission_partenaire_emetteur": 20,
    "taxe": round((50+30+20)*POURCENTAGE_TAXE, 2)

}
