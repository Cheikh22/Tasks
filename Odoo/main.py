from comptable import comtabiliser,CODE_COMPTE_CLIENT_ORDINAIRE

date = '2022-01-14 16:00:11'

input_1_1 = {
    "type_transaction": "01",
    "libelle": "Transfert: client ordinaire  vers client PRO ",
    "id_transaction": 'TR 1.1',
    "date": date,
    "montant": 1000,
    "frais": 50
}

input_5_1 = {
    "type_transaction": "05",
    "libelle": "Retrait: client ordinaire  du caisse RimCash",
    "id_transaction": 'TR 5.1',
    "date": date,
    "montant": 1000,
    "frais": 50
}

input_6_1 = {
    "type_transaction": "06",
    "libelle": "Retrait: client commerçant  du caisse RimCash",
    "id_transaction": 'TR 6.1',
    "date": date,
    "montant": 1000,
    "frais": 50
}

input_7_1 = {
    "type_transaction": "07",
    "libelle": "Alimentation: client ordinaire , du caisse RimCash",
    "id_transaction": 'TR 7.1',
    "date": date,
    "montant": 500,
}

input_8_1 = {
    "type_transaction": "08",
    "libelle": "Alimentation: client commerçant , du caisse RimCash",
    "id_transaction": 'TR 8.1',
    "date": date,
    "montant": 500,
}

input_9_1 = {
    "type_transaction": "09",
    "libelle": "Paiement: client ordinaire , client commerçant",
    "id_transaction": 'TR 9.1',
    "date": date,
    "montant": 400,
    "frais": 60
}

input_10_1 = {
    "type_transaction": "10",
    "libelle": "Paiement: client commerçant , client commerçant",
    "id_transaction": 'TR 10.1',
    "date": date,
    "montant": 400,
    "frais": 60
}

input_11_1 = {
    "type_transaction": "11",
    "libelle": "Paiement classique: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 11.1',
    "date": date,
    "montant": 400,
    "frais": 60
}

input_12_1 = {
    "type_transaction": "12",
    "libelle": "Paiement classique: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 12.1',
    "date": date,
    "montant": 400,
    "frais": 60
}

input_13_1 = {
    "type_transaction": "13",
    "libelle": "Paiement Ecommerce: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 13.1',
    "date": date,
    "montant": 400,
    "frais": 40
}

input_14_1 = {
    "type_transaction": "14",
    "libelle": "Paiement Ecommerce: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 14.1',
    "date": date,
    "montant": 400,
    "frais": 40
}

input_15_1 = {
    "type_transaction": "151",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.1',
    "date": date,
    "montant": 50,
    "cout_achat": 47,
}
input_15_2 = {
    "type_transaction": "152",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.2',
    "date": date,
    "montant": 50,
    "cout_achat": 47,
}
input_15_3 = {
    "type_transaction": "153",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.3',
    "date": date,
    "montant": 50,
    "cout_achat": 47,
}

input_16_1 = {
    "type_transaction": "16",
    "libelle": "Paiement Facture: client RimCash, facturiers",
    "id_transaction": 'TR 16.1',
    "date": date,
    "montant": 3500,
    "frais": 70
}

input_17_1 = {
    "type_transaction": "17",
    "libelle": "Paiement Facture: client RimCash, via agence",
    "id_transaction": 'TR 17.1',
    "date": date,
    "montant": 3500,
    "frais": 70
}

input_18_1 = {
    "type_transaction": "18",
    "libelle": "Renboursement de facture: client RimCash, commerçant RimCash",
    "id_transaction": 'TR 18.1',
    "date": date,
    "montant": 400,
    "frais": 40
}

input_19_1 = {
    "type_transaction": "19",
    "libelle": "Renboursement de facture: commerçant RimCash, commerçant RimCash",
    "id_transaction": 'TR 19.1',
    "date": date,
    "montant": 400,
    "frais": 40
}

input_20_1 = {
    "type_transaction": "20",
    "libelle": "Transfert de masse: client pro vers multiple clients ordinaire",
    "id_transaction": 'TR 20.1',
    "date": date,
    "montant": 77000,
    "frais": 80,
    "recepteurs":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,15000,45],[CODE_COMPTE_CLIENT_ORDINAIRE,24000,60],[CODE_COMPTE_CLIENT_ORDINAIRE,38000,75]
    ]
}

input_21_1 = {
    "type_transaction": "21",
    "libelle": "depot cagnotte: clients ordinaire depot dans une cagnotte",
    "id_transaction": 'TR 21.1',
    "date": date,
    "montant": 1000,
    "frais": 50
}

input_22_1 = {
    "type_transaction": "22",
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
    "id_transaction": 'TR 22.1',
    "date": date,
    "montant": 4000,
    "frais": 50
}

input_23_1 = {
    "type_transaction": "23",
    "libelle": "Versement: Versement de montant à une agence par un agent trésorier",
    "id_transaction": 'TR 23.1',
    "date": date,
    "montant": 8000,
}

input_24_1 = {
    "type_transaction": "24",
    "libelle": "Retrait: Retrait de montant d'une agence par un agent trésorier ",
    "id_transaction": 'TR 24.1',
    "date": date,
    "montant": 7000,
}


input_25_1 = {
    "type_transaction": "25",
    "libelle": "Transfert: cagnotte vers multiple clients ordinaire",
    "id_transaction": 'TR 25.1',
    "date": date,
    "montant": 20000,
    "recepteurs":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,4000],[CODE_COMPTE_CLIENT_ORDINAIRE,7000],[CODE_COMPTE_CLIENT_ORDINAIRE,9000]
    ]
}

#comtabiliser(**input_5_1)
# comtabiliser(**input_6_1)
# comtabiliser(**input_7_1)
# comtabiliser(**input_8_1)
# comtabiliser(**input_9_1)
# comtabiliser(**input_10_1)
# comtabiliser(**input_11_1)
# comtabiliser(**input_12_1)
# comtabiliser(**input_13_1)
# comtabiliser(**input_14_1)
# comtabiliser(**input_15_1)
# comtabiliser(**input_15_2)
# comtabiliser(**input_15_3)
# comtabiliser(**input_16_1)
# comtabiliser(**input_17_1)
# comtabiliser(**input_18_1)
# comtabiliser(**input_19_1)
comtabiliser(**input_20_1)
# comtabiliser(**input_21_1)
# comtabiliser(**input_22_1)
# comtabiliser(**input_23_1)
# comtabiliser(**input_24_1)
# comtabiliser(**input_25_1)