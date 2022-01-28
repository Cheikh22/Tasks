
import odoolib
from utile import *  

HOSTNAME = "cheikh.odoo.com"
DATABASE = "cheikh"
LOGIN = "cheikh.raby24@gmail.com"
PASSWORD = "cheikh2434"
PORT = 443
PROTOCOL = "jsonrpcs"
JOURNAL_TRANSFERT = "TestComptable"

POURCENTAGE_TAXE = 0.14  # La taxe est fixée à 14% de la commission


def comtabiliser(type_transaction, id_transaction, date, libelle, montant,cout_achat=0, frais_de_depart=0,frais_versement=0, recepteurs=[]) :

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

    value = type_transaction
    taxe = frais_de_depart*POURCENTAGE_TAXE
    commission = frais_de_depart-taxe
    commission_partenaire=0

    if value == '01':
        transaction = ecriture_comptable_1_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '02.1':
        transaction = ecriture_comptable_2_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '02.2':
        transaction = ecriture_comptable_2_2(account_model, id_transaction, date, journal, libelle, montant, commission, taxe, commission_partenaire)
    elif value == '03.1':
        transaction = ecriture_comptable_3_1(account_model, id_transaction, date, journal, libelle, montant,frais_versement)
    elif value == '03.2':
        transaction = ecriture_comptable_3_2(account_model, id_transaction, date, journal, libelle, montant)
    elif value == '04.1':
        transaction = ecriture_comptable_4_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '04.2':
        transaction = ecriture_comptable_4_2(account_model, id_transaction, date, journal, libelle, montant, commission, taxe,commission_partenaire)
    elif value == '04.3':
        transaction = ecriture_comptable_4_3(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '04.4':
        transaction = ecriture_comptable_4_4(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '05.1':
        transaction = ecriture_comptable_5_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '05.2':
        transaction = ecriture_comptable_5_2(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '06.1':
        transaction = ecriture_comptable_6_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '06.2':
        transaction = ecriture_comptable_6_2(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '07.1':
        transaction = ecriture_comptable_7_1(account_model, id_transaction, date, journal, libelle, montant)
    elif value == '07.2':
        transaction = ecriture_comptable_7_2(account_model, id_transaction, date, journal, libelle, montant, frais_versement)
    elif value == '08.1':
        transaction = ecriture_comptable_8_1(account_model, id_transaction, date, journal, libelle, montant)
    elif value == '08.2':
        transaction = ecriture_comptable_8_2(account_model, id_transaction, date, journal, libelle, montant, frais_versement)
    elif value == '09':
        transaction = ecriture_comptable_9_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '10':
        transaction = ecriture_comptable_10_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '11':
        transaction = ecriture_comptable_11_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '12':
        transaction = ecriture_comptable_12_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '13':
        transaction = ecriture_comptable_13_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '14':
        transaction = ecriture_comptable_14_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '15.1':
        taxe_marge=(montant-cout_achat)*POURCENTAGE_TAXE
        margeRimCash=montant-cout_achat-taxe_marge
        transaction = ecriture_comptable_15_1(account_model, id_transaction, date, journal, libelle, montant,cout_achat,margeRimCash,taxe_marge)
    elif value == '15.2':
        taxe_marge=(montant-cout_achat)*POURCENTAGE_TAXE
        margeRimCash=montant-cout_achat-taxe_marge
        transaction = ecriture_comptable_15_2(account_model, id_transaction, date, journal, libelle, montant,cout_achat,margeRimCash,taxe_marge)
    elif value == '15.3':
        taxe_marge=(montant-cout_achat)*POURCENTAGE_TAXE
        margeRimCash=montant-cout_achat-taxe_marge
        transaction = ecriture_comptable_15_3(account_model, id_transaction, date, journal, libelle, montant,cout_achat,margeRimCash,taxe_marge)
    elif value == '16':
        transaction = ecriture_comptable_16_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '17.1':
        transaction = ecriture_comptable_17_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '17.2':
        transaction = ecriture_comptable_17_2(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '18':
        transaction = ecriture_comptable_18_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '19':
        transaction = ecriture_comptable_19_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '20':
        transaction = ecriture_comptable_20_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe, recepteurs)
    elif value == '21':
        transaction = ecriture_comptable_21_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '22':
        transaction = ecriture_comptable_22_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)
    elif value == '23':
        transaction = ecriture_comptable_23_1(account_model, id_transaction, date, journal, libelle, montant)
    elif value == '24':
        transaction = ecriture_comptable_24_1(account_model, id_transaction, date, journal, libelle, montant)
    elif value == '25':
        transaction = ecriture_comptable_25_1(account_model, id_transaction, date, journal, libelle, montant, recepteurs)
    elif value == '26':
        transaction = ecriture_comptable_26_1(account_model, id_transaction, date, journal, libelle, montant, commission, taxe)

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
