from typing import List
import odoolib


HOSTNAME = "cheikh.odoo.com"
DATABASE = "cheikh"
LOGIN = "cheikh.raby24@gmail.com"
PASSWORD = "cheikh2434"
PORT = 443
PROTOCOL = "jsonrpcs"

JOURNAL_TRANSFERT = "TestComptable"

CODE_COMPTE_CLIENT_ORDINAIRE = 2100000002   # Clients RimCash Ordinaire
CODE_COMPTE_CLIENT_PRO = 2100000003         # Clients RimCash Pro
CODE_COMPTE_CLIENT_OCCASIONNELS = 2100000004   # Clients occansionnels
CODE_COMPTE_CLIENT_COMMERCANTS = 2100000005   # Clients commerçant
CODE_COMPTE_AGENCE_PARTENAIRE = 2100000006  # Agence partenaire
CODE_COMPTE_FACTURIERS = 2100000008   #  Facturiers

CODE_COMPTE_TAXE = 3230000001  # Taxes sur les opérations financieres
CODE_COMPTE_CAISSE_AGENCES_RIMASH = 1000001001 #Caisses Agences RimCash
CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE = 1000002001 #Caisses Agences Partenaires
CODE_COMPTE_ESPERCES = 101501   # Espèces
CODE_COMPTE_CAGNOTTE = 2160000001   # Cagnotte
CODE_COMPTE_TRESORIER = 1000000001   # Tresorier







CODE_COMPTE_COMMISSION = 7029000001  # Commissions RimCash / transfert d'argents
CODE_COMPTE_COMMISSION_MULTIPLE = 7029000002  # Commissions RimCash / transfert multiple
CODE_COMPTE_COMMISSION_RETRAIT = 7029001001   #  Commissions  RimCash / Retrait d'argents
CODE_COMPTE_COMMISSION_ACHAT_BIEN = 7029003001   #  Commissions  RimCash / Achat du bien
CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE = 7029003002   #  Commissions  RimCash / Achat du bien E-commerce
CODE_COMPTE_COMMISSION_FACTURIER = 7029005001   #  Commissions  RimCash / paiement facturier
CODE_COMPTE_COMMISSION_VERSEMENT = 7029002001   #  Commissions  RimCash / versement d'argents
CODE_COMPTE_COMMISSION_DEPOT_CAGNOTTE = 7029004001   #  Commissions RimCash / Depot dans une cagnotte


CODE_COMPTE_MARGE_MAURITEL = 7029006001   #  Marge / vente carte de recharge Mauritel
CODE_COMPTE_MARGE_MATTEL = 7029006002   #  Marge / vente carte de recharge Mattel
CODE_COMPTE_MARGE_CHINGUITEL = 7029006003   #  Marge / vente carte de recharge Chinguitel
 
CODE_COMPTE_STOCK_CR_MAURITEL = 3500000001  #Stock carte de recharge Mauritel
CODE_COMPTE_STOCK_CR_MATTEL = 3500000002  #Stock carte de recharge Mattel
CODE_COMPTE_STOCK_CR_CHINGUITEL = 3500000003  #Stock carte de recharge Chinguitel

 


POURCENTAGE_MARGE_MAURITEL = 0.10
POURCENTAGE_MARGE_MATTEL = 0.10
POURCENTAGE_MARGE_CHINGUITEL = 0.10



POURCENTAGE_TAXE = 0.14  # La taxe est fixée à 14% de la commission


##############################################


def transform_date_form(old_date):
    new_date = old_date.split('-')
    new_date.reverse()
    return '-'.join(new_date)


# Ecriture comptable 1.1     Transfert de montant entre deux clients RimCash		

def ecriture_comptable_1_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


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


# Ecriture comptable 5.1      Retrait d'espèces via une agence par un client Rimcash

def ecriture_comptable_5_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 6.1      Retrait d'espèces via une agence par un commerçant Rimcash

def ecriture_comptable_6_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction






# Ecriture comptable 7.1    Alimentation du solde client Rimcash via une agence 

def ecriture_comptable_7_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_VERSEMENT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 8.1    Alimentation du solde commerçant Rimcash via une agence 

def ecriture_comptable_8_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_VERSEMENT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 9.1      Paiement sur la demande d'un commerçant RimCash par un client RimCash

def ecriture_comptable_9_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 10.1      Paiement sur la demande d'un commerçant RimCash par un commerçant RimCash

def ecriture_comptable_10_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 11.1     Paiement classique à commerçant RimCash par un client RimCash

def ecriture_comptable_11_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 12.1     Paiement classique à commerçant RimCash par un commerçant RimCash

def ecriture_comptable_12_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 13.1     Paiement E-commerce à commerçant RimCash par un commerçant RimCash

def ecriture_comptable_13_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 14.1     Paiement E-commerce à commerçant RimCash par un client RimCash

def ecriture_comptable_14_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction





# Ecriture comptable 15.1    Paiement de carte téléphonique par un client RimCash Mauritel

def ecriture_comptable_15_1(id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_MAURITEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_MAURITEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 15.2     Paiement de carte téléphonique par un client RimCash Mattel

def ecriture_comptable_15_2(id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_MATTEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_MATTEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 15.3      Paiement de carte téléphonique par un client RimCashChinguitel

def ecriture_comptable_15_3(id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_CHINGUITEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_CHINGUITEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 16.1     Paiement de facture par un client RimCash à un facturier

def ecriture_comptable_16_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_FACTURIERS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_FACTURIER)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant + commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 17.1    Paiement de facture par un client RimCash à un facturier via une agence

def ecriture_comptable_17_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_FACTURIERS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_FACTURIER)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 18.1     Rembourssement de facture à un client RimCash par un commerçant RimCash

def ecriture_comptable_18_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant-commission-taxe , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 19.1     Rembourssement de facture à un commerçant RimCash par un commerçant RimCash

def ecriture_comptable_19_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant-commission-taxe , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction






# Ecriture comptable 20.1     Paiement de plusieurs clients RimCash par un client RimCash Pro (Entreprise) 

def ecriture_comptable_20_1(id_transaction, date, journal, libelle, montant,commission=0,taxe=0,recepteurs=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_commision_multiple = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_MULTIPLE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]
    listAll = []
    for i in range(len(recepteurs)):
        list1=(0, 0, {'debit': recepteurs[i][1], 'credit': recepteurs[i][2]+recepteurs[i][2]*POURCENTAGE_TAXE,'account_id': recepteurs[i][0], 'name': libelle}),(0, 0, {'debit': recepteurs[i][2], 'credit': 0,'account_id': compte_commision, 'name': libelle}),(0, 0, {'debit': recepteurs[i][2]*POURCENTAGE_TAXE, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        listAll.append(list1)
    print(listAll)

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision_multiple, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
            listAll
            
        ]
    }
    return transaction



# Ecriture comptable 21.1     Dépôt de montant par un client RimCash dans une cagnotte

def ecriture_comptable_21_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 22.1     Transfert du solde de la cagnotte vers un client RimCash

def ecriture_comptable_22_1(id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 23.1     Versement de montant à une agence par un agent trésorier

def ecriture_comptable_23_1(id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_TRESORIER)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 24.1     Retrait de montant d'une agence par un agent trésorier

def ecriture_comptable_24_1(id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_TRESORIER)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 25.1     Fermeture de la cagnotte et remboussement des dépôts faits par les clients rimCash

def ecriture_comptable_25_1(id_transaction, date, journal, libelle, montant,recepteurs=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    listAll = [(0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle})]
    for i in range(len(recepteurs)):
        compte_beneficiaire = account_model.search([('code', '=', recepteurs[i][0])])[0]
        list1=(0, 0, {'debit': recepteurs[i][1], 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        listAll.append(list1)
    print(listAll)

    
    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': listAll
    }
    return transaction




connection = odoolib.get_connection(
    hostname=HOSTNAME,
    database=DATABASE,
    login=LOGIN,
    password=PASSWORD,
    port=PORT,
    protocol=PROTOCOL
)


try:
    if connection.get_user_context():
        print('Connection established!!!')
except:
    print('Connection failed!!!')


# Initialisation des models à utiliser
journal_model = connection.get_model('account.journal')
account_model = connection.get_model('account.account')
move_model = connection.get_model('account.move')


journal_t = journal_model.search(
    [('name', '=', JOURNAL_TRANSFERT)])  # Si n'existe pas retourne []
if not journal_t:
    print("Ce journal n'existe pas!!!")
    quit()
else:
    journal = journal_t[0]


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
    "recepteurs":[
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
    "recepteurs":[
        [CODE_COMPTE_CLIENT_ORDINAIRE,4000],[CODE_COMPTE_CLIENT_ORDINAIRE,7000],[CODE_COMPTE_CLIENT_ORDINAIRE,9000]
    ]
}








def comtabiliser(type_transaction, id_transaction, date, journal, libelle, montant,cout_achat=0,margeRimCash=0, commission=0, taxe=0, recepteurs=[]) :
    value = type_transaction
    if value == '01':
        transaction = ecriture_comptable_1_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '05':
        transaction = ecriture_comptable_5_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '06':
        transaction = ecriture_comptable_6_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '07':
        transaction = ecriture_comptable_7_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '08':
        transaction = ecriture_comptable_8_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '09':
        transaction = ecriture_comptable_9_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '10':
        transaction = ecriture_comptable_10_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '11':
        transaction = ecriture_comptable_11_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '12':
        transaction = ecriture_comptable_12_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '13':
        transaction = ecriture_comptable_13_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '14':
        transaction = ecriture_comptable_14_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '15':
        transaction = ecriture_comptable_15_1(id_transaction, date, journal, libelle, montant,cout_achat,margeRimCash,taxe)
    elif value == '16':
        transaction = ecriture_comptable_16_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '17':
        transaction = ecriture_comptable_17_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '18':
        transaction = ecriture_comptable_18_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '19':
        transaction = ecriture_comptable_19_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '20':
        transaction = ecriture_comptable_20_1(id_transaction, date, journal, libelle, montant, commission, taxe, recepteurs)
    elif value == '21':
        transaction = ecriture_comptable_21_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '22':
        transaction = ecriture_comptable_22_1(id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '23':
        transaction = ecriture_comptable_23_1(id_transaction, date, journal, libelle, montant)
    elif value == '24':
        transaction = ecriture_comptable_24_1(id_transaction, date, journal, libelle, montant)
    elif value == '25':
        transaction = ecriture_comptable_25_1(id_transaction, date, journal, libelle, montant, recepteurs)

    # Ajout des pièces comptables
    print("Import en cours .......")

    try:
        move = move_model.create(transaction)
        move_model.action_post(move)
        print('La transaction qui a pour référence : ' +
            transaction['ref'] + ' a été importée')
    except Exception as err:
        print('La transaction qui a pour référence : ' +
            transaction['ref'] + ' n a pas été importée')
        print('The error: ', str(err))

    print("Import terminé!!!")

comtabiliser(**input_25_1)