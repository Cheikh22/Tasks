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

CODE_COMPTE_TAXE = 3230000001  # Taxes sur les opérations financieres
CODE_COMPTE_CAISSE_AGENCES_RIMASH = 1000001001 #Caisses Agences RimCash
CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE = 1000002001 #Caisses Agences Partenaires
CODE_COMPTE_ESPERCES = 101501   # Espèces
CODE_COMPTE_FACTURIERS = 2100000008   #  Facturiers

CODE_COMPTE_COMMISSION = 7029000001  # Commissions RimCash / transfert d'argents
CODE_COMPTE_COMMISSION_RETRAIT = 7029001001   #  Commissions  RimCash / Retrait d'argents
CODE_COMPTE_COMMISSION_ACHAT_BIEN = 7029003001   #  Commissions  RimCash / Achat du bien
CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE = 7029003002   #  Commissions  RimCash / Achat du bien E-commerce
CODE_COMPTE_COMMISSION_FACTURIER = 7029005001   #  Commissions  RimCash / paiement facturier
CODE_COMPTE_COMMISSION_VERSEMENT = 7029002001   #  Commissions  RimCash / versement d'argents

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


# Ecriture comptable 1.1

def ecriture_comptable_1_1(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
    compte_origine = account_model.search(
        [('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search(
        [('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search(
        [('code', '=', CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert +
             commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0,
             'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,
             'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,
             'account_id': compte_taxe, 'name': libelle}),
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


# Ecriture comptable 5.1

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



# Ecriture comptable 7.1

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



# Ecriture comptable 9.1

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



# Ecriture comptable 11.1

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


# Ecriture comptable 13.1

def ecriture_comptable_13_1(reference, date, journal, libelle, valeur_du_bien, commission=0, taxe=0):
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



# Ecriture comptable 15.1 Mauritel

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


# Ecriture comptable 15.2 Mattel

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



# Ecriture comptable 15.3 Chinguitel

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




# Ecriture comptable 16.1

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


date = '08-01-2022'
date = transform_date_form(date)


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




transaction = ecriture_comptable_16_1(**input_16_1)


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
