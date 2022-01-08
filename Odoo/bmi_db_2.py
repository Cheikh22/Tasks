import odoolib


HOSTNAME = "adnbmi.odoo.com"
DATABASE = "adnbmi"
LOGIN = "abeidadnan@gmail.com"
PASSWORD = "adnBMI20"
PORT = 443
PROTOCOL = "jsonrpcs"

JOURNAL_TRANSFERT = "TestTRF"

CODE_COMPTE_CLIENT_ORDINAIRE = 2100000002   # Clients RimCash Ordinaire
CODE_COMPTE_CLIENT_PRO = 2100000003         # Clients RimCash Pro
CODE_COMPTE_COMMISSION = 7029000001         # Commissions RimCash / transfert d'argents
CODE_COMPTE_TAXE = 3230000001               # Taxes sur les opérations financieres

POURCENTAGE_TAXE = 0.14                     # La taxe est fixée à 14% de la commission


##############################################


def transform_date_form(old_date):
    new_date = old_date.split('-')
    new_date.reverse()
    return '-'.join(new_date)


def ecriture_comptable(reference, date, journal, libelle, valeur_nette_du_transfert, commission=0, taxe=0):
    compte_origine = account_model.search([('code','=',CODE_COMPTE_CLIENT_ORDINAIRE)])[0]
    compte_beneficiaire = account_model.search([('code','=',CODE_COMPTE_CLIENT_PRO)])[0]
    compte_commision = account_model.search([('code','=',CODE_COMPTE_COMMISSION)])[0]
    compte_taxe = account_model.search([('code','=',CODE_COMPTE_TAXE)])[0]

    transaction = {
        'ref': reference,
        'date': date,
        'journal_id': journal,
        'line_ids': [
            (0, 0, {'debit': 0, 'credit': valeur_nette_du_transfert+commission+taxe, 'account_id': compte_origine, 'name': libelle}),
            (0, 0, {'debit': valeur_nette_du_transfert, 'credit': 0, 'account_id': compte_beneficiaire, 'name': libelle}),
            (0, 0, {'debit': commission, 'credit': 0, 'account_id': compte_commision, 'name': libelle}),
            (0, 0, {'debit': taxe, 'credit': 0, 'account_id': compte_taxe, 'name': libelle}),
        ]
    }
    return transaction




connection = odoolib.get_connection (
    hostname = HOSTNAME,
    database = DATABASE,
    login = LOGIN,
    password = PASSWORD,
    port = PORT,
    protocol = PROTOCOL
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



journal_t = journal_model.search([('name','=',JOURNAL_TRANSFERT)]) # Si n'existe pas retourne []
if not journal_t:
    print("Ce journal n'existe pas!!!")
    quit()
else:
    journal = journal_t[0]



libelle = "Transfert: client ordinaire 37486414 vers client PRO 27777732"
reference = 'TR000001'
date = '28-12-2021'
date = transform_date_form(date)
valeur_nette_du_transfert = 4000
commission = 50
taxe = round(commission*POURCENTAGE_TAXE, 2)


transaction = ecriture_comptable(reference, date, journal, libelle, valeur_nette_du_transfert, commission, taxe)


# Ajout des pièces comptables
print("Import en cours .......")

try:
    move = move_model.create(transaction)
    move_model.action_post(move)
    print('La transaction qui a pour référence : ' + transaction['ref'] + ' a été importée')
except Exception as err:
    print('La transaction qui a pour référence : ' + transaction['ref'] + ' n a pas été importée')
    print('The error: ', str(err))

print("Import terminé!!!")
