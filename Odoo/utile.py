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

input_3_1 = {
    "libelle": "Transfert: client occasionnel 44554411 client ordinaire 37486414 vers",
    "reference": 'TR 3.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)

}

input_3_2 = {
    "libelle": "Transfert: client occasionnel 44554411 client ordinaire 37486414 vers",
    "reference": 'TR 3.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)

}


input_4_1 = {
    "libelle": "Transfert: client occasionnel 44554411 client vers occasionnels 37486414 ",
    "reference": 'TR 4.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)

}

input_4_2 = {
    "libelle": "Transfert: client occasionnel 44554411 client vers occasionnels 37486414 ",
    "reference": 'TR 4.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)

}

input_5_1 = {
    "libelle": "Retrait: client ordinaire 37486414 du caisse RimCash",
    "reference": 'TR 5.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_retrait": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)

}

input_7_1 = {
    "libelle": "Alimentation: client ordinaire , du caisse RimCash",
    "reference": 'TR 7.1',
    "journal": journal,
    "date": date,
    "montant_alimentation": 500,
    "commission": 20,
    "taxe": round((20)*POURCENTAGE_TAXE, 2)

}

input_9_1 = {
    "libelle": "Paiement: client ordinaire , client commerçant",
    "reference": 'TR 9.1',
    "journal": journal,
    "date": date,
    "valeur_du_bien": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)

}
input_11_1 = {
    "libelle": "Paiement classique: client RimCash, commerçant RimCash",
    "reference": 'TR 11.1',
    "journal": journal,
    "date": date,
    "valeur_du_bien": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)

}
input_13_1 = {
    "libelle": "Paiement Ecommerce: client RimCash, commerçant RimCash",
    "reference": 'TR 13.1',
    "journal": journal,
    "date": date,
    "valeur_du_bien": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)

}

input_15_1 = {
    "libelle": "Paiement de carte: par client RimCash",
    "reference": 'TR 15.1',
    "journal": journal,
    "date": date,
    "montant_de_vente": 50,
    "cout_achat": 47,
    "margeRimCash": 3,
    "taxe": round((3)*POURCENTAGE_TAXE, 2)

}

input_16_1 = {
    "libelle": "Paiement Facture: client RimCash, facturiers",
    "reference": 'TR 16.1',
    "journal": journal,
    "date": date,
    "montant_paye": 3500,
    "commission": 70,
    "taxe": round((70)*POURCENTAGE_TAXE, 2)

}

