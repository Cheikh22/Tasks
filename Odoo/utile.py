from bmi_db_2 import CODE_COMPTE_CLIENT_ORDINAIRE
from comptable import journal,POURCENTAGE_TAXE

def transform_date_form(old_date):
    new_date = old_date.split('-')
    new_date.reverse()
    return '-'.join(new_date)


date = '08-01-2022'
date = transform_date_form(date)

input_1_1 = {
    "libelle": "Transfert: client ordinaire  vers client PRO ",
    "reference": 'TR 1.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_1_2 = {
    "libelle": "Transfert: client ordinaire vers agence partenaire",
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
    "libelle": "Transfert: client ordinaire vers client occasionnel",
    "reference": 'TR 2.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_2_2 = {
    "libelle": "Transfert: client ordinaire vers client occasionnel ",
    "reference": 'TR 2.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)
}

input_2_3 = {
    "libelle": "Transfert: client ordinaire vers client occasionnel",
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
    "libelle": "Transfert: client occasionnel client ordinaire vers",
    "reference": 'TR 3.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)
}

input_3_2 = {
    "libelle": "Transfert: client occasionnel client ordinaire vers",
    "reference": 'TR 3.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)
}

input_4_1 = {
    "libelle": "Transfert: client occasionnel client vers occasionnels  ",
    "reference": 'TR 4.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)
}

input_4_2 = {
    "libelle": "Transfert: client occasionnel  client vers occasionnels  ",
    "reference": 'TR 4.2',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 1000,
    "commission": 50,
    "commission_partenaire_recepteur": 30,
    "taxe": round((50+30)*POURCENTAGE_TAXE, 2)
}

input_5_1 = {
    "libelle": "Retrait: client ordinaire  du caisse RimCash",
    "reference": 'TR 5.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_retrait": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)
}

input_6_1 = {
    "libelle": "Retrait: client commerçant  du caisse RimCash",
    "reference": 'TR 6.1',
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

input_8_1 = {
    "libelle": "Alimentation: client commerçant , du caisse RimCash",
    "reference": 'TR 8.1',
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

input_10_1 = {
    "libelle": "Paiement: client commerçant , client commerçant",
    "reference": 'TR 10.1',
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

input_12_1 = {
    "libelle": "Paiement classique: commerçant RimCash, commerçant RimCash",
    "reference": 'TR 12.1',
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

input_14_1 = {
    "libelle": "Paiement Ecommerce: commerçant RimCash, commerçant RimCash",
    "reference": 'TR 14.1',
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

input_17_1 = {
    "libelle": "Paiement Facture: client RimCash, via agence",
    "reference": 'TR 17.1',
    "journal": journal,
    "date": date,
    "montant_paye": 3500,
    "commission": 70,
    "taxe": round((70)*POURCENTAGE_TAXE, 2)
}

input_18_1 = {
    "libelle": "Renboursement de facture: client RimCash, commerçant RimCash",
    "reference": 'TR 18.1',
    "journal": journal,
    "date": date,
    "valeur_du_bien": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}

input_19_1 = {
    "libelle": "Renboursement de facture: commerçant RimCash, commerçant RimCash",
    "reference": 'TR 19.1',
    "journal": journal,
    "date": date,
    "valeur_du_bien": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}
input_20_1 = {
    "libelle": "Transfert de masse: client pro vers multiple clients ordinaire",
    "reference": 'TR 20.1',
    "journal": journal,
    "date": date,
    "valeur_nette_du_transfert": 20000,
    "commission_multiple": 150,
    "taxe_multiple": round(150*POURCENTAGE_TAXE, 2),
    "employes":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,5000,45],[CODE_COMPTE_CLIENT_ORDINAIRE,7000,60],[CODE_COMPTE_CLIENT_ORDINAIRE,9000,75]
    ]
}
input_21_1 = {
    "libelle": "depot cagnotte: clients ordinaire depot dans une cagnotte",
    "reference": 'TR 21.1',
    "journal": journal,
    "date": date,
    "valeur_de_depot": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_22_1 = {
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
    "reference": 'TR 22.1',
    "journal": journal,
    "date": date,
    "solde_de_cagnotte": 4000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_23_1 = {
    "libelle": "Versement: Versement de montant à une agence par un agent trésorier",
    "reference": 'TR 23.1',
    "journal": journal,
    "date": date,
    "montant_de_versement": 8000,
}

input_24_1 = {
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
    "reference": 'TR 24.1',
    "journal": journal,
    "date": date,
    "montant_de_retrait": 7000,
}


input_25_1 = {
    "libelle": "Transfert: cagnotte vers multiple clients ordinaire",
    "reference": 'TR 25.1',
    "journal": journal,
    "date": date,
    "solde_de_cagnotte": 20000,
    "beneficiaires":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,4000],[CODE_COMPTE_CLIENT_ORDINAIRE,7000],[CODE_COMPTE_CLIENT_ORDINAIRE,9000]
    ]
}
