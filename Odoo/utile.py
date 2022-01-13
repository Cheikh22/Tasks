from bmi_db_2 import CODE_COMPTE_CLIENT_ORDINAIRE
from comptable import journal,POURCENTAGE_TAXE

def transform_date_form(old_date):
    new_date = old_date.split('-')
    new_date.reverse()
    return '-'.join(new_date)



date = '12-01-2022'
date = transform_date_form(date)


input_1_1 = {
    "type_transaction": "01",
    "libelle": "Transfert: client ordinaire  vers client PRO ",
    "id_transaction": 'TR 1.1',
    "journal": journal,
    "date": date,
    "montant": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_5_1 = {
    "type_transaction": "05",
    "libelle": "Retrait: client ordinaire  du caisse RimCash",
    "id_transaction": 'TR 5.1',
    "journal": journal,
    "date": date,
    "montant": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)
}

input_6_1 = {
    "type_transaction": "06",
    "libelle": "Retrait: client commerçant  du caisse RimCash",
    "id_transaction": 'TR 6.1',
    "journal": journal,
    "date": date,
    "montant": 1000,
    "commission": 50,
    "taxe": round((50)*POURCENTAGE_TAXE, 2)
}

input_7_1 = {
    "type_transaction": "07",
    "libelle": "Alimentation: client ordinaire , du caisse RimCash",
    "id_transaction": 'TR 7.1',
    "journal": journal,
    "date": date,
    "montant": 500,
    "commission": 20,
    "taxe": round((20)*POURCENTAGE_TAXE, 2)
}

input_8_1 = {
    "type_transaction": "08",
    "libelle": "Alimentation: client commerçant , du caisse RimCash",
    "id_transaction": 'TR 8.1',
    "journal": journal,
    "date": date,
    "montant": 500,
    "commission": 20,
    "taxe": round((20)*POURCENTAGE_TAXE, 2)
}

input_9_1 = {
    "type_transaction": "09",
    "libelle": "Paiement: client ordinaire , client commerçant",
    "id_transaction": 'TR 9.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)
}

input_10_1 = {
    "type_transaction": "10",
    "libelle": "Paiement: client commerçant , client commerçant",
    "id_transaction": 'TR 10.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)
}

input_11_1 = {
    "type_transaction": "11",
    "libelle": "Paiement classique: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 11.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)
}

input_12_1 = {
    "type_transaction": "12",
    "libelle": "Paiement classique: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 12.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 60,
    "taxe": round((60)*POURCENTAGE_TAXE, 2)
}

input_13_1 = {
    "type_transaction": "13",
    "libelle": "Paiement Ecommerce: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 13.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}

input_14_1 = {
    "type_transaction": "14",
    "libelle": "Paiement Ecommerce: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 14.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}

input_15_1 = {
    "type_transaction": "15",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.1',
    "journal": journal,
    "date": date,
    "montant": 50,
    "cout_achat": 47,
    "margeRimCash": 3,
    "taxe": round((3)*POURCENTAGE_TAXE, 2)
}

input_16_1 = {
    "type_transaction": "16",
    "libelle": "Paiement Facture: client RimCash, facturiers",
    "id_transaction": 'TR 16.1',
    "journal": journal,
    "date": date,
    "montant": 3500,
    "commission": 70,
    "taxe": round((70)*POURCENTAGE_TAXE, 2)
}

input_17_1 = {
    "type_transaction": "17",
    "libelle": "Paiement Facture: client RimCash, via agence",
    "id_transaction": 'TR 17.1',
    "journal": journal,
    "date": date,
    "montant": 3500,
    "commission": 70,
    "taxe": round((70)*POURCENTAGE_TAXE, 2)
}

input_18_1 = {
    "type_transaction": "18",
    "libelle": "Renboursement de facture: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 18.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}

input_19_1 = {
    "type_transaction": "19",
    "libelle": "Renboursement de facture: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 19.1',
    "journal": journal,
    "date": date,
    "montant": 400,
    "commission": 40,
    "taxe": round((40)*POURCENTAGE_TAXE, 2)
}
input_20_1 = {
    "type_transaction": "20",
    "libelle": "Transfert de masse: client pro vers multiple clients ordinaire",
    "id_transaction": 'TR 20.1',
    "journal": journal,
    "date": date,
    "montant": 20000,
    "commission": 150,
    "taxe": round(150*POURCENTAGE_TAXE, 2),
    "employes":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,5000,45],[CODE_COMPTE_CLIENT_ORDINAIRE,7000,60],[CODE_COMPTE_CLIENT_ORDINAIRE,9000,75]
    ]
}
input_21_1 = {
    "type_transaction": "21",
    "libelle": "depot cagnotte: clients ordinaire depot dans une cagnotte",
    "id_transaction": 'TR 21.1',
    "journal": journal,
    "date": date,
    "montant": 1000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_22_1 = {
    "type_transaction": "22",
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
    "id_transaction": 'TR 22.1',
    "journal": journal,
    "date": date,
    "montant": 4000,
    "commission": 50,
    "taxe": round(50*POURCENTAGE_TAXE, 2)
}

input_23_1 = {
    "type_transaction": "23",
    "libelle": "Versement: Versement de montant à une agence par un agent trésorier",
    "id_transaction": 'TR 23.1',
    "journal": journal,
    "date": date,
    "montant": 8000,
}

input_24_1 = {
    "type_transaction": "24",
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
    "id_transaction": 'TR 24.1',
    "journal": journal,
    "date": date,
    "montant": 7000,
}


input_25_1 = {
    "type_transaction": "25",
    "libelle": "Transfert: cagnotte vers multiple clients ordinaire",
    "id_transaction": 'TR 25.1',
    "journal": journal,
    "date": date,
    "montant": 20000,
    "beneficiaires":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,4000],[CODE_COMPTE_CLIENT_ORDINAIRE,7000],[CODE_COMPTE_CLIENT_ORDINAIRE,9000]
    ]
}

