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

def ecriture_comptable_1_1(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# # Ecriture comptable 1.2
# def ecriture_comptable_1_2(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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
# def ecriture_comptable_1_3(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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

# def ecriture_comptable_2_1(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 2.2
# def ecriture_comptable_2_2(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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
# def ecriture_comptable_2_3(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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

# def ecriture_comptable_3_1(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 3.2
# def ecriture_comptable_3_2(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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

# def ecriture_comptable_4_1(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
#     compte_origine = account_model.search(
#         [('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
#     compte_beneficiaire = account_model.search(
#         [('code', '=', CODE_COMPTE_CLIENT_OCCASIONNELS)])[0]
#     compte_commision = account_model.search(
#         [('code', '=', CODE_COMPTE_COMMISSION)])[0]
#     compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

#     transaction = {
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +
#              commission+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
#              'account_id': compte_beneficiaire, 'name': libelle}),
#             (0, 0, {'debit': commission, 'credit': 0,
#              'account_id': compte_commision, 'name': libelle}),
#             (0, 0, {'debit': taxe, 'credit': 0,
#              'account_id': compte_taxe, 'name': libelle}),
#         ]
#     }
#     return transaction


# # Ecriture comptable 4.2
# def ecriture_comptable_4_2(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission +
#              commission_partenaire_recepteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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
# def ecriture_comptable_4_3(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0, taxe=0):
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
#         'ref': reference,
#         'date': date,
#         'journal_id': journal,
#         'line_ids': [
#             (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission+commission_partenaire_recepteur +
#              commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
#             (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
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

def ecriture_comptable_5_1(reference, date, journal, libelle, valeur_nette_du_retrait, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_retrait +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_nette_du_retrait, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 6.1      Retrait d'espèces via une agence par un commerçant Rimcash

def ecriture_comptable_6_1(reference, date, journal, libelle, valeur_nette_du_retrait, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_retrait +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_nette_du_retrait, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction






# Ecriture comptable 7.1    Alimentation du solde client Rimcash via une agence 

def ecriture_comptable_7_1(reference, date, journal, libelle, montant_alimentation, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_VERSEMENT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_alimentation +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_alimentation, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 8.1    Alimentation du solde commerçant Rimcash via une agence 

def ecriture_comptable_8_1(reference, date, journal, libelle, montant_alimentation, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_VERSEMENT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_alimentation +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_alimentation, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 9.1      Paiement sur la demande d'un commerçant RimCash par un client RimCash

def ecriture_comptable_9_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 10.1      Paiement sur la demande d'un commerçant RimCash par un commerçant RimCash

def ecriture_comptable_10_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 11.1     Paiement classique à commerçant RimCash par un client RimCash

def ecriture_comptable_11_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 12.1     Paiement classique à commerçant RimCash par un commerçant RimCash

def ecriture_comptable_12_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 13.1     Paiement E-commerce à commerçant RimCash par un commerçant RimCash

def ecriture_comptable_13_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 14.1     Paiement E-commerce à commerçant RimCash par un client RimCash

def ecriture_comptable_14_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction





# Ecriture comptable 15.1    Paiement de carte téléphonique par un client RimCash Mauritel

def ecriture_comptable_15_1(reference, date, journal, libelle, montant_de_vente,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_MAURITEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_MAURITEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_de_vente , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 15.2     Paiement de carte téléphonique par un client RimCash Mattel

def ecriture_comptable_15_2(reference, date, journal, libelle, montant_de_vente,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_MATTEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_MATTEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_de_vente , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 15.3      Paiement de carte téléphonique par un client RimCashChinguitel

def ecriture_comptable_15_3(reference, date, journal, libelle, montant_de_vente,cout_achat, margeRimCash=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_STOCK_CR_CHINGUITEL)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_MARGE_CHINGUITEL)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_de_vente , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': cout_achat, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': margeRimCash-taxe, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 16.1     Paiement de facture par un client RimCash à un facturier

def ecriture_comptable_16_1(reference, date, journal, libelle, montant_paye, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_FACTURIERS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_FACTURIER)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_paye + commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_paye, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 17.1    Paiement de facture par un client RimCash à un facturier via une agence

def ecriture_comptable_17_1(reference, date, journal, libelle, montant_paye, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_FACTURIERS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_FACTURIER)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_paye +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_paye, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 18.1     Rembourssement de facture à un client RimCash par un commerçant RimCash

def ecriture_comptable_18_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien-commission-taxe , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 19.1     Rembourssement de facture à un commerçant RimCash par un commerçant RimCash

def ecriture_comptable_19_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_du_bien-commission-taxe , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_du_bien-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction






# Ecriture comptable 20.1     Paiement de plusieurs clients RimCash par un client RimCash Pro (Entreprise) 

def ecriture_comptable_20_1(reference, date, journal, libelle, valeur_nette_du_transfert,commission_multiple=0,taxe_multiple=0,employees=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_commision_multiple = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_MULTIPLE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]
    for i in range(len(employees)):
        list1=(0, 0, {'debit': employees[i][1], 'credit': employees[i][2]+employees[i][2]*POURCENTAGE_TAXE,'account_id': employees[i][0], 'name': libelle}),(0, 0, {'debit': employees[i][2], 'credit': 0,'account_id': compte_commision, 'name': libelle}),(0, 0, {'debit': employees[i][2]*POURCENTAGE_TAXE, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        listAll = list1
    print(listAll)

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +commission_multiple+taxe_multiple, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': commission_multiple, 'credit': 0,'account_id': compte_commision_multiple, 'name': libelle}),
            (0, 0, {'debit': taxe_multiple, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
            listAll
            
        ]
    }
    return transaction



# Ecriture comptable 21.1     Dépôt de montant par un client RimCash dans une cagnotte

def ecriture_comptable_21_1(reference, date, journal, libelle, valeur_de_depot, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_de_depot +commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_de_depot, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 22.1     Transfert du solde de la cagnotte vers un client RimCash

def ecriture_comptable_22_1(reference, date, journal, libelle, solde_de_cagnotte, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': solde_de_cagnotte, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': solde_de_cagnotte-commission-taxe, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 23.1     Versement de montant à une agence par un agent trésorier

def ecriture_comptable_23_1(reference, date, journal, libelle, montant_de_versement):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_TRESORIER)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_de_versement , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_de_versement, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 24.1     Retrait de montant d'une agence par un agent trésorier

def ecriture_comptable_24_1(reference, date, journal, libelle, montant_de_versement):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_TRESORIER)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant_de_versement , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant_de_versement, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 25.1     Fermeture de la cagnotte et remboussement des dépôts faits par les clients rimCash

def ecriture_comptable_25_1(reference, date, journal, libelle, solde_de_cagnotte,beneficiaire=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    
    (0, 0, {'debit': beneficiaire[i][1], 'credit': 0,'account_id': beneficiaire[i][0], 'name': libelle})
    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': solde_de_cagnotte, 'account_id': compte_origine, 'name': libelle}) for i in range(len(beneficiaire))
        ]
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


date = '10-01-2022'
date = transform_date_form(date)


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




transaction = ecriture_comptable_25_1(**input_25_1)


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
