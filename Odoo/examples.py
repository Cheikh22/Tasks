from bmi_db_2 import CODE_COMPTE_CLIENT_ORDINAIRE
from comptable import journal



date = '2022-01-14 16:00:11.25485+00'

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
    "frais": 3
}
input_15_2 = {
    "type_transaction": "152",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.2',
    "date": date,
    "montant": 50,
    "cout_achat": 47,
    "frais": 3
}
input_15_3 = {
    "type_transaction": "153",
    "libelle": "Paiement de carte: par client RimCash",
    "id_transaction": 'TR 15.3',
    "date": date,
    "montant": 50,
    "cout_achat": 47,
    "frais": 3
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
    "montant": 20000,
    "frais": 150,
    "recepteurs":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,5000,45],[CODE_COMPTE_CLIENT_ORDINAIRE,7000,60],[CODE_COMPTE_CLIENT_ORDINAIRE,9000,75]
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
    "libelle": "Transfert: cagnotte vers clients ordinaire ",
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








# # Ecriture comptable 1.2
# def ecriture_comptable_1_2(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 1.3
# def ecriture_comptable_1_3(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_commission_partenaire_emetteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_emetteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_emetteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 2.1

# def ecriture_comptable_2_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 2.2
# def ecriture_comptable_2_2(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 2.3
# def ecriture_comptable_2_3(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_commission_partenaire_emetteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_emetteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_emetteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 3.1

# def ecriture_comptable_3_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 3.2
# def ecriture_comptable_3_2(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 4.1

# def ecriture_comptable_4_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 4.2
# def ecriture_comptable_4_2(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 4.3
# def ecriture_comptable_4_3(id_transaction, date, journal, libelle, montant, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commission = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_commission_partenaire_recepteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_commission_partenaire_emetteur = account_model.search(
#         [('code', '=', CODE_COMPTE_AGENCE_PARTENAIRE)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': id_transaction,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': montant+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': montant, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commission, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
#             (0, 0, {'debit': commission_partenaire_emetteur, 'credit': 0,
#              'account_id': compte_commission_partenaire_emetteur, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction
