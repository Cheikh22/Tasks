
CODE_COMPTE_CLIENT_ORDINAIRE = 2100000002   # Clients RimCash Ordinaire
CODE_COMPTE_CLIENT_PRO = 2100000003         # Clients RimCash Pro
CODE_COMPTE_CLIENT_OCCASIONNELS = 2100000004   # Clients occansionnels
CODE_COMPTE_CLIENT_COMMERCANTS = 2100000005   # Clients commerçant
CODE_COMPTE_AGENCE_PARTENAIRE = 2100000006  # Agence partenaire
CODE_COMPTE_FACTURIERS = 2100000008   #  Facturiers
CODE_COMPTE_CAGNOTTE = 2160000001   # Cagnotte
CODE_COMPTE_MISE_DISPOSITION_ENCOURS = 2180000001   # Mise disposition en cours

CODE_COMPTE_CAISSE_AGENCES_RIMASH = 1000001001 #Caisses Agences RimCash
CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE = 1000002001 #Caisses Agences Partenaires
CODE_COMPTE_ESPERCES = 101501   # Espèces
CODE_COMPTE_TRESORIER = 1000000001   # Tresorier

CODE_COMPTE_TAXE = 3230000001  # Taxes sur les opérations financieres
CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT = 3260000001  # Commissions Agences partenaires / transfert d'argents
CODE_COMPTE_COMMISSION_PARTENAIRE_RETRAIT = 3260001001  # Commissions Agences partenaires / Retrait d'argents
CODE_COMPTE_COMMISSION_PARTENAIRE_VERSEMENT = 3260002001  # Commissions Agences partenaires / Versement d'argents
CODE_COMPTE_COMMISSION_PARTENAIRE_FACTURIER = 3260003001  # Commissions RimCash /  paiement facturier
CODE_COMPTE_VIREMENT_BANQUAIRE = 3590001001   #  Virement banquaire 

CODE_COMPTE_COMMISSION_TRANSFERT = 7029000001  # Commissions RimCash / transfert d'argents
CODE_COMPTE_COMMISSION_MULTIPLE = 7029000002  # Commissions RimCash / transfert multiple
CODE_COMPTE_COMMISSION_RETRAIT = 7029001001   #  Commissions  RimCash / Retrait d'argents
CODE_COMPTE_COMMISSION_ACHAT_BIEN = 7029003001   #  Commissions  RimCash / Achat du bien
CODE_COMPTE_COMMISSION_ACHAT_BIEN_ECOMMERCE = 7029003002   #  Commissions  RimCash / Achat du bien E-commerce
CODE_COMPTE_COMMISSION_FACTURIER = 7029005001   #  Commissions  RimCash / paiement facturier
CODE_COMPTE_COMMISSION_VERSEMENT = 7029002001   #  Commissions  RimCash / versement d'argents
CODE_COMPTE_COMMISSION_DEPOT_CAGNOTTE = 7029004001   #  Commissions RimCash / Depot dans une cagnotte
CODE_COMPTE_FRAIS_VERSEMENT = 6021000001   #  Frais payé par RimCash / versement d'argents
CODE_COMPTE_COMMISSION_VIREMENT_BANQUAIRE = 7029002002  # Commissions RimCash /  Virement banquaire

CODE_COMPTE_MARGE_MAURITEL = 7029006001   #  Marge / vente carte de recharge Mauritel
CODE_COMPTE_MARGE_MATTEL = 7029006002   #  Marge / vente carte de recharge Mattel
CODE_COMPTE_MARGE_CHINGUITEL = 7029006003   #  Marge / vente carte de recharge Chinguitel
 
CODE_COMPTE_STOCK_CR_MAURITEL = 3500000001  #Stock carte de recharge Mauritel
CODE_COMPTE_STOCK_CR_MATTEL = 3500000002  #Stock carte de recharge Mattel
CODE_COMPTE_STOCK_CR_CHINGUITEL = 3500000003  #Stock carte de recharge Chinguitel

TAXE_TEST_MULTIPLE = 0.14

##############################################


# Ecriture comptable 1.1     Transfert de montant entre deux clients RimCash		

def ecriture_comptable_1_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
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



# Ecriture comptable 2.1     Transfert de montant d'un client RimCash à un client occasionnel (mise à disposition par compte)

def ecriture_comptable_2_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
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



# Ecriture comptable 2.1.1      Paiement béneficiaire

def ecriture_comptable_2_1_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction




# Ecriture comptable 2.2     Transfert de montant d'un client RimCash à un client occasionnel (mise à disposition par compte)

def ecriture_comptable_2_2(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commission = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
    compte_commission_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant+commission +commission_partenaire+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commission, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commission_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 2.2.1      Paiement béneficiaire

def ecriture_comptable_2_2_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction



# Ecriture comptable 3.1    Transfert de montant d'un client occasionnel à un client Rimcash via une agence (recharge)

def ecriture_comptable_3_1(account_model, id_transaction, date, journal, libelle, montant, frais_versement=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_frais_versement = account_model.search([('code', '=', CODE_COMPTE_FRAIS_VERSEMENT)])[0]
    compte_commission_partenaire_versement = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_VERSEMENT)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': 0, 'credit': frais_versement,'account_id': compte_frais_versement, 'name': libelle}),
            (0, 0, {'debit': frais_versement, 'credit': 0,'account_id': compte_commission_partenaire_versement, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 3.2    Transfert de montant d'un client occasionnel à un client Rimcash via une agence

def ecriture_comptable_3_2(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]

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




# Ecriture comptable 4.1

def ecriture_comptable_4_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
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



# Ecriture comptable 4.1.1      Paiement béneficiaire

def ecriture_comptable_4_1_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction



# Ecriture comptable 4.2
def ecriture_comptable_4_2(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commission = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
    compte_commission_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant+commission +commission_partenaire+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commission, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commission_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 4.2.1      Paiement béneficiaire

def ecriture_comptable_4_2_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction




# Ecriture comptable 4.3
def ecriture_comptable_4_3(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commission = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
    compte_commission_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant+commission +commission_partenaire+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commission, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commission_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 4.3.1      Paiement béneficiaire

def ecriture_comptable_4_3_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction





# Ecriture comptable 4.4
def ecriture_comptable_4_4(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire_recepteur=0, commission_partenaire_emetteur=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_commission = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_TRANSFERT)])[0]
    compte_commission_partenaire_recepteur = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT)])[0]
    compte_commission_partenaire_emetteur = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_TRANSFERT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant+commission+commission_partenaire_recepteur +commission_partenaire_emetteur+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commission, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire_recepteur, 'credit': 0,'account_id': compte_commission_partenaire_recepteur, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire_emetteur, 'credit': 0,'account_id': compte_commission_partenaire_emetteur, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 4.4.1      Paiement béneficiaire

def ecriture_comptable_4_4_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_MISE_DISPOSITION_ENCOURS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        ]
    }
    return transaction




# Ecriture comptable 5.1      Retrait d'espèces via une agence par un client Rimcash

def ecriture_comptable_5_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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




# Ecriture comptable 5.2      Retrait d'espèces via une agence par un client Rimcash

def ecriture_comptable_5_2(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_commision_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+commission_partenaire+ taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commision_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 6.1      Retrait d'espèces via une agence par un commerçant Rimcash

def ecriture_comptable_6_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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





# Ecriture comptable 6.2      Retrait d'espèces via une agence par un commerçant Rimcash

def ecriture_comptable_6_2(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_RETRAIT)])[0]
    compte_commision_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_RETRAIT)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+commission_partenaire+ taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commision_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 7.1    Alimentation du solde client Rimcash via une agence 

def ecriture_comptable_7_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]

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



# Ecriture comptable 7.2    Alimentation du solde client Rimcash via une agence (recharge)

def ecriture_comptable_7_2(account_model, id_transaction, date, journal, libelle, montant, frais_versement=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_frais_versement = account_model.search([('code', '=', CODE_COMPTE_FRAIS_VERSEMENT)])[0]
    compte_commission_partenaire_versment = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_VERSEMENT)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': 0, 'credit': frais_versement,'account_id': compte_frais_versement, 'name': libelle}),
            (0, 0, {'debit': frais_versement, 'credit': 0,'account_id': compte_commission_partenaire_versment, 'name': libelle}),
        ]
    }
    return transaction





# Ecriture comptable 8.1    Alimentation du solde commerçant Rimcash via une agence 

def ecriture_comptable_8_1(account_model, id_transaction, date, journal, libelle, montant):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_RIMASH)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
        ]
    }
    return transaction





# Ecriture comptable 8.2    Alimentation du solde commerçant Rimcash via une agence (recharge)

def ecriture_comptable_8_2(account_model, id_transaction, date, journal, libelle, montant, frais_versement=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_COMMERCANTS)])[0]
    compte_frais_versement = account_model.search([('code', '=', CODE_COMPTE_FRAIS_VERSEMENT)])[0]
    compte_commission_partenaire_versement = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_VERSEMENT)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant , 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': 0, 'credit': frais_versement,'account_id': compte_frais_versement, 'name': libelle}),
            (0, 0, {'debit': frais_versement, 'credit': 0,'account_id': compte_commission_partenaire_versement, 'name': libelle}),
        ]
    }
    return transaction





# Ecriture comptable 9.1      Paiement sur la demande d'un commerçant RimCash par un client RimCash

def ecriture_comptable_9_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_10_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_11_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_12_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_13_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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


# Ecriture comptable 14.1     Paiement E-commerce à commerçant RimCash par un client RimCash

def ecriture_comptable_14_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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





# Ecriture comptable 15.1    Paiement de carte téléphonique par un client RimCash Mauritel

def ecriture_comptable_15_1(account_model, id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
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
            (0, 0, {'debit': margeRimCash, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction


# Ecriture comptable 15.2     Paiement de carte téléphonique par un client RimCash Mattel

def ecriture_comptable_15_2(account_model, id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
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
            (0, 0, {'debit': margeRimCash, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 15.3      Paiement de carte téléphonique par un client RimCashChinguitel

def ecriture_comptable_15_3(account_model, id_transaction, date, journal, libelle, montant,cout_achat, margeRimCash=0, taxe=0):
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
            (0, 0, {'debit': margeRimCash, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




# Ecriture comptable 16.1     Paiement de facture par un client RimCash à un facturier

def ecriture_comptable_16_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_17_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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




# Ecriture comptable 17.2    Paiement de facture par un client RimCash à un facturier via une agence

def ecriture_comptable_17_2(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, commission_partenaire=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAISSE_AGENCES_PARTENAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_FACTURIERS)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_FACTURIER)])[0]
    compte_commision_partenaire = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_PARTENAIRE_FACTURIER)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': montant +commission+commission_partenaire+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': montant, 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': commission_partenaire, 'credit': 0,'account_id': compte_commision_partenaire, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0,'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction



# Ecriture comptable 18.1     Rembourssement de facture à un client RimCash par un commerçant RimCash

def ecriture_comptable_18_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_19_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
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

def ecriture_comptable_20_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0, recepteurs=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_MULTIPLE)])[0]
    compte_taxe = account_model.search([('code', '=', CODE_COMPTE_TAXE)])[0]
    listAll = [(0, 0, {'debit': 0, 'credit': montant +commission+taxe, 'account_id': compte_origine, 'name': libelle}),(0, 0, {'debit': commission, 'credit': 0,'account_id': compte_commision, 'name': libelle}),(0, 0, {'debit': round(taxe,2), 'credit': 0,'account_id': compte_taxe, 'name': libelle})]
    for i in range(len(recepteurs)):
        compte_beneficiaire = account_model.search([('code', '=', recepteurs[i][0])])[0]
        beneficiaire = (0, 0, {'debit': recepteurs[i][1], 'credit': 0,'account_id': compte_beneficiaire,'name': libelle})
        frais = (0, 0, {'debit': 0, 'credit': recepteurs[i][2],'account_id': compte_beneficiaire,'name': libelle})
        commiss = (0, 0, {'debit': recepteurs[i][2]-round(recepteurs[i][2]*TAXE_TEST_MULTIPLE,2), 'credit': 0,'account_id': compte_commision,'name': libelle})
        tax = (0, 0, {'debit': round(recepteurs[i][2]*TAXE_TEST_MULTIPLE,2), 'credit': 0,'account_id': compte_taxe, 'name': libelle})
        listAll.append(beneficiaire)
        listAll.append(frais)
        listAll.append(commiss)
        listAll.append(tax)

    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': listAll
           
    }
    return transaction



# Ecriture comptable 21.1     Dépôt de montant par un client RimCash dans une cagnotte

def ecriture_comptable_21_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_DEPOT_CAGNOTTE)])[0]
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

def ecriture_comptable_22_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_DEPOT_CAGNOTTE)])[0]
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

def ecriture_comptable_23_1(account_model, id_transaction, date, journal, libelle, montant):
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

def ecriture_comptable_24_1(account_model, id_transaction, date, journal, libelle, montant):
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

def ecriture_comptable_25_1(account_model, id_transaction, date, journal, libelle, montant,recepteurs=[]):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CAGNOTTE)])[0]
    listAll = [(0, 0, {'debit': 0, 'credit': montant, 'account_id': compte_origine, 'name': libelle})]
    for i in range(len(recepteurs)):
        compte_beneficiaire = account_model.search([('code', '=', recepteurs[i][0])])[0]
        list1=(0, 0, {'debit': recepteurs[i][1], 'credit': 0,'account_id': compte_beneficiaire, 'name': libelle})
        listAll.append(list1)
    
    transaction = {
        'ref': id_transaction,
        'date': date,
        'journal_id': journal,
        'line_ids': listAll
    }
    return transaction




# Ecriture comptable 26.1     Transfert d'un client RimCash a autre Banque

def ecriture_comptable_26_1(account_model, id_transaction, date, journal, libelle, montant, commission=0, taxe=0):
    compte_origine = account_model.search([('code', '=', CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code', '=', CODE_COMPTE_VIREMENT_BANQUAIRE)])[0]
    compte_commision = account_model.search([('code', '=', CODE_COMPTE_COMMISSION_VIREMENT_BANQUAIRE)])[0]
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

